import re
from operator import itemgetter

f = open( "input", "r").read().strip()

# once per line, run this
for line in f.split("\n"):
    matches = re.match('(\d+) players; last marble is worth (\d+) points', line )
    playerCount = int(matches[1])
    lastMarble = int(matches[2])

    plays = [0]
    players={}
    currPlayer=1
    pos = 0

    for i in range(1,lastMarble+1):
        if i % 23 == 0:
            if pos - 7 < 0:
                pos = len( plays ) - 7 + pos
            else:
                pos = pos - 7 % len( plays )

            if currPlayer not in players:
                players[currPlayer] = 0

            players[ currPlayer ] += i + plays.pop( pos )
        else:
            pos = ( pos + 2 ) % len( plays )
            plays.insert(pos, i )

        # too much noise
        #print("[",currPlayer,"] ", plays)

        currPlayer = currPlayer  % playerCount + 1

    final = sorted(players.items(), key=itemgetter(1), reverse=True )
    print( final[0][1] )