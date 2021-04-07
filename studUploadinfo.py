import studeninfo
import random
import numpy as np
import pandas as pd
import getindianname as name        # using for random name
import csv

state=['Haryana', 'Uttar Pradesh','Uttarakhand', 'Rajasthan','Maharashtra', 'Madhya Pradesh','West Bengal',
       'Bihar','Himachal Pradesh','Jharkhand','Andhra Pradesh','Odisha','Chhattisgarh','Punjab', 'Gujarat','Tamil Nadu',
       'Kerala','Karnataka','Goa','Manipur','Meghalaya','Mizoram','Nagaland', 'Telangana','Tripura','Arunachal Pradesh',
       'Sikkim']
st_name=[]
test_center=[]
stud_name = []

### genrating random details of stdents

for var in range(10000):
       Name = name.randname()
       stud_name.append(Name)
       b = random.choice(state)
       c = studeninfo.get_key(b)
       st_name.append(b)
       test_center.append(c)
       studeninfo.marks()                 # call marks function

###   Store all the information of data

data={'student_id':np.arange(10001,20001),"student_name":stud_name,"States":st_name,"Test_center":test_center,"MATH":studeninfo.math,"SCIENCE":studeninfo.sci,
       "PHYSICS":studeninfo.phy,"CHEMISTRY":studeninfo.che,"BIOLOGY":studeninfo.bio,"TOTAL":studeninfo.total,"PERCENTAGE":studeninfo.per_list}

##  Create the csv file and all data store in csv file formate.

df = pd.DataFrame(data=data)
df.to_csv("student.csv")

