#Marisol Moraes & Andreas Moreno, 3/13/24, Lab 7 
import atbash 
import caesar_cipher
import check_input

def main():
  user_input = check_input.get_int_range("Secret Decoder Ring:\n1. Encrypt\n2. Decrypt\n", 1, 2)

  if user_input == 1:
    encryption_type = check_input.get_int_range("Enter encryption type:\n1. Atbash\n2. Caesar\n", 1, 2)
    message_encrypt = input("Enter message: ")
    file = open('message.txt', 'w')
    match encryption_type:

      case 1:
        c = atbash.AtbashCipher()
        message = c.encrypt_message(message_encrypt)
        file.write(message)
        print('Encrypted message saved to "message.txt".')

      case 2:
        shift_value = check_input.get_int_range('Enter shift value: ', 0, 25)
        c = caesar_cipher.CaesarCipher(shift_value)
        message = c.encrypt_message(message_encrypt)
        file.write(message)
        print('Encrypted message saved to "message.txt".')

    file.close()

  else:
    decryption_type = check_input.get_int_range("Enter decryption type:\n1. Atbash\n2. Caesar\n", 1, 2)
    file = open('message.txt', 'r')
    encrypted_message = file.read()
    file.close()

    if decryption_type == 1:
      c = atbash.AtbashCipher()
      decrypted_message = c.decrypt_message(encrypted_message)
      print('Decrepted message: ' + decrypted_message)

    else:
      shift_value = check_input.get_int_range('Enter shift value: ', 0, 25)
      c = caesar_cipher.CaesarCipher(shift_value)
      decrypted_message = c.decrypt_message(encrypted_message)
      print('Decrepted message: ' + decrypted_message)

main()

