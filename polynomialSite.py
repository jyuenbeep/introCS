PAGE_TITLE = "My Favorite Polynomial"

def generateBody():
    body = "<h1>My Favorite Polynomial</h1>\n"
    body += "<h2> 8X^3 + 8X + 8 </h2>\n"
    body += "<h3>why it's my favorite:</h3>\n"
    body += "<p>I like this polynomial because it is just satisfying to see. Reason one being: eight is my favorite number, so having all the coefficients being eight just feels right. Secondly, I like even numbers the most, so having the first exponent being two, the root of all even numbers, is even better. Though this explanation isn't too special at all, I enjoy this polynomial because what numbers I love.</p>\n"
    return body

def makePolyTable(start, end):
    count = start - 1
    phrase = '<table border="1%"> <th>x</th> <th>8X^3 + 8X + 8 </th>'
    while count < end+1:
        phrase += ('<tr><td>' + str(count) + '</td><td>' + str((8 *(count**2)) + (8*count) + 8) + '</td></tr>\n')
        count += 1
    return (phrase + '</table>')

page = '''
<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
        _TABLE_
    </body>
</html>
'''

page = page.replace("_TITLE_",PAGE_TITLE)
page = page.replace("_BODY_",generateBody())
page = page.replace("_TABLE_",makePolyTable(-20, 50))

print(page)
