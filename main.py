## PRECISA pip install -U discord.py[voice]
## https://www.youtube.com/watch?v=TFdO7oqkMzI
## pip install youtube_dl
## git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg

import discord
import os
from random import choice
from discord.ext import commands
from discord.ext import tasks
import random
import youtube_dl

client = commands.Bot(command_prefix='-')
status = ['Jogando Galo de Rinha em C', 'Ultra trolha', '∞³ > ∞²', '-gHelp for Help']
joinFlag = 0
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.event
async def on_ready():
    change_status.start()
    print('O {0.user} TA ON RAPAZIADA'.format(client))


# Playa musica
@client.command(pass_context=True)
async def gPlay(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send('ESPERA A MUSICA ACABAR O PROCESSO NAO É OTIMIZADO')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))


# Pausa musica
@client.command(pass_context=True)
async def gPause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('NAO TA TOCANDO NADA PQ TU QUER PAUSAR?????')

@client.command(pass_context=True)
async def gGALO(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("mp3/galo.mp3"))

@client.command(pass_context=True)
async def gKNOCK(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("mp3/knock.mp3"))

@client.command(pass_context=True)
async def gVUKVUK(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("mp3/vukvuk.mp3"))
    await ctx.send('É VUK VUK POR 10H, VUK VUK VUK VUK VUK')

@client.command(pass_context=True)
async def ultratrolha(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/588545039777660949/830584778608214066/unknown.png')

@client.command(pass_context=True)
async def umapeca(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/238065523961757696/790033127619821608/unknown.png')

@client.command(pass_context=True)
async def gdPlay(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


# Resume musica
@client.command(pass_context=True)
async def gResume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('JA TA TOCANDO ESSA MERDA PRA Q ISSO VEI?!?!?!?')


# PARA TUDO PARA TUDO
@client.command(pass_context=True)
async def gStop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


# JOINA
@client.command(pass_context=True)
async def gJoin(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('CONECTA NO VOICE CORNO')


# SAI DO CANAL
@client.command(pass_context=True)
async def gLeave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

    else:
        await ctx.send('EU NÃO TO NO CANAL PORRA')


# Ajuda
@client.command(pass_context=True)
async def gHelp(ctx):
    await ctx.send(
        '```\nCOMANDOS:\n-gJoin -- Entra no canal\n-gLeave -- Sai do canal\n-gPlay [url] -- toca musica do yt (favor não colocar livestream)\n-gVUKVUK\n-gGALO\n-gHelp -- Tu recem digitou essa porra pra q tu vai querer usar isso aqui dnv wtf\n```')
    await ctx.send(
        '```\n**Memes**\n-kayara\n-among\n-ultra\n-picotinha\n-salazar\n-murilo\n-nehmole -- n eh mole\n-matematica\n-getTomorrowsDate\n```')


# MEMES DESSA PORRA#
##################################################################################################################################
@client.command(pass_context=True)
async def kayara(ctx):
    await ctx.send('streamer\ndançarina')


@client.command(pass_context=True)
async def among(ctx):
    await ctx.send('ඞ')


@client.command(pass_context=True)
async def ultra(ctx):
    await ctx.send('trolha')


@client.command(pass_context=True)
async def picotinha(ctx):
    await ctx.send('salazar')


@client.command(pass_context=True)
async def salazar(ctx):
    await ctx.send('picotinha')


@client.command(pass_context=True)
async def murilo(ctx):
    await ctx.send('É MURILLO PORRA, TEM DOIS L CARALHO')


@client.command(pass_context=True)
async def nehmole(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/588545039777660949/829071161186189352/d317a2456aad6e995454ea93a96ce3ee3e3f9f32a73ecaf16b5b6dd30eb0736b_1.png')


@client.command(pass_context=True)
async def matematica(ctx):
    i = random.randint(0, 1)
    if i == 0:
        await ctx.send(
            'https://cdn.discordapp.com/attachments/588545039777660949/829072028744548402/EKopsiQW4AAVFX8.png')
    else:
        await ctx.send(
            'https://cdn.discordapp.com/attachments/588545039777660949/829072011947016192/ExB7WK8W8AgM4SF.png')


@client.command(pass_context=True)
async def getTomorrowsDate(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/597584201818046515/829030594796191845/48382146_333240393936526_3546234963072385024_n.png')


##################################################################################################################################

client.run('TOKEN')
