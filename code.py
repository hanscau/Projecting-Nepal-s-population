import csv
import numpy as np

#population Function, returns population value
def populationFunction(K,A,r,t):
	e = 2.7182818284590452353602874713527
	r = float(r)
	t = float(t)
	temp = -1 * r * t
	temp2 = A * np.power(e,temp)
	P = (K)/(1 + temp2)
	return P

#function to find A, returns A
def Afunction(K):
	A = 0.00
	A = K/8339978.00 - 1
	return A

#function to calculate error score
def errorFunction(yearList,populationList, K, r):
	Ar = float(Afunction(K))
	errorSum = 0
	for num in range(len(yearList)):
		errorSum += (float(populationFunction(K,Ar,r,yearList[num])) - float(populationList[num]))**2

	return errorSum

#Open csv dataset
with open('Nepal Population Dataset.csv','rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

#Parse its population to a list
population = []
for data in your_list:
	population.append(data[4])

#Parse years to a list
year = []
for data in your_list:
	year.append(data[3])

#Pop off header
year.pop(0)
population.pop(0)

#List containing the range of K values
KList = []
for num in range(10982821,23570795,108282):
	KList.append(num)
	
#List containing the range of r values
rList = []
for num in range(50,150,1):
	rList.append(num)
	
rList2 = []
for data in rList:
	rList2.append(data/1000.00)
	
rList = rList2

rList = np.array(rList)
population = np.array(population)
year = np.array(year)

errorList = []
combi = []

#Iterate through every values of K and r, calculate its error value and append it to a list
for Knum in KList:
	for rnum in rList:
		combi.append(Knum)
		combi.append(rnum)
		combi.append(errorFunction(year, population,Knum,rnum))
		errorList.append(combi)
		combi = []

#Prints out all the data
for data in errorList:
	print(data)

temp = float(errorList[0][2])
rFinal = 0.0
KFinal = 0.0

#Find the K and r with lowest error value
for data in errorList:
	if( temp > float(data[2])):
		temp = float(data[2])
		rFinal = float(data[1])
		KFinal = float(data[0])

#Values
print("============")
print(KFinal)
print(rFinal)
print(temp)

	
		
