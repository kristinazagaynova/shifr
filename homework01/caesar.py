import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    n = shift
    x = plaintext
    for i in x:
        if i.isalpha():
            if ((ord(i) + n > 90) and (ord(i) <= 90)) or ord(i) + n > 122 and ord(i) <= 122:
                i = chr(ord(i) - 26)
            i = chr(ord(i) + n)
        ciphertext=ciphertext+i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    n = shift
    x = ciphertext
    for i in x:
        if i.isalpha():
            if ((ord(i) - n < 65) and (ord(i) >= 65)) or ord(i) - n < 97 and ord(i) >= 97:
                i = chr(ord(i) + 26)
            i = chr(ord(i) - n)
        plaintext = plaintext + i
    return plaintext
    


