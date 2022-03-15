from discord.ext import commands
import discord
from replit import db
import os

class word(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def word(self, ctx, word):
      channel = self.bot.get_channel(847536284675211307)
      if ctx.author.id == 550054495069929495:    
        db["word"] = word
        await channel.send(f'Word is now "{word}" in <#848646927653404723>')

def setup(bot):
    bot.add_cog(word(bot))