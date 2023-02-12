import os
import json
import mysql.connector


def Aggregated_User():
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="Aggregated"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Aggregate_User (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER, Registered_Users INTEGER)")
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
                            if file.endswith(".json"):
                                # Read the JSON data from the file
                                with open(file_path, 'r') as f:
                                    data = json.load(f)
                                    transaction_data = (data['data']['aggregated'])
                                    for item in transaction_data:
                                        if item == 'registeredUsers':
                                            Registered_Users = transaction_data['registeredUsers']
                                            cleaned_data.append({'State':filename,'Year':year_name,'Registered_Users': Registered_Users})

    for item in cleaned_data:
        sql = ("""INSERT INTO Aggregate_User (State, Year, Registered_Users) VALUES(%s, %s, %s)""")
        val = (item['State'], item['Year'], item['Registered_Users'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()
