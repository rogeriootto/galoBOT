## //----------------------------- PRECISA DISSO PRA RODAR O BOT -----------------------------//

## PRECISA pip install -U discord.py[voice]
## https://www.youtube.com/watch?v=ml-5tXRmmFk
## pip install youtube_dl
## git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
## pip install pytube3

## //-------------------------------------------------------------------//


## //----------------------------- IMPORTS -----------------------------//
import discord
import os
from random import choice
from discord.ext import commands
from discord.ext import tasks
import random
import drawfunction
import youtubeshit
import json

## //-------------------------------------------------------------------//


## //----------------------------- COISAS IMPORTANTES PARA O BOT COMEÇAR A RODAR -----------------------------//

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

## //--------------------------------------------------------------------------------------------------------//


## //----------------------------- AJUDA -----------------------------//

@client.command(pass_context=True)
async def gHelp(ctx):
    await ctx.send('```\nCOMANDOS:\n-gJoin -- Entra no canal\n-gLeave -- Sai do canal\n-gPlay [url] -- toca musica do yt (favor não colocar livestream)\n-gVUKVUK\n-gGALO\n-gHelp -- Tu recem digitou essa porra pra q tu vai querer usar isso aqui dnv wtf\n```')
    await ctx.send('```\n**Memes**\n-kayara\n-among\n-ultra\n-picotinha\n-salazar\n-murilo\n-nehmole -- n eh mole\n-matematica\n-getTomorrowsDate\n-todaywasagoodday```')

## //-----------------------------------------------------------------//


## //----------------------------- FUNÇÕES PARA O YOUTUBE -----------------------------//
# Playa musica
@client.command(pass_context=True)
async def gPlay(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    try:
        if song_there:
            os.remove("song.mp3")
            youtubeshit.play(ctx, url, voice)

    except PermissionError:
        await ctx.send('ESPERA A MUSICA ACABAR O PROCESSO NAO É OTIMIZADO')

# Pausa musica
@client.command(pass_context=True)
async def gPause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('NAO TA TOCANDO NADA PQ TU QUER PAUSAR?????')

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

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if (ctx.voice_client):
        voice.stop()
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('EU NÃO TO NO CANAL PORRA')

## //-------------------------------------------------------------------------------------------//


## //----------------------------- MEMES COM AUDIO QUE O BOT TOCA -----------------------------//

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

## //--------------------------------------------------------------------------------------------//


## //----------------------------- FUNÇÕES PARA O SISTEMA DO BANCO ------------------------------//




## //--------------------------------------------------------------------------------------------//


## //----------------------------- FUNÇÕES PARA O MEME DOS DRAW ---------------------------------//

@client.command(pass_context=True)
async def gDraw(ctx):

    embed, file = drawfunction.randDraw(ctx)
    await ctx.send(embed=embed, file=file)

@client.command(pass_context=True)
async def jesus(ctx):

    embed, file = drawfunction.jesus(ctx)
    await ctx.send(embed=embed, file=file)

@client.command(pass_context=True)
async def ultratrolha(ctx):

    embed, file = drawfunction.ultratrolha(ctx)
    await ctx.send(embed=embed, file=file)

@client.command(pass_context=True)
async def among(ctx):

    embed, file = drawfunction.among(ctx)
    await ctx.send(embed=embed, file=file)

@client.command(pass_context=True)
async def galosniper(ctx):

    embed, file = drawfunction.galosniper(ctx)
    await ctx.send(embed=embed, file=file)

## //---------------------------------------------------------------------------------------------------//


## //----------------------------- ALGUNS MEMES QUE SÓ PRINTAM NO DISCORD -----------------------------//


@client.command(pass_context=True)
async def umapeca(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/238065523961757696/790033127619821608/unknown.png')

@client.command(pass_context=True)
async def kayara(ctx):
    await ctx.send('streamer\ndançarina')

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
async def malloc(ctx):
    await ctx.send('https://twitter.com/c0dehard/status/1327718161848872960')

@client.command(pass_context=True)
async def todaywasagoodday(ctx):
    await ctx.send('https://twitter.com/Vocaloidplush/status/1382417359311233027')

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

## //------------------------------------------------------------------//

## //----------------------------- TOKEN -----------------------------//
client.run(TOKEN)
## //-----------------------------------------------------------------//
