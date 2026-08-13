def is_pangram(sentence):
    sentence = sentence.lower()
    return all(letter in sentence for letter in "abcdefghijklmnopqrstuvwxyz")
    
