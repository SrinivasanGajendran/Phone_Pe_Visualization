import os
import json
import mysql.connector


def Map_User():
    conn = mysql.connector.connect(
            host="localhost",
            user="srini",
            password="password",
            database="Phone_pe"
        )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Map_User (ID  INTEGER  AUTO_INCREMENT PRIMARY  KEY, State TEXT, Year INTEGER, District TEXT, Registered_User INTEGER)")
    root_folder = "D:/python/project/PhonePe_data/data/map/user/hover/country/india/state"
    cleaned_data = []
    for filename in os.listdir(root_folder):
            file_path = os.path.join(root_folder, filename)
            if os.path.isdir(file_path):
                directory_1 = f"D:/python/project/PhonePe_data/data/map/user/hover/country/india/state/{filename}"
                for year_name in os.listdir(directory_1):
                    file_path_1 = os.path.join(directory_1, year_name)
                    if os.path.isdir(file_path_1):
                        root_folder_1 = f"D:/python/project/PhonePe_data/data/map/user/hover/country/india/state/{filename}/{year_name}"
                        for subdir, dirs, files in os.walk(root_folder_1):
                            for file in files:
                                file_path = os.path.join(subdir, file)
                                if file.endswith(".json"):
                                    # Read the JSON data from the file
                                    with open(file_path, 'r') as f:
                                        data = json.load(f)
                                        transaction_data = (data['data']['hoverData'])
                                        for item in transaction_data:
                                            District = item
                                            Registered_User = transaction_data[item]['registeredUsers']
                                            cleaned_data.append({'State':filename,'Year':year_name,'District':District, 'Registered_User':Registered_User})
    for item in cleaned_data:
        sql = ("""INSERT INTO Map_User (State, Year, District, Registered_User  ) VALUES(%s, %s, %s, %s)""")
        val = (item['State'], item['Year'], item['District'], item['Registered_User'])
        cursor.execute(sql, val)
        conn.commit()
    cursor.close()
    conn.close()
    #print(cleaned_data)

