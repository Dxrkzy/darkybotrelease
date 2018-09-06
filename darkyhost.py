#Hi there!
#Iam the creator of the bot
#If you see this message it will most likely be that i gave you permission to it
#Feel free2add me on discord!
#My tag is Dxrkzy#4783
#Have Fun!

#imports(don't mess with it)
import discord
import itertools
import youtube_dl
from youtube_dl import YoutubeDL
import sys
import traceback
from async_timeout import timeout
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
import datetime
import traceback
import logging
from itertools import cycle
import os
#prefix                       #commands_prefix means the prefix of the bot, feel free 2 change that :)
bot = commands.Bot (command_prefix=commands.when_mentioned_or('.'))
status = ['.info for help', 'coded by dxrkzy', 'DarkyBot is lit', 'i can play music aswell :D', 'New version is nongey', 'i love oofing', 'how about NO! :D', 'version 1.0.2', 'esskeetit', 'esskeetit','Dxrkzy#4783 Is ALLMIGHTY', "Who said bots can't be lit?"]

api = str(os.environ.get('RIOT_KEY'))

async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

#startup screen in python, better not change it.
players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@bot.event
async def on_ready():
    print("Loadin... Please wait!")
    print("Thank You For Using My Bot :3")
    print("Bot Fully loaded!")
    print("ID:" + bot.user.id)
    print("Name:" + bot.user.name)
    print("Dxrkzy Our Soul And Our Saviour :)")

#bot commands, if you mess up here the bot might not work properly!
@bot.command(pass_context=True)
@commands.has_any_role('PokeMaster')
async def purge(ctx, amount=999):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say('**Done!** :wave:')

@bot.command(pass_context=True)
async def oof(ctx):
    while True:
        await bot.say("**Fidget Spinners :joy:**")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'fidget spinner' in message.content.lower():
        await bot.send_message(message.channel, "**Never talk about that ever again!:angry: They are my Soul and My Heart D:**")
    if message.author == bot.user:
        return
    if 'hi' in message.content.lower():
        await bot.send_message(message.channel, "**Welcome! :smile:**")
    if 'bot' in message.content.lower():
        await bot.send_message(message.channel, "**For any help try contacting @Dxrkzy#4783 :smile:**")
    if 'darkybot' in message.content.lower():
        await bot.send_message(message.channel, "**For any help try contacting @Dxrkzy#4783 :smile:**")
    if 'dxrkzy' in message.content.lower():
        await bot.send_message(message.channel, "**Don't You Dare Call His Name! :angry:**")
    if 'darkybot' in message.content.lower():
        await bot.send_message(message.channel,"**What do you want!:angry:**")
    if 'trashcan' in message.content.lower():
        await bot.send_message(message.channel, "**Trashcan, You mean your house :D***")
    if 'fuck' in message.content.lower():
        await bot.delete_messages(mgs)
        await bot.send_message(message.channel,"**Don't curse in here!:angry:**")

    await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx):
    	channel = ctx.message.channel
    	t1 = time.perf_counter()
    	await bot.send_typing(channel)
    	t2 = time.perf_counter()
    	embed=discord.Embed(title="**NoPong4u**!", description='But it took {}ms :unamused:.'.format(round((t2-t1)*1000)), color=0x8B008B)
    	await bot.say(embed=embed)

case = 0

