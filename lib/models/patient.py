from models.__init__ import CURSOR,CONN  
from models.doctor import Doctor


class Patient:
    all = {} 

    def __init__(self, name, gender, ssn, age, address, id=None): 
        self.name = name 
        self.gender = gender
        self.ssn = ssn
        self.age = age
        self.address = address
    
    def __repr__(self): 
        return f'<Patient name = {self.name}>'
    
    @property 
    def name(self): 
        return self._name 
    
    @name.setter 
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 20:
            self._name = new_name

# Create a patient table if it doesnt  exist  
    @classmethod 
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS patients ( 
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            gender TEXT,
            ssn INTEGER,
            age INTEGER, 
            address TEXT 
        )
        """ 
        CURSOR.execute(sql) 
        CONN.commit() 

# Delete a patient table  
    @classmethod 
    def drop_table(cls): 
        sql = "DROP TABLE IF EXISTS patients" 
        CURSOR.execute(sql) 
        CONN.commit() 

# Save patient to the database 
    def save(self): 
        sql = """ 
            INSERT INTO patients (name,gender,ssn,age,address)
            VALUES (?, ?, ?, ?, ?)
        """ 
        CURSOR.execute(sql,(self.name, self.gender, self.ssn, self.age, self.address)) 
        CONN.commit() 
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
       
# Create new patients into the database 
    @classmethod
    def create_individual_patient(cls,name,gender,ssn,age,address): 
        new_patient = cls(name=name, gender=gender, ssn=ssn, age=age, address=address) 
        new_patient.save() 
        return new_patient  

# Delete patients from database 
    def delete(self): 
        sql = """ 
            DELETE FROM patients 
            WHERE id = ? 
        """ 
        CURSOR.execute(sql, (self.id,)) 
        CONN.commit() 
        self.id = None 
        # del type(self).all[self.id]

# categorize the patient table
    @classmethod 
    def instance_from_db(cls,row): 
        patient = cls.all.get(row[0])  
        if patient: 
            patient.name = row[1] 
            patient.gender = row[2] 
            patient.ssn = row[3] 
            patient.age = row[4] 
            patient.address = row[5] 
        else: 
            patient = cls(name=row[1], gender=row[2], ssn=row[3], age=row[4], address=row[5]) 
            patient.id = row[0] 
            cls.all[patient.id] = patient 
        return patient


# Get all patients from database 
    @classmethod  
    def get_all(cls): 
        sql = "SELECT * FROM patients"  
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

# Finds a patient in the database 
    @classmethod 
    def find_by_id(cls,id): 
        sql = """ 
            SELECT * FROM patients 
            WHERE id = ? 
        """ 
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None 

# Finds patients by their name 
    @classmethod 
    def find_by_name(cls,name): 
        sql = """ 
            SELECT * FROM patients 
            WHERE name = ? 
        """ 
        rows = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(rows) 

# Update a patient 
    def update(self): 
        sql = """ 
        UPDATE patients 
        SET name = ?, gender = ?, ssn = ?, age = ?, address = ? 
        WHERE id = ?
        """ 
        CURSOR.execute(sql, (self.name, self.gender, self.ssn, self.age, self.address, self.id)) 
        CONN.commit()
        return self 

# list of doctors
    def doctors(self): 
        # breakpoint()
        sql = """ 
        SELECT * FROM doctors 
        WHERE patient_id = ? 
        """  
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        # breakpoint()
        CONN.commit() 
        # breakpoint()
        return [Doctor.instance_from_db(row) for row in rows]

    



        