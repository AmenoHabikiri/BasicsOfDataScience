import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_excel("Covid19IndiaData_30032020.xlsx")
def create_PMF(data):#creating PMF
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
def mean_variance(prob_lis,Age_index):#calculating expectation and variance:
    ExpectedVal=0
    Variance=0
    for i in range(0,len(prob_lis)):
        ExpectedVal+= prob_lis[i]*Age_index[i]
        Variance+=prob_lis[i]*Age_index[i]*Age_index[i]
    Variance-=ExpectedVal*ExpectedVal
    print(ExpectedVal,Variance)
#for_all_patients    
Age,Age_index,prob_lis=create_PMF(data)
mean_variance(prob_lis,Age_index)
Results=pd.DataFrame({"Age of Person":Age_index,"Probability of being affected":prob_lis})
print(Results)
plt.hist(Age,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Probability of person being infected")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()#showing PMF
#for Recovered
#divide the dataset into recovered and dead
data_recovered=data[data["StatusCode"]=="Recovered"]
Age_recovered,Age_recovereed_index,prob_lis_recovered=create_PMF(data_recovered)
mean_variance(prob_lis_recovered,Age_recovereed_index)
Results1=pd.DataFrame({"Age of Person":Age_recovereed_index,"P(recovered)":prob_lis_recovered})
print(Results1)
plt.hist(Age_recovered,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Number of person who recovered")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()#showing PMF
#for Dead
data_dead=data[data["StatusCode"]=="Dead"]
Age_dead,Age_dead_index,prob_lis_dead=create_PMF(data_dead)
mean_variance(prob_lis_dead,Age_dead_index)
Results2=pd.DataFrame({"Age of Person":Age_dead_index,"P(dead)":prob_lis_dead})
print(Results2)
plt.hist(Age_dead,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Number of persons who died")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()#showing PMF
#for male or female
#female
data_female=data[data["GenderCode0F1M"]==0]
Age_female,Age_female_index,prob_female_lis=create_PMF(data_female)
mean_variance(prob_female_lis,Age_female_index)
Results3=pd.DataFrame({"Age of Person":Age_female_index,"P(female|infected)":prob_female_lis})
print(Results3)
plt.hist(Age_female,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Number of persons who are female among infected")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()
#male
data_male=data[data["GenderCode0F1M"]==1]
Age_male,Age_male_index,prob_male_lis=create_PMF(data_male)
mean_variance(prob_male_lis,Age_male_index)
Results4=pd.DataFrame({"Age of Person":Age_male_index,"P(male|infected)":prob_male_lis})
print(Results4)
plt.hist(Age_male,bins=100)
plt.xlabel("Age of person")
plt.xticks(range(1,100,10))
plt.ylabel("Number of persons who are male among infected")
plt.title("COVID 19 DATA OF INDIA TILL 31st March")  
plt.show()






