def is_palindrome(text:str):
    cleanText = text.replace(" ", "").lower()
    for i in range(len(cleanText)):
        if cleanText[i] != cleanText[-(1 + i)]:
            return False
    return True

print("is nhamor a palindrome? -> ", is_palindrome("nhamor"))