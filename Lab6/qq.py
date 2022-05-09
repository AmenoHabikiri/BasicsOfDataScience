import pandas as pd
import matplotlib.pyplot as plt
import datetime
def create_PMF(Age):#creating PMF
    Age_index=[]
    for i in Age: 
        if i not in Age_index:
            Age_index.append(i)
    Age_index.sort()
    prob_lis=[0 for i in range(0,len(Age_index))]
    for i in range(0,len(Age)):
        for j in range(0,len(Age_index)):
            if (Age[i]==Age_index[j]):
                prob_lis[j]+=1
    for i in range(0,len(prob_lis)):
        prob_lis[i]=prob_lis[i]/len(Age)
    return Age_index,prob_lis
def mean_variance(prob_lis,Age_index):#calculating expectation and variance:
    ExpectedVal=0
    Variance=0
    for i in range(0,len(prob_lis)):
        ExpectedVal+= prob_lis[i]*Age_index[i]
        Variance+=prob_lis[i]*Age_index[i]*Age_index[i]
    Variance-=ExpectedVal*ExpectedVal
    print(ExpectedVal,Variance)
data = pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx", header=1, sheet_name="TableS1")
data1 = data[data["ExposureType"]!="Lives-works-studies in Wuhan"] #for non Wuhan residents
exposureL1=[]
exposureR1=[]
onset1=[]
incubation1=[]

for i in data1["ExposureL"]:
    exposureL1.append(i)
for i in data1["ExposureR"]:
    exposureR1.append(i)
for i in data1["Onset"]:
    onset1.append(i)
for i in range(0,len(exposureL1)):
    if str(exposureL1[i]) == "NaT":
        exposureL1[i] = pd.Timestamp(datetime.date(2019, 12, 1))
for i in range(0,len(onset1)):
    if str(onset1[i]) == "NaT":
        onset1[i] = exposureR1[i] + datetime.timedelta(days=1)
for i in range(0, len(exposureL1)):
    for j in range(0, len(onset1)):
        if i == j:
            incubation1.append((onset1[i] - exposureL1[i]))
incube1=[]
for i in range(0,len(incubation1)):
    incube1.append(str(incubation1[i])[0:2])
    if (incube1[i]=="Na"):
        incube1[i]=1
    else:
        incube1[i]=int(incube1[i])
incube1_index=[]
incube1_prob=[]
incube1_index,incube1_prob=create_PMF(incube1)
Results=pd.DataFrame({"Incubation Period":incube1_index,"No of observation":incube1_prob})
print(Results)
plt.hist(incube1,bins=len(incube1_index))
#plt.show()
mean_variance(incube1_prob,incube1_index)
#for all affected
exposureL2=[]
exposureR2=[]
onset2=[]
incubation2=[]
incube2=[]
for i in data["ExposureL"]:
    exposureL2.append(i)
for i in data["ExposureR"]:
    exposureR2.append(i)
for i in data["Onset"]:
    onset2.append(i)
for i in range(0,len(exposureL2)):
    if str(exposureL2[i]) == "NaT":
        exposureL2[i] = pd.Timestamp(datetime.date(2019, 12, 1))
for i in range(0,len(onset2)):
    if str(onset2[i]) == "NaT":
        onset2[i] = exposureR2[i] + datetime.timedelta(days=1)
for i in range(0, len(exposureL2)):
    for j in range(0, len(onset2)):
        if i == j:
            incubation2.append((onset2[i] - exposureL2[i]))
for i in range(0,len(incubation2)):
    incube2.append(str(incubation2[i])[0:2])
    if (incube2[i]=="Na"):
        incube2[i]=1
    else:
        incube2[i]=int(incube2[i])
incube2_index=[]
incube2_prob=[]
incube2_index,incube2_prob=create_PMF(incube2)
Results=pd.DataFrame({"Incubation Period":incube2_index,"No of observation":incube2_prob})
print(Results)
plt.hist(incube2,bins=len(incube2_index))
#plt.show()
mean_variance(incube2_prob,incube2_index)
