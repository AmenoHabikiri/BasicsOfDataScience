"""
Created on Thu Apr  9 19:28:12 2020
Lab part1
@author: Sagar
"""
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_excel("Covid19IndiaData_30032020.xlsx")

#Part 1 a)
agelist=[]     #List to contain ages of all the persons suffering from Covid-19 in India
for i in data["Age"]:
    agelist.append(i)
fairagelist=[]   #List of ages of all suffered persons with no repetition in ages
for i in agelist:
    if i not in fairagelist:
        fairagelist.append(i)
fairagelist.sort()
probage= []  #List to contain probabilities of person being infected at given age
dic= {}
for i in fairagelist:
    dic[i]= (agelist.count(i))/len(agelist)
probage= list(dic.values())
Result= pd.DataFrame({"Age of person": fairagelist,"Probability of being infected": probage})
print(Result)
plt.scatter(fairagelist,probage,c= "m")
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Probability of person being infected")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
Expectance= 0
for i in dic:
    Expectance+=(i*dic[i])
print("Expected Age of infected person= ",Expectance)
Var= 0
for i in dic:
    Var+=(i*i*dic[i])
Var= Var-(Expectance*Expectance)
print("Variance of pmf = ",Var)
print("Variance is too high")
print("Large variance tells that the data points are very much spread from the expected value")
print("From graph it is prominent that the distribution spreads wide from the expected value")
print("\n")

#Part 1 b.)
data2= data[(data["StatusCode"]=="Recovered")]
#data of only persons who recovered 
data3= data2["Age"]
agelist2= []
for i in data3:
    agelist2.append(i)
fairagelist2=[]   #List of ages of all suffered persons with no repetition in ages
for i in agelist2:
    if i not in fairagelist2:
        fairagelist2.append(i)
fairagelist2.sort()
probage2= []  #List to contain probabilities of person being infected at given age
dic2= {}
for i in fairagelist2:
    dic2[i]= (agelist2.count(i))/len(agelist2)
probage2= list(dic2.values())
Result2= pd.DataFrame({"Age of person": fairagelist2,"P(Recovered)": probage2})
print(Result2)
plt.scatter(fairagelist2,probage2,c= "g")
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("P(Recovered)")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
Expectance1= 0
for i in dic2:
    Expectance1+=(i*dic2[i])
print("Expected Age of infected person who Recovered= ",Expectance1)
Var1= 0
for i in dic2:
    Var1+=(i*i*dic2[i])
Var1= Var1-(Expectance1*Expectance1)
print("Variance is ", Var1)


data4= data[(data["StatusCode"]=="Dead")]
#data of only persons who died
data5= data4["Age"]
agelist3= []
for i in data5:
    agelist3.append(i)
fairagelist3=[]   #List of ages of all suffered persons with no repetition in ages
for i in agelist3:
    if i not in fairagelist3:
        fairagelist3.append(i)
fairagelist3.sort()
probage3= []  #List to contain probabilities of person being infected at given age
dic3= {}
for i in fairagelist3:
    dic3[i]= (agelist3.count(i))/len(agelist3)
probage3= list(dic3.values())
Result3= pd.DataFrame({"Age of person": fairagelist3,"P(Dead)": probage3})
print(Result3)
plt.scatter(fairagelist3,probage3,c= "m")
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("P(Dead)")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
Expectance2= 0
for i in dic3:
    Expectance2+=(i*dic3[i])
print("Expected Age of infected person given Dead = ",Expectance2)
Var2= 0
for i in dic3:
    Var2+=(i*i*dic3[i])
Var2= Var2-(Expectance2*Expectance2)
print("Variance is ", Var2)
print("Expectations are not the same")
print("The expected age that a person can recover from COVID-19 is very less than the expected \
age of a person who dies from disease. Also, it is expected that elder people have high chances\
of dying due to COVID-19")

#Part1 c.)
data6= data[(data["GenderCode0F1M"]==0)]
#data of only females
data7= data6["Age"]
agelist4= []
for i in data7:
    agelist4.append(i)
fairagelist4=[]   #List of ages of all suffered persons with no repetition in ages
for i in agelist4:
    if i not in fairagelist4:
        fairagelist4.append(i)
