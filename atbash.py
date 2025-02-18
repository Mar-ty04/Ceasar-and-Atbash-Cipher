from cipher import Cipher


class AtbashCipher(Cipher):
  def _encrypt_letter(self, letter):
    return chr((-1 * (ord(letter) - 64) % 26)+65)

  def _decrypt_letter(self, letter):
    return self._encrypt_letter(letter)