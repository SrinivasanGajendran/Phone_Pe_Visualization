import Aggregated_Transaction
import Aggregated_User
import Map_Transaction
import Map_User
import Top_Transaction
import Top_User
import Cloning_Github_Repo
import os

def create():
    path = "D:/python/project/PhonePe_data"
    isExist = os.path.exists(path)
    if isExist:
         Aggregated_Transaction.Aggregated_Transaction()
         Aggregated_User.Aggregated_User()
         Map_Transaction.Map_Transaction()
         Map_User.Map_User()
         Top_Transaction.Top_Transaction_Districts()
         Top_Transaction.Top_Transaction_Pincodes()
         Top_User.Top_User_Pincodes()
         Top_User.Top_User_Districts()
    else:
         Cloning_Github_Repo.check()
         Aggregated_Transaction.Aggregated_Transaction()
         Aggregated_User.Aggregated_User()
         Map_Transaction.Map_Transaction()
         Map_User.Map_User()
         Top_Transaction.Top_Transaction_Districts()
         Top_Transaction.Top_Transaction_Pincodes()
         Top_User.Top_User_Pincodes()
         Top_User.Top_User_Districts()

