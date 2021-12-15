import os
import time

path = input("Enter the path of the directory you want to clean up : ")
current_time = time.time()
daysToDeleteFrom = int(input("Number of days you want to delete from : "))

if os.path.exists(path):
    
    listOfFiles = os.listdir(path)
    for i in listOfFiles:
        file_time = os.stat(path+'/'+i).st_mtime
        days_difference = ((current_time - file_time) / 86400)
        if days_difference >= daysToDeleteFrom:
            os.remove(path+'/'+i)
            print("Removed : "+i)
else : 
    print("Error : The path you specified was not found")
