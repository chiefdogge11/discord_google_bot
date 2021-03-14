# pip install beautifulsoup4, discord.py,wikipedia-api,aiohttp, datamart-isi
import time
import discord
from discord.ext import commands
import json
import requests
import aiohttp
import asyncio
import wikipediaapi
# ------------------------------------------ bot functions

client = commands.Bot(command_prefix='/')

TOKEN = 'example token'  # change token


@client.event
async def on_ready():
    # await client.get_channel("enter channel id here").send("bot is online")
    print("bot is ready")


@client.command()
async def helpme(ctx):
    await ctx.send("Available commands: /wiki and /search. When searching more than one word, please uses double quotations(""). /wiki searches your question using wikipedia and /search searches using DuckDuckGo and returns a URL")


@client.command()
async def pong(ctx):
    await ctx.send("You Pinged Your Last PONG")


@client.command()
async def search(ctx, keyword):
    async with aiohttp.ClientSession() as cs:
        r = requests.get("https://api.duckduckgo.com/?q=" +
                         keyword + "&format=json&pretty=1&atb=v253-1")
        data = json.loads(str(r.text))
        embed = discord.Embed(
            title=keyword,
            color=ctx.author.color
        )
        result = data["RelatedTopics"]
        links = []
        for i in range(1):
            links.append(data["RelatedTopics"][i]["FirstURL"])
        print(links)
        await ctx.send(links)


@client.command()
async def wiki(ctx, keyword):
    wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page(keyword)

    print("Page - Title: %s" % page_py.title)

    print("Page - Summary: %s" % page_py.summary[0:500])

    await ctx.send(page_py.title + "\n" + page_py.summary[0:500] + "\n" + page_py.fullurl)

# wikifull command char limted 2000 does not work
# @client.command()
# async def wikifull(ctx, keyword):
#   wiki_wiki = wikipediaapi.Wikipedia(
#     language='en',
#     extract_format=wikipediaapi.ExtractFormat.WIKI
#   )
#   p_wiki = wiki_wiki.page(keyword)
#   await ctx.send(p_wiki.text)


client.run('example token')  # change token
