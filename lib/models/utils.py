from __init__ import CURSOR, CONN

def custom_property(conds=None, deletable=False):
    # lets you create a property of the class it's called in 
    # by using desired_property_name = custom_property(setter_condtion_function)

    def getter(self):
        return getattr(self, f'_{p.name}')

    if conds is None:
        def setter(self, value):
            setattr(self, f'_{p.name}', value)
    else:
        def setter(self, value):
            if conds(value):
                setattr(self, f'_{p.name}', value)
            else:
                raise ValueError(f'Invalid value for {p.name}')

    if deletable:
        def deleter(self):
            delattr(self, f'_{p.name}')
    else:
        deleter = None
        
    p = AutoNameProperty(getter, setter, deleter)
    return p

class AutoNameProperty(property):
    # used in custom_property so as not to have to pass the 
    # desired property name as an argument
    def __set_name__(self, cls, name):
        self.name = name

# def SQLCreateTable():

#     def creater(self):
        
#         sql = """
#             CREATE TABLE IF NOT EXISTS employees (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             job_title TEXT,
#             department_id INTEGER,
#             FOREIGN KEY (department_id) REFERENCES departments(id))
#         """

#     m = AutoNameProperty(creater)

# class AutoMakeSQL(classmethod):
#     def __set_name__(self, cls, name):
#             self.name = name
# def SQLDropTable(table_name):
#     # def dropper_wrapper(self):
#     #     @classmethod
#     def dropper(cls):
#         sql = """
#                 DROP TABLE IF EXISTS ?;
#             """
#         CURSOR.execute(sql, (table_name,))
#         CONN.commit()

#     # p = AutoMakeSQL(dropper)
#     # return p
#     return dropper