import discord
from discord.ext import commands
import random as ran
import style

class Fun(commands.Cog):
    cog_version = "0.1.2"
    def __init__(self, bot):
        self.bot = bot

    # ;roll {sides}
    @commands.command(brief="- Roll Dice", description="- Rolls a dice with any number of sides")  # ;roll
    async def roll(self, ctx, sides: int):
        try:
            if sides <= 0:
                await ctx.send(f"{ctx.author.mention}, dice must have a positive number of sides.")
                return
            roll_result = ran.randint(1, sides)
            await ctx.send(f"{ctx.author.mention} rolled {roll_result} on a D{sides}")
            print(f"{style.color.BLUE}Info:{style.color.END} {ctx.command.name} run successfully")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;magic8ball {question}
    @commands.command(brief="- magic8ball", description="- magic8ball")
    async def magic8ball(self, ctx, question: str):
        try:
            ran_list = ["Most definitely", "Yes", "Perchance", "maybe", "Probably Not", "No", "Most Defintely Not"]
            ran_result = ran.choice(ran_list)
            await ctx.send(f"{ctx.author.mention}, {ran_result}.")
            print(f"{style.color.BLUE}Info:{style.color.END} {ctx.command.name} run successfully")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

async def setup(bot):
    await bot.add_cog(Fun(bot))