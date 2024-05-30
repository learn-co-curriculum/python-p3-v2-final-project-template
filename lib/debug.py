#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.doctor import Doctor
from models.patient import Patient

import ipdb

Doctor.drop_table()
Doctor.create_table()
Patient.drop_table()
Patient.create_table()

Patient.create_individual_patient("Joel Smith", "male", '123-45-6789', 23, "Queens NY")
Patient.create_individual_patient("Jane Doe", "female", '987-65-4321', 25, "Brentwood NY")
Patient.create_individual_patient("John Doe", "male", '111-11-1111', 30, "Flushing NY")

Doctor.create_individual_doctor("Dr. John", "Cardiologist", 1)
Doctor.create_individual_doctor("Dr. Jane", "Dermatologist", 2)
Doctor.create_individual_doctor("Dr. Bob", "Neurologist", 3)

ipdb.set_trace()
