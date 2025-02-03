import discord
from discord.ext import commands
import os
import asyncio

# Read the client token
with open("token.txt", "r") as token_file:
    token = token_file.readline().strip()
    print(token)

# Define Bot Class (No Need for CommandTree)
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=";", intents=intents)

    async def setup_hook(self):
        await load_cogs(self)
        await self.tree.sync()  # Sync slash commands
        print("Slash commands synced!")

# Load all cogs in the `cogs` folder
async def load_cogs(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

# Run the bot
async def main():
    bot = MyBot()
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
