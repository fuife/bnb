import discord
from discord import channel
from discord.ext import commands
from discord import Intents
intents=discord.Intents.all()

bot= commands.Bot(command_prefix='!',intents=intents)
@bot.event
async def on_ready():
    print("> 夸黑 is online <")
@bot.event  #member join
async def on_member_join(member):
    print(f'{member} join!')
    channel=bot.get_channel(884494495197061191)
    await channel.send(f'{member} is join~')
@bot.event  #member leave
async def on_member_remove(member):
    print(f'{member} is leave!')
    channel=bot.get_channel(884494586624487425)
    await channel.send(f'{member} is 7414!')
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')






bot.run ('ODg0NDc0ODgwMjc0MzMzNzc2.YTZBbA.7RzpE7Vk5maeaKM2nj11YQihhho')