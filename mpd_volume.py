import mpd
import sys

scriptMode = sys.argv[1]

client = mpd.MPDClient()
client.connect('localhost', 6600)
client.password("yourmpdpasswordorcommentifyoudonthave")

volLvl = int(client.status()['volume'])

if scriptMode == "up":
    volLvl += 1
    client.setvol(volLvl)
elif scriptMode == "down":
    volLvl -= 1
    client.setvol(volLvl)
elif scriptMode == "mute":
    volLvl = 0
    client.setvol(volLvl)
