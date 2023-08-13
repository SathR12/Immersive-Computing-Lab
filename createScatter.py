import matplotlib.pyplot as plt
import numpy as np 
import csv

def generateScatterHead(HEAD_DATA_PATH : str):
    x, y, z, a, b, c, d = [], [], [], [], [], [], [] #individual components of the data 
    entries = []
    with open(HEAD_DATA_PATH, "r") as head_data:
        data_reader = csv.reader(head_data)
        for row in data_reader:
            entries.append(row)
    
    for row in range(1, len(entries)): 
        x.append(float(entries[row][0]))
        y.append(float(entries[row][1]))
        z.append(float(entries[row][2]))
        a.append(float(entries[row][3]))
        b.append(float(entries[row][4]))
        c.append(float(entries[row][5]))
        d.append(float(entries[row][6]))
        
    time = [int(x) for x in range(1, len(entries))]
    plt.scatter(time, x)
    plt.scatter(time, y)
    plt.scatter(time, z)
    plt.scatter(time, a)
    plt.scatter(time, b)
    plt.scatter(time, c)
    plt.scatter(time, d)
    plt.title("Head")
    plt.legend(list("xyzabcd"), loc = "best")
    #plt.figure() commented out as it opens an empty window 
    

def generateScatterLeftEye(LEFT_EYE_DATA_PATH : str):
    x, y, z, a, b, c, d = [], [], [], [], [], [], [] #individual components of the data 
    entries = []
    with open(LEFT_EYE_DATA_PATH, "r") as left_eye_data:
        data_reader = csv.reader(left_eye_data)
        for row in data_reader:
            entries.append(row)
    
    for row in range(1, len(entries)): 
        x.append(float(entries[row][0]))
        y.append(float(entries[row][1]))
        z.append(float(entries[row][2]))
        a.append(float(entries[row][3]))
        b.append(float(entries[row][4]))
        c.append(float(entries[row][5]))
        
    time = [int(x) for x in range(1, len(entries))]
    plt.scatter(time, x)
    plt.scatter(time, y)
    plt.scatter(time, z)
    plt.scatter(time, a)
    plt.scatter(time, b)
    plt.scatter(time, c)
    plt.title("Left Eye")
    plt.legend(list("xyzabc"), loc = "best")
    plt.figure()
    
def generateScatterRightEye(RIGHT_EYE_DATA_PATH : str):
    x, y, z, a, b, c, d = [], [], [], [], [], [], [] #individual components of the data 
    entries = []
    with open(RIGHT_EYE_DATA_PATH, "r") as right_eye_data:
        data_reader = csv.reader(right_eye_data)
        for row in data_reader:
            entries.append(row)
    
    for row in range(1, len(entries)): 
        x.append(float(entries[row][0]))
        y.append(float(entries[row][1]))
        z.append(float(entries[row][2]))
        a.append(float(entries[row][3]))
        b.append(float(entries[row][4]))
        c.append(float(entries[row][5]))
        
    time = [int(x) for x in range(1, len(entries))]
    plt.scatter(time, x)
    plt.scatter(time, y)
    plt.scatter(time, z)
    plt.scatter(time, a)
    plt.scatter(time, b)
    plt.scatter(time, c)
    plt.title("Right Eye")
    plt.legend(list("xyzabc"), loc = "best")
    plt.figure()
    
    
    
    

