import mpd
import sys

scriptMode = sys.argv[1]

client = mpd.MPDClient()
client.connect('localhost', 6600)
client.password("yourmpdpasswordorcommentifyoudonthave")

if scriptMode == "previous":
    client.previous()
elif scriptMode == "playpause":
    client.pause()
elif scriptMode == "next":
    client.next()
elif scriptMode == "repeat":
    client.repeat()
elif scriptMode == "shuffle":
    client.shuffle()
