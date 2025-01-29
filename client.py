import discord
from discord.ext import commands
import os
import asyncio

# Read the client token
with open("token.txt", "r") as token_file:
    token = token_file.readline().strip()
    print(token)

# Initialize the client
client = commands.Bot(command_prefix=";", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Client logged in as {client.user}')

# Load all cogs in the `cogs` folder
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{filename[:-3]}")  # Await this
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

# Run the client
async def main():
    async with client:
        await load_cogs()
        await client.start(token)

if __name__ == "__main__":
    asyncio.run(main())