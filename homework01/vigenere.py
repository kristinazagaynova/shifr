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
                if ord(k[d % len(k)]) >= 65 and ord(k[d % len(k)]) <= 90:
                    s = ord(k[d % len(k)]) - 65
                elif ord(k[d % len(k)]) >= 97 and ord(k[d % len(k)]) <= 122:
                    s = ord(k[d % len(k)]) - 97
                if ord(i)>=65 and ord(i)<=90:
                    i = chr((((ord(i) - 65) + s) % 26) + 65)
                if ord(i)>=97 and ord(i)<=122:
                    i = chr((((ord(i) - 97) + s) % 26) + 97
            d=d+1
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
                if ord(k[d % len(k)]) >= 65 and ord(k[d % len(k)]) <= 90:
                    s = ord(k[d % len(k)]) - 65
                elif ord(k[d % len(k)]) >= 97 and ord(k[d % len(k)]) <= 122:
                    s = ord(k[d % len(k)]) - 97
                if ord(i)>=65 and ord(i)<=90:
                    i = chr((((ord(i) - 65) - s) % 26) + 65)
                if ord(i)>=97 and ord(i)<=122:
                    i = chr((((ord(i) - 97) - s) % 26) + 97)
            d=d+1
            plaintext=plaintext+i
    return plaintext
