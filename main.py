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
  
def refactorString(playersData):
  
  split = playersData.split()
  count=0
  x=1
  playerDict = {}
  for word in split:
      word = word.translate({ord('/'):None})
      word = word.translate({ord(':'):None})
      word = word.translate({ord('{'):None})
      word = word.translate({ord('}'):None})
      word = word.translate({ord('['):None})
      word = word.translate({ord(']'):None})
      word = word.translate({ord(','):None})
      word = word.translate({ord("'"):None})
      #print(word)
      if(word == 'realname'):
          x = 0
      if(word == 'personclanid'):
          x=1
      if(count %2==0 and x ==1):
          temp = word
      
      elif(count %2 !=0 and x == 1):
          playerDict[temp] = word
      count+=1

  return playerDict


bot = commands.Bot(command_prefix='.')

@bot.command()

async def find(ctx,arg):

    req = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=F6086DBECB8E52EE9F423E64BDE57573&steamids='+arg)
    #print("\n\n raw json data\n")
    json_data = req.json()
    #print(json_data)

    playersData = str(json_data['response']['players'])
    
    playerDict = refactorString(playersData)
    embed = discord.Embed(
      title = playerDict['personaname'],
      description= "Steam data of "+  playerDict['personaname'],
      color = discord.Color.dark_green()
    )
    print( playerDict['avatar'])
    embed.set_thumbnail(url ='https://cdn.freebiesupply.com/images/large/2x/steam-logo-transparent.png')
    await ctx.send(embed = embed)

    



bot.run(os.environ['token'])

