
f = open( "input", "r")

contents = f.read()

lines = contents.split("\n")

for i in range( 0 , len(lines[0] ) ):
    mash = set()
    for line in lines:
        line = line[:i] + line[(i+1):]
        if( line in mash ):
            print(line)
            exit(0)
        mash.add(line)
