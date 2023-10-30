def caesar(start_text, shift_amount,cipher_direction):
  final_text = ""
  if cipher_direction == "decode":
    shift_amount*= -1
    
  for letter in start_text:
    if letter in alphabet:
      position = alphabet.index(letter)  
      new_position = position + shift_amount
      if new_position >= lenght_alphabet:
        new_position = new_position % lenght_alphabet
      code= alphabet[new_position]
      final_text += code
    else:
      final_text += letter
      
  print(f"The {cipher_direction} text is:", final_text)

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


lenght_alphabet = len(alphabet)
again = False
while not again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % lenght_alphabet
  caesar(text, shift, direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    again = True
    print("Goodbye")