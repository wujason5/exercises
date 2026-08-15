def find_anagrams(word, candidates):
    anagram = []
    wordl = word.lower()

    for words in candidates:
        wordsl = words.lower()
        if wordsl == wordl:
            continue
        if sorted(wordsl) == sorted(wordl):
            anagram.append(words)
    return anagram


                
                
