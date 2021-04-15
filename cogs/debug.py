from discord.ext import commands, tasks
from sys import version_info as pyv
from discord import __version__ as dcv
from lyricsgenius import __version__ as lgv

class Utilities(commands.Cog, name='Utilities'):
    """Utility commands to know/operate the bot!!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about', brief='About the bot.', description='Information on the bot. Type \'~about techinf\' to get technical information.')
    async def about(self, ctx, technef = 'None'):
        await ctx.send(u"Personal bot for Lunoirex#5661 | Made with \u2665 by Zukashi#7071")
        if technef.lower() == 'techinf':
            await ctx.send("**Techincal Information:**")
            await ctx.send("```\nPython {}.{}.{}\n---------------\nDiscord.py v{}\n---------------\nLyricGenius v{}\n---------------\nPing: {}ms```".format(pyv.major, pyv.minor, pyv.micro, dcv, lgv, int(self.bot.latency * 1000)))

    @commands.command(name='shutdown', brief='Shutdown the bot.', description='Turns off the bot. Can only be used by an authorized personnel.')
    async def shutdown(self, ctx):
        if ctx.author.id != 463657352386707456 or 690400661786984468:
            await ctx.send('You\'re not authorized for this!')
        else:
            await ctx.send('Shutting down . . . /')
            await self.bot.close()

def setup(bot):
    bot.add_cog(Utilities(bot))