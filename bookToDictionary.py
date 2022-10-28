def bookToDictionary(text):
    tally = {}
    text = text.replace('---', ' ')
    text = text.replace('--', ' ')
    s = text.split()
    for i in s:
        y = 0
        while y < len(i):
            if i[0] < 'A' or i[0] > 'Z' and i[0] < 'a' or i[0] > 'z':
                i = i.replace(i[0], '')
            elif i[len(i)-1] < 'A' or i[len(i)-1] > 'Z' and i[len(i)-1] < 'a' or i[len(i)-1] > 'z':
                i = i.replace(i[len(i)-1], '')
            else:
                if i[y] >= '0' and i[y] <= '9':
                    i = i.replace(i[y], '')
                else:
                    y += 1
        i = i.lower()
        if i != '':
            if i not in tally:
                tally[i] = 1
            else:
                tally[i] += 1
    return tally

def categorize(tally):
    categorized = {'total':0, 'xy':0, 'ae':0}
    for i in tally:
        categorized['total'] += 1
    for y in tally:
        if y[0] == 'x' or y[0] == 'y':
            categorized['xy'] += 1
        elif y[0] == 'a' or y[0] == 'e':
            categorized['ae'] += 1
    return categorized

with open("moby.txt") as s:
    dictionary = bookToDictionary(s.read())
print(dictionary)
print(categorize(dictionary))
