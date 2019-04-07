from collections import Counter


def main():
    #open file
    pblottery_file = open("pbnumbers.txt","r")
    #creae a pblottery_temp_list to read the file
    pblottery_temp_list = pblottery_file.read().splitlines()
    #close the file
    pblottery_file.close()

    #split each element of Regular number into individual numbers and store in regular_number_list
    regular_number_temp_list=[]
    regular_number_list=[]
    for i in range(len(pblottery_temp_list)):
        regular_number_temp_list.append(pblottery_temp_list[i].split())
        regular_number_list.append(regular_number_temp_list[i][0])
        regular_number_list.append(regular_number_temp_list[i][1])
        regular_number_list.append(regular_number_temp_list[i][2])
        regular_number_list.append(regular_number_temp_list[i][3])
        regular_number_list.append(regular_number_temp_list[i][4])

    print("Display the frequency of each Regular Number 1每69 ")
    for j in range(69):
        if j<10:

            print('Number:',j+1,'Frequency:',Counter(regular_number_list)['0'+str(j+1)])
        else:
            print('Number:',j+1,'Frequency:',Counter(regular_number_list)[str(j+1)])

    print("-------------------------------------------------------- ")

    #split each element of PowerBall number into individual numbers and store in powerBall_number_lis
    powerBall_number_temp_list=[]
    powerBall_number_list=[]

    #Display the frequency of each number 1每69,
    for m in range(len(pblottery_temp_list)):
        powerBall_number_temp_list.append(pblottery_temp_list[m].split())
        powerBall_number_list.append(powerBall_number_temp_list[m][5])


    #Display the frequency of each Powerball number 1每26
    print("Display the frequency of each PowerBall Number 1每26 ")
    for n in range(26):
        if n<10:
            print('Number:',n+1,'Frequency:',Counter(powerBall_number_list)["0"+str(n+1)])
        else:
            print('Number:',n+1,'Frequency:',Counter(powerBall_number_list)[str(n+1)])


main()