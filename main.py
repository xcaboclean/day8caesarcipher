def encrypt(plain_text, shift_amount):
  
  cipher_text = ""
  
  for letter in plain_text:
    position  = alphabet.index(letter)
    new_position = position + shift_amount
    
    if new_position >= lenght_alphabet:
      new_position = new_position % lenght_alphabet
      
    code_cipher = alphabet[new_position]
    cipher_text += code_cipher
    
  print("The encoded text is:", encrypted_text)

def dencrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    
    if position < 0:
      new_position = lenght_alphabet + position
    code = alphabet[new_position]
    plain_text += code
  print("The decode text is:", dencrypted_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','-',' ']


lenght_alphabet = len(alphabet)

print(f"lenght_alphabet: {lenght_alphabet}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  encrypted_text = encrypt(text, shift)
elif direction =="decode":
  dencrypted_text = dencrypt(text, shift)
else:
  print("Invalid direction.")