# Phone_Visualization

Visualizing Phone_Pe Transaction And Users Data. 

**Step-1:**
Download the github repo using **requests,os,json,git** package in python and store it in a folder. Sometimes it throws an error **GIT_PYTHON_REFRESH** at that time use this **os.environ["GIT_PYTHON_REFRESH"] = "quiet"** before calling **git**.

```
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
def check():
        url = "https://api.github.com/repos/PhonePe/pulse"
        response = requests.get(url)
        if response.status_code == 200:
            repo = json.loads(response.text)
            clone_url = repo["clone_url"]
            repo_url = clone_url
            local_path = "D:/python/project/PhonePe_data"
            repo_1 = git.Repo.clone_from(repo_url, local_path)
```

**Step-2:**
We have to connect to our DB to store the data which we got from the github. I have created separate files for each type of data which i am going to diplay for the users.
Before creating the tables we need to check whether the database already exist or not, if not we need to create and connect to it. 
**Table_Names: ____Aggregated_transaction,Aggregated_user,map_Transaction,Map_User,Top_transaction,Top_User___

**Step-3:**
We will be Using Mysql-Connector in python to connect with the database then we will check for the **.json** files in the folders using **os** package and start extracting the required data and create a table insert it.

**Step-4**:
After extracting all the data we will create a dashboard using **Streamlit** and retrieves the data from the created tables to present it in the platform and include pie & Bar charts.

**Step-5:**
Now we will create a file name **combined** which holds all the other files once it is called all the file's will start to execute.

**Step-6**
this **Combined** will be called in the **Streamlit** file.

___Packages_Used:-___
*import os
*import muysql-connector
*import streamlit
*import json
*import git
*import pandas
*import plotly.express
