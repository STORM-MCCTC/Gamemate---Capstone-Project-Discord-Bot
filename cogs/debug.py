import discord
from discord.ext import commands
# import uptime

devserver = 1285212145788915772

class Debug(commands.Cog):
    cog_version = "0.0.1"
    def __init__(self, bot):
        self.bot = bot

    # /ping - Guild-specific slash command
    @discord.app_commands.command(name="ping", description="Pings the bot")
    @discord.app_commands.guilds(discord.Object(id=devserver))
    async def slash_ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong :3")

    # ;ping - Legacy command
    @commands.command(brief="- Pings Client", description="- Pings Client")
    async def debug_ping(self, ctx, user_id, server_id):
        await ctx.send("Pong :3")
        # print(f"User ID: {user_id}, Server ID: {server_id}, "), uptime.print_uptime

async def setup(bot):
    await bot.add_cog(Debug(bot))