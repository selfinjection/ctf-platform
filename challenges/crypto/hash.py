import hashlib

WORDS = ['crypted', 'encrypted']

def hash_text(text):
    hash = hashlib.sha256()
    hash.update(text.encode())
    return hash.hexdigest()

def crack_hash(hash_value, words):
    for word in words:
        word = word.strip()
        if hash_value == hash_text(word):
            return word
    return None

def main():
    hash_value = '954d1bb83d80bb6f6e746b28f0de3ec4c4ed980cfe67ed23a9159cd464ff339a'
    original_text = crack_hash(hash_value, WORDS)
    print(f'The original text is: {original_text}')

main()