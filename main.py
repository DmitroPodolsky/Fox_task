def word_frequency(args: list) -> dict:
    answer = {}
    for words in args:
        if not words:
            answer['']= 1 if '' not in answer else answer['']+1
        words = words.replace('.','').replace(',','').lower()
        for word in words.split(): answer[word] = 1 if word not in answer else answer[word]+1
    return answer
print(word_frequency(["The quick brown fox","jumps over the lazy dog.","The dog barks,","and the fox runs away."]))