from models.__init__ import CONN, CURSOR


class Drink_Orders:
    def __init__(self, customer_name, customer_id, drink_name, drink_id, quantity=1):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.drink_name = drink_name
        self.drink_id = drink_id
        self.quantity = quantity

    @classmethod
    def create_order(cls, customer_name, customer_id, drink_name, drink_id):
        # Check if the customer has already ordered this drink
        existing_order = CURSOR.execute('''
            SELECT quantity FROM drink_orders
            WHERE customer_id = ? AND drink_id = ?
        ''', (customer_id, drink_id)).fetchone()

        if existing_order:
            # If the drink exists, update the quantity
            new_quantity = existing_order[0] + 1
            CURSOR.execute('''
                UPDATE drink_orders
                SET quantity = ?
                WHERE customer_id = ? AND drink_id = ?
            ''', (new_quantity, customer_id, drink_id))
            CONN.commit()
            print(f"{customer_name} has ordered another {drink_name}. New quantity: {new_quantity}")
        else:
            CURSOR.execute('''
                INSERT INTO drink_orders (customer_name, customer_id, drink_name, drink_id, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (customer_name, customer_id, drink_name, drink_id, 1))
            CONN.commit()
            print(f"Order for {customer_name} - {drink_name} added to the database.")
    
    @classmethod
    def delete_orders(cls, customer_id):
        sql = "DELETE FROM drink_orders WHERE customer_id = ?"
        CURSOR.execute(sql, (customer_id,))
        CONN.commit()

    @classmethod
    def find_by_customer(cls, customer_id):
        sql = '''
        SELECT * FROM drink_orders
        WHERE customer_id = ?
        '''
        rows = CURSOR.execute(sql, (customer_id,)).fetchall()
        if rows:
            return rows
        else:
            return None
