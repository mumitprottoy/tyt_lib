import datetime

def log_error(error:str):
    file = open('error_logs.txt', 'a')
    
    file.write("\n"*3)
    file.write("="*10+"\n")

    file.write(str(datetime.datetime.now())[:-10]+"\n")
    file.write(error)
    
    file.write('\n'+"="*10+"\n")