fairagelist4.sort()
probage4= []  #List to contain probabilities of person being infected at given age
dic4= {}
for i in fairagelist4:
    dic4[i]= (agelist4.count(i))/len(agelist4)
probage4= list(dic4.values())
Result4= pd.DataFrame({"Age of person": fairagelist4,"P(Infected|Female)": probage4})
print(Result4)
plt.scatter(fairagelist4,probage4,c= "g")
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("P(Infected|Female)")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
Expectance3= 0
for i in dic4:
    Expectance3+=(i*dic4[i])
print("Expected Age of infected person given female= ",Expectance3)
Var3= 0
for i in dic4:
    Var3+=(i*i*dic4[i])
Var3= Var3-(Expectance3*Expectance3)
print("Variance of pmf = ",Var3)
print("\n")

data8= data[(data["GenderCode0F1M"]==1)]
#data of only males
data9= data8["Age"]
agelist5= []
for i in data9:
    agelist5.append(i)
fairagelist5=[]   #List of ages of all suffered persons with no repetition in ages
for i in agelist5:
    if i not in fairagelist5:
        fairagelist5.append(i)
fairagelist5.sort()
probage5= []  #List to contain probabilities of person being infected at given age
dic5= {}
for i in fairagelist5:
    dic5[i]= (agelist5.count(i))/len(agelist5)
probage5= list(dic5.values())
Result5= pd.DataFrame({"Age of person": fairagelist5,"P(Infected|Male)": probage5})
print(Result5)
plt.scatter(fairagelist5,probage5,c= "r")
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("P(Infected|Male)")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
Expectance4= 0
for i in dic5:
    Expectance4+=(i*dic5[i])
print("Expected Age of infected person given male= ",Expectance4)
Var4= 0
for i in dic5:
    Var4+=(i*i*dic5[i])
Var4= Var4-(Expectance4*Expectance4)
print("Variance of pmf = ",Var4)
print("Expected age in case of only males and only females is almost same \n")
print("PMFs are not identically distributed. No. of infected females are much larger than men.\
In males, the infected people are more in age group 20-50 than in other age groups.\
While in females, no. of infected persons are same in almost every age group.")

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:28:12 2020
lab part 2a,b
@author: Sagar
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx", header=1, sheet_name="TableS1")

# Part2
# For Non Wuhan Residents
Incub1 = []
lis1 = []
data1 = data[(data["ExposureType"] != "Lives-works-studies in Wuhan")]
Expl1 = []
Expr1 = []

onset1 = []

for i in data1["ExposureL"]:
    Expl1.append(i)
for i in data1["Onset"]:
    onset1.append(i)
for i in data1["ExposureR"]:
    Expr1.append(i)
# Cleaning Method:- In those cases, where onset data is not present, ExposureR+1day is used as per word file
for i in range(len(onset1)):
    if str(onset1[i]) == "NaT":
        onset1[i] = Expr1[i] + datetime.timedelta(days=1)

for i in range(0, len(Expl1)):
    for j in range(0, len(onset1)):
        if i == j:
            lis1.append((onset1[i] - Expl1[i]))

for i in range(len(lis1)):
    lis1[i] = str(lis1[i])
    lis1[i] = lis1[i][:2]
for i in range(len(lis1)):
    if lis1[i] != "Na":
        if int(lis1[i]) > 0:
            Incub1.append(int(lis1[i]))

unique1 = []
for i in Incub1:
    if i not in unique1:
        unique1.append(i)
unique1.sort()

dic1 = {}
for i in unique1:
    dic1[i] = Incub1.count(i) / (len(Incub1))
prob1 = list(dic1.values())
result1 = pd.DataFrame(
    {"No. of days in Incubation Period": unique1, "PMF of the given Incubation Period for Non WR": prob1})

dic2 = {}
for i in unique1:
    dic2[i] = Incub1.count(i)

Mean1 = 0
for i in dic1:
    Mean1 += (i * dic1[i])

Variance2 = -(Mean1 * Mean1)
for i in dic1:
    Variance1 = (i * i * dic1[i])

# For Wuhan Residents
Incub2 = []
lis2 = []
data2 = data[(data["ExposureType"] == "Lives-works-studies in Wuhan")]
Expl2 = []
onset2 = []
for i in data2["ExposureL"]:
    Expl2.append(i)
