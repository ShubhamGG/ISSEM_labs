#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def decrypt(s, text):
    message = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha: 
            letterindex = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letterindex]
        else:
            result = result + letter
    return result
 
#check the above function


text = "COOKIE"
s = 3
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
print ("Decrypted" + decrypt(s, text))