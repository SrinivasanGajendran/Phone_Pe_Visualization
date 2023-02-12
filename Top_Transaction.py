import os
import json
import mysql.connector

def Top_Transaction_Districts():
    conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="Phone_pe"
        )
    cursor = conn.cursor()
    #cursor.execute("CREATE TABLE Top_Transaction_District (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER, District TEXT, Count INTEGER, Amount REAL)")
    root_folder = "D:/python/project/PhonePe_data/data/top/transaction/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/top/transaction/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/top/transaction/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = (data['data']['districts'])
                                        for item in transaction_data:
                                            District = item['entityName']
                                            Count = item['metric']['count']
                                            Amount = item['metric']['amount']
                                            cleaned_data.append({'State':filename, 'Year':year_name, 'District':District,'Count':Count, 'Amount': Amount})
    for item in cleaned_data:
        sql = ("""INSERT INTO Top_Transaction_District (State, Year, District, Count, Amount  ) VALUES(%s, %s, %s, %s, %s)""")
        val = (item['State'], item['Year'], item['District'], item['Count'], item['Amount'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()


def Top_Transaction_Pincodes():
    conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="Phone_pe"
        )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Top_Transaction_Pincode (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER, Pincodes INTEGER, Count INTEGER, Amount REAL)")
    root_folder = "D:/python/project/PhonePe_data/data/top/transaction/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/top/transaction/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/top/transaction/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = (data['data']['pincodes'])
                                        for item in transaction_data:
                                            Pincodes = item['entityName']
                                            Count = item['metric']['count']
                                            Amount = item['metric']['amount']
                                            cleaned_data.append({'State':filename, 'Year':year_name, 'Pincodes':Pincodes,'Count':Count, 'Amount': Amount})
    for item in cleaned_data:
        sql = ("""INSERT INTO Top_Transaction_Pincode (State, Year, Pincodes, Count, Amount  ) VALUES(%s, %s, %s, %s, %s)""")
        val = (item['State'], item['Year'], item['Pincodes'], item['Count'], item['Amount'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()

Top_Transaction_Pincodes()

