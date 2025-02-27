import discord
from discord.ext import commands

class Utills(commands.Cog):
    cog_version = "0.0.1"
    def __init__(self, bot):
        self.bot = bot

    # ;avatar {user}
    @commands.command(brief="- Shows the avatar of a user", description="- Displays the avatar of a mentioned user or yourself if no user is mentioned.")
    async def avatar(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        await ctx.send(f"{user.mention}'s avatar: {user.avatar.url}")

    # ;account {user}
    @commands.command(brief="- Shows the avatar of a user", description="- Displays the avatar of a mentioned user or yourself if no user is mentioned.")
    async def account(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        display_name = user.display_name
        user_id = user.id
        username = user.name
        discriminator = user.discriminator
        created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(user, discord.Member):
            joined_at = user.joined_at.strftime("%Y-%m-%d %H:%M:%S") if user.joined_at else "Unknown"
        else:
            joined_at = "Not in server"

        embed = discord.Embed(
        title=f"{display_name}'s account",
        color=discord.Color.blue()
        )
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="Username", value=f"{username}#{discriminator}", inline=True)
        embed.add_field(name="User ID", value=user_id, inline=True)
        embed.add_field(name="Account Created", value=created_at, inline=True)
        
        await ctx.send(embed=embed)


    # ;serverinfo
    @commands.command(brief="- Displays server information", description="- Provides details about the current server.")
    async def serverinfo(self, ctx): 
        server = ctx.guild 
            
        # Collecting server information
        server_name = server.name
        server_id = server.id
        owner = server.owner
        created_at = server.created_at.strftime('%Y-%m-%d %H:%M:%S')
        member_count = server.member_count
        text_channels = len(server.text_channels)
        voice_channels = len(server.voice_channels)
        roles = len(server.roles)
            
        # Creating an embed with the server information
        embed = discord.Embed(title=f"Server Information for {server_name}", color=discord.Color.blue())
        embed.add_field(name="Server Name", value=server_name, inline=True)
        embed.add_field(name="Server ID", value=server_id, inline=True)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Created At", value=created_at, inline=True)
        embed.add_field(name="Member Count", value=member_count, inline=True)
        embed.add_field(name="Text Channels", value=text_channels, inline=True)
        embed.add_field(name="Voice Channels", value=voice_channels, inline=True)
        embed.add_field(name="Roles", value=roles, inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utills(bot))
