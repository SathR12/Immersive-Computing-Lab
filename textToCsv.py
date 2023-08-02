import csv 

#initializing constants for the paths for files 
READ_PATH_HEAD_DATA = r"C:\Users\ARISE_students\VR_data\head_data.txt"
WRITE_PATH_HEAD_DATA = r"C:\Users\ARISE_students\VR_data\head_data_csv.csv"
READ_PATH_LEFT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\left_eye_data.txt"
WRITE_PATH_LEFT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\left_eye_data_csv.csv"
READ_PATH_RIGHT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\right_eye_data.txt"
WRITE_PATH_RIGHT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\right_eye_data_csv.csv"

def txtToCsv(r_path : str, w_path : str, eyeData = False):
    txt_list = []
    with open(r_path, "r") as f_read: #text file is "f"
        data_reader = csv.reader(f_read) #make sure delimiter is set to empty string for commas to appear 
        for row in data_reader:
            txt_list.append("".join(row).split("\n"))
    
    
    #removes the purged message on top of txt file 
    txt_list.pop(0)    
    #print(txt_list)

    with open(w_path, "w") as f_write:
        if eyeData == False: 
            fieldnames = list("xyzabcd")
            data_writer = csv.DictWriter(f_write, dialect = "excel", fieldnames = fieldnames, lineterminator = '\n')
            dictDump = {}
            data_writer.writeheader()
            for idx in range(len(txt_list)):
                if idx % 2 == 0 :
                    strToList = txt_list[idx][0]
                    strToList = strToList.lstrip("(")
                    strToList = strToList.rstrip(")")
                    dump = strToList.split()
                    dictDump["x"] =  float(dump[0])
                    dictDump["y"] =  float(dump[1])
                    dictDump["z"] =  float(dump[2])
                    
                elif idx % 2 == 1:
                    strToList = txt_list[idx][0]
                    strToList = strToList.lstrip("(")
                    strToList = strToList.rstrip(")")
                    dump = strToList.split()
                    dictDump["a"] =  float(dump[0])
                    dictDump["b"] =  float(dump[1])
                    dictDump["c"] =  float(dump[2])
                    dictDump["d"] =  float(dump[3])
                
                    data_writer.writerow(dictDump)
                    dictDump.clear()
        else:
            fieldnames = list("xyzabc")
            data_writer = csv.DictWriter(f_write, dialect = "excel", fieldnames = fieldnames, lineterminator = '\n')
            dictDump = {}
            data_writer.writeheader()
            for idx in range(len(txt_list)):
                if idx % 2 == 0 :
                    strToList = txt_list[idx][0]
                    strToList = strToList.lstrip("(")
                    strToList = strToList.rstrip(")")
                    dump = strToList.split()
                    dictDump["x"] =  float(dump[0])
                    dictDump["y"] =  float(dump[1])
                    dictDump["z"] =  float(dump[2])
                    
                elif idx % 2 == 1:
                    strToList = txt_list[idx][0]
                    strToList = strToList.lstrip("(")
                    strToList = strToList.rstrip(")")
                    dump = strToList.split()
                    dictDump["a"] =  float(dump[0])
                    dictDump["b"] =  float(dump[1])
                    dictDump["c"] =  float(dump[2])
                
                    data_writer.writerow(dictDump)
                    dictDump.clear()
            
if __name__ == "__main__":
    txtToCsv(READ_PATH_HEAD_DATA, WRITE_PATH_HEAD_DATA, eyeData = False)
    txtToCsv(READ_PATH_LEFT_EYE_DATA, WRITE_PATH_LEFT_EYE_DATA, eyeData = True)
    txtToCsv(READ_PATH_RIGHT_EYE_DATA, WRITE_PATH_RIGHT_EYE_DATA, eyeData = True)
    print("Script executed")
        
    
    
    
