import discord
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

#discord login token
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client = commands.Bot(command_prefix='.')
client.remove_command("help")

#yelp api key
api_key = os.getenv('yelp_api_key')

headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'  



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
        await ctx.send("Looks like you didn't put in a real city or type of food. (Ex: .food burlingame korean)")

@client.command()
async def help(ctx):
    embed = discord.Embed()
    embed.description = "Hey! This is just a simple yelp bot that gives you some food recs in the city of your choice. Try using .food [INSERT CITY HERE] [INSERT FOOD TYPE HERE]"
    await ctx.send(embed = embed)
            



client.run(TOKEN)

#put number of reviews
#