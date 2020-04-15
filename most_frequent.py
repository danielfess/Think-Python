def most_frequent(str):
    """Prints (letter, frequency) of decreasing frequency in a string.

    str: string

    output: None
    """

    d = dict()
    str_new = ''.join(str.lower().split())
    for letter in str_new:
        d[letter] = d.setdefault(letter,0) + 1
    items = d.items()
    invert_dict = []
    for letter, freq in items:
        invert_dict.append((freq, letter))
    invert_dict.sort()
    for freq, letter in invert_dict[::-1]:
        print(freq,letter)

print('English:')
most_frequent("Students compile a collection of their texts in a variety of genres over time and choose two pieces to present for summative assessment. In the majority of cases, the work in the student’s collection will arise from normal classwork, as the examples below illustrate. The annotations capture insights by the student’s teacher, using the features of quality, with a view to establishing the level of achievement the text reflects. The purpose of the annotations is to make the teacher's thinking visible. The annotations were confirmed by the Quality Assurance group, consisting of practicing English teachers and representatives of the Inspectorate, the SEC and JCT.")

print('French:')
most_frequent("Maître Corbeau, sur un arbre perché,Tenait en son bec un fromage.Maître Renard, par l’odeur alléché,Lui tint à peu près ce langage :« Hé ! bonjour, Monsieur du Corbeau.Que vous êtes joli ! Que vous me semblez beau !Sans mentir, si votre ramageSe rapporte à votre plumage,Vous êtes le Phénix des hôtes de ces bois. »A ces mots le Corbeau ne se sent pas de joie ;Et pour montrer sa belle voix,Il ouvre un large bec, laisse tomber sa proie.Le Renard s’en saisit, et dit : « Mon bon Monsieur,Apprenez que tout flatteurVit aux dépens de celui qui l’écoute :Cette leçon vaut bien un fromage, sans doute.Le Corbeau, honteux et confus,Jura, mais un peu tard, qu’on ne l’y prendrait plus.")










