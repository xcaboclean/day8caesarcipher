def encrypt(text, shift):
  cipher_text = ""
  for position in range(len(text)):
    letter = text[position]
    new_position = alphabet.index(letter) + shift
    if new_position >= lenght_alphabet:
      new_position = new_position % lenght_alphabet
    code_cipher = alphabet[new_position]
    cipher_text += code_cipher
  print(cipher_text)

def dencrypt(cipher_text, shift):
  text = ""
  for position in range(len(cipher_text)):
    letter = cipher_text[position]
    new_position = alphabet.index(letter) - shift 
    if new_position < 0:
      new_position = lenght_alphabet + new_position
    code = alphabet[new_position]
    text += code
  print(text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenght_alphabet = len(alphabet)
print(f"lenght_alphabet: {lenght_alphabet}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  encrypted_text = encrypt(text, shift)
  print("The encoded text is:", encrypted_text)
else:
  dencrypted_text = dencrypt(text, shift)
  print("The decode text is:", dencrypted_text)