from collections import Counter

def main():
    #open file
    pblottery_file = open("pbnumbers.txt","r")
    #creae a pblottery_temp_list to read the file
    pblottery_temp_list = pblottery_file.read().splitlines()
    #close the file
    pblottery_file.close()

    #split each element into individual numbers and store in the pblottery_list
    pblottery_list=[]
    for i in range(len(pblottery_temp_list)):
        number_set =pblottery_temp_list[i].split()
        for n in range(len(number_set)):
            pblottery_list.append(number_set[n])

    #Display the 10 most common numbers, ordered by frequency
    print("Display the 10 most common numbers, ordered by frequency ")
    for n in range(10):
        print('Number:',Counter(pblottery_list).most_common(10)[n][0],'Frequende:',Counter(pblottery_list).most_common(10)[n][1])

    print("-------------------------------------------------------- ")
    #Display the 10 least common numbers, ordered by frequency
    print("Display the 10 least common numbers, ordered by frequency ")
    for m in range(10):
        print('Number:',Counter(pblottery_list).most_common()[:-11:-1][m][0],'Frequence:',Counter(pblottery_list).most_common()[:-11:-1][m][1])

main()