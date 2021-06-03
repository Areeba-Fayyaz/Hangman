def update_dashes(secret,dashes,guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == guess:
            result = result+guess
        else:
            result = result +dashes[i]
    return result
