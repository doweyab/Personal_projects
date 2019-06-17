print("This code doesn't handle upper-case letters or punctuation.")
vowels = "eaoui"
consonants = "bcdfghjklmnpqrstvwxyz"

def get_consonant_prefix(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    i = 0
    consonant_prefix = ""
    while (consonants.find(word[i]) > -1):
        consonant_prefix += word[i]
        i += 1
    return consonant_prefix

def get_tail(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    i = 0
    consonant_prefix = ""
    while (consonants.find(word[i]) > -1):
        consonant_prefix += word[i]
        i += 1
    tail = word[i:]
    return tail

#Enter a sentence here for it to be converted to pig-latin.
print('''
it could be something like "all this pig latin is making me hungry"
''')
sentence = input("Give me a msg to translate: ")
pig_sentence = ""
for word in sentence.split(" "):
    if(vowels.find(word[0]) > -1):
        pig_sentence = pig_sentence + word + "yay "
    else:
        pig_sentence = pig_sentence + get_tail(word) + get_consonant_prefix(word) + "ay "
print(pig_sentence)