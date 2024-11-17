import string
decrypted_text = ""
encrypted_text = "edr"
shift =3
alphabet = string.ascii_lowercase
alphabet_list = []
for char in alphabet:
    alphabet_list.append(char)
for char in encrypted_text:
    i = alphabet_list.index(char) - shift
    print(alphabet_list[i])
    if i < 0:
        i = abs(i + len(alphabet_list))
    decrypted_text += alphabet_list[i]