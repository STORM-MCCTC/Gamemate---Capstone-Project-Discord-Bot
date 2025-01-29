import discord
from discord.ext import commands
from datetime import datetime, timedelta

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ;kick {member} {reason}
    @commands.command(brief="Kick a user from the server", description="Kicks the specified user with an optional reason")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot kick yourself!")
            return
        
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked from the server. Reason: {reason or 'No reason provided.'}")

    # ;ban {member} {reason}
    @commands.command(brief="Ban a user from the server", description="Bans the specified user with an optional reason")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot ban yourself!")
            return
        
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned from the server. Reason: {reason or 'No reason provided.'}")

    # ;unban {member}
    @commands.command(brief="Unban a previously banned user", description="Unbans the user by their name and discriminator")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member_name):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member_name.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} has been unbanned.")
                return

        await ctx.send(f"User {member_name}#{member_discriminator} was not found.")

    # ;mute {member} {duration} {reason}
    @commands.command(brief="Mute a user in the server", description="Mutes the specified user for a certain duration")
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, duration: int = 10, *, reason=None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)
        
        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} has been muted for {duration} minutes. Reason: {reason or 'No reason provided.'}")
        
        # Unmute after the duration expires
        await discord.utils.sleep_until(datetime.now() + timedelta(minutes=duration))
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} has been unmuted.")

    # ;warn {member} {reason} 
    warnings = {}  # Keep track of warnings
    @commands.command(brief="Warn a user", description="Issues a warning to the specified user with an optional reason")
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot warn yourself!")
            return
        
        if member not in self.warnings:
            self.warnings[member] = []
        
        self.warnings[member].append((reason, datetime.now()))
        await ctx.send(f"{member.mention} has been warned. Reason: {reason or 'No reason provided.'}")

    # ;clear {amount}
    @commands.command(brief="Clear a number of messages in a channel", description="Clears the specified number of messages from the channel")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        if amount <= 0:
            await ctx.send("The number of messages to clear must be greater than zero.")
            return

        await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message itself
        await ctx.send(f"Cleared {amount} messages.", delete_after=5)

    # Error handling for permission errors
    @kick.error
    @ban.error
    @unban.error
    @mute.error
    @warn.error
    @clear.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the necessary permissions to use this command.")
        else:
            await ctx.send("An error occurred while processing the command.")

# Add the Cog to the bot
async def setup(bot):
    await bot.add_cog(Admin(bot))