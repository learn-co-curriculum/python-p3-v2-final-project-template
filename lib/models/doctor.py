# from models.patient import Patient
from models.__init__ import CURSOR, CONN

class Doctor:
    all = {} 
    specializations = ['Cardiologist', 'Neurologist', 'Pediatrician', 'Dermatologist', 'Radiologist']

    def __init__(self, name, specialization, patient_id, id=None):
        self.name = name 
        self.specialization = specialization
        self.patient_id = patient_id
        self.id = id
        Doctor.all[id] = self

    def __repr__(self): 
        return f'<Doctor name = {self.name}>' 

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        if isinstance(patient_id, int):
            self._patient_id = patient_id
        else:
            raise TypeError("Patient ID must be an integer") 
    
    @property 
    def specialization(self): 
        return self._specialization 
    
    @specialization.setter 
    def specialization(self, new_specialization): 
        if new_specialization in Doctor.specializations: 
            self._specialization = new_specialization

# Create a table for doctor
    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS doctors ( 
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            specialization TEXT, 
            patient_id INTEGER 
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

# save db to table
    # def save(self): 
    #     sql = """ 
    #         INSERT INTO patients (name, specialization, patient_id)
    #         VALUES (?, ?, ?)
    #     """ 
    #     CURSOR.execute(sql,(self.name, self.specialization, self.patient_id)) 
    #     CONN.commit() 
    #     self.id = CURSOR.lastrowid

# save a doctor to db
    def save_doctor(self):
        sql = """
            INSERT INTO doctors (name, specialization, patient_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.specialization, self.patient_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
# create a new doctor
    @classmethod
    def create_individual_doctor(cls, name, specialization, patient_id):
        new_doctor = cls(name=name, specialization=specialization, patient_id=patient_id)
        new_doctor.save_doctor()
        return new_doctor  

    @classmethod 
    def instance_from_db(cls,row): 
        doctor = cls.all.get(row[0]) 
        if doctor: 
            doctor.name = row[1] 
            doctor.specialization = row[2] 
            doctor.patient_id = row[3] 
        else: 
            doctor = cls(name=row[1], specialization=row[2], patient_id=row[3]) 
            doctor.id = row[0] 
            cls.all[doctor.id] = doctor 
        return doctor

#get all doctors from db 
    @classmethod 
    def get_all_doctor(cls): 
        sql = "SELECT * FROM doctors"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        # for row in rows:
        #     cls.instance_from_db(row)
        #     return list(cls.all.values())
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
            

# find doctor by name in db 
    @classmethod 
    def find_by_name(cls, name): 
        sql = """ 
            SELECT * FROM doctors 
            WHERE name = ? 
        """ 
        row = CURSOR.execute(sql, (name,)).fetchone() 
        return cls.instance_from_db(row) if row else None 

#find doctor by id in db 
    @classmethod 
    def find_by_id(cls, id): 
        sql = """ 
            SELECT * FROM doctors 
            WHERE id = ? 
        """ 
        row = CURSOR.execute(sql, (id,)).fetchone() 
        return cls.instance_from_db(row) if row else None 

# delete table from db
    @classmethod 
    def drop_table(cls): 
        sql = "DROP TABLE IF EXISTS doctors" 
        CURSOR.execute(sql) 
        CONN.commit() 

# update doctor to db
    def update(self):
        sql = """
            UPDATE doctors
            SET name = ?, specialization = ?, patient_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.specialization, self.patient_id, self.id))
        CONN.commit()
        return self

# delete dr from db
    def delete(self):
        sql = "DELETE FROM doctors WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        return self
        