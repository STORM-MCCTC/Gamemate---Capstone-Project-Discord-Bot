import discord
from discord.ext import commands
import requests

class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;rouseravatar {username}
    @commands.command(brief="- Fetches a Roblox user's avatar", description="- Retrieves and displays a Roblox user's avatar")
    async def rouseravatar(self, ctx, username: str):
        # Step 1: Get User ID from Username
        user_id_url = "https://users.roblox.com/v1/usernames/users"
        payload = {"usernames": [username], "excludeBannedUsers": True}
        headers = {"Content-Type": "application/json"}

        response = requests.post(user_id_url, json=payload, headers=headers)
        
        if response.status_code != 200 or not response.json().get("data"):
            await ctx.send(f"❌ User '{username}' not found!")
            return

        user_id = response.json()["data"][0]["id"]

        # Step 2: Get Avatar Image URL
        avatar_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png"
        avatar_response = requests.get(avatar_url)

        if avatar_response.status_code != 200 or not avatar_response.json().get("data"):
            await ctx.send(f"❌ Could not retrieve avatar for '{username}'")
            return

        avatar_data = avatar_response.json()["data"][0]

        if avatar_data["state"] != "Completed":
            await ctx.send(f"❌ Avatar for '{username}' is not available.")
            return

        avatar_image_url = avatar_data["imageUrl"]

        # Step 3: Create and Send Embed
        embed = discord.Embed(title=f"{username}'s Avatar", color=discord.Color.blue())
        embed.set_image(url=avatar_image_url)

        await ctx.send(embed=embed)

    # ;rouserinfo {username}
    @commands.command(brief="- Fetches Roblox user info", description="- Retrieves and displays a Roblox user's information")
    async def rouserinfo(self, ctx, username: str):
        """Fetches Roblox user info and sends an embed with details"""

        try:
            # Step 1: Get User ID from Username
            user_id_url = "https://users.roblox.com/v1/usernames/users"
            payload = {"usernames": [username], "excludeBannedUsers": True}
            headers = {"Content-Type": "application/json"}

            response = requests.post(user_id_url, json=payload, headers=headers)
            
            if response.status_code != 200:
                await ctx.send(f"❌ Error fetching user ID. Status Code: {response.status_code}")
                return
            
            data = response.json()
            if not data.get("data"):
                await ctx.send(f"❌ User '{username}' not found!")
                return

            user_id = data["data"][0]["id"]

            # Step 2: Get User Info
            user_info_url = f"https://users.roblox.com/v1/users/{user_id}"
            user_info_response = requests.get(user_info_url)

            if user_info_response.status_code != 200:
                await ctx.send(f"❌ Could not retrieve info for '{username}'. Status Code: {user_info_response.status_code}")
                return

            user_info = user_info_response.json()

            display_name = user_info.get("displayName", "N/A")
            created_at = user_info.get("created", "N/A").split("T")[0]  # Format date
            description = user_info.get("description", "No description available.")
            banned_status = "❌ Banned" if user_info.get("isBanned", False) else "✅ Active"

            # Step 3: Get Avatar Image
            avatar_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png"
            avatar_response = requests.get(avatar_url)

            if avatar_response.status_code != 200:
                await ctx.send(f"❌ Error fetching avatar. Status Code: {avatar_response.status_code}")
                return

            avatar_data = avatar_response.json().get("data", [])

            if not avatar_data or avatar_data[0]["state"] != "Completed":
                avatar_image_url = "https://tr.rbxcdn.com/empty_avatar.png"  # Default avatar if unavailable
            else:
                avatar_image_url = avatar_data[0]["imageUrl"]

            # Step 4: Create Embed
            embed = discord.Embed(title=f"Roblox User Info: {display_name}", color=discord.Color.blue())
            embed.set_thumbnail(url=avatar_image_url)
            embed.add_field(name="Username", value=username, inline=True)
            embed.add_field(name="Display Name", value=display_name, inline=True)
            embed.add_field(name="User ID", value=user_id, inline=True)
            embed.add_field(name="Account Created", value=created_at, inline=True)
            embed.add_field(name="Status", value=banned_status, inline=True)
            embed.add_field(name="Description", value=description, inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(Roblox(bot))