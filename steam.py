import requests
import array as arr
from replit import db

lastprice =0;

#returns json format of player's public data 
def getSteamDetails(steamid):

    req = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=F6086DBECB8E52EE9F423E64BDE57573&steamids='+steamid)

    steam_data = req.json()
    return steam_data
  

#takes the string format of data and refactors it into a dictionary
def refactorString(playersData):
  
  split = playersData.split()
  count=0
  x=1
  playerDict = {}
  for word in split:
    word = word.translate({ord('{'):None})
    word = word.translate({ord('}'):None})
    word = word.translate({ord('['):None})
    word = word.translate({ord(']'):None})
    word = word.translate({ord(','):None})
    word = word.translate({ord("'"):None})
    if(word[-1] == ':'):
        word = word[:-1]
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



def marketPrice(itemname):
  req = requests.get('http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=' + itemname)

  json_data = req.json()
  if(len(json_data) == 1 ):
    print('invalid')
    return -1
  price = json_data['lowest_price']
  return price



def checkItemExists(itemName):
  req = requests.get('http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=' + itemName)

  json_data = req.json()
  if(len(json_data) ==1 ):
      return False

  else: 
      return True


def AddItemToDatabase(itemName):
  
  itemName = itemName[:-1]
    
  if 'MarketItemList' in db.keys():
    if(itemName in db['MarketItemList']):
      print('Item already added.')
      return False
    itemList = db['MarketItemList']
    itemList.append(itemName)
    db['MarketItemList'] = itemList
  
  else: 
    db['MarketItemList'] = [itemName]
  
  print(db['MarketItemList'])
  return True


def ClearList():
  del(db['MarketItemList'])
  print(db['MarketItemList'])

def removeItemFromList(itemName):
  if 'MarketItemList' in db.keys():
    itemList = db['MarketItemList']
    itemList.remove('itemName')
    db['MarketItemList'] = itemList
    return 1
  else:
    return -1


def returnList():
  if 'MarketItemList' in db.keys():
    return db['MarketItemList']
  else:
     return -1