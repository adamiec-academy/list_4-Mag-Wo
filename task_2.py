def my_split(text):

    list = []
    word = ""

    for letter in text:
        if letter != " ":
           word += letter
        elif word != "":
            list.append(word)
            word = ""

      
    return list