for i in data2["Onset"]:
    onset2.append(i)
for i in range(len(Expl2)):
    if str(Expl2[i]) == "NaT":
        Expl2[i] = pd.Timestamp(datetime.date(2019, 12, 1))
# Exposure L Date has been set to 1/12/2019 for missing data as per word file
for i in range(0, len(Expl2)):
    for j in range(0, len(onset2)):
        if i == j:
            lis2.append((onset2[i] - Expl2[i]))

for i in range(len(lis2)):
    lis2[i] = str(lis2[i])
    lis2[i] = lis2[i][:2]
for i in range(len(lis2)):
    if lis2[i] != "Na":
        if int(lis2[i]) > 0:
            Incub2.append(int(lis2[i]))

unique2 = []
for i in Incub2:
    if i not in unique2:
        unique2.append(i)
unique2.sort()
dic3 = {}
for i in unique2:
    dic3[i] = Incub2.count(i)

# Including both WR and non WR

for i in dic3:
    if i in dic2:
        dic2[i] += dic3[i]
    else:
        dic2[i] = dic3[i]
length = len(Incub1) + len(Incub2)
for i in dic2:
    dic2[i] = dic2[i] / length

x = list(dic2.keys())
x.sort()
dic = {}
for i in x:
    dic[i] = dic2[i]
X = list(dic.keys())
Y = list(dic.values())

result = pd.DataFrame({"No. of days in Incubation Period": X, "PMF of the given Incubation Period": Y})
print(result)
plt.scatter(X, Y, c="g")
plt.xlabel("No. of days in Incubation Period")
plt.ylabel("PMF of the given Incubation Period")
plt.show()

Mean = 0
for i in dic:
    Mean += (i * dic[i])
print("Expected Incubation Period is ", Mean, "days")

Variance = -(Mean * Mean)
for i in dic:
    Variance = (i * i * dic[i])
print("Variance is", Variance)

print(result1)
plt.scatter(unique1, prob1, c="m")
plt.xlabel("No. of days in Incubation Period")
plt.ylabel("PMF of the given Incubation Period for Non WR")
plt.xticks(range(1, 40, 2))
plt.show()
print("Expected Incubation Period in case of Non WR is", Mean1, "days")
print("Variance is", Variance1)

print("Expected Incubation Period is quite different in the two cases.")

