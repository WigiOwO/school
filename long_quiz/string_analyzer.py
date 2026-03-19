def analyze_string(text):
    info = {}
    info["original"] = text
    reverse = ""
    uppers = 0
    lowers = 0
    digs = 0
    for i in range(len(text)):
        reverse += text[-(1 + i)]
        if text[i].isupper():
            uppers += 1
        elif text[i].islower():
            lowers += 1
        elif text[i].isdigit():
            digs += 1
    info["reversed"] = reverse
    info["length"] = len(text)
    info["uppercase"] = uppers
    info["lowercase"] = lowers
    info["digits"] = digs

    return info
