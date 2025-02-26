import discord
from discord.ext import commands
import random as ran

cog_verison = "0.0.1"

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

    # ;magic8ball {question}
    @commands.command(brief="- magic8ball", description="- magic8ball")
    async def magic8ball(self, ctx, question: str):
        ran_list = ["Most definitely", "Yes", "Perchance", "maybe", "Probably Not", "No", "Most Defintely Not"]
        ran_result = ran.choice(ran_list)
        await ctx.send(f"{ctx.author.mention}, {ran_result}.")

async def setup(bot):
    await bot.add_cog(Fun(bot))