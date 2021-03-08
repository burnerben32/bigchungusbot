import discord
from discord.ext import commands
import json
import os

# prefix
client = commands.Bot(command_prefix=">")

# >helpme section
@client.command()
async def helpme(ctx):
    embed=discord.Embed(title="BigChungusBot Help Center", color=discord.Color.green())
    embed.add_field(name=">penis", value="find out big chungus's true penis size.")
    embed.add_field(name=">boobs", value="find out big chungus's opinion on boobs.")
    embed.add_field(name=">helpme", value="silly you already know this command.")
    embed.add_field(name=">mrg", value=("mrg as in most real guns, use this command to find who has the most REAL guns."))
    embed.add_field(name=">amogus", value=("Use this command to find the sus imposter(this is a reference to the popular game among us)"))
    embed.add_field(name=">baziga", value="Secret command only high tech ops know, oh shit nvm its on the public help list now.")
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print("Big Chungus is ready for war.")

@client.command()
async def penis(ctx):
    await ctx.send("5FT IN LENGTH")

@client.command()
async def boobs(ctx):
    embed=discord.Embed(title="I Love Boobies", description="i really love boobies", color=discord.Color.red())
    await ctx.send(embed=embed)


@client.command()
async def mrg(ctx):
    await ctx.send("Of course Tristian has the most real guns! Silly goose.")

@client.command()
async def amogus(ctx):
    embed=discord.Embed(title="There Is A Chungus Among Us!", url="https://www.youtube.com/watch?v=8-NcrRzH0vA", description="Click this link for more!")
    await ctx.send(embed=embed)

@client.command()
async def bazinga(ctx):
    await ctx.send("bazonga")

# token fetching

with open("token.json", "r") as TOKEN_OPEN :
    TOKEN = json.load(TOKEN_OPEN)

for realTOKEN in TOKEN :
    print("token fetched")

client.run(realTOKEN)