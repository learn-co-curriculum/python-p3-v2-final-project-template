from models.__init__ import CURSOR, CONN

class Address:
    def __init__(self, email:str, person_id:int):
        self.email = email
        self.person_id = person_id

    def __repr__(self):
        return f"Address(email={self.email}, person_id={self.person_id})"
       
    def __create_table__():
        sql = """create table addresses (
            id INTEGER NOT NULL, 
            email VARCHAR(30) NOT NULL, 
            person_id INTEGER NOT NULL, 
            PRIMARY KEY (id),
            FOREIGN KEY(person_id) REFERENCES contacts (id)
        );
        """
        CURSOR.execute(sql)

    # def save(self, CURSOR, contact_id):
    #     if self.id is None:
    #         sql = "INSERT INTO addresses (contact_id, email) VALUES (?, ?)"
    #         CURSOR.execute(sql, (contact_id, self.email))
    #         self.id = CURSOR.lastrowid
        
    def create(email:str, person_id:int):
        sql = "INSERT INTO addresses (email, person_id) VALUES (?, ?)"
        c = CURSOR.execute(sql, (email, person_id))
        CONN.commit()
        return c.lastrowid
    
    def read_by_person_id(person_id:int):
        sql = "select (id, email, person_id) from addresses where person_id = ?"
        return CURSOR.execute(sql, (person_id,))
    
    def read_all():
        sql = "select id, email, person_id from addresses"
        rows = CURSOR.execute(sql)
        ret = []
        for (id, email, person_id) in rows:
            addr = Address(email, person_id)
            addr._id = id
            ret.append(addr)
        return ret
    
    def update_email(new_email:str):
        pass
    
    def update_person_id(person_id:int):
        pass
    