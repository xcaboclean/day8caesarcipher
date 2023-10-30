def caesar(start_text, shift_amount,cipher_direction):
  final_text = ""
  if cipher_direction == "decode":
    shift_amount*= -1
    
  for letter in start_text:
    position = alphabet.index(letter)
     
    new_position = position + shift_amount
    
    if new_position >= lenght_alphabet:
       new_position = new_position % lenght_alphabet
    
    code= alphabet[new_position]
    final_text += code
  
  print(f"The {cipher_direction} text is:", fi'nal_text)

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','-',' ']


lenght_alphabet = len(alphabet)

print(f"lenght_alphabet: {lenght_alphabet}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)