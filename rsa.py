# %%
# Get 2 prime numbers, in which the product of the two is the public key
from typing import List
import math 

class RSA:
    # Mock variables
    p =  53; q = 59; e = 3; k=2

    def __init__(self, message):
        super().__init__()
        self.encode(message)

    def encode(self, message: str) -> List[int]:
        self.encoded = []
        for letter in message:
            self.encoded.append(ord(letter))

    def encrypt(self):
        crypt_message = []
        for i in self.encoded:
            crypt_message.append(i**self.e % self.public_key)
        return crypt_message
    
    def decrypt(self, array):
        decrypt_message = []
        for i in array:
            decrypt_message.append(i**self.__private_key % self.public_key)
        return decrypt_message

    @property
    def __phi(self) -> int:
        return (self.p-1)*(self.q-1)
    
    @property
    def __private_key(self):
        return int((self.__phi*self.k+1)/self.e)

    @property
    def public_key(self) -> int:
        return self.p * self.q
# %%
