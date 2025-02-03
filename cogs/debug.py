import discord
from discord.ext import commands

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /ping
    @discord.app_commands.command(name="ping", description="Pings the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong :3")

    # ;ping
    @commands.command(brief="- Pings Client", description="- Pings Client")
    async def legacy_ping(self, ctx):
        await ctx.send("Pong :3")

async def setup(bot):
    await bot.add_cog(Debug(bot))
    bot.tree.add_command(Debug.ping)  # Register slash command