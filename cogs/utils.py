from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from asyncio import sleep 

class Utilities(commands.Cog):
    """Utilities, mostly moderation"""
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='clear', aliases=['cls'], brief='Clears messages', description='Clears a specified amount of messages. Takes no big than 100 messages at once.')
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amt):
        try:
            amt = int(amt)
        except:
            await ctx.send('Only numbers allowed as argument!')
            return

        if amt > 100:
            await ctx.send('Only 100 messages at a time dude!!')
            return

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send('Are you sure to delete {} messages? (Reply with yes/y or anything else for no)'.format(amt))
        msgrecv = await self.bot.wait_for('message', check=check)

        if msgrecv.content.lower() == 'yes' or 'y':
            await ctx.channel.purge(limit=amt + 3)
            msgsent = await ctx.send('Cleared {} messages :white_check_mark:'.format(amt))
            await sleep(3)
            await msgsent.delete()

        else:
            msgsent = await ctx.send('Didn\'t touch the messages. *sigh*')
            await sleep(3)
            await msgsent.delete()

    @clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, CheckFailure):
            await ctx.send(ctx.message.channel, "Looks like you don't have the `manage_messages` permission.")

def setup(bot):
    bot.add_cog(Utilities(bot))
