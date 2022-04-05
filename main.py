import discord

TOKEN = 'OTYwMzM5OTg3OTM1NjkwNzUy.YkpATw.aP9hARFVf5c2VexfQOr4ZHIxwKI'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return 

    if user_message.lower() == '!sf':
        await message.channel.send(f'Hey {username}, did you want food recs or things to do?')

    if user_message.lower() == 'food':
        embed = discord.Embed()
        embed.description = "Here's my personal yelp list! https://www.yelp.com/collection/SipP2Y4RtJDGEFKZKWDqww/SF"
        await message.channel.send(embed=embed)
        return

    if user_message.lower() == 'fun':
        embed = discord.Embed()
        embed.description = "Here's a link to trip advisor! https://www.tripadvisor.com/Tourism-g60713-San_Francisco_California-Vacations.html"
        await message.channel.send(embed=embed)
        return
        # await message.channel.send("Here's my personal yelp list.")
            
            
            
    



client.run(TOKEN)