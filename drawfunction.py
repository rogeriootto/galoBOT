import discord
import random

def randstats():

    kakera = random.randint(500, 9999)
    likerank = random.randint(1, 10)
    claimrank = random.randint(1, 10)
    return kakera, likerank, claimrank

def randDraw(ctx):

    sel = random.randint(1, 4)
    if sel == 1:
        embed, file = jesus(ctx)
        return embed, file
    elif sel == 2:
        embed, file = ultratrolha(ctx)
        return embed, file
    elif sel == 3:
        embed, file = among(ctx)
        return embed, file
    elif sel == 4:
        embed, file = galosniper(ctx)
        return embed, file

def jesus(ctx):

    kakera, likerank, claimrank = randstats()
    embed = discord.Embed(color=discord.Colour.red())
    file = discord.File("img/jesus.png", filename=("jesus.png"))
    embed.add_field(name="Jesus\n",
                    value=f"\n\nBiblia :male_sign:\nAnimanga roulette. {kakera} :gem:\nClaim Rank: #{claimrank}\nLike Rank:#{likerank}",
                    inline=True)
    embed.set_image(url="attachment://jesus.png")
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Belongs to {ctx.author.name}")
    return embed, file

def ultratrolha(ctx):

    kakera, likerank, claimrank = randstats()

    embed = discord.Embed(color=discord.Colour.red())
    file = discord.File("img/ultratrolha.png", filename=("ultratrolha.png"))
    embed.add_field(name="Ultra Trolha\n",
                    value=f"\n\nUltra Trolha :question:\nAnimanga roulette. {kakera} :gem:\nClaim Rank: #{claimrank}\nLike Rank:#{likerank}",
                    inline=True)
    embed.set_image(url="attachment://ultratrolha.png")
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Belongs to {ctx.author.name}")
    return embed, file

def among(ctx):

    kakera, likerank, claimrank = randstats()

    embed = discord.Embed(color=discord.Colour.red())
    file = discord.File("img/among.png", filename=("among.png"))
    embed.add_field(name="Among\n",
                    value=f"\n\nඞ :question:\nAnimanga roulette. {kakera} :gem:\nClaim Rank: #{claimrank}\nLike Rank:#{likerank}",
                    inline=True)
    embed.set_image(url="attachment://among.png")
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Belongs to {ctx.author.name}")
    return embed, file

def galosniper(ctx):

    kakera, likerank, claimrank = randstats()

    embed = discord.Embed(color=discord.Colour.red())
    file = discord.File("img/galosniper.png", filename=("galosniper.png"))
    embed.add_field(name="GALO SNIPER\n",
                    value=f"\n\nGalo :chicken:\nAnimanga roulette. {kakera} :gem:\nClaim Rank: #{claimrank}\nLike Rank:#{likerank}",
                    inline=True)
    embed.set_image(url="attachment://galosniper.png")
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Belongs to {ctx.author.name}")
    return embed, file

