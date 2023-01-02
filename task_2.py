def my_split(text):

    result = []
    word = ""

    for letter in text:
        if letter != " ":
           word += letter
        elif word != "":
            result.append(word)
            word = ""
     
    if word != "":
        result.append(word)

      
    return result
