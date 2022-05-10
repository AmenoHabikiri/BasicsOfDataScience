"""
Created on Thu Apr  9 19:28:12 2020
Lab part1
@author: Sagar
"""
import pandas as pd
import matplotlib.pyplot as plt
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
print(lis1)
for i in range(len(lis1)):
    lis1[i] = str(lis1[i])
    lis1[i] = lis1[i][:2]
for i in range(len(lis1)):
    if lis1[i] != "Na":
        if int(lis1[i]) > 0:
            Incub1.append(int(lis1[i]))
print(Incub1)
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

Variance1 = -(Mean1 * Mean1)
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