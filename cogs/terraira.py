import discord
from discord.ext import commands

class TerrairaCommands(commands.Cog):
    cog_version = "0.0.1"
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
        formatted_bossname = bossname.replace(" ", "_")
        if formatted_bossname.lower() == "king_slime" or \
        formatted_bossname.lower() == "eye_of_cthulhu" or \
        formatted_bossname.lower() == "eater_of_worlds" or \
        formatted_bossname.lower() == "brain_of_cthulhu" or \
        formatted_bossname.lower() == "queen_bee" or \
        formatted_bossname.lower() == "skeletron" or \
        formatted_bossname.lower() == "deerclops" or \
        formatted_bossname.lower() == "wall_of_flesh" or \
        formatted_bossname.lower() == "queen_slime" or \
        formatted_bossname.lower() == "the_twins" or \
        formatted_bossname.lower() == "the_destroyer" or \
        formatted_bossname.lower() == "skeletron_prime" or \
        formatted_bossname.lower() == "mechdusa" or \
        formatted_bossname.lower() == "plantera" or \
        formatted_bossname.lower() == "golem" or \
        formatted_bossname.lower() == "duke_fishron" or \
        formatted_bossname.lower() == "empress_of_light" or \
        formatted_bossname.lower() == "lunatic_cultist" or \
        formatted_bossname.lower() == "moon_lord" or \
        formatted_bossname.lower() == "dark_mage" or \
        formatted_bossname.lower() == "ogre" or \
        formatted_bossname.lower() == "betsy" or \
        formatted_bossname.lower() == "flying_dutchman" or \
        formatted_bossname.lower() == "mourning_wood" or \
        formatted_bossname.lower() == "pumpking" or \
        formatted_bossname.lower() == "everscream" or \
        formatted_bossname.lower() == "santa-nk1" or \
        formatted_bossname.lower() == "ice_queen" or \
        formatted_bossname.lower() == "martian_saucer" or \
        formatted_bossname.lower() == "solar_pillar" or \
        formatted_bossname.lower() == "nebula_pillar" or \
        formatted_bossname.lower() == "vortex_pillar" or \
        formatted_bossname.lower() == "stardust_pillar" or \
        formatted_bossname.lower() == "ocram" or \
        formatted_bossname.lower() == "lepus" or \
        formatted_bossname.lower() == "turkor_the_ungrateful":
            url = f"https://terraria.wiki.gg/wiki/Bosses#{formatted_bossname}"
            embed = discord.Embed(description=f"[{bossname} on Terraria Wiki]({url})")
            await ctx.send(embed=embed)
        else:
            await ctx.send("invalid, make sure you put that in corectly")

async def setup(bot):
    await bot.add_cog(TerrairaCommands(bot))