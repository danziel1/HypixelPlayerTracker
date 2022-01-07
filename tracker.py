import requests
import json
import time

names = ['player1', 'player2'] # set to the names you want to track
key = 'key' # set this to your api key [/api new]
webhook = 'webhookt url' # set this to your webhook url
delay = 15 # seconds in delay between checking people's stats. This is to avoid rate limits (120 requests/min)!
print("Starting")

while True:
  for player in names:
    getuuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}').json()
    uuid = getuuid['id']
    params = {'key':key, 'uuid':uuid}
    getstats = requests.get('https://api.hypixel.net/player', params=params).json()
    stats = getstats['player']['stats']['Duels']
    
    # get current games played, set to 0 if haven't played yet
    try:
        played = str(stats['games_played_duels'])
    except:
        played = '0'
    try:
        classic = str(stats['classic_duel_rounds_played'])
    except:
        classic = '0'
    try:
        sumo = str(stats['sumo_duel_rounds_played'])
    except:
        sumo = '0'
    try:
        sw = str(stats['sw_duel_rounds_played'])
    except:
        sw = '0'
    try:
        bridge = str(stats['bridge_duel_rounds_played'])
    except:
        bridge = '0'
    try:
        boxing = str(stats['boxing_duel_rounds_played'])
    except:
        boxing = '0'
    try:
        op = str(stats['op_duel_rounds_played'])
    except:
        op = '0'
    try:
        uhc = str(stats['uhc_duel_rounds_played'])
    except:
        uhc = '0'
    try:
        parkour = str(stats['parkour_eight_rounds_played'])
    except:
        parkour = '0'
    old = False
    
    try: # check if player is stored
        datafile = open(f'./data/{player}.json', 'r')
        datafile.close()
        try: # gets old stats
            datafile = open(f'./data/{player}.json', 'r')
            data = json.load(datafile)
            
            oldplayed = data[player]['played']
            oldclassic = data[player]['classic']
            oldsumo = data[player]['sumo']
            oldsw = data[player]['sw']
            oldbridge = data[player]['bridge']
            oldboxing = data[player]['boxing']
            oldop = data[player]['op']
            olduhc = data[player]['uhc']
            oldparkour = data[player]['parkour']

            datafile.close()
            old = True
        except Exception as e: # if you get an error here, please report it!
            print(e)
            
    except: # if player not stored > creates file
        datafile = open(f'./data/{player}.json', 'w')
        dump = {player:{"played":played,"classic":classic,"sumo":sumo,"sw":sw,"bridge":bridge,"boxing":boxing,"op":op,"uhc":uhc,"parkour":parkour}}
        json.dump(dump, datafile)
        datafile.close()

    if old: # if player was stored > overrides data
        
        if played > oldplayed:
            datafile = open(f'./data/{player}.json', 'w')
            dump = {player:{"played":played,"classic":classic,"sumo":sumo,"sw":sw,"bridge":bridge,"boxing":boxing,"op":op,"uhc":uhc,"parkour":parkour}}
            json.dump(dump, datafile)
            datafile.close()
            

            
            # checks for what the new game was
            if int(oldclassic) < int(classic):
                mode = 'classic'
                oldmodewins = oldclassic
                newmodewins = classic
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldsumo) < int(sumo):
                mode = 'sumo'
                oldmodewins = oldsumo
                newmodewins = sumo
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldsw) < int(sw):
                mode = 'skywars'
                oldmodewins = oldsw
                newmodewins = sw
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldbridge) < int(bridge):
                mode = 'bridge'
                oldmodewins = oldbridge
                newmodewins = bridge
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldboxing) < int(boxing):
                mode = 'boxing'
                oldmodewins = oldboxing
                newmodewins = boxing
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldop) < int(op):
                mode = 'op'
                oldmodewins = oldop
                newmodewins = op
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(olduhc) < int(uhc):
                mode = 'uhc'
                oldmodewins = olduhc
                newmodewins = uhc
                data = {
                "content" : f"{player} is playing {mode}\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            elif int(oldparkour) < int(parkour):
                mode = 'parkour'
                oldmodewins = oldparkour
                newmodewins = parkour
                data = {
                "content" : f"{player} is playing {mode}.\n({oldmodewins} > {newmodewins})"
                }
                result = requests.post(webhook, json = data)
            else:
                print(f"{player} played an unknown duel REPORT THIS.") # if it shows this make a report on the github pls ;)


        else: # if someone wasn't updated
            pass
        
  print(f"Finished checking players!\nSleeping {delay} seconds.")
  time.sleep(delay)
