
def count_vowels_and_consonants(text: str) -> dict:
    dic=dict()
    a="unli"
    for x in text:
        x=x.lower()
        if x == "a" or x== "e" or x== "i" or x== "o" or x== "u":
            dic.setdefault(a,0)
            dic[a] += 1 
    return dic
            


print(count_vowels_and_consonants("sulaymonov bunyodi"))



