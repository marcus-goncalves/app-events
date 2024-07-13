import string
import unidecode

def convert_key(name: str) -> str:
    return unidecode.unidecode(name).lower().translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")