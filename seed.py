#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('vivify.db',check_same_thread=False)
cursor = connection.cursor()


create_statement = '''INSERT INTO users (business_id,username,password) VALUES ("buss-01","rick_ross","imabawse");'''
cursor.execute(create_statement)

create_statement2 = '''INSERT INTO energy (business_id,draw,generator_watts, generator_fuel_hr, max_fuel, current_fuel) 
                    VALUES ("buss-01",1200,2000,1.2,100,85);'''
cursor.execute(create_statement2)

create_statement3 = '''INSERT INTO inventory (business_id, inventory_type,inventory_class,quantity,on_order) 
                    VALUES ("buss-01","water pump","honda",100,200);'''
cursor.execute(create_statement3)

create_statement4 = '''INSERT INTO inventory (business_id, inventory_type,inventory_class,quantity,on_order) 
                    VALUES ("buss-01","portapotty","shitter",5,100);'''
cursor.execute(create_statement4)

create_statement5 = '''INSERT INTO inventory (business_id, inventory_type,inventory_class,quantity,on_order) 
                    VALUES ("buss-01","u bends","max-pipes",7,200);'''
cursor.execute(create_statement5)



connection.commit()
cursor.close()
connection.close()