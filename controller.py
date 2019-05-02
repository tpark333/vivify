#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
import json
from model import Model 
import subprocess
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


DATABASE = 'vivify.db'  


@app.route('/dashboard', methods=['GET', 'POST'])
def database_render():
    if request.method == 'GET':
        # business_id = DB CALL TO GET BUS ID DEPENDING ON USERNAME (sessions?) 
        with Model(DATABASE) as db:         
            db.cursor.execute('''
            SELECT business_id, draw, generator_watts,generator_fuel_hr,max_fuel,current_fuel
            FROM energy
            WHERE business_id = "buss-01";
            ''')
            energy_data = db.cursor.fetchall()
            

            db.cursor.execute('''
            SELECT inventory_type,inventory_class,quantity,on_order
            FROM inventory
            WHERE business_id = "buss-01";
            ''')
            inventory_data = db.cursor.fetchall()
        
        business_id = energy_data[0][0]
        draw = energy_data[0][1]
        generator_watts = energy_data[0][2]
        generator_fuel_hr = energy_data[0][3]
        max_fuel = energy_data[0][4]
        current_fuel = energy_data[0][5]

        inventory_type = [] 
        inventory_class = []
        quantity = []
        on_order = []
        
        for i in range(0,len(inventory_data)):
            inventory_type.append(inventory_data[i][0]) 
        for i in range(0,len(inventory_data)):
            inventory_class.append(inventory_data[i][1])
        for i in range(0,len(inventory_data)):
            quantity.append(inventory_data[i][2])
        for i in range(0,len(inventory_data)):
            on_order.append(inventory_data[i][3])

        energy_json = {}
        inventory_json = {}
        

        energy_json['energy']=[{"draw":draw,"generator_watts":generator_watts,
        "generator_fuel_hr":generator_fuel_hr,"max_fuel":max_fuel,"current_fuel":current_fuel}]

        for i in range(0,len(inventory_data)):
            inventory_json['inventory'+str(i)]=[{"inventory_type":inventory_type[i],"inventory_class":inventory_class[i],
            "quantity":quantity[i],"on_order":on_order[i]}]

        return jsonify({"one":[energy_json],"two":[inventory_json]})
        
#need to add sessions, key (generate key)
#add login
#add register
#inventory, employee, energy,order,supplier
#LOOK INTO PAYMENT API!!!
#hash and salt passwords?? is it necessary
#datetime library to turn into normal time from unix
        
        
        




        


if __name__ == '__main__':
    app.run(debug=True)