"""
Created on Thu Apr  9 19:28:12 2020
lab part 2c
@author: Sagar
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx", header=1, sheet_name="TableS2")
data1 = data["Onset"]
Onsetl = []
for i in data1:
    Onsetl.append(i)
data2 = data["Hospitalization/Isolation"]
Hospl = []
for i in data2:
    Hospl.append(i)
list1 = []
for i in range(0, len(Onsetl)):
    for j in range(0, len(Hospl)):
        if i == j:
            list1.append((Onsetl[i] - Hospl[j]))
for i in range(len(list1)):
    list1[i] = str(list1[i])
    list1[i] = list1[i][:2]
HOlist = []
for i in range(len(list1)):
    if list1[i] != "Na":
        HOlist.append(abs(int(list1[i])))
HOunique = []
for i in HOlist:
    if i not in HOunique:
        HOunique.append(i)
HOunique.sort()
dic1 = {}
for i in HOunique:
    dic1[i] = (HOlist.count(i)) / (len(HOlist))
prob = list(dic1.values())
result = pd.DataFrame({"Period between Onset to Hospitalization (in days)": HOunique, "PMF of the period": prob})
print("Data For Dead Patients")
print(result)
plt.scatter(HOunique, prob, c="m")
plt.xlabel("Period between Onset to Hospitalization (in days)")
plt.xticks(range(0, 11, 1))
plt.ylabel("PMF of the period")
plt.title("Onset to Hospitalization Analysis of Covid-19 in case of dead patients")
plt.show()

Deathl = []
data3 = data["Death"]
for i in data3:
    Deathl.append(i)
list2 = []
for i in range(0, len(Onsetl)):
    for j in range(0, len(Deathl)):
        if i == j:
            list2.append((Onsetl[i] - Deathl[j]))
for i in range(len(list2)):
    list2[i] = str(list2[i])
    list2[i] = list2[i][:3]
XOlist = []
for i in range(len(list2)):
    if list2[i] != "NaT":
        XOlist.append(abs(int(list2[i])))
XOunique = []
for i in XOlist:
    if i not in XOunique:
        XOunique.append(i)
XOunique.sort()
dic2 = {}
for i in XOunique:
    dic2[i] = (XOlist.count(i)) / (len(XOlist))
prob2 = list(dic2.values())
result2 = pd.DataFrame({"Period between Onset to Death (in days)": XOunique, "PMF of the period": prob2})
print(result2)
plt.scatter(XOunique, prob2, c="r")
plt.xlabel("Period between Onset to Death (in days)")
plt.xticks(range(0, 50, 2))
plt.ylabel("PMF of the period")
plt.title("Onset to Death Analysis of COVID-19 in case of dead patients")
plt.show()

list3 = []
for i in range(0, len(Hospl)):
    for j in range(0, len(Deathl)):
        if i == j:
            list3.append((Hospl[i] - Deathl[j]))
for i in range(len(list3)):
    list3[i] = str(list3[i])
    list3[i] = list3[i][:3]
XHlist = []
for i in range(len(list3)):
    if list3[i] != "NaT":
        XHlist.append(abs(int(list3[i])))
XHunique = []
for i in XHlist:
    if i not in XHunique:
        XHunique.append(i)
XHunique.sort()
dic3 = {}
for i in XHunique:
    dic3[i] = (XHlist.count(i)) / (len(XHlist))
prob3 = list(dic3.values())
result3 = pd.DataFrame({"Period between Hospitalization to Death (in days)": XHunique, "PMF of the period": prob3})
print(result3)
plt.scatter(XHunique, prob3, c="g")
plt.xlabel("Period between Hospitalization to Death (in days)")
plt.xticks(range(0, 26, 2))
plt.ylabel("PMF of the period")
plt.title("Hospitalization to Death Analysis of COVID-19 in case of dead patients")
plt.show()
print("There is no similarity in the distribution in the three cases")
print("From HO plot, it can concluded that large number of patients were hospitalized/isolated after more than \
three days")
print("From XO plot, it can be concluded that maximum COVID-19 patients died within 8-20 days \
after observation of symptoms.")
print("From XH plot, it can be concluded that maximum number of isolated patients who died, died within 4- 15 days")

data4 = pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx", header=1, sheet_name="TableS1")
data5 = data4["Onset"]
data6 = data4["DateHospitalizedIsolated"]
onset = []
isolated = []
for i in data5:
    onset.append(i)
for i in data6:
    isolated.append(i)
list4 = []
for i in range(0, len(onset)):
    for j in range(0, len(isolated)):
        if i == j:
            list4.append((onset[i] - isolated[j]))
for i in range(len(list4)):
    list4[i] = str(list4[i])
    list4[i] = list4[i][:3]
for i in range(len(list4)):
    if list4[i][2] == "d":
        list4[i] = list4[i][:2]
XHlistsur = []
for i in range(len(list4)):
    if list4[i] != "NaT":
        XHlistsur.append(abs(int(list4[i])))
XHuniquesur = []
for i in XHlistsur:
    if i not in XHuniquesur:
        XHuniquesur.append(i)
XHuniquesur.sort()
dic4 = {}
for i in XHuniquesur:
    dic4[i] = (XHlistsur.count(i)) / (len(XHlistsur))
prob4 = list(dic4.values())
print("Data For Surviving Patients")
result4 = pd.DataFrame({"Period between onset to hospitalization (in days)": XHuniquesur, "PMF of the period": prob4})
print(result4)
plt.scatter(XHuniquesur, prob4, c="g")
plt.xlabel("Period between onset to hospitalization (in days) in case of surviving patients")
plt.xticks(range(0, 26, 2))
plt.ylabel("PMF of the period")
plt.title("Onset to Hospitalization Analysis of COVID-19 in case of surviving patients")
plt.show()

print("On comparing the HO plot for surviving and death patients, it can be seen that surviving \
had isolated them early as compared to dead patients. Majority of surviving patients had isolated them \
within four days of symptoms. While those died isolated them after 3-4 days of symptoms.")