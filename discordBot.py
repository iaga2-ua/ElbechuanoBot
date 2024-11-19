import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Obtener el token
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '!', intents=intents)

@bot.command()
async def frases(ctx):
  canal_id = 451431438143717416
  canal = bot.get_channel(int(canal_id))

  if canal:
    frases_celebres = canal.history(limit=None)
    frases_list = [mensaje async for mensaje in frases_celebres]
    random_frase = random.choice(frases_list).content
    await ctx.send(random_frase)

@bot.command()
async def pxg(ctx):
  await ctx.send("**FRESCOOOO!**")  

bot.run(TOKEN)

