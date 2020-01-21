def rotate_word(word,int):
    """Encrypts (word) using a Caesar cypher, rotating word by the integer (int).
    """
    
    new_word = ''
    for letter in word:
        if 97 <= ord(letter.lower()) <= 122 :
            new_letter = chr((int + ord(letter.lower())-ord('a'))%26 + ord('a'))
        else:
            new_letter = letter
        new_word = new_word + new_letter
    return new_word

encrypted_joke = "Uv gurer. Guvf vf abg ernyyl wbxr. Whfg univat fbzr sha jvgu gubfr jub pna'g ebg13 na negvpyr. Gb or ernyyl zrna, sbyybj-hc gb guvf negvpyr jvgu fbzrguvat yvxr 'Obl, gung jnf gur shaavrfg wbxr V rire urneq!' Stush"

print(rotate_word(encrypted_joke,-13))


