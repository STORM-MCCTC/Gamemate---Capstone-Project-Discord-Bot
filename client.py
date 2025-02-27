import discord
from discord.ext import commands
import os
import asyncio
import style

# Read the client token
with open("token.txt", "r") as token_file:
    token = token_file.readline().strip()
    print(f"{style.color.BLUE}client-token: {style.color.END}{style.color.BLACK}{token}{style.color.END}")

# Define Bot Class
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=";", intents=intents)

    async def setup_hook(self):
        await load_cogs(self)
        await self.tree.sync() # Sync slash commands
        print(f"{style.color.GREEN}Slash commands synced!{style.color.END}")
        print(f"{style.color.GREEN}Legacy commands synced!{style.color.END}")

# Load all cogs in the `cogs` folder
async def load_cogs(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                # Load the cog extension
                await bot.load_extension(f"cogs.{filename[:-3]}")

                # Find the actual cog name from bot.cogs
                cog_name = next((name for name in bot.cogs.keys() if name.lower() == filename[:-3].lower()), None)

                if cog_name:
                    cog = bot.get_cog(cog_name)
                    cog_version = getattr(cog, "cog_version", "Unknown version")
                    print(f"{style.color.BLUE}Loaded cog:{style.color.END} {filename} - v{cog_version}")
                else:
                    print(f"{style.color.YELLOW}Warning:{style.color.END} {filename} was loaded but not recognized as a cog.")

            except Exception as e:
                print(f"{style.color.RED}Failed to load cog {filename}: {e}{style.color.END}")
    print(f"{style.color.BLUE}Loaded cogs:{style.color.END} {bot.cogs.keys()}")

# Run the bot
async def main():
    bot = MyBot()
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
