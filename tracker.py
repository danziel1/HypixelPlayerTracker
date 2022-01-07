import requests
import json
import time


names = [
'player1',
'player2',
'player3'
] # set to the names you want to track
key = 'api key' # set this to your api key [/api new]
webhook = 'webhook url' # set this to your webhook url
delay = 15 # seconds in delay between checking people's stats. This is to avoid rate limits (120 requests/min)!
print("Starting")

while True:
  for player in names:
    time.sleep(1) # fixes error from spamming hypixel api
    print(f"Checking {player}")
    try:
      getuuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}').json()
      uuid = getuuid['id']
    except:
      print(f"{player} doesn't seem to exist! Douple check your spelling.")
    params = {'key':key, 'uuid':uuid}
    getstats = requests.get('https://api.hypixel.net/player', params=params).json()
    duels = getstats['player']['stats']['Duels']
    bedwars = getstats['player']['stats']['Bedwars']
    # get current games played, set to 0 if haven't played yet
    
    # DUELS
    try:
        duelsplayed = str(duels['games_played_duels'])
    except:
        duelsplayed = '0'
    try:
        classic = str(duels['classic_duel_rounds_played'])
    except:
        duelsclassic = '0'
    try:
        duelssumo = str(duels['sumo_duel_rounds_played'])
    except:
        duelssumo = '0'
    try:
        duelssw = str(duels['sw_duel_rounds_played'])
    except:
        duelssw = '0'
    try:
        duelsbridge = str(duels['bridge_duel_rounds_played'])
    except:
        duelsbridge = '0'
    try:
        duelsboxing = str(duels['boxing_duel_rounds_played'])
    except:
        duelsboxing = '0'
    try:
        duelsop = str(duels['op_duel_rounds_played'])
    except:
        duelsop = '0'
    try:
        duelsuhc = str(duels['uhc_duel_rounds_played'])
    except:
        duelsuhc = '0'
    try:
        duelsparkour = str(duels['parkour_eight_rounds_played'])
    except:
        duelsparkour = '0'
        
        
    # BEDWARS
    try:
        bwplayed = str(bedwars['games_played_bedwars'])
    except:
        bwplayed = '0'
    try:
        bwsolo = str(bedwars['eight_one_games_played_bedwars'])
    except:
        bwsolo = '0'
    try:
        bwdouble = str(bedwars['eight_two_games_played_bedwars'])
    except:
        bwdouble = '0'
    try:
        bwtripple = str(bedwars['four_three_games_played_bedwars'])
    except:
        bwtripple = '0'
    try:
        bwquad = str(bedwars['four_four_games_played_bedwars'])
    except:
        bwquad = '0'
    try:
        bwfourvfour = str(bedwars['two_four_games_played_bedwars'])
    except:
        bwfourvfour = '0'
    stored = False
    
    try: # check if player is stored
        datafile = open(f'./data/{player}.json', 'r')
        datafile.close()
        try: # gets old stats
            datafile = open(f'./data/{player}.json', 'r')
            data = json.load(datafile)
            
            oldduelsplayed = data[player]['duelsplayed']
            oldduelsclassic = data[player]['duelsclassic']
            oldduelssumo = data[player]['duelssumo']
            oldduelssw = data[player]['duelssw']
            oldduelsbridge = data[player]['duelsbridge']
            oldduelsboxing = data[player]['duelsboxing']
            oldduelsop = data[player]['duelsop']
            oldduelsuhc = data[player]['duelsuhc']
            oldduelsparkour = data[player]['duelsparkour']
            
            oldbwplayed = data[player]['bwplayed']
            oldbwsolo = data[player]['bwsolo']
            oldbwdouble = data[player]['bwdouble']
            oldwbtripple = data[player]['bwtripple']
            oldbwquad = data[player]['bwquad']
            oldbwfourvfour = data[player]['bwfourvfour']
            
            
            datafile.close()
            stored = True
        except Exception as e: # if you get an error here, please report it!
            print(e)
            
    except: # if player not stored > creates file
        datafile = open(f'./data/{player}.json', 'w')
        dump = {player:{"duelsplayed":duelsplayed,"duelsclassic":classic,"duelssumo":duelssumo,"duelssw":duelssw,"duelsbridge":duelsbridge,"duelsboxing":duelsboxing,"duelsop":duelsop,"duelsuhc":duelsuhc,"duelsparkour":duelsparkour,"bwplayed":bwplayed,"bwsolo":bwsolo,"bwdouble":bwdouble,"bwtripple":bwtripple,"bwquad":bwquad,"bwfourvfour":bwfourvfour}}
        json.dump(dump, datafile)
        datafile.close()
        print(f"Adding {player} to database.")

    if stored: # if player was stored > overrides data
        
        if duelsplayed > oldduelsplayed:
            datafile = open(f'./data/{player}.json', 'w')
            dump = {player:{"duelsplayed":duelsplayed,"duelsclassic":classic,"duelssumo":duelssumo,"duelssw":duelssw,"duelsbridge":duelsbridge,"duelsboxing":duelsboxing,"duelsop":duelsop,"duelsuhc":duelsuhc,"duelsparkour":duelsparkour,"bwplayed":bwplayed,"bwsolo":bwsolo,"bwdouble":bwdouble,"bwtripple":bwtripple,"bwquad":bwquad,"bwfourvfour":bwfourvfour}}
            json.dump(dump, datafile)
            datafile.close()
            

            
            # checks for what the new game was
            if int(oldduelsclassic) < int(duelsclassic):
                mode = 'Classic Duels'
                oldmodewins = oldduelsclassic
                newmodewins = classic
            elif int(oldduelssumo) < int(duelssumo):
                print("1")
                mode = 'Sumo Duels'
                oldmodewins = oldduelssumo
                newmodewins = duelssumo
            elif int(oldduelssw) < int(duelssw):
                mode = 'Skywars Duels'
                oldmodewins = oldduelssw
                newmodewins = duelssw
            elif int(oldduelsbridge) < int(duelsbridge):
                mode = 'Bridge Duels'
                oldmodewins = oldduelsbridge
                newmodewins = duelsbridge
            elif int(oldduelsboxing) < int(duelsboxing):
                mode = 'Boxing Duels'
                oldmodewins = oldduelsboxing
                newmodewins = duelsboxing
            elif int(oldduelsop) < int(duelsop):
                mode = 'OP Duels'
                oldmodewins = oldduelsop
                newmodewins = duelsop
            elif int(oldduelsuhc) < int(duelsuhc):
                mode = 'UHC Duels'
                oldmodewins = oldduelsuhc
                newmodewins = duelsuhc
            elif int(oldduelsparkour) < int(duelsparkour):
                mode = 'Parkour Duels'
                oldmodewins = oldduelsparkour
                newmodewins = duelsparkour
                
        if bwplayed > oldbwplayed:
            datafile = open(f'./data/{player}.json', 'w')
            dump = {player:{"duelsplayed":duelsplayed,"duelsclassic":classic,"duelssumo":duelssumo,"duelssw":duelssw,"duelsbridge":duelsbridge,"duelsboxing":duelsboxing,"duelsop":duelsop,"duelsuhc":duelsuhc,"duelsparkour":duelsparkour,"bwplayed":bwplayed,"bwsolo":bwsolo,"bwdouble":bwdouble,"bwtripple":bwtripple,"bwquad":bwquad,"bwfourvfour":bwfourvfour}}
            json.dump(dump, datafile)
            datafile.close()    
            # BEDWARS
            if int(oldbwsolo) < int(bwsolo):
                mode = 'Bedwars Solo'
                oldmodewins = oldbwsolo
                newmodewins = bwsolo
            elif int(oldbwdouble) < int(bwdouble):
                mode = 'Bedwars Doubles'
                oldmodewins = oldbwdouble
                newmodewins = bwdouble
            elif int(oldwbtripple) < int(bwtripple):
                mode = 'Bedwars Tripples'
                oldmodewins = oldbwdouble
                newmodewins = bwdouble
            elif int(oldbwquad) < int(bwquad):
                mode = 'Bedwars Quads'
                oldmodewins = oldwbtripple
                newmodewins = bwtripple

            elif int(oldbwfourvfour) < int(bwfourvfour):
                mode = 'Bedwars 4v4'
                oldmodewins = oldbwfourvfour
                newmodewins = bwfourvfour
            else:
                print(f"> {player} Unknown mode")
                mode = 'UNKNOWN'
                oldmodewins = 'UNKNOWN'
                newmodewins = 'UNKNOWN'
                pass
            
            # webhook send
            data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
            result = requests.post(webhook, json = data)


        else: # if someone wasn't updated
            pass
        
  print(f"Finished checking {len(names)} players! Sleeping {delay} seconds.\n-----\n")
  time.sleep(delay)
