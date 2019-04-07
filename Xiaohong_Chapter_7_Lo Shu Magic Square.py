loShuMagicSquarevalues = [[4,9,2],
                          [3,5,7],
                          [8,1,6]]

def main():

    print(loShuMagicSquarevalues[0])
    print(loShuMagicSquarevalues[1])
    print(loShuMagicSquarevalues[2])

    if Checkingfunction()==True:
        print("This list is a Lo Shu Magic Square.")
    else:
        print("This list is not a Lo Shu Magic Square.")

def Checkingfunction():
    if loShuMagicSquarevalues[0][0]+loShuMagicSquarevalues[0][1]+loShuMagicSquarevalues[0][2]!=15:
        return False
    elif loShuMagicSquarevalues[1][0]+loShuMagicSquarevalues[1][1]+loShuMagicSquarevalues[1][2]!=15:
        return False
    elif loShuMagicSquarevalues[2][0]+loShuMagicSquarevalues[2][1]+loShuMagicSquarevalues[2][2]!=15:
        return False
    elif loShuMagicSquarevalues[0][0]+loShuMagicSquarevalues[1][0]+loShuMagicSquarevalues[2][0]!=15:
        return False
    elif loShuMagicSquarevalues[0][1]+loShuMagicSquarevalues[1][1]+loShuMagicSquarevalues[2][1]!=15:
        return False
    elif loShuMagicSquarevalues[0][2]+loShuMagicSquarevalues[1][2]+loShuMagicSquarevalues[2][2]!=15:
        return False
    elif loShuMagicSquarevalues[0][0]+loShuMagicSquarevalues[1][1]+loShuMagicSquarevalues[2][2]!=15:
        return False
    elif loShuMagicSquarevalues[0][2]+loShuMagicSquarevalues[1][1]+loShuMagicSquarevalues[2][0]!=15:
        return False
    else:
        return True

main()