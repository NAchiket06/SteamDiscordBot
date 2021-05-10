import requests


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