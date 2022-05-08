import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_excel("Covid19IndiaData_30032020.xlsx")
def create_PMF(data):
    Age=[]
    Age_index=[]
    for i in data['Age']:
        Age.append(i)
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
    return Age,Age_index,prob_lis
def mean_variance(prob_lis,Age_index):
    ExpectedVal=0
    Variance=0
    for i in range(0,len(prob_lis)):
        ExpectedVal+= prob_lis[i]*Age_index[i]
        Variance+=prob_lis[i]*Age_index[i]*Age_index[i]
    Variance-=ExpectedVal*ExpectedVal
    print(ExpectedVal,Variance)
#showing PMF
Age,Age_index,prob_lis=create_PMF(data)
mean_variance(prob_lis,Age_index)
Results=pd.DataFrame({"Age of Person":Age_index,"Probability of being affected":prob_lis})
print(Results)
plt.hist(Age,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Probability of person being infected")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
#plt.show()
#calculating expectation and variance:

