from models.__init__ import CURSOR, CONN

class AutoNameProperty(property):
    # used in custom_property so as not to have to pass the 
    # desired property name as an argument
    def __set_name__(self, cls, name):
        self.name = name

class AutoStaticMethod(staticmethod):
    # like AutoNameProperty but for creating static methods
    def __set_name__(self, cls, name):
        self.name = name

class AutoClassMethod(classmethod):
    # like AutoNameProperty but for creating class methods
    def __set_name__(self, cls, name):
        self.name = name

def check_nonempty_str(value, string): 
    if not isinstance(value, str):
        raise TypeError(f"{string} must be a string.")
    if not value:
        raise ValueError(f"{string} must not be empty")
    return True

def custom_property(conds=None, deletable=False):
    # lets you create a property of the class it's called in 
    # by using desired_property_name = custom_property(setter_condition_function)

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

def SQL_drop_table(table_name):
    # This is designed to be used as drop_table = SQLDropTable(sql_table_name)
    # inside of a class definition to give it a static table drop method
    # .format is used instead of sql replacement because table names can't
    # be replaced the latter way
    def dropper():
        sql = f"""
            DROP TABLE IF EXISTS {table_name};
        """
        CURSOR.execute(sql)
        CONN.commit()

    return AutoStaticMethod(dropper)

def SQL_delete(table_name):
    def delete(self):
        sql = f"""
            DELETE FROM {table_name}
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        # the dict has to be called working_insts!!!!
        del type(self).working_insts[self.id]

        # Set the id to None
        self.id = None

    return delete

def SQL_get_all():
    # use this with get_all = SQL_get_all()
    # for this one it was easy to take table_name out as an arg because the class will have that field anyways
    def get_all(cls):
        sql = f"""
            SELECT *
            FROM {cls.table_name}
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    return AutoClassMethod(get_all)

def SQL_show_all():
    def show_all(cls):
        for item in cls.get_all():
            print(item)
    return AutoClassMethod(show_all)

# def SQL_print_all_names():
#     def print_all_names(cls): 
#         return [obj.name for obj in cls.get_all()]
#     return AutoClassMethod(print_all_names)

def punctuate_str(list, get_name = False):
    # note!!!! this is using the object, NOT the table row
    # set get_name to True when you want to print out the name attributes from (band) objects
    if len(list) == 1:
        return list[0] if not get_name else list[0].name
    if len(list) == 2:
        return f'{list[0]} and {list[1]}' if not get_name else f'{list[0].name} and {list[1].name}'
    with_and = list.copy() # there is probably a less intensive way than this
    if get_name: 
        with_and = [obj.name for obj in with_and]
    with_and[-1] = f'and {with_and[-1]}'
    return ', '.join(with_and)

def SQL_find_by_attribute(attribute_name, fetch_one=True):
    # use this with find_by_{attribute name here} = SQL_find_by_attribute(attribute_name) to make a method where you input the value for that attribute
    # and look through the table for a match (can set fetch_one to False if you want to get all matches)
    def finder(cls, attribute_value):
        sql = f"""
            SELECT *
            FROM {cls.table_name}
            WHERE {attribute_name} = ?
        """

        row = CURSOR.execute(sql, (attribute_value,)).fetchone() if fetch_one else CURSOR.execute(sql, (attribute_value,)).fetchall()
        # from concert import Concert
        # if cls == Concert and row:
        #     # this is kind of sloppy but i like it more than having this whole method in Concert for each attr
        #     from city import City
        #     print(row)
        #     new_row = (*row[:3], City.find_by_id(row[3]), row[4])
        #     return cls.instance_from_db(new_row)
        return cls.instance_from_db(row) if row else None

    # finder.__name__ = f'find_by_{attribute}'
    return AutoClassMethod(finder)

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