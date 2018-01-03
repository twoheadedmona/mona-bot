# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import safygiphy
import requests
import io

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot",
             command_prefix="!", pm_help=True)

giphy = safygiphy.Giphy()
players = {}
# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' +
          str(len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(
        discord.__version__, platform.python_version()))
    print('--------')


@client.event
async def on_message(message):
    member = message.author
    emb = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
    if message.content.startswith('!test'):
        await client.send_message(member, 'Test')

    if message.content.startswith('!hi'):
        await client.send_message(message.channel, embed=emb)

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, ":ping_pong: Pong!")

    if message.content.startswith('!bye'):
        await client.send_message(message.channel, 'bye cruel world')
        await    client.logout()
        await    client.close()

    if message.content.startswith('!8ball'):
        msg = message.content.replace("!8ball", "").lstrip().rstrip()
        ballsays = ":8ball: says: "
        if message.content.endswith("?"):
            if msg[:2] == 'wh' or msg[0] == 'h':
                await client.send_message(message.channel, embed=discord.Embed(
                    title = ballsays + "I'm sorry, I can't answer that",
                    description ="Ask me a yes or no question, and make sure you use **?** ",
                    color=0x0099ff
                ))
            else:
                answers = ("It is certain :8ball:",
                           "It is decidedly so :8ball:",
                           "Without a doubt :8ball:",
                           "Yes, definitely :8ball:",
                           "You may rely on it :8ball:",
                           "As I see it, yes :8ball:",
                           "Most likely :8ball:",
                           "Outlook good :8ball:",
                           "Yes :8ball:",
                           "Signs point to yes :8ball:",
                           "Reply hazy try again :8ball:",
                           "Ask again later :8ball:",
                           "Better not tell you now :8ball:",
                           "Cannot predict now :8ball:",
                           "Concentrate and ask again :8ball:",
                           "Don't count on it :8ball:",
                           "My reply is no :8ball:",
                           "My sources say no :8ball:",
                           "Outlook not so good :8ball:",
                           "Very doubtful :8ball:")
                embed = discord.Embed(title= ballsays,
                                      description=random.choice(answers),
                                      color=0x0099ff)
                await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(message.channel, embed=discord.Embed(
                title = ballsays + "Ask me a question",
                description = "And make sure you use **?**",
                color = 0x0099ff
            ))
    
    if message.content.startswith("!coin"):
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, "\U000026AA")
        else:
            await client.add_reaction(message, "\U000026AB")

            
    if message.content.startswith("!gif"):
        gif_tag = message.content.replace("!gif", "").lstrip().rstrip()
        rgif = giphy.random(tag = str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.startswith('!play '):

        # yt_url = message.content[6:]
        channel = message.author.voice.voice_channel
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player("https://www.youtube.com/watch?v=MAzp5fMJTtk")
        # players[message.server.id] = player
        player.start()

            


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

# This is a basic example of a call and response command. You tell it do "this" and it does it.


# @client.command()
# async def ping(*args):
#     await client.say(":ping_pong: Pong!")


# @client.command()
# async def bye(*args):
#     await client.say('bye cruel world')
#     await client.logout()


# @client.command()
# async def users(*args):
#     msg = "Bots:\n"
#     for user in client.get_all_members():
#         if user.bot:
#             msg += '{0.mention}\n'.format(user)
#         else:
#             await client.say(user.mention)
#     await client.say(msg)

# @client.command(pass_context=True)
# async def hey(ctx, value):
#     embed = discord.Embed(description = "What's cooking", color = 0xffee00)
#     if value == "you":
#         await client.say(embed=embed)
#     else:
#         pass


client.run('MzkwMTQ4MTU2NjQzNjA2NTQ5.DRJ9kA.XeXwoR8FdY2fQnJoq12qCK_90iI')

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
