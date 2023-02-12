import mysql.connector
import os
import json
# Connect to the database

def Aggregated_Transaction():
    conn = mysql.connector.connect(
    host="localhost",
    user="srini",
    password="password"
    )

    # Create a cursor object
    cursor = conn.cursor()
    # Check if the database exists
    sql = "SHOW DATABASES LIKE 'Phone_Pe'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="Phone_Pe"
        )
        root_folder = "D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state"
        state_name = []
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Aggregate_Transaction (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT,YEAR INTEGER ,Type_Of_Transaction TEXT, Total INTEGER, Amount REAL)")
        for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                if file.endswith(".json"):

                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = data['data']['transactionData']
                                        # Transform the data to extract the relevant information
                                        for item in transaction_data:
                                            name = item['name']
                                            total = item['paymentInstruments'][0]['count']
                                            amount = item['paymentInstruments'][0]['amount']
                                            state_name.append(
                                                {'state': filename, 'year': year_name, 'name': name, 'total': total,
                                                 'amount': amount})
        for item_1 in state_name:
            sql = ("""INSERT INTO Aggregate_Transaction (State, Year, Type_Of_Transaction, Total, Amount) VALUES(%s, %s, %s, %s, %s)""")
            val = (item_1['state'], item_1['year'], item_1['name'], item_1['total'], item_1['amount'])
            cursor.execute(sql, val)
            conn.commit()
    else:
        sql = "CREATE DATABASE Phone_Pe"
        cursor.execute(sql)
        conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="Phone_Pe"
        )
        root_folder = "D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state"
        state_name = []
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Aggregate_Transaction (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT,YEAR INTEGER ,Type_Of_Transaction TEXT, Total INTEGER, Amount REAL)")
        for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = data['data']['transactionData']
                                        # Transform the data to extract the relevant information
                                        for item in transaction_data:
                                            name = item['name']
                                            total = item['paymentInstruments'][0]['count']
                                            amount = item['paymentInstruments'][0]['amount']
                                            state_name.append(
                                                {'state': filename, 'year': year_name, 'name': name, 'total': total,
                                                 'amount': amount})
        for item_1 in state_name:
            sql = ("""INSERT INTO Aggregate_Transaction (State, Year, Type_Of_Transaction, Total, Amount) VALUES(%s, %s, %s, %s, %s)""")
            val = (item_1['state'], item_1['year'], item_1['name'], item_1['total'], item_1['amount'])
            cursor.execute(sql, val)
            conn.commit()


    # Close the cursor and connection
    cursor.close()
    conn.close()
