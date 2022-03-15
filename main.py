from discord.ext import commands
import discord
from replit import db
import os
import keep_alive

bot = commands.Bot(command_prefix="+", case_insensitive=True)

bot.remove_command('help')

for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		name = file[:-3]
		bot.load_extension(f"cogs.{name}")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
      print("shutdown")
      try:
        await bot.logout()
      except:
        print("EnvironmentError")
        bot.clear()

@bot.command()
@commands.is_owner()
async def load(ctx, *, name: str):
	try:
		bot.load_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog loaded')


@bot.command()
@commands.is_owner()
async def reload(ctx, *, name: str):
	try:
		bot.reload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog reloaded')


@bot.command()
@commands.is_owner()
async def unload(ctx, *, name: str):
	try:
		bot.unload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog unloaded')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the fagot chain"))
  print(f"Bot is online. {len(bot.guilds)} server")

keep_alive.keep_alive()
bot.run(os.environ['token'])
