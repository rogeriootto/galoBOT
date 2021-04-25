## //----------------------------- PRECISA DISSO PRA RODAR O BOT -----------------------------//

## PRECISA pip install -U discord.py[voice]
## https://www.youtube.com/watch?v=TFdO7oqkMzI
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


## //----------------------------- JOGO DA VELHA VAMO TESTAR ------------------------------//

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2], #Linha horizontal
    [3, 4, 5], #Linha horizontal
    [6, 7, 8], #Linha horizontal
    [0, 3, 6], #Linha vertical
    [1, 4, 7], #Linha vertical
    [2, 5, 8], #Linha vertical
    [0, 4, 8], #Diagonal
    [2, 4, 6]  #Diagonal
]

@client.command(pass_context=True)
async def gVelha(ctx, p2 : discord.Member):
    
    global gameOver

    if gameOver:
        global board
        global player1
        global player2
        global turn
        global count

        board =[":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:",]

        turn = ""
        gameOver = False
        count = 0

        player1 = ctx.author
        player2 = p2

        # Printa o tabuleiro
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x==8:
                line += "" + board[x]
                await ctx.send(line)
                line = ""
            else:
                line+= "" + board[x]

        # DETERMINA OS TURNOS
        num = random.randint(1,2)
        if num == 1:
            turn = player1
            await ctx.send("Vez de: <@"+ str(player1.id) + "> :regional_indicator_x:")
        elif num == 2:
            turn = player2
            await ctx.send("Vez de: <@"+ str(player2.id) + "> :o2:")
    else:
        await ctx.send("Ja tem gente jogando, pera ae")

@client.command(pass_contex=True)
async def colocar(ctx, pos : int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    
    if not gameOver:
        if ctx.author == player1 or ctx.author == player2:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"

                elif turn == player2:
                    mark = ":o2:"
                
                if 0 < pos < 10 and board[pos-1] == ":white_large_square:":
                    board[pos-1] = mark
                    count += 1

                    # printa o tabuleiro dnv
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x==8:
                            line += "" + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line+= "" + board[x]

                    checkWinner(winningConditions, mark)
                    if gameOver:
                        await ctx.send(mark +" ganhou!")
                    elif count >= 9:
                        await ctx.send("Empate!")
                        gameOver = True

                    #Switch turns
                    if not gameOver:
                        if turn == player1:
                            await ctx.send("Vez de :<@"+ str(player2.id) + "> :o2:")
                            turn = player2
                        elif turn == player2:
                            await ctx.send("Vez de: <@"+ str(player1.id) + "> :regional_indicator_x:")
                            turn = player1
                else:
                    await ctx.send("Ta colocando em um lugar errado irmão")
            else:
                await ctx.send("NÃO É TUA VEZ MAL EDUCADO")
        else:
            await ctx.send("Cara tu não tá nem jogando, sai daqui")
    else:
        await ctx.send("Começa um jogo aí po, não sou adivinha (-gVelha)")

@client.command(pass_context=True)
async def gVelhaStop(ctx):
    global gameOver
    global player1
    global player2

    if ctx.author == player1 or ctx.author == player2:
        gameOver = True
        await ctx.send("Jogo entre <@"+ str(player1.id) +"> e <@" + str(player2.id) + "> foi interrompido!")
    else:
        await ctx.send("Você nem ta jogando, sai daqui")

def checkWinner(winningConditions, mark):
    global gameOver
    global count

    for condition in winningConditions:
        if  mark == board[condition[0]] and mark == board[condition[1]] and mark == board[condition[2]]:
            gameOver = True

@client.command(pass_context=True)
async def gVelhaHelp(ctx):

    embed = discord.Embed(color=discord.Colour.red())
    file = discord.File("img/VelhaHelp.png", filename=("VelhaHelp.png"))
    embed.add_field(name="VelhaHelp\n",
                    value="Para começar o jogo, digite: **-gVelha @Pessoa**\n\nPara interromper o jogo, use: **-gVelhaStop**\n\nCada pessoa tem seu turno;\nPara realizar sua jogada você precisa usar o comando, **-colocar**\nPara escolher o lugar, você digita o numero do quadrado que vai ser inserido;\n**Exemplo: -colocar 5**",
                    inline=True)
    embed.set_image(url="attachment://VelhaHelp.png")
    await ctx.send(embed = embed, file=file)

@gVelha.error
async def velhaErro(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ta escolhendo errado, tem que escolher duas pessoas")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Ta fazendo muito errado, vc tem que pingar com quem vc quer jogar (ex: -gVelha @nome1 @nome2)")

@colocar.error
async def place_error (ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Coloca um valor valido pra posição aí (1-9) (ex: -place 3)")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Vc não tá colocando um numero, bota um numero ae de 1 a 9 plmds")

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
