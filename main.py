from textToCsv import txtToCsv
from createScatter import generateScatterRightEye, generateScatterLeftEye, generateScatterHead
import matplotlib.pyplot as plt

READ_PATH_HEAD_DATA = r"C:\Users\ARISE_students\VR_data\head_data.txt"
WRITE_PATH_HEAD_DATA = r"C:\Users\ARISE_students\VR_data\head_data_csv.csv"
READ_PATH_LEFT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\left_eye_data.txt"
WRITE_PATH_LEFT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\left_eye_data_csv.csv"
READ_PATH_RIGHT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\right_eye_data.txt"
WRITE_PATH_RIGHT_EYE_DATA = r"C:\Users\ARISE_students\VR_data\right_eye_data_csv.csv"
READ_PATH_TIME_DATA = r"C:\Users\ARISE_students\VR_data\time_data.txt"
WRITE_PATH_TIME_DATA = r"C:\Users\ARISE_students\VR_data\time_data_csv.csv"

if __name__ == "__main__":
    txtToCsv(READ_PATH_HEAD_DATA, WRITE_PATH_HEAD_DATA, eyeData = False)
    txtToCsv(READ_PATH_LEFT_EYE_DATA, WRITE_PATH_LEFT_EYE_DATA, eyeData = True)
    txtToCsv(READ_PATH_RIGHT_EYE_DATA, WRITE_PATH_RIGHT_EYE_DATA, eyeData = True)
    print("### Successfully converted to CSV ###")
    generateScatterLeftEye(WRITE_PATH_LEFT_EYE_DATA)
    generateScatterRightEye(WRITE_PATH_RIGHT_EYE_DATA)
    generateScatterHead(WRITE_PATH_HEAD_DATA)
    plt.show()
    
    
    


    