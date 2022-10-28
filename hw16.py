data = '''1,Hannah,85,90,92,85,72,86
4,Leah,100,100,79,A,78,95
1,Lee-Ann,85,70,88,82,89,99
1,Heidi,75,85,94,71,94,83
3,Lyndsey,93,98,81,94,A,89
1,Rhonda,A,76,70,78,98,96
2,Annie,73,96,97,73,76,82
1,April,84,79,98,A,79,82
3,Charmaine,78,96,83,96,70,71
3,Dorothy,84,85,87,77,94,95
1,Lynsay,91,98,96,88,A,95
4,Charlene,78,86,91,97,97,72
2,Nadine,74,73,87,85,A,75
4,Penny,87,84,75,93,94,100
2,Roseann,74,90,72,87,90,85
4,Sharron,A,72,99,95,91,82
4,Anita,A,89,77,100,89,74
2,Stacey,75,72,83,95,88,97'''

def makeHTMLTable(x):
    print ("<table border = '1'>")
    for i in range(len(x)):
        print ("  <tr>")
        for y in range(len(x[i])):
            print ("    <td>", end = '')
            print (x[i][y], end = '')
            print ("</td>")
        print ("  </tr>")
    print ("</table>")

nums = [[1,2,3], [10], [12,15]]
print( makeHTMLTable(nums))

def makeHTMLTable2(data):
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    for y in range(len(data)):
        x = 2
        total = 0
        length = len(data[i]) - 3 # dropping lowest score
        while x < len(data[y]):
            if 'A' not in data[y]:
                if data[y][x] != min(data[y][2::]):
                    total += int(data[y][x])
            else:
                if data[y][x] != 'A':
                    total += int(data[y][x])
            x += 1
        data[y].append(total/length)
    return makeHTMLTable(data)

print(makeHTMLTable2(data))
