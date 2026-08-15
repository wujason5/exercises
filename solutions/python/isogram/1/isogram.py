def is_isogram(phrase):
    repeat = []
    phrase = phrase.lower()
    for i in phrase:
        if i.isalpha():
            if i not in repeat:
                repeat.append(i)
            else:
                return False
    return True
            
            
