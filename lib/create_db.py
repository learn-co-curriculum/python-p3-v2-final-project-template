from models.contact import Contact
from models.address import Address
from random import randint

if __name__ == "__main__":
    Contact.__create_table__()
    Address.__create_table__()