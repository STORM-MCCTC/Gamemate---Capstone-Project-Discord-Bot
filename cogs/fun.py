import discord
from discord.ext import commands
import random as ran
import style

class Fun(commands.Cog):
    cog_version = "0.1.3"
    def __init__(self, bot):
        self.bot = bot

    # ;roll {sides}
    @commands.command(brief="- Roll Dice", description="- Rolls a dice with any number of sides")
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

    # ;cutiemeter
    @commands.command(brief="- rates how cute you are", description="- rates how cute you are")
    async def cutiemeter(self, ctx, user= None):

        try:
            meter = ran.randrange(1, 101)
            if user == None:
                if meter <= 30:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the cute o' meter. quite sad innit.")
                elif meter <=60 and meter >= 31:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the cute o' meter. awwww")
                elif meter <=100 and meter >= 61:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the cute o' meter. OMG >~< YOUR SUCH A CUTIE PATOOTIE :3")
            else:
                if meter <= 30:
                    await ctx.send(f"{user} is {meter}% on the cute o' meter. quite sad innit.")
                elif meter <=60 and meter >= 31:
                    await ctx.send(f"{user} is {meter}% on the cute o' meter. awwww")
                elif meter <=100 and meter >= 61:
                    await ctx.send(f"{user} is {meter}% on the cute o' meter. OMG >~< YOUR SUCH A CUTIE PATOOTIE :3")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;queermeter
    @commands.command(brief="- rates how queer you are", description="- rates how queer you are")
    async def queermeter(self, ctx, user= None):

        try:
            meter = ran.randrange(1, 101)
            if user == None:
                if meter <= 30:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the queer o' meter. most Straight person ever.")
                elif meter <=60 and meter >= 31:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the queer o' meter. little fruity.")
                elif meter <=100 and meter >= 61:
                    await ctx.send(f"{ctx.author.mention} is {meter}% on the queer o' meter. Straight up Homosexual.")
            else:
                if meter <= 30:
                    await ctx.send(f"{user} is {meter}% on the queer o' meter. most Straight person ever.")
                elif meter <=60 and meter >= 31:
                    await ctx.send(f"{user} is {meter}% on the queer o' meter. little fruity.")
                elif meter <=100 and meter >= 61:
                    await ctx.send(f"{user} is {meter}% on the queer o' meter. Straight up Homosexual.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

async def setup(bot):
    await bot.add_cog(Fun(bot))