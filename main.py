import Aggregate
import top
import Cloning_Github_Repo
import os

def create():
    path = "D:/python/project/PhonePe_data"
    isExist = os.path.exists(path)
    if isExist:
         Aggregate.Aggregated_Transaction()
         Aggregate.Aggregated_User()
         top.Top_Transaction_Districts()
         top.Top_User_Pincodes()
         top.Top_User_Districts()
    else:
         Cloning_Github_Repo.check()
         Aggregate.Aggregated_User()
         top.Top_Transaction_Districts()
         top.Top_User_Pincodes()
         top.Top_User_Districts()


