import os
import discord
import requests
import json

from discord.ext import commands

def getSteamid(username):
  req = requests.get('https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=F6086DBECB8E52EE9F423E64BDE57573&vanityurl='+username)
  
  json_data = req.json() # gets json data of steamid of given username
  id = json_data['response']["steamid"]
  return id

def getSteamDetails(steamid):

    req = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=F6086DBECB8E52EE9F423E64BDE57573&steamids='+steamid)

    steam_data = req.json()
    return steam_data

bot = commands.Bot(command_prefix='.')

@bot.command()

async def find(ctx,arg):

    req = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=F6086DBECB8E52EE9F423E64BDE57573&steamids='+arg)
    json_data = req.json()
    print(json_data)

    name = json_data["response"]['players']
    print('\n\n name \n' + name)

    jsonString = json.dumps(name)
    print("\n\n\n" + jsonString)

    string = jsonString[1:-1]
    print('\n\n\n' + string)


    



bot.run(os.environ['token'])

