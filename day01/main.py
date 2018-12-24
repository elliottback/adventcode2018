f = open( "input", "r")

contents = f.read()

lines = contents.split("\n")
shift = 0;

for line in lines:
    shift += int(line)

print(shift)