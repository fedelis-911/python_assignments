file_name=input("enter the name of file you wish to open here. ")
#if "png" or "jpg" in file_name:
try:
    with open(file_name,"r")as file:
            file.write("content you wish to write to file")
except FileNotFoundError:
        print("!!  filename error!!")

except Exception:
      m=open(file_name,"rb")
       
    
    