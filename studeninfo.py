import random
import csv
import pandas as pd
import numpy as np

##  To create a Dictionary for States ##

Test_center=['Delhi','Mumbai','Kolkata','Hyderabad','Agra','Chennai','Banglore','Aasam']
states = {'Delhi':['Haryana', 'Uttar Pradesh','Uttarakhand', 'Rajasthan'],
        'Mumbai':['Maharashtra', 'Madhya Pradesh'],
        'kolkata':['West Bengal','Bihar','Himachal Pradesh','Jharkhand'],
        'Hyderabad':['Andhra Pradesh','Odisha','Chhattisgarh'],
        'Agra':['Punjab', 'Gujarat'],
        'Chennai':['Tamil Nadu', 'Kerala'],
        'Banglore':['Karnataka','Goa'],
        'Aasam':['Manipur','Meghalaya','Mizoram','Nagaland', 'Telangana','Tripura','Arunachal Pradesh','Sikkim']}

### Create Function to return random key of States ##

def get_key(val):
        for key, value in states.items():
            x =len(value)
            for i in range(x):
                if val == value[i]:
                    return key
        return "key doesn't exist"

#### create multiple list for marks , percentage and total ##
math = []
sci = []
phy = []
che =[]
bio =[]
total = []
per_list = []
def marks():                              ### Marks funtion use genrate random marks of 5 subject
    mat=random.randint(30,100)
    math.append(mat)
    science = random.randint(30,100)
    sci.append(science)
    physics = random.randint(30, 100)
    phy.append(physics)
    chemisty = random.randint(30, 100)
    che.append(chemisty)
    biology = random.randint(30, 100)
    bio.append(biology)
    tot = mat+science+physics+chemisty+biology
    total.append(tot)
    per = tot *100/500
    per_list.append(per)


class InvalidStudentID(Exception):
    def __init__(self):
        print("Invalid Student ID")


data = pd.read_csv("student.csv")             ###  csv file data load

df = pd.DataFrame(data)

#### create studentinfo funciton to display the data of student if reqired

def student_info():
    try:
        s_id=int(input("Enter student id :="))
        for i in data["student_id"]:
            if (i==s_id) :
                print("Welcome!!!.....")
                name = data["student_name"][i - 10001]
                center = data["Test_center"][i - 10001]
                percentage = data["PERCENTAGE"][i-10001]
                value = df.PERCENTAGE.rank(pct=True)
                print(f"Student Name := {name} ")
                print(f"Test Center := {center}")
                print(f"Percentage := {percentage}")
                print(f"percentile:= {value[i-10001]}")
    except:
            raise InvalidStudentID


## create teacherinfo function to display the all the data of state

def teacher_info():

        st_name = input("Enter your state := ")
        State = data["States"] == st_name
        Info = data[State]
        avg_math = np.average(Info['MATH'])
        avg_sci = np.average(Info['SCIENCE'])
        avg_phy = np.average(Info['PHYSICS'])
        avg_che = np.average(Info['CHEMISTRY'])
        avg_bio = np.average(Info['BIOLOGY'])
        l = avg_math, avg_sci, avg_phy, avg_che, avg_bio
        print(f"Average marks of Math:= {avg_math}")
        print(f"Average mraks of Science:= {avg_sci}")
        print(f"Average marks of Physics:= {avg_phy}")
        print(f"Average marks of Chemistry:= {avg_che}")
        print(f"Average marks of Biology:= {avg_bio}")
        print(f"Tough subject:= {np.max(l)}")
        print(f"Easiest subject:= {np.min(l)}")