import re
import string

f = open( "input", "r").read();
pattern = re.compile( "|".join( map( lambda char: char + char.upper() + "|" + char.upper() + char, list(string.ascii_lowercase) ) ) )
hasMore = lambda text: re.search(pattern, text) is not None

for letter in list(string.ascii_lowercase):
    text = re.sub("[" + letter + letter.upper() + "]", "", f)

    while hasMore( text ):
        text = re.sub(pattern, "", text )

    print( letter, " - ", len( text ) )
