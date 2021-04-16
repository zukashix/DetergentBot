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
        await ctx.send("By the way, this bot is open-sourced at https://github.com/Zukashi2077/DetergentBot")
        await ctx.send("If you find any bugs, please create an issue on the GitHub page!")
        if technef.lower() == 'techinf':
            await ctx.send("**Techincal Information:**")
            await ctx.send("```\nPython {}.{}.{}\n---------------\nDiscord.py v{}\n---------------\nLyricGenius v{}\n---------------\nPing: {}ms```".format(pyv.major, pyv.minor, pyv.micro, dcv, lgv, int(self.bot.latency * 1000)))

def setup(bot):
    bot.add_cog(Utilities(bot))
