import discord as dis
from discord.ext import commands
import requests as req
import random as ran
from bs4 import BeautifulSoup
import style

class Warframe(commands.Cog):
    cog_version = "1.0.2"
    def __init__(self, bot):
        self.bot = bot

    # ;cetus
    @commands.command(brief="- Check Cetus day/night cycle", description="- Returns whether it is currently day or night on the Plains of Eidolon along with the time remaining until the next transition.")
    async def cetus(self, ctx):
        try:
            cetus = req.get("https://api.warframestat.us/pc/en/cetusCycle")
            cetus_data = cetus.json()
            if cetus_data['isDay']:
                await ctx.send(f"Operator, the plains of Cetus are currently bathed in *daylight*. {cetus_data['timeLeft']} remains until *nightfall* descends.")
            else:
                await ctx.send(f"Operator, the plains of Cetus are enveloped in *night*. The sun will rise in {cetus_data['timeLeft']}")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;vallis
    @commands.command(brief="- Check Vallis warm/cold cycle", description="- Returns whether it is currently warm or cold in Orb Vallis along with the time remaining until the next transition.")
    async def vallis(self, ctx):
        try:
            vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
            vallis_data = vallis.json()
            if vallis_data['isWarm']:
                await ctx.send(f"Operator, it is currently... *warm* on the Vallis. The transition to *cold* will occur in {vallis_data['timeLeft']}.")
            else:
                await ctx.send(f"Operator, conditions on the Vallis are currently... *cold*. Warmth will return in {vallis_data['timeLeft']}.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;cambion
    @commands.command(brief="- Check Cambion Drift Vome/Fass cycle", description="- Returns whether it is currently Vome or Fass in the Cambion Drift along with the time remaining until the next transition.")
    async def cambion(self, ctx):
        try:
            cambion = req.get("https://api.warframestat.us/pc/en/cambionCycle")
            cambion_data = cambion.json()
            if cambion_data['state'] == "vome":
                await ctx.send(f"Operator, it is currently... *Vome* on the Cambion Drift. {cambion_data['timeLeft']} remains until *Fass* emerges.")
            else:
                await ctx.send(f"Operator, the Cambion Drift is under the influence of *Fass*. The cycle will shift to *Vome* in {cambion_data['timeLeft']}.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;zariman
    @commands.command(brief="- Check Zariman faction control", description="- Returns whether the Zariman is currently controlled by Corpus or Grineer along with the time remaining until the next transition.")
    async def zariman(self, ctx):
        try:
            zariman = req.get("https://api.warframestat.us/pc/en/zarimanCycle")
            zariman_data = zariman.json()
            if zariman_data['isCorpus']:
                await ctx.send(f"Operator, the Zariman is currently under *Corpus* influence. {zariman_data['timeLeft']} until the *Grineer* seize control.")
            else:
                await ctx.send(f"Operator, the Zariman is currently controlled by the *Grineer*. The shift to *Corpus* control will occur in {zariman_data['timeLeft']}.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;voidtrader
    @commands.command(brief="- Check Void Trader schedule", description="- Returns the time remaining until Baro Ki'Teer arrives and his location.")
    async def voidtrader(self, ctx):
        try:
            voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
            voidtrader_data = voidtrader.json()
            await ctx.send(f"Operator, Baro Ki'Teer will return in *{voidtrader_data['startString']}* at the *{voidtrader_data['location']}*.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;archon
    @commands.command(brief="- Check Archon Hunt reset timer", description="- Returns the time remaining until the next Archon Hunt reset.")
    async def archon(self, ctx):
        try:
            archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
            archon_data = archon.json()
            await ctx.send(f"Operator, the Archon Hunt will reset in *{archon_data['eta']}*.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;sortie
    @commands.command(brief="- Check Sortie reset timer", description="- Returns the time remaining until the next Sortie reset.")
    async def sortie(self, ctx):
        try:
            sortie = req.get("https://api.warframestat.us/pc/en/sortie")
            sortie_data = sortie.json()
            await ctx.send(f"Operator, the sortie will reset in *{sortie_data['eta']}*.")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;warframe_api
    @commands.command(brief="- Get Warframe API link", description="- Sends an embedded message containing a link to the Warframe API documentation.")
    async def warframe_api(self, ctx):
        try:
            embed = dis.Embed(description="[api.warframestat.us](https://api.warframestat.us/pc/en)")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;randomframe
    @commands.command(brief="- Get a random Warframe", description="- Randomly selects a Warframe from the available list and provides a link to its wiki page.")
    async def randomframe(self, ctx):
        try:
            frames = ["Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Cyte-09", "Dagath", "Dante", "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow", "Hildryn", "Hydroid", "Inaros", "Ivara", "Jade", "Khora", "Koumei", "Kullervo", "Lavos", "Limbo", "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia", "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Titania", "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"]
            random_frame = ran.choice(frames)
            embed = dis.Embed(color=0xcc13ad, description=f"Operator, your randomized Warframe is... [{random_frame}](https://warframe.fandom.com/wiki/{random_frame}).")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;updates
    @commands.command(brief="- Get latest Warframe updates", description="- Scrapes the Overframe website to fetch and display the most recent Warframe updates.")
    async def updates(self, ctx):
        try:
            url = "https://overframe.gg/"
            response = req.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(class_='index_itemBundleName__iwGSM')
            embed = dis.Embed(title="Warframe Updates", color=0xcc13ad)
            embed.description = "Operator, here are all the most recent updates for Warframe:\n\n"
            for element in elements:
                embed.description += f"{element.get_text(strip=True)}\n"
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

    # ;wfwiki
    @commands.command(brief="- Get Warframe Wiki link", description="- Sends an embedded message containing a link to the Warframe Fandom wiki.")
    async def wfwiki(self, ctx):
        try:
            embed = dis.Embed(description="[warframe.fandom.com](https://warframe.fandom.com/wiki)")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")

async def setup(bot):
    await bot.add_cog(Warframe(bot))