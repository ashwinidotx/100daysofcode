
def CountFrequency(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890 ,."
    counter = {letter: 0 for letter in alphabets}

    for ch in sentence:
        counter[ch] += 1 
    
    for key in counter:
        if counter[key] != 0:
            if key!= ' ':
                print(str(key)+" character has "+str(counter[key])+" number of occurences.")

CountFrequency(input("Enter a Sentence: "))
