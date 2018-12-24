import re
import string

f = open( "input", "r").read();
pattern = re.compile( "|".join( map( lambda char: char + char.upper() + "|" + char.upper() + char, list(string.ascii_lowercase) ) ) )
hasMore = lambda text: re.search(pattern, text) is not None

while hasMore( f ):
    f = re.sub(pattern, "", f )

print( len( f ) )