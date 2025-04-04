import discord
from discord.ext import commands, tasks
import sqlite3
import aiohttp

# Twitch API credentials (Set these later)

# Read the api key
def read_line_from_file(filename, line_number):
    with open(filename, "r") as file:
        # Read the lines into a list
        lines = file.readlines()
        if 0 <= line_number < len(lines):
            return lines[line_number].strip()
        else:
            return None

TWITCH_API_KEY = read_line_from_file("config.txt", 1)  
TWITCH_CLIENT_ID = read_line_from_file("config.txt", 2)  

class TwitchNotifications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = sqlite3.connect("twitch_notifications.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                server_id INTEGER,
                channel_id INTEGER,
                twitch_username TEXT
            )
        """)
        self.db.commit()

        self.live_streamers = set()  # Track currently live streamers
        self.check_twitch_streams.start()  # Start background task

    def __del__(self):
        self.db.close()

    def is_admin():
        """Decorator to check if the user is an admin."""
        def predicate(ctx):
            return ctx.author.guild_permissions.administrator
        return commands.check(predicate)

    async def fetch_twitch_stream_status(self, streamer):
        """Queries the Twitch API to check if a streamer is live."""
        if not TWITCH_API_KEY or not TWITCH_CLIENT_ID:
            return None  # API credentials not set

        url = f"https://api.twitch.tv/helix/streams?user_login={streamer}"
        headers = {
            "Client-ID": TWITCH_CLIENT_ID,
            "Authorization": f"Bearer {TWITCH_API_KEY}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["data"][0] if data["data"] else None
                return None

    @tasks.loop(minutes=2)
    async def check_twitch_streams(self):
        """Polls Twitch API for live streams and sends notifications."""
        self.cursor.execute("SELECT DISTINCT server_id, channel_id, twitch_username FROM notifications")
        tracked_streamers = self.cursor.fetchall()

        for server_id, channel_id, streamer in tracked_streamers:
            stream_data = await self.fetch_twitch_stream_status(streamer)

            if stream_data and streamer not in self.live_streamers:
                self.live_streamers.add(streamer)  # Mark as live
                channel = self.bot.get_channel(channel_id)
                if channel:
                    await channel.send(f"🎥 **{streamer}** is now LIVE on Twitch!\n🔗 https://twitch.tv/{streamer}")

            elif not stream_data and streamer in self.live_streamers:
                self.live_streamers.remove(streamer)  # Mark as offline

    @commands.command(brief="Set the Discord channel for Twitch notifications.")
    @is_admin()
    async def set_twitch_channel(self, ctx, channel: discord.TextChannel):
        """Sets the channel where Twitch notifications will be sent."""
        self.cursor.execute("""
            INSERT OR REPLACE INTO notifications (server_id, channel_id, twitch_username) 
            VALUES (?, ?, ?)
        """, (ctx.guild.id, channel.id, ""))
        self.db.commit()
        await ctx.send(f"Twitch notifications will be sent to {channel.mention}.")

    @commands.command(brief="Track a Twitch streamer.")
    @commands.has_permissions(administrator=True)
    async def add_twitch_streamer(self, ctx, streamer: str):
        """Adds a Twitch streamer to be tracked."""
        self.cursor.execute("SELECT channel_id FROM notifications WHERE server_id = ?", (ctx.guild.id,))
        result = self.cursor.fetchone()
        
        if result is None:
            await ctx.send("You need to set a Twitch notification channel first using `set_twitch_channel`.")
            return

        self.cursor.execute("""
            INSERT INTO notifications (server_id, channel_id, twitch_username) 
            VALUES (?, ?, ?)
        """, (ctx.guild.id, result[0], streamer))
        
        self.db.commit()
        await ctx.send(f"Now tracking Twitch streamer `{streamer}` for this server.")

    @commands.command(brief="Remove a Twitch streamer from tracking.")
    @commands.has_permissions(administrator=True)
    async def remove_twitch_streamer(self, ctx, streamer: str):
        """Removes a Twitch streamer from being tracked."""
        self.cursor.execute("""
            SELECT twitch_username FROM notifications 
            WHERE server_id = ? AND twitch_username = ?
        """, (ctx.guild.id, streamer))
        
        if not self.cursor.fetchone():
            await ctx.send(f"Streamer `{streamer}` is not being tracked on this server.")
            return

        self.cursor.execute("""
            DELETE FROM notifications 
            WHERE server_id = ? AND twitch_username = ?
        """, (ctx.guild.id, streamer))
        self.db.commit()

        await ctx.send(f"Stopped tracking Twitch streamer `{streamer}`.")

    @commands.command(brief="List tracked Twitch streamers.")
    async def list_twitch_streamers(self, ctx):
        """Lists all Twitch streamers being tracked in the server."""
        self.cursor.execute("SELECT twitch_username FROM notifications WHERE server_id = ?", (ctx.guild.id,))
        streamers = [row[0] for row in self.cursor.fetchall()]
        if streamers:
            await ctx.send(f"Tracking these Twitch streamers: {', '.join(streamers)}")
        else:
            await ctx.send("No Twitch streamers are being tracked yet.")

    @commands.command(brief="Manually check if a streamer is live.")
    async def check_live(self, ctx, streamer: str):
        """Allows users to manually check if a Twitch streamer is live."""
        stream_data = await self.fetch_twitch_stream_status(streamer)
        if stream_data:
            await ctx.send(f"🎥 **{streamer}** is currently LIVE! 🔗 https://twitch.tv/{streamer}")
        else:
            await ctx.send(f"❌ **{streamer}** is currently offline.")

    @commands.command(brief="Force a Twitch API recheck.")
    async def force_check(self, ctx):
        """Force an immediate Twitch API recheck instead of waiting for the interval."""
        await self.check_twitch_streams()
        await ctx.send("✅ Manually checked Twitch stream statuses.")

async def setup(bot):
    """Loads the TwitchNotifications cog into the bot."""
    await bot.add_cog(TwitchNotifications(bot))
