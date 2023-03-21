import mysql.connector
import os
import json
import pandas as pd

#Pandas table Width Increment
desired_width = 320
pd.set_option('display.width',desired_width)
pd.set_option('display.max_columns',20)
#----------------------------------------------#

root_folder = "D:/python/project/PhonePe_data/data/aggregated/transaction/country/india/state"
state_name = []
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
                        quarter = int(file.strip('.json'))
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
                                        {'state': filename, 'year': year_name,'Quarter':quarter, 'name': name,'total': total,
                                         'amount': amount})
df = pd.DataFrame(state_name,columns=['state','year','Quarter','name','total','amount'])


def Aggregated_Transaction():
    conn = mysql.connector.connect(
    host="localhost",
    user="srini",
    password="password"
    )
    # Create a cursor object
    cursor = conn.cursor()
    # Check if the database exists
    sql = "SHOW DATABASES LIKE 'testing'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="testing"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Aggregate_Transaction (ID  INTEGER  AUTO_INCREMENT PRIMARY KEY, State TEXT,YEAR INTEGER ,Quarter INTEGER,Type_Of_Transaction TEXT, Total INTEGER, Amount REAL)")
        for i,row in df.iterrows():
            sql = ("""INSERT INTO Aggregate_Transaction (State, Year, Quarter,Type_Of_Transaction, Total, Amount) VALUES(%s, %s, %s, %s, %s, %s)""")
            val = (row['state'], row['year'], row['Quarter'],row['name'], row['total'], row['amount'])
            cursor.execute(sql, val)
            conn.commit()
    else:
        conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password"
        )
    # Create a cursor object
        cursor = conn.cursor()
        sql = "CREATE DATABASE testing"
        cursor.execute(sql)
        conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="testing"
        )
        cursor = conn.cursor()
        cursor.execute(
        "CREATE TABLE Aggregate_Transaction (ID  INTEGER  AUTO_INCREMENT PRIMARY KEY, State TEXT,YEAR INTEGER ,Quarter INTEGER,Type_Of_Transaction TEXT, Total INTEGER, Amount REAL)")
        for i, row in df.iterrows():
            sql = (
                """INSERT INTO Aggregate_Transaction (State, Year,Quarter, Type_Of_Transaction, Total, Amount) VALUES(%s, %s, %s, %s, %s,%s)""")
            val = (row['state'], row['year'],row['Quarter'], row['name'], row['total'], row['amount'])
            cursor = conn.cursor()
            cursor.execute(sql, val)
            conn.commit()
        cursor.close()
        conn.close()



def Aggregated_User():
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="testing"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Aggregate_User (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER,Quarter INTEGER, Registered_Users INTEGER)")
    root_folder = "D:/python/project/PhonePe_data/data/aggregated/user/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
        file_path = os.path.join(root_folder, filename)
        if os.path.isdir(file_path):
            directory_1 = f"D:/python/project/PhonePe_data/data/aggregated/user/country/india/state/{filename}"
            for year_name in os.listdir(directory_1):
                file_path_1 = os.path.join(directory_1, year_name)
                if os.path.isdir(file_path_1):
                    root_folder_1 = f"D:/python/project/PhonePe_data/data/aggregated/user/country/india/state/{filename}/{year_name}"
                    for subdir, dirs, files in os.walk(root_folder_1):
                        for file in files:
                            file_path = os.path.join(subdir, file)
                            quarter = int(file.strip('.json'))
                            if file.endswith(".json"):
                                # Read the JSON data from the file
                                with open(file_path, 'r') as f:
                                    data = json.load(f)
                                    transaction_data = (data['data']['aggregated'])
                                    for item in transaction_data:
                                        if item == 'registeredUsers':
                                            Registered_Users = transaction_data['registeredUsers']
                                            cleaned_data.append({'State':filename,'Year':year_name,'Quarter':quarter, 'Registered_Users': Registered_Users})
    df = pd.DataFrame(cleaned_data,columns=['State','Year','Quarter','Registered_Users'])
    for i,row in df.iterrows():
        sql = ("""INSERT INTO Aggregate_User (State, Year,Quarter, Registered_Users) VALUES(%s, %s, %s, %s)""")
        val = (row['State'], row['Year'],row['Quarter'], row['Registered_Users'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()



