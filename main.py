alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenght_alphabet = len(alphabet)
print(f"lenght_alphabet: {lenght_alphabet}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
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


encrypted_text = encrypt(text, shift)
print("The encoded text is:", encrypted_text)


dencrypted_text = dencrypt("hnanqnefynts", shift)
print("The decode text is:", dencrypted_text)