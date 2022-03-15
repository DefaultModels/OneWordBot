from discord.ext import commands
import discord
from replit import db
import os

class on_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.channel.id == 848646927653404723:
        value = db["word"]

        if message.content != value:
          await message.delete()

def setup(bot):
    bot.add_cog(on_message(bot))