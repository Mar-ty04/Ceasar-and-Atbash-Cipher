import abc


class Cipher(abc.ABC):
  def __init__(self):
    self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  
  @property
  def alphabet(self):
    return self._alphabet

  
  def encrypt_message(self, message): 
    message = message.upper()
    encrypted_message = ''
    for char in message:
        if char in self._alphabet:
            encrypted_message += self._encrypt_letter(char)
        else:
            encrypted_message += char
    return encrypted_message
  
  def decrypt_message(self, message):
    message = message.upper()
    decrypted_message = ''
    for char in message:
        if char in self._alphabet:
            decrypted_message += self._decrypt_letter(char)
        else:
            decrypted_message += char
    return decrypted_message

  @abc.abstractmethod
  def _encrypt_letter(self, letter):
    raise NotImplementedError()

  @abc.abstractmethod
  def _decrypt_letter(self, letter):
    raise NotImplementedError()


  