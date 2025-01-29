import discord
from discord.ext import commands

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;ping
    @commands.command(brief="- Pings Client", description="- Pings Client")  # ;ping
    async def ping(self, ctx):
        await ctx.send("Pong :3")

async def setup(bot):
    await bot.add_cog(Debug(bot))