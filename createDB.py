from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

import sqlite3

Base = declarative_base()

#PII table
class PII(Base):
    __tablename__ = 'PII'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String)
    address = Column(String)
    allergies = Column(String)
    biometric = Column(String)
    certificate = Column(String)
    deviceidentifiers = Column(String)
    dob = Column(String)
    emailre = Column(String)
    fax = Column(String)
    hospital = Column(String)
    ipaddress = Column(String)
    labresults = Column(String)
    labels = Column(String)
    medicaid = Column(String)
    medicalrecordnumbers = Column(String)
    name = Column(String)
    phone = Column(String)
    planBeneficiaryNumber = Column(String)
    serial = Column(String)
    ssn = Column(String)
    uniqueid = Column(String)
    url = Column(String)

    files = relationship("Files", back_populates="pii")

# files table
class Files(Base):
    __tablename__ = 'Files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String)
    no_pii_text = Column(String)
    pii_id = Column(Integer, ForeignKey('PII.id'))

    pii = relationship("PII", back_populates="files")

# create/connect to exestive database
engine = create_engine('sqlite:///PII.db', echo=True)

# create those tables
Base.metadata.create_all(engine)

# create the session
Session = sessionmaker(bind=engine)
session = Session()

########################### manual entries section #########################################

# new_entry = PII(
#     id           = "0000",
#     name="John Doe",
#     emailre="john.doe@example.com",
#     phone="123-456-7890"
# )

# session.add(new_entry)
# session.commit()

# # Delete all rows in the 'Files' table
# session.query(Files).delete()

# # Delete all rows in the 'PII' table
# session.query(PII).delete()

session.commit()  # Don’t forget to commit!

######################################## example print #####################################

pii_records = session.query(PII).all()
for record in pii_records:
    print(record.id, record.name, record.emailre)

# pure SQLite here

# def createDatabase():
#     conn = sqlite3.connect('PII.db') # connect or create
#     conn.execute("PRAGMA foreign_keys = ON")
#     cursor = conn.cursor() # creating a cursor for interaction
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS PII 
#         (
#             id INTEGER PRIMARY KEY,
#             account TEXT,
#             address TEXT,
#             allergies TEXT,
#             biometric TEXT,
#             certificate TEXT,
#             deviceidentifiers TEXT,
#             dob TEXT,
#             emailre TEXT,
#             fax TEXT,
#             hospital TEXT,
#             ipaddress TEXT,
#             labresults TEXT,
#             labels TEXT,
#             medicaid TEXT,
#             medicalrecordnumbers TEXT,
#             name TEXT,
#             phone TEXT,
#             planBeneficiaryNumber TEXT,
#             serial TEXT,
#             ssn TEXT,
#             uniqueid TEXT,
#             url TEXT
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Files (
#             id INTEGER PRIMARY KEY,
#             author TEXT,
#             no_pii_text TEXT,
#             pii_id INTEGER,
#                 FOREIGN KEY (pii_id) REFERENCES PII(id)
#         )               
#     ''')

#     conn.commit()
#     conn.close()

# createDatabase()