import os
import json
import mysql.connector


def Top_Transaction_Districts():
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="testing"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Top_Transaction_District (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER,Quarter INTEGER, District TEXT, Count INTEGER, Amount REAL)")
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
                            quarter = int(file.strip('.json'))
                            if file.endswith(".json"):
                                # Read the JSON data from the file
                                with open(file_path, 'r') as f:
                                    data = json.load(f)
                                    transaction_data = (data['data']['districts'])
                                    for item in transaction_data:
                                        District = item['entityName']
                                        Count = item['metric']['count']
                                        Amount = item['metric']['amount']
                                        cleaned_data.append(
                                            {'State': filename, 'Year': year_name,'Quarter':quarter, 'District': District, 'Count': Count,
                                             'Amount': Amount})


    for item in cleaned_data:
        sql = ("""INSERT INTO Top_Transaction_District (State, Year, Quarter, District, Count, Amount  ) VALUES(%s, %s, %s, %s, %s, %s)""")
        val = (item['State'], item['Year'],item['Quarter'], item['District'], item['Count'], item['Amount'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()


def Top_User_Pincodes():
    conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="testing"
        )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Top_User_Pincode (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER,Quarter INTEGER , Pincodes INTEGER, Registered_User INTEGER)")
    root_folder = "D:/python/project/PhonePe_data/data/top/user/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/top/user/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/top/user/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                quarter = int(file.strip('.json'))
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = (data['data']['pincodes'])
                                        for item in transaction_data:
                                            Pincodes = item['name']
                                            Registered_User = item['registeredUsers']
                                            cleaned_data.append({'State':filename, 'Year':year_name,'Quarter':quarter, 'Pincodes':Pincodes,'Registered_User':Registered_User})
    for item in cleaned_data:
        sql = ("""INSERT INTO Top_User_Pincode (State, Year, Quarter ,Pincodes, Registered_User) VALUES(%s, %s, %s, %s, %s)""")
        val = (item['State'], item['Year'],item['Quarter'] ,item['Pincodes'], item['Registered_User'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()


def Top_User_Districts():
    conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="testing"
        )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Top_User_Districts (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER,Quarter INTEGER ,District TEXT, Registered_User INTEGER)")
    root_folder = "D:/python/project/PhonePe_data/data/top/user/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/top/user/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/top/user/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                quarter = int(file.strip('.json'))
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = (data['data']['districts'])
                                        for item in transaction_data:
                                            District = item['name']
                                            Registered_User = item['registeredUsers']
                                            cleaned_data.append({'State':filename, 'Year':year_name,'Quarter':quarter,'District':District,'Registered_User':Registered_User})
    for item in cleaned_data:
        sql = ("""INSERT INTO Top_User_Districts (State, Year,Quarter ,District, Registered_User) VALUES(%s, %s, %s, %s, %s)""")
        val = (item['State'], item['Year'],item['Quarter'] ,item['District'], item['Registered_User'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()





