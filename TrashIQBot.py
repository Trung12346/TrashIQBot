from discord.ext import commands
from discord.utils import get
import discord
from random import randint
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Ready")


@client.command()
async def hello(ctx):
    choice = randint(0, 2)
    if choice == 0:
        ans = "hi"
    if choice == 1:
        ans = "hello"
    if choice == 2:
        ans = "chào anh bạn"
    await ctx.send(ans)
@client.command()

async def hi(ctx):
    choice = randint(0, 2)
    if choice == 0:
        ans = "hi"
    if choice == 1:
        ans = "hello"
    if choice == 2:
        ans = "chào anh bạn"
    await ctx.send(ans)

@client.command()
async def howgay(ctx, member: discord.Member):
    print(ctx.author)
    gay_rat = randint(0, 100)
    if gay_rat < 50:
        rate = "Thẳng rồi"
    elif gay_rat >= 50:
        rate = "Khổ thân thằng bé:_("
    gay_rat_new = "mày " + str(gay_rat) + "% gay."
#    member = get(ctx.guild.member, name = member)
    embed = discord.Embed(title = "GayRater", description = gay_rat_new, colour = discord.Colour.purple())
    embed.set_footer(text = f"{member.mention} {rate}")
    embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMsKIhugXddX09Mcacq19IrHU4jsWpCf4k0w&usqp=CAU")
    await ctx.send(embed = embed)

@client.command()
async def pingtest(ctx):
    await ctx(ctx.author.mention)

client.run(os.getenv("token"))
