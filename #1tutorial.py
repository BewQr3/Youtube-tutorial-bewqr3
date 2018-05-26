import discord
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "Z")

@client.event
async def on_ready():
    print(client.user.name)
    print("------------")
#so these are just basically on_ready stuff so the these will be printed as soon as bot is ready..

#now making some basic commands
@client.command(pass_context=True)
async def hi(ctx):
    await client.say("Hey! :wave:")

client.run("your token here")
# you will need to add your token here
#This token can get you full control to a bot, so better not give it to the wrong person...
