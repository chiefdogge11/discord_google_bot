
import time
import discord
from discord.ext import commands
import json
import requests
#from googlesearch import search
import aiohttp
# from flask_cors import CORS, cross_origin
import asyncio
#from search_engine_parser import GoogleSearch
#from gsearch.googlesearch import search

client = commands.Bot(command_prefix='-')

TOKEN = 'ODIwMjIyNjUyODcwNDI2NjU1.YEyB3w.hZ1YeqBGmrLRiN8DH7s__9y5m4I'

# app = Flask(name)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# async def googlesearch(keyword, size):
#   query = keyword
#   results = []
#   for i in search(query, tld ="co.in",num=size , stop = size, pause = 2):
#     print("i was here")
#     results.append(i)
#   print(results)
#   return results

# ------------------------------------------ bot functions


@client.event
async def on_ready():
    print('Bot is ready. only search once every 30 seconds')


@client.command()
async def ping(ctx, keyword, size):
    await ctx.send("It works {} and {}".format(keyword, size))


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
        for i in range(3):
            links.append(data["RelatedTopics"][i]["FirstURL"])
        print(links)
        await ctx.send(links)
# async def on_message(message):
#     if message.content.startswith('search'):
#         searchContent = ""
#         print("i was here")
#         text = str(message.content).split(' ')
#         print("i was here2")
#         for i in range(2, len(text)):
#             searchContent = searchContent + text[i]
#             print(searchContent)
#             print("i was here3")

#         for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
#             await message.channel.send(j)
#             print(j)
#             print("i was here4")

    # query = keyword
    # results = []
    # x = await search(query, tld ="co.in",num=size , stop = size, pause = 2)
    # for i in x:
    #   print("i was here")
    #   results.append(i)
    # await ctx.send("It works {} and {}".format(keyword, size))
    # print(search(query, tld ="co.in",num=size , stop = size, pause = 2))
    # #print(results)
    # await ctx.send(results)


client.run('ODIwMjIyNjUyODcwNDI2NjU1.YEyB3w.hZ1YeqBGmrLRiN8DH7s__9y5m4I')
