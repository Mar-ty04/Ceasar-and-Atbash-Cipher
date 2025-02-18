import cipher

class CaesarCipher(cipher.Cipher):
  def __init__(self, shift):
    super().__init__()
    self.shift = shift

  def _encrypt_letter(self, letter):
    return chr(((ord(letter) - 64 + self.shift) % 26)+64) 

  def _decrypt_letter(self, letter):
    return chr(((ord(letter) - 64 - self.shift) % 26)+64) 
