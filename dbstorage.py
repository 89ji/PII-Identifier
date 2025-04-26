from typing import Dict, List
from cryptography.fernet import Fernet
import sqlite3
import os
import json

class Database:
    def __init__(self):

        initDb = True
        if os.path.exists("PHI.db"):
            initDb = False

        self.connection = sqlite3.connect("PHI.db")

        if initDb:
            # Setting up tables
            self.connection.execute('''
                CREATE TABLE FernetKey (
                    Key TEXT PRIMARY KEY);''')
            
            self.connection.execute('''
                CREATE TABLE Data (
                    Hash TEXT PRIMARY KEY,
                    Data TEXT);''')

            # Setting up fernet key
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)

            keyStr = self.key.decode("utf-8")
            self.connection.execute(f"INSERT INTO FernetKey VALUES (?);", (keyStr, ))
            self.connection.commit()

        else:
            # Loading fernet key 
            result = self.connection.execute("SELECT Key FROM FernetKey;")
            for item in result:
                print(f"Found key in db: {item[0]}")
                self.key = item[0]
                self.cipher = Fernet(self.key)


    def store_phi(self, identifier, phi_lists :Dict[str, List[bytes]]):
        result = self.connection.execute("SELECT Data FROM Data WHERE Hash = ?;", (identifier, ))

        ct = 0
        for item in result:
            ct += 1

        if ct != 0:
            self.connection.execute("DELETE FROM Data WHERE Hash = ?;", (identifier, ))
            self.connection.commit()

        storeDict: Dict[str, List[str]] = {}

        for type, phi_list in phi_lists.items():
            phi_list = [self.cipher.encrypt(item).decode("utf-8") for item in phi_list]
            storeDict[type] = phi_list

        toStore = json.dumps(storeDict)
        self.connection.execute(f"INSERT INTO Data VALUES (?, ?);", (identifier, toStore, ))
        self.connection.commit()



    def retrieve_phi(self, identifier):
        result = self.connection.execute("SELECT Data FROM Data WHERE Hash = ?;", (identifier, ))

        for item in result:
            fromStore = item[0]
            dict = json.loads(fromStore)

            phi_lists = {}

            for type, phi_list in dict.items():
                phi_list = [self.cipher.decrypt(item) for item in phi_list]
                phi_lists[type] = phi_list
            return phi_lists
        
        raise Exception
    
instance: Database = Database()