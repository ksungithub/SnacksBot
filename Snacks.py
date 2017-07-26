import discord
import asyncio
import random
import json
import urllib3
import requests
import os
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands

'''Disables the SSL warning, that is printed to the console.'''
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print ("Bot Online!")
    print ("Name: {}".format(client.user.name))
    print ("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='type !commands')) 

 
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True)
async def commands(ctx):
    await client.say("!ping, !joinv, !play, !stop, !getbans, !connect, !disconnect, !clear, !roles, !games")


@client.command(pass_context=True)
async def games(ctx):
    await client.say("At the moment, these games are available: !guess")

@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '/n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

@client.command()
async def joinv(*, chid):
	ytturl = 'https://www.youtube.com/watch?v=EqWRaAF6_WY'
	ytturl = str.strip(ytturl)
	global chid2
	chid2 = client.get_channel(chid)
	global voice
	voice = await client.join_voice_channel(chid2)
	global player
	player = await voice.create_ytdl_player(ytturl)
	player.start() 
	player.volume = 0.0 

@client.command()
async def play(*, yturl: str):
	global yturl2
	yturl2 = yturl
	if player.is_playing():
		player.stop()
		await startpl()
	else:
		await startpl()
		
async def startpl():
	global player
	player = await voice.create_ytdl_player(yturl2)
	player.start()
	player.volume = 0.01

@client.command()
async def stop():
	player.stop()

@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = []
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

@client.command(pass_context=True)
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += role.name + ", " 
	await client.say(result)


'''@client.event
async def guess(ctx):
    if message.author == client.user:
        return
    await client.send_message(message.channel, 'Guess a number between 1 to 10')
    def guess_check(m):
        return m.content.isdigit()
    guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
    answer = random.randint(1, 10)
    if guess is None:
        fmt = 'Sorry, you took too long. It was {}.'
        await client.send_message(message.channel, fmt.format(answer))
        return
    if int(guess.content) == answer:
        await client.send_message.channel, ('You are right!')
    else:
        await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))''' 


client.run("MzMxNjc1NDc5MTg4NzAxMTg3.DEqxnA.Pg8fWaFajcAlSQUXYFtffuiy5cE")




