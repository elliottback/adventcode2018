f = open( "input", "r")

contents = f.read()

lines = contents.split("\n")
shift = 0;
freq = set()

while 1:
    for line in lines:
        shift += int(line)
        if shift in freq :
            print( shift )
            exit(0)
        else:
            freq.add( shift )
