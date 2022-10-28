data = """period1 Krystal 90 45 32 65 66
period1 Tau 59 65 93 88 22 78
period1 Chang 40 97 90 28 31 99
period1 Shan 30 26 35 73 77 99
period1 Bryn 79 93 30 29 23 79 20
period1 Maggie-Rae 78 54 64 50 77
period1 Tiwlip 22 28 54 26 93
period1 Refugio 75 36 83 88 93
period2 Floro 91 74 38 79 20 88 93
period2 Sharilyn 81 76 22 88 73
period2 Alaine 43 56 39 26 71 93
period2 Paula 33 36 24 65 50
period2 Andera 38 90 38 44 24
period2 Onyeka 74 49 32 48 83
period3 Gaia 87 63 82 83 47 74 49
period3 Samira 93 76 84 41 73
period3 Mikaela 84 43 88 22 45
period3 Farrah 75 73 85 42 79
period3 Tiara 62 31 69 53
period3 Valeriy 61 52 86 82 41"""

def studentAverage(s):
    lis = s.split()
    total = 0
    count = 2
    while count < len(lis):
        total += int(lis[count])
        count += 1
    print (lis[0] + ' ' + lis[1], end = ' ')
    print (total / (len(lis) - 2))

print('studentAverage')
studentAverage("period1 Dave 10 20 30")
studentAverage("period1 Kay 100 20 90 88 95")

def studentAverageDropLowest(s):
    lis = s.split()
    total = 0
    count = 2
    while count < len(lis):
        lis[count] = int(lis[count])
        count += 1
    count = 2
    while count < len(lis):
        if lis[count] != min(lis[2::]):
            total += lis[count]
        count += 1
    print (lis[0] + ' ' + lis[1], end = ' ')
    print (total / (len(lis) - 3))

print('\n' + 'studentAverageDropLowest')
studentAverageDropLowest("period1 Dave 10 20 30")

def compareAverages(data):
    student = data.split("\n")
    i = 0
    while i < len(student):
        s = student[i].split()
        count = 2
        total = 0

        while count < len(s):
            s[count] = int(s[count])
            total += s[count]
            count += 1
        print (s[0] + ' ' + s[1], end = ' ')
        print ((total / (len(s) - 2)), end = ' ')

        count = 2
        total = 0
        while count < len(s):
            if s[count] != min(s[2::]):
                total += s[count]
            count += 1
        print (total / (len(s) - 3))
        i += 1

print( "\n" + "compareAverages")
compareAverages(data)
