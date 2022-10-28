file = open('2012_SAT_Results.csv','r')
data = file.read()

def phaseOne(data):
    list = []
    dataList = []
    data = data.split('\n')
    for i in range(len(data)):
        list = data[i].split(',')
        dataList += [list]
    return dataList

dataList = phaseOne(data)

def phaseTwo(dataList):
    i = 0
    while i < len(dataList):
        if 's' in dataList[i][2:]:
            dataList.remove(dataList[i])
        else:
            i += 1

    for i in range(len(dataList)):
        dataList[i] = dataList[i][1:]
    dataList[0] = ['SCHOOL NAME', 'Num of SAT Test Takers', 'Reading', 'Math', 'Writing']
    i = 0

    for i in range(len(dataList)):
        total = 0
        if i != 0:
            y = 1
            while y < len(dataList[i]):
                total += int(dataList[i][y])
                y += 1
            total = total / 4
            dataList[i].append(total)
        else:
            dataList[0].append('Average Score')
    return dataList

dataList = phaseTwo(dataList)

def phaseThree(dataList):
    phrase = "<table border = '1'>\n"
    for i in range(len(dataList)):
        phrase += "  <tr>\n"
        for y in range(len(dataList[i])):
            phrase += "    <td>"
            phrase += str(dataList[i][y])
            phrase += "</td>\n"
        phrase += "  </tr>\n"
    phrase += "</table>"
    return phrase
whole_table = phaseThree(dataList)

def phraseThreeRemove(dataList):
    x = 1
    while x < len(dataList):
        if str(dataList[x]).isalpha():
            x += 1
        else:
            if dataList[x][len(dataList[x])-1] < 550:
                dataList.remove(dataList[x])
            else:
                x += 1
    return dataList
top_table = phaseThree(phraseThreeRemove(dataList))

def phaseFour():
    whole = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<title>table</title>\n" + "</head>\n" + "<body>\n"
    whole += "<h1>\n" + "TOP SCORING SCHOOLS" + "</h1>\n"
    whole += top_table
    whole += "<h1>\n" + "ALL SCHOOLS" + "</h2>\n"
    whole += whole_table
    whole += "</body>\n" + "</html>"
    return(whole)
print(phaseFour())
