import discord
from discord.ext import commands
import json
import youtube_dl
import random

# Leer la configuración desde config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']
    PREFIX = config['prefix']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Configura el reproductor de audio
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, url):
        channel = ctx.author.voice.channel
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice_client is None:
            voice_client = await channel.connect()

        ydl_opts = {'format': 'bestaudio'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            voice_client.play(discord.FFmpegPCMAudio(url2))

    @commands.command()
    async def stop(self, ctx):
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            await ctx.send("La música ha sido detenida.")

# Comandos adicionales
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

@bot.event
async def on_ready():
    print('Bot is ready.')

bot.add_cog(Music(bot))

# Se inicia el bot
bot.run(TOKEN)
