StartingNum=input("Entering the number of organisams:")
AveDailyIncrease = input("Entering the average daily population increase as a percentage(%):")
numOfdays = input("Entering the numbers of days to organisms that wiil be left to multiply:")
countNum=1
population=int(StartingNum)
print("Day Approximate Pupulation")
while countNum<=int(numOfdays):
    print (countNum,"\t",format(population,".1f"))
    population = population*(1+int(AveDailyIncrease)/100)
    countNum=countNum+1