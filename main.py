import discord

TOKEN = 'OTYwMzM5OTg3OTM1NjkwNzUy.YkpATw.aP9hARFVf5c2VexfQOr4ZHIxwKI'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Hey there')


client.run(TOKEN)