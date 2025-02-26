import asyncio
import discord
from discord.ext import commands
from mcstatus import JavaServer
import requests

cog_verison = "0.0.1"

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;mcserverinfo {server_address} {server_port}
    @commands.command(brief="- Get server info", description="- Get detailed information about a Minecraft server")
    async def mcserverinfo(self, ctx, server_address: str, server_port: int = 25565):
        try:
            server = JavaServer.lookup(f"{server_address}:{server_port}", timeout=3)
            try:
                status = await asyncio.to_thread(server.status)
            except Exception as e:
                await ctx.send(f"Failed to retrieve server status: {e}")
                return
            try:
                query = await asyncio.to_thread(server.query)
                players_online = query.players.names
                plugins = query.software.plugins if query.software.plugins else "No plugins"
            except Exception:
                players_online = "Query not enabled"
                plugins = "Query not enabled"
            embed = discord.Embed(
                title=f"Server Info for {server_address}:{server_port}",
                color=discord.Color.blue()
            )
            embed.add_field(name="Latency", value=f"{status.latency} ms", inline=False)
            embed.add_field(name="Version", value=status.version.name, inline=False)
            embed.add_field(name="Players Online", value=f"{status.players.online}/{status.players.max}", inline=False)
            embed.add_field(name="MOTD", value=status.description, inline=False)
            embed.add_field(name="Players List", value="\n".join(players_online) if isinstance(players_online, list) else players_online, inline=False)
            embed.add_field(name="Plugins", value=plugins, inline=False)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Failed to retrieve server info: {e}")

    # ;mcwiki
    @commands.command(brief="- Minecraft Wiki", description="- Minecraft Wiki")
    async def mcwiki(self, ctx):
        embed = discord.Embed(description="[minecraft.wiki](https://minecraft.wiki/)")
        await ctx.send(embed=embed)

    # ;randommcwiki
    @commands.command(brief="- Random Minecraft Wiki page", description="- Random Minecraft Wiki page")
    async def ranmcwiki(self, ctx):
        embed = discord.Embed(description=f"[minecraft.wiki/random](https://minecraft.wiki/wiki/Special:Random)")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Minecraft(bot))