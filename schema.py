#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('vivify.db',check_same_thread=False)
cursor = connection.cursor()


create_statement = 'CREATE TABLE users(pk INTEGER PRIMARY KEY AUTOINCREMENT, business_id VARCHAR, username VARCHAR, password VARCHAR);'
cursor.execute(create_statement)

create_statement2 = 'CREATE TABLE energy(pk INTEGER PRIMARY KEY AUTOINCREMENT, business_id VARCHAR, draw FLOAT, generator_watts FLOAT, generator_fuel_hr FLOAT, max_fuel FLOAT, current_fuel FLOAT);'
cursor.execute(create_statement2)

create_statement3 = 'CREATE TABLE inventory(pk INTEGER PRIMARY KEY AUTOINCREMENT, business_id VARCHAR, inventory_type VARCHAR, inventory_class VARCHAR, quantity INTEGER, on_order INTEGER);'
cursor.execute(create_statement3)

cursor.close()
connection.close()