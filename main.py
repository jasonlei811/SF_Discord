import discord
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands
#discord login token
TOKEN = 'OTYwMzM5OTg3OTM1NjkwNzUy.YkpATw.aP9hARFVf5c2VexfQOr4ZHIxwKI'

client = discord.Client()
client = commands.Bot(command_prefix='.')
client.remove_command("help")

#yelp api key
api_key = os.getenv('yelp_api_key')

headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'  


# @client.event
# async def on_ready():
#     try:
#         print('We have logged in as {0.user}'.format(client))
#         city = "burlingame"
#         food_type = "korean"

#         params={'term': food_type, 'location': city}  
#         req = requests.get(url, params=params, headers=headers)
#         parsed = json.loads(req.text)

#         embed = discord.Embed()
#         channel = client.get_channel(960313523324452906)
#         await channel.send('Here are some options!')
#         # message = ''
#         message = ''
#         for business in parsed['businesses'][0:15]:
#             business_name = business['name']
#             business_rating = business['rating']
#             business_link = business['url']
#             message += (f'[{business_name}]({business_link}) - {str(business_rating)}\n\n')
#         embed.description = message
#         await channel.send(embed=embed)
#     except KeyError:
#         await channel.send("Looks like you didn't put in a real city or type of food. (Ex: /food burlingame korean)")


"""
to do: send in one whole message instead of one by one
bonus points: send as an embed
#done 

to do: parse city for user
example: if user puts sf or SF or san fran, location should be "san francisco"


to do: if search yields 0 results, return an error
bonus points: add suggestions to bot's reply (ex. "here are some suggestions: "mexican", "korean", etc.)
#done

to do: make a .help command to help user (bot should return a message showing how to use commands)
#done

if you're bored: 
    - add an extra argument to command in case user wants to sort by reviews or location
    - if you are working with embeds, add hyperlinks to results so that user can click on result to open yelp page
#done
"""
@client.command()
async def food(ctx, arg1, arg2):
    try:
        city = arg1
        food_type = arg2
        if city == 'sf' or 'SF':
            city == 'san francisco'

        params={'term': food_type, 'location': city}  
        req = requests.get(url, params=params, headers=headers)
        parsed = json.loads(req.text)

        embed = discord.Embed()
        
        await ctx.send('Here are some options!')
        message = ''
        for business in parsed['businesses'][0:15]:
            business_name = business['name']
            business_rating = business['rating']
            business_link = business['url']
            message += (f'[{business_name}]({business_link}) - {str(business_rating)}\n\n')
        embed.description = message
        await ctx.send(embed=embed)
    except KeyError:
        await ctx.send("Looks like you didn't put in a real city or type of food. (Ex: /food burlingame korean)")

@client.command()
async def help(ctx):
    embed = discord.Embed()
    embed.description = "Hey! This is just a simple yelp bot that gives you some food recs in the city of your choice. Try using .food [INSERT CITY HERE] [INSERT FOOD TYPE HERE]"
    await ctx.send(embed = embed)

# or:

# @commands.command()
# async def test(ctx):
#     pass

# bot.add_command(test)

# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}: {user_message} ({channel})')

#     if message.author == client.user:
#         return 

#     if user_message.lower() == '!sf':
#         await message.channel.send(f'Hey {username}, did you want food recs or things to do?')

#     if user_message.lower() == 'food':
#         response = await message.channel.send(f"What kind of food are you looking for? {username}")
        
#         params={'term':{response}, 'location': 'San Francisco'}  
#         req = requests.get(url, params=params, headers=headers)
#         parsed = json.loads(req.text)
        

#         for business in parsed['businesses']:
#             print(business)
#             business_name = business['name']
#             business_rating = business['rating']
#             await message.channel.send(business_name, '-', business_rating)
        
        # embed = discord.Embed()
        # embed.description = "Here's my personal yelp list! https://www.yelp.com/collection/SipP2Y4RtJDGEFKZKWDqww/SF"
        # await message.channel.send(embed=embed)
        # return

    
    
    # if user_message.lower() == 'fun':
    #     embed = discord.Embed()
    #     embed.description = "Here's a link to trip advisor! https://www.tripadvisor.com/Tourism-g60713-San_Francisco_California-Vacations.html"
    #     await message.channel.send(embed=embed)
    #     return
    #     # await message.channel.send("Here's my personal yelp list.")
            
            
            
    



client.run(TOKEN)