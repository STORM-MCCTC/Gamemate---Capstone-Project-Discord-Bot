import discord
from discord.ext import commands

class TerrairaCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;terrawiki
    @commands.command()
    async def terrawiki(self, ctx):
        embed = discord.Embed(description="[Terraria Wiki](https://terraria.wiki.gg/)")
        await ctx.send(embed=embed)

    # ;randomterrawiki
    @commands.command()
    async def randomterrawiki(self, ctx):
        embed = discord.Embed(description=f"[Random Terraria Wiki Page](https://terraria.wiki.gg/wiki/Special:Random)")
        await ctx.send(embed=embed)

    # ;bosshelp {bossname}
    @commands.command()
    async def boss(self, ctx, *, bossname: str):
        formatted_bossname = bossname.replace(" ", "_")  # Replace spaces with underscores
        url = f"https://terraria.wiki.gg/wiki/Bosses#{formatted_bossname}"
        embed = discord.Embed(description=f"[{bossname} on Terraria Wiki]({url})")
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(TerrairaCommands(bot))