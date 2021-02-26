# %%
# Get 2 prime numbers, in which the product of the two is the public key

class RSA:
    # Mock variables
    p =  53; q = 59; e = 3; k=2

    def encrypted(self):
        pass

    def phi(self) -> int:
        return (self.p-1)*(self.q-1)
    
    @property
    def private_key(self) -> float:
        return (self.k*self.phi() + 1)/self.e

    @property
    def public_key(self) -> int:
        return self.p * self.q
