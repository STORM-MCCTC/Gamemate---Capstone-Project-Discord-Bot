import discord
from discord.ext import commands
import random as ran

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;roll {sides}
    @commands.command(brief="- Roll Dice", description="- Rolls a dice with any number of sides")  # ;roll
    async def roll(self, ctx, sides: int):
        if sides <= 0:
            await ctx.send(f"{ctx.author.mention}, dice must have a positive number of sides.")
            return
        roll_result = ran.randint(1, sides)
        await ctx.send(f"{ctx.author.mention} rolled {roll_result} on a D{sides}")
        result = ran.randint(1, 100)
        if user is None:
            await ctx.send(f"{ctx.author.mention} is a {result} on the Gay O' Meter")
        else:
            await ctx.send(f"{user.mention} is a {result} on the Gay O' Meter")

    # ;magic8ball {question}
    @commands.command()
    async def magic8ball(self, ctx, question: str):
        ran_list = ["Most definitely", "Yes", "Perchance", "maybe", "Probably Not", "No", "Most Defintely Not"]
        ran_result = ran.choice(ran_list)
        await ctx.send(f"{ctx.author.mention}, {ran_result}.")

async def setup(bot):
    await bot.add_cog(Fun(bot))