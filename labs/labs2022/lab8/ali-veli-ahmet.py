inpStr = "students"

def calculate_average(file):
    with open(file, "r", encoding= "utf-8") as std:

        dictStd = {}
        index = 0
        stdList = []
        for i in std:

            tempList = i.replace("\n", "").replace("\t", " ").split()

            isHave = False
            for j in stdList:
                for k in j:
                    if k == tempList[0]:
                        isHave = True

            if isHave:
                stdList[index - 1].append(int(tempList[1]))             
            else:
                stdList.append([tempList[0], int(tempList[1])])
                index += 1     

        for j in stdList:
            sum = 0
            for k in range(len(j) - 1):
                sum += j[k + 1]
            dictStd[j[0]] = round(sum / (len(j) - 1), 2)
        
        return dictStd

def find_min(file):

    with open(file, "r", encoding= "utf-8") as std:

        minGrade = None
        name = ""

        for i in std:
            lineList = i.replace("\n", "").replace("\t", " ").split()
            if minGrade == None:
                name, minGrade = lineList[0], int(lineList[1])
                continue
            if minGrade > int(lineList[1]):
                name, minGrade = lineList[0], int(lineList[1])
        
        print(f"{name}\t{minGrade}")

for key, value in calculate_average(inpStr).items():
    print(f"{key}\t{value}")

find_min(inpStr)


            

