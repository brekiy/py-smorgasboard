def shift_letter(letter: chr, amount: int) -> chr:
    a_ascii = ord('a')
    return chr(a_ascii + (((ord(letter.lower()) - a_ascii) + amount) % 26))

def shift_cipher(message: str, amount: int) -> str:
    return "".join([shift_letter(x, amount) for x in message])

print(shift_cipher("ncevy", 13), shift_cipher("gpvsui", 25), shift_cipher("ugflgkg", -18) + shift_cipher("wjmmf", -1))
