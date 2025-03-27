import discord
from discord.ext import commands
import style

devserver = 1285212145788915772

class Debug(commands.Cog):
    cog_version = "0.1.2"
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
        try:
            await ctx.send("Pong :3")
            print(f"{style.color.BLUE}Info:{style.color.END} {ctx.command.name} run successfully")
        except Exception as e:
            await ctx.send(f"something went wrong... Exception:{e}")
            print(f"{style.color.RED}Error: {ctx.command.name} Exception: {e}{style.color.END}")
        
async def setup(bot):
    await bot.add_cog(Debug(bot))