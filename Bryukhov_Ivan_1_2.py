cubeList = []
for oddNumbers in range(1,1001):
    if oddNumbers % 2 == 1:
        cubeList.append(oddNumbers)
        oddNumbers = oddNumbers**3
        print(oddNumbers)



