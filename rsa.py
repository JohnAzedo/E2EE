# %%
# Get 2 prime numbers, in which the product of the two is the public key
from typing import List
from sympy import sieve
from random import randint
import math 

class RSA:
    def __init__(self):
        super().__init__()
        self.e = 3 
        self.k = 2
        self.get_primes()

    def get_primes(self):
        primes = [i for i in sieve.primerange(1, 1000) if i%6 == 5]
        self.__q = primes[randint(0, len(primes))]
        self.__p = primes[randint(0, len(primes))]

    def encode(self, message: str) -> List[int]:
        encoded_message = []
        for letter in message:
            encoded_message.append(ord(letter))
        return encoded_message

    def encrypt(self, message: str) -> List[int]:
        encoded = self.encode(message)
        crypt_message = []
        for i in encoded:
            crypt_message.append(i**self.e % self.public_key)
        return crypt_message
    
    def decrypt(self, array: List[int]) -> str:
        decrypt_message = []
        for i in array:
            decrypt_message.append(i**self.__private_key % self.public_key)
        return self.decode(decrypt_message)

    def decode(self, array: List[int]) -> str:
        decoded_message = []
        for i in array:
            decoded_message.append(chr(i))
        return ''.join(decoded_message)

    @property
    def __phi(self) -> int:
        return (self.__p-1)*(self.__q-1)
    
    @property
    def __private_key(self):
        return int((self.__phi*self.k+1)/self.e)

    @property
    def public_key(self) -> int:
        return self.__p*self.__q