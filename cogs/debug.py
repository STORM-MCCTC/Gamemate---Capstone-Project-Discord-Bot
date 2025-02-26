import discord
from discord.ext import commands

cog_verison = "0.0.1"

devserver = 1285212145788915772

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /ping - Guild-specific slash command
    @discord.app_commands.command(name="ping", description="Pings the bot")
    @discord.app_commands.guilds(discord.Object(id=devserver))
    async def slash_ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong :3")

    # ;ping - Legacy command
    @commands.command(brief="- Pings Client", description="- Pings Client")
    async def debug_ping(self, ctx):
        await ctx.send("Pong :3")

async def setup(bot):
    await bot.add_cog(Debug(bot))