import os
import discord
import requests
import json
import steam as st
import crypt as cp
from keep_alive import keep_alive

from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()

async def find(ctx,arg):

    if(arg == ""):
        await ctx.send("Provide a steam64ID.")
        return
    #get public data of user acc to his steam id
    json_data = st.getSteamDetails(arg)
    #get only required data from the public data
    playersData = str(json_data['response']['players'])
    #convert the string data type to dictionary
    playerDict = st.refactorString(playersData)
    #print the data
    embed = discord.Embed(
      title = playerDict['personaname'],
      description= "Steam data of "+  playerDict['personaname'] + '\nUsername : ' + playerDict['personaname'] + '\nProfile URL ' + playerDict['profileurl'] + '\n ',
      color = discord.Color.red()
    )
    embed.set_thumbnail(url =playerDict['avatarfull'])
    await ctx.send(embed = embed)
  
@bot.command()
async def crp(ctx):
    df = cp.getData()
    cryp_name = df["coin_name"]
    cryp_symbol = df['coin_symbol']
    price = df['price']
    change1h = df['percent_change_1h']
    change24h = df['percent_change_24h']
    change7d = df['percent_change_7d']

    desc = ""
    for i in range(5):
      desc += cryp_name[i] +  "\t" + cryp_symbol[i] +  "\t" + str(price[i]) +  "\t" + str(change1h[i]) + "\t" + str(change24h[i]) +  "\t" + str(change7d[i]) +'\n'


    embed1=discord.Embed(color=0xd50101 if change24h[0]<0 else 0x00ff11)
    embed1.add_field(name="**Name**", value=cryp_name[0], inline=True)
    embed1.add_field(name="Symbol", value=cryp_symbol[0], inline=True)
    embed1.add_field(name="Price", value=str(price[0]) + " $", inline=True)
    embed1.add_field(name="%Change 1H", value=str(change1h[0]), inline=True)
    embed1.add_field(name="%Change 24H", value=str(change24h[0]), inline=True)
    embed1.add_field(name="%Change 7D", value=str(change7d[0]), inline=True)
    
    await ctx.send(embed=embed1)

    embed2=discord.Embed(color=0xd50101 if change24h[1]<0 else 0x00ff11)
    embed2.add_field(name="**Name**", value=cryp_name[1], inline=True)
    embed2.add_field(name="Symbol", value=cryp_symbol[1], inline=True)
    embed2.add_field(name="Price", value=str(price[1]) + " $", inline=True)
    embed2.add_field(name="%Change 1H", value=str(change1h[1]), inline=True)
    embed2.add_field(name="%Change 24H", value=str(change24h[1]), inline=True)
    embed2.add_field(name="%Change 7D", value=str(change7d[1]), inline=True)

    await ctx.send(embed=embed2)

    embed3=discord.Embed(color=0xd50101 if change24h[2]<0 else 0x00ff11)
    embed3.add_field(name="**Name**", value=cryp_name[2], inline=True)
    embed3.add_field(name="Symbol", value=cryp_symbol[2], inline=True)
    embed3.add_field(name="Price", value=str(price[2]) + " $", inline=True)
    embed3.add_field(name="%Change 1H", value=str(change1h[2]), inline=True)
    embed3.add_field(name="%Change 24H", value=str(change24h[2]), inline=True)
    embed3.add_field(name="%Change 7D", value=str(change7d[2]), inline=True)

    await ctx.send(embed=embed3)

    embed4=discord.Embed(color=0xd50101 if change24h[3]<0 else 0x00ff11)
    embed4.add_field(name="**Name**", value=cryp_name[3], inline=True)
    embed4.add_field(name="Symbol", value=cryp_symbol[3], inline=True)
    embed4.add_field(name="Price", value=str(price[3]) + " $", inline=True)
    embed4.add_field(name="%Change 1H", value=str(change1h[3]), inline=True)
    embed4.add_field(name="%Change 24H", value=str(change24h[3]), inline=True)
    embed4.add_field(name="%Change 7D", value=str(change7d[3]), inline=True)

    await ctx.send(embed=embed4)

    embed5=discord.Embed(color=0xd50101 if change24h[4]<0 else 0x00ff11)
    embed5.add_field(name="**Name**", value=cryp_name[4], inline=True)
    embed5.add_field(name="Symbol", value=cryp_symbol[4]+ "          ", inline=True)
    embed5.add_field(name="Price", value=str(price[4]) + " $", inline=True)
    embed5.add_field(name="%Change 1H", value=str(change1h[4]), inline=True)
    embed5.add_field(name="%Change 24H", value=str(change24h[4]), inline=True)
    embed5.add_field(name="%Change 7D", value=str(change7d[4]), inline=True)
    embed5.set_footer(text="*data based on [CoinMarketCap](https://coinmarketcap.com)")
    
    await ctx.send(embed=embed5)

keep_alive()
bot.run(os.environ['token'])

