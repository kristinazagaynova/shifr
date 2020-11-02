def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    x=plaintext
    k=keyword
    d=0
    for i in x:
            if i.isalpha():
                if ord(k[d])>=65 and ord(k[d]) <=90:
                    if (((ord(i) + ord(k[d])%65) > 90) and (ord(i) <= 90)) or (((ord(i) + ord(k[d])%65) > 122 )and (ord(i) <= 122)):
                        i=chr(ord(i)-26)
                    i=chr(ord(i)+ord(k[d])%65)
                elif ord(k[d])>=97 and ord(k[d]) <=122:
                    if (((ord(i) + ord(k[d])%97) > 90) and (ord(i) <= 90))or (((ord(i) + ord(k[d])%97)>122) and (ord(i) <= 122)):
                        i=chr(ord(i)-26)    
                    i=chr(ord(i)+ord(k[d])%97)
                d=d+1
                if d==len(k):
                    d=0
            ciphertext=ciphertext+i
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    x=ciphertext
    k=keyword
    d=0
    for i in x:
            if i.isalpha():
                if ord(k[d])>=65 and ord(k[d]) <=90:
                    if (((ord(i) - ord(k[d])%65) < 65) and (ord(i) >= 65)) or (((ord(i) - ord(k[d])%65) < 97)and (ord(i) >= 97)):
                        i=chr(ord(i)+26)
                    i=chr(ord(i)-ord(k[d])%65)
                elif ord(k[d])>=97 and ord(k[d]) <=122:
                    if (((ord(i) - ord(k[d])%97)  <65) and (ord(i) >= 65))or (((ord(i) - ord(k[d])%97)<97) and (ord(i) >= 97)):
                        i=chr(ord(i)+26)    
                    i=chr(ord(i)-ord(k[d])%97)
                d=d+1
                if d==len(k):
                    d=0
            plaintext=plaintext+i
    return plaintext
