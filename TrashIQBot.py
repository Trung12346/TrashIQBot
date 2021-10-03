from discord.ext import commands
import discord
from random import randint

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Ready")


@client.command()
async def hello(message):
    choice = randint(0, 2)
    if choice == 0:
        ans = "hi"
    if choice == 1:
        ans = "hello"
    if choice == 2:
        ans = "chào anh bạn"
    await message.send(ans)
@client.command()

async def hi(message):
    choice = randint(0, 2)
    if choice == 0:
        ans = "hi"
    if choice == 1:
        ans = "hello"
    if choice == 2:
        ans = "chào anh bạn"
    await message.send(ans)

@client.command()
async def howgay(message):
    gay_rat = randint(0, 100)
    if gay_rat < 50:
        rate = "Thẳng rồi"
    elif gay_rat >= 50:
        rate = "Khổ thân thằng bé:_("
    gay_rat = str(gay_rat)
    get_id = int(message.author.mention.replace("!", "").replace("<", "").replace(">", "").replace("@", ""))
    gay_rat_new = "mày " + gay_rat + "% gay."
    embed = discord.Embed(title = "GayRater", description = gay_rat_new, colour = discord.Colour.purple())
    embed.set_footer(text = f"{client.get_user(get_id)}{rate}")
    embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMsKIhugXddX09Mcacq19IrHU4jsWpCf4k0w&usqp=CAU")
    await message.send(embed = embed)

@client.command()
async def pingtest(message):
    await message(message.author.mention)

client.run("ODk0MDEwMTg4OTk3MjIyNDkx.YVjx3g.kHd4udh7dAd7-OUPVOEVk1t-7rQ")