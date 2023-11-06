#from models.Children import Child
from models.__init__ import CURSOR,CONN


class Parent:
    all_parents=[]
    all={}
    def __init__(self,name,bio):
        self.name=name
        self._bio=bio
        Parent.all_parents.append(self)

    def __repr__(self):
        return f"<{self.name},{self.bio}>"

    # CLI can only read Print
    def my_children(self):
        child=[a.name for a in Child.spawn if a.father==self or a.mother==self]
        print(f'{self.name}\'s children are {child}')

    def get_name(self):
        return self._name

    def set_name(self,name):
        if type(name)==str:
            if len(name)>0:
                self._name=name

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self,new_bio):
        if type(new_bio)==str and len(new_bio)>15:
            self._bio=new_bio

    name=property(get_name,set_name)

    @classmethod
    def create_table(cls):
        sql="""
        create table if not exists parents(
            id INTEGER PRIMARY KEY,
            name TEXT,
            bio TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql="""
           drop table if exists parents;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name,bio):
        parent=cls(name,bio)
        parent.save()
        return parent
    
    def save(self):
        sql="""
           insert into parents(name,bio)
           values(?,?)
        """
        CURSOR.execute(sql,(self.name,self.bio))
        CONN.commit()
        self.id=CURSOR.lastrowid
    
    @classmethod
    def instance_from_db(cls,row):
        parents=cls.all.get(row[0])
        if parents:
            parents.name=row[1]
            parents.bio=row[2]
        else:
            parents = cls(row[1],row[2])
            parents.id=row[0]
            cls.all[parents.id]=parents
        return parents

    @classmethod
    def get_all_parents(cls):
        sql="""
           select * 
           from parents
        """
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row)for row in rows]

    def delete(self):
        sql="""
           delete from parents
           where id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        self.id=None
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
           select *
           from parents
           where id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    

class Child:
    spawn=[]
    all={}

    def __init__(self,name,bio,father,mother):
        self.name=name
        self._bio=bio
        self.father=father
        self.mother=mother
        Child.spawn.append(self)

    def __repr__(self):
        return f"<Name:{self.name}, Bio:{self.bio},Father:{self.father.name},Mother:{self.mother.name}>"


    def get_name(self):
        return self._name

    def set_name(self,name):
        if type(name)==str:
            if len(name)>0:
                self._name=name

    def get_father(self):
        return self._father 

    def set_father(self,parent):
        if type(parent)==Parent:
            self._father=parent
    
    def get_mother(self):
        return self._mother 

    def set_mother(self,parent):
        if type(parent)==Parent:
            self._mother=parent
    
    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self,new_bio):
        if type(new_bio)==str and len(new_bio)>15:
            self._bio=new_bio

    name=property(get_name,set_name)
    father=property(get_father,set_father)
    mother=property(get_mother,set_mother)

    @classmethod
    def create_table(cls):
        sql="""
        create table if not exists children(
            id INTEGER PRIMARY KEY,
            name TEXT,
            bio TEXT,
            father TEXT,
            mother TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql="""
           drop table if exists children;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls,name,bio,father,mother):
        child=cls(name,bio,father,mother)
        child.save()
        return child
    
    def save(self):
        sql="""
           insert into children(name,bio,father,mother)
           values(?,?,?,?)
        """
        father=str(self.father.name)
        mother=str(self.mother.name)
        CURSOR.execute(sql,(self.name,self.bio,father,mother))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    
    @classmethod
    def instance_from_db(cls,row):
        child=cls.all.get(row[0])
        if child:
            child.name=row[1]
            child.bio=row[2]
            child.father=row[3]
            child.mother=row[4]
        else:
            child = cls(row[1],row[2],row[3],row[4])
            child.id=row[0]
            cls.all[child.id]=child
        return child

    @classmethod
    def get_all_children(cls):
        sql="""
           select * 
           from children
        """
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row)for row in rows]

    def delete(self):
        sql="""
           delete from children
           where id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        self.id=None
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
           select *
           from children
           where id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_father(cls,father):
        sql="""
           select *
           from children
           where father = ?
        """
        row=CURSOR.execute(sql,(father,)).fetchall()
        #when in cli this should print "Name must be a string" as an error
        return [cls.instance_from_db(row)for row in rows]
    
    @classmethod
    def find_by_father(cls,mother):
        sql="""
           select *
           from children
           where mother = ?
        """
        row=CURSOR.execute(sql,(mother,)).fetchall()
        #when in cli this should print "Name must be a string" as an error
        return [cls.instance_from_db(row)for row in rows]
