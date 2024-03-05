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

class AutoStaticMethod(staticmethod):
    # like AutoNameProperty but for creating static methods
    def __set_name__(self, cls, name):
        self.name = name

# class AutoClassMethod(classmethod):
#     def __set_name__(self, cls, name):
#         self.name = name

# type_conversions = {
#     "int": "INTEGER",
#     "str": "TEXT"
# }

# def SQL_create_table(table_name, foreign_keys=None):
# doesn't work because we need an instance to get those attributes!
# as in calling __dict__ on an instance
#     # creates classmethod that takes a table name and a dict of foreign keys
#     # as keys with the table they point to as values
#     def table_creater(cls):

#         table_contents = ""
#         for attribute in cls.__dict__.items():
#             if attribute[0] != "id":
#                 table_contents += f"\n{attribute[0]} {type_conversions[type(attribute[1]).__name__]}"
#                 if not attribute == cls.__dict__.items()[-1]:
#                     table_contents += ","
#         if foreign_keys:
#             for item in foreign_keys.items():
#                 table_contents += f"\nFOREIGN KEY ({item[0]}) REFERENCES {item[1]}(id)"
#                 if item != foreign_keys.items()[-1]:
#                     table_contents += ","

#         sql = """
#             CREATE TABLE IF NOT EXISTS {} ({})
#         """.format(table_name, table_contents)

#     # m = AutoClassMethod(table_creater)
#     return AutoClassMethod(table_creater)

def SQL_drop_table(table_name):
    # This is designed to be used as drop_table = staticmethod(SQLDropTable(sql_table_name))
    # inside of a class definition to give it a static table drop method
    # .format is used instead of sql replacement because table names can't
    # be replaced the latter way
    def dropper():
        sql = """
                DROP TABLE IF EXISTS {};
            """.format(table_name)
        CURSOR.execute(sql)
        CONN.commit()

    return AutoStaticMethod(dropper)