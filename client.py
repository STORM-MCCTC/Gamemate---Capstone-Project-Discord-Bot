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
                # Access the cog and its version if available
                cog = bot.get_cog(filename[:-3])  # Get the loaded cog by name
                if hasattr(cog, "cog_version"):
                    print(f"{style.color.BLUE}Loaded cog:{style.color.END} {filename} - v{cog.cog_version}")
                else:
                    print(f"{style.color.YELLOW}Loaded cog:{style.color.END} {filename} - Unknown version")
            except Exception as e:
                print(f"{style.color.RED}Failed to load cog {filename}: {e}{style.color.END}")

# Run the bot
async def main():
    bot = MyBot()
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