def caseno():
    global case
    caseno += 1
    return case

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member, args=None):

    if not args:
        embed = discord.Embed(title='Ban Command' + str(case), timestamp=datetime.datetime.utcnow(), color=0x8B008B)
        embed.add_field(name='User', value='{}'.format(user.name) + '#{}'.format(user.discriminator) + ' (<@{}>)'.format(user.id))
        embed.add_field(name='Moderator', value='{}'.format(ctx.message.author.name) + '#{}'.format(ctx.message.author.discriminator))
        embed.add_field(name='Reason', value='None')
        embed.set_footer(text='{}'.format(user.name) + '#{} **is banned, and you enjoyed it!**'.format(user.discriminator))
        embed.set_thumbnail(url=user.avatar_url)
    else:
        embed = discord.Embed(title='Ban | Case #' + str(case), timestamp=datetime.datetime.utcnow(), color=0x8B008B)
        embed.add_field(name='User', value='{}'.format(user.name) + '#{}'.format(user.discriminator) + ' (<@{}>)'.format(user.id))
        embed.add_field(name='Moderator', value='{}'.format(ctx.message.author.name) + '#{}'.format(ctx.message.author.discriminator))
        embed.add_field(name='Reason', value=' '.join(args).replace('/{}/g', "He probably didn't behave pretty well. OOF :joy:"))
        embed.set_footer(text='{}'.format(user.name) + '#{} **is banned, and you enjoyed it!**'.format(user.discriminator))
        embed.set_thumbnail(url=user.avatar_url)

    await bot.send_message(discord.Object(id='486559331282845710'), embed=embed)
    await bot.ban(user)


@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
    pass
    """kick a user from the server but man, don't be too mean ;-;"""
    await bot.kick(userName)
    await bot.say(" Annoying kid got kicked :smile:")

@bot.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
        title = 'Help/info',
        description = 'Information about DarkyBot',
    )

    embed.set_author(name='Help/info About me :D')
    embed.add_field(name='.purge', value=' purge messages >2, <100', inline=False)
    embed.add_field(name='.ping', value='shows your ping', inline=False)
    embed.add_field(name='.kick @user reason', value='kick user', inline=False)
    embed.add_field(name='.ban @user reason', value='ban user', inline=False)
    embed.add_field(name='.join', value='let the bot join vc', inline=False)
    embed.add_field(name='.play url', value='play music through YT-url', inline=False)
    embed.add_field(name='.queue url', value='puts url into queue', inline=False)
    embed.add_field(name='.pause', value='pauses music', inline=False)
    embed.add_field(name='.resume', value='resumes music', inline=False)
    embed.add_field(name='.stop', value='stops music', inline=False)
    embed.add_field(name='.dc', value='disconnects bot', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/484779813031116803/485396657362567178/20180901_123238.png')


@bot.command(pass_context=True)
async def privatecmdxd(ctx):
    embed = discord.Embed(
        title = 'OOF',
        description = 'Please someone kill me :D',

    )

    embed.set_author(name="very gey")
    embed.add_field(name="call me very gay pls", value='Xal is also very gay', inline=False)
    embed.add_field(name="so are you very nongey?", value='ySe', inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/484779813031116803/485396657362567178/20180901_123238.png")
    embed.set_image(url='https://cdn.discordapp.com/attachments/484779813031116803/485396657362567178/20180901_123238.png')

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def join(ctx):
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    await bot.join_voice_channel(channel)


@bot.command(pass_context=True)
async def leave(ctx, voice_client: discord.VoiceClient):
    voice_client = bot.voice_client_in(server)
    await discord.VoiceClient.disconnect()


@bot.command(pass_context=True)
async def play(ctx, *, args):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player("ytsearch:"+ args, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.volume = 0.6
    player.start()
    await bot.say("**Song is now playing**")

@bot.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@bot.command(pass_context=True)
async def queue(ctx, *, args):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player= await voice_client.create_ytdl_player("ytsearch:"+ args, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await bot.say('**Song Entered The Queue :smile:**')

@bot.command(pass_context=True)
async def dc(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    await bot.say('**Bot Left The Channel :wave:**')

@bot.command()
@commands.has_any_role('eboladezecmdmagniemand')
async def logout():
    await bot.say('**logging out, please wait...**')
    await bot.say('~~See you Later :D~~')
    await bot.logout()

bot.loop.create_task(change_status())
bot.run(str(os.environ.get('BOT_TOKEN')))
