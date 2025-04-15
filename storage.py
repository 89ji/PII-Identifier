from cryptography.fernet import Fernet

class Database:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.storage = {}
        instance = self

    def store_phi(self, identifier, phi_lists):
        self.storage[identifier] = {} 

        for type, phi_list in phi_lists.items():
            phi_list = [self.cipher.encrypt(item) for item in phi_list]
            self.storage[identifier][type] = phi_list

    def retrieve_phi(self, identifier):
        phi_lists = {}
        for type, phi_list in self.storage[identifier].items():
            phi_list = [self.cipher.decrypt(item) for item in phi_list]
            phi_lists[type] = phi_list
        return phi_lists
    
instance: Database = None