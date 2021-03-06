import unittest
from rsa import RSA


class RSATest(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()
        self.message = 'And I am Iron Man'

    def test_flow(self):
        encrypt_message = self.rsa.encrypt(self.message)
        decrypt_message = self.rsa.decrypt(encrypt_message)
        self.assertEqual(self.message, decrypt_message)
