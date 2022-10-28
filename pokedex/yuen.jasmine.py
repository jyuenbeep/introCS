STYLE = '''
table, td, tr, th {
    text-align:center;
    margin-left:auto;
    margin-right:auto;
    padding-right:10px;
    padding-left:10px;
    background-color:#e79c9c;
    opacity:90%;
    font-weight:bolder;
    font-family:Courier;
    position:relative;
    border-width:3px;
    border-style:solid;
    border-collapse: collapse;
    border-color:#9D80C6;
    z-index:-1;
    }
body {
    text-align:center;
    background-image: url('https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2020%2F04%2Fpokemon-pikachu-video-chat-backgrounds-download-info-003.jpg?quality=95&w=1170&cbr=1&q=90&fit=max');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}
h1 {
    font-family:Garamond;
    color:white;
    font-size:70px;
    text-shadow:
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
}
p {
    margin-left:150px;
    margin-right:150px;
    padding-bottom: 20px;
    font-family:Garamond;
    font-weight:bolder;
    font-size:130%;
}
nav {
    background-color:#9D80C6;
    padding-top:10px;
    padding-bottom:10px;
    opacity:95%;
    z-index:0;
    position: fixed;
    top: 0px;
    width:100%;
    display: flex;
    justify-content: space-around;
}
nav li {
   display: inline-block;
   position: relative;
   font-size:30px;
   font-family:Garamond;
   padding-left:40px;
   padding-right:40px;
}
nav li ul {
   display: none;
   position: absolute;
   width: 200px;
   top: 100%;
   padding: 0;
   background:black;
   padding:none;
}
nav li:hover > ul {
   display: block;
}
nav li > ul > li:hover {
    background-color:white;
}
nav li > ul > li:hover > a:link{
    color:black;
}
nav a:link, nav li{
    text-decoration: none;
    color: white;
}
a:visited:hover {
    color:black;
}
a:visited {
    color:white;
}
h1 {
    padding-top:90px;
}
.gif {
    height:30%;
    width:auto;
}
.Normal{background-color:#A8A878}
.Fire{background-color:#F08030}
.Water{background-color:#6890F0}
.Flying{background-color:#A890F0}
.Grass{background-color:#78C850}
.Poison{background-color:#A040A0}
.Electric{background-color:#F8D030}
.Ground{background-color:#E0C068}
.Psychic{background-color:#F85888}
.Rock{background-color:#B8A038}
.Ice{background-color:#98D8D8}
.Bug{background-color:#A8B820}
.Dragon{background-color:#7038F8}
.Ghost{background-color:#705898}
.Dark{background-color:#705848}
.Fairy{background-color:#e76d88}
.Steel{background-color:#B8B8D0}
.Fighting{background-color:#C03028}
'''

TITLE = 'pokedex'
PARAGRAPH = '''
<p> I think Pokemon are really cool; I've been watching
the Pokemon franchise since I was young so I grew up with it! I think my favorite Pokemon
has to be Zorua, and maybe Snivy is a close second. In my honest opinion, the Sword and Shield game
(actually any of the newer ones) isn't as bad as hardcore fans make it out to be. The CG is done really
well so it still captures some Pokemon aesthetic while changing to a more modern video game style.
As for my favovrite generation I think it might be X & Y... Why? I don't know. It just stuck with me,
especially the legendaries.
</p>
'''

file = open('pokemon/pokemon.csv','r')
data = file.read()

def demo(data):
    data = data.split("\n")
    for y in range(len(data)):
        data[y] = str(data[y])
        data[y] = data[y].split(",")
    return data
data = demo(data)

def makeHTMLTable(data):
    end = ("<table>\n")
    imag = 1
    i = 0
    end += ("<th>" + '''<img  src="img/front/0.png">''' + "</th>")
    end += ("<th>" + '''<img  src="img/back/0.png">''' + "</th>")
    while i < (len(data[0])):
        if i != 2:
            end += ("<th>")
            end += data[0][i]
            end += ("</th>")
            i += 1
        elif i == 2:
            end += ("<th>" + "Type(s)" + "</th>")
            i += 2
    for i in range(1, len(data)-1):
        y = 0
        end += ("  <tr>")
        end += ("<td>" + '''<img  src="img/front/imag.png">''' + "</td>")
        end += ("<td>" + '''<img  src="img/back/imag.png">''' + "</td>")
        end = end.replace("imag", str(imag))
        while y < (len(data[i])):
            if y != 2:
                end += ("    <td>")
                end += (data[i][y])
                end += ("</td>")
                y += 1
            elif y == 2:
                end += ("<td>" + "<div class = typpe> typpe </div>" + "<div class = tyee> tyee </div>" + "</td>")
                end = end.replace("typpe", data[i][y])
                end = end.replace("tyee", data[i][y+1])
                y += 2
        end += ("  </tr>")
        imag += 1
    end += ("</table>")
    return end

def makeTypes(data):
    types = []
    for i in range(1, len(data)-1):
        for y in range(2, 4):
            if data[i][y] not in types and data[i][y] != '':
                types += [data[i][y]]
    return types

pokeList = makeTypes(data)

def createNavBar(data):
    nav = '''
      <nav>
        <ul>
          <li><a href="home.html">Home</a></li>
          <li><a href="all.html">All Pokemon</a></li>
          <li>Types
             <ul>
    '''
    navTypes = makeTypes(data)
    for i in range(len(navTypes)):
        nav += '''<li><a href="x.html">x</a></li>'''
        nav = nav.replace("x", navTypes[i])
    nav += '''
             </ul>
           </li>
           <li><a href="top.html">Top 10</a></li>
         </ul>
       </nav>'''
    return nav

def home():
    site = '''
    <DOCTYPE HTML>
    <html>
      <head>
        <title>
          ?TITLE?
        </title>
        <link rel="stylesheet" href="stylesheet.css">
      </head>
      <body>
        ?NAV?
        ?HEADING?
        ?PARAGRAPH?
        <div>?IMAGE? ?IMAGE? ?IMAGE?</div>
      </body>
    </html>'''
    site = site.replace("?NAV?", createNavBar(data))
    site = site.replace("?TITLE?", TITLE)
    site = site.replace("?HEADING?", "<h1>Home</h1>")
    site = site.replace("?PARAGRAPH?", PARAGRAPH)
    site = site.replace("?IMAGE?", '''<img src = "https://64.media.tumblr.com/0564b6a3c851e821c81a2c643f4911f6/cd69cf00bbaa6537-e0/s500x750/8affdceebbe434e6f58ec1997fcd3786cb53c6df.gifv" class = "gif">''')
    return site

f = open("home.html", "w")
f.write(home())
f.close()

def allPokemon():
    site = '''
    <DOCTYPE HTML>
    <html>
      <head>
        <title>
          ?TITLE?
        </title>
        <link rel="stylesheet" href="stylesheet.css">
        <style>
          ?STYLE?
        </style>
      </head>
      <body>
        ?NAV?
        ?HEADING?
        ?PARAGRAPH?
        ?BODY?
      </body>
    </html>'''
    site = site.replace("?HEADING?", "<h1>All Pokemon</h1>")
    site = site.replace("?NAV?", createNavBar(data))
    site = site.replace("?TITLE?", TITLE)
    site = site.replace("?BODY?", makeHTMLTable(data))
    site = site.replace("?PARAGRAPH?", '''<p>I changed the color of each type per pokemon to a specific
                                             color that I coded to each type. I also combined the type 1
                                             and type 2 columns into one "type(s)" column, containing all
                                             the types for that pokemon.</p>''')
    return site

f = open("all.html", "w")
f.write(allPokemon())
f.close()

f = open("stylesheet.css", "w")
f.write(STYLE)
f.close()

def makePage(pokeList, pokeType):
    #splitdata = demo(data)
    end = ("<table>\n")
    #x = 1
    i = 0
    end += ("<th>" + '''<img  src="img/front/0.png">''' + "</th>")
    end += ("<th>" + '''<img  src="img/back/0.png">''' + "</th>")
    while i < (len(data[0])):
        if i != 2:
            end += ("<th>")
            end += data[0][i]
            end += ("</th>")
            i += 1
        elif i == 2:
            end += ("<th>" + "Type(s)" + "</th>")
            i += 2
    for i in range(1, len(data)-1):
        if pokeType in data[i]:
            x  = i
            y = 0
            end += ("<tr>")
            end += ("<td>" + '''<img  src="img/front/imag2.png">''' + "</td>")
            end += ("<td>" + '''<img  src="img/back/imag2.png">''' + "</td>")
            end = end.replace("imag2", str(x))
            while y < (len(data[i])):
                if y != 2:
                    end += ("<td>")
                    end += (data[i][y])
                    end += ("</td>")
                    y += 1
                elif y == 2:
                    end += ("<td>" + "<div class = typpe> typpe </div>" + "<div class = tyee> tyee </div>" + "</td>")
                    end = end.replace("typpe", data[i][y])
                    end = end.replace("tyee", data[i][y+1])
                    y += 2
            end += ("</tr>")
    end += ("</table>")
    return end

for pokeType in pokeList:
    sitetype = '''
    <DOCTYPE HTML>
    <html>
        <head>
        <title>
          ?TITLE?
        </title>
        <link rel="stylesheet" href="stylesheet.css">
        <style>
          ?STYLE?
        </style>
      </head>
      <body>
        ?NAV?
        <h1>?HEADING?</h1>
        <p>Here are all the pokemon with the ?PARAGRAPH? type!</p>
        ?BODY?
      </body>
    </html>'''
    sitetype = sitetype.replace("?HEADING?", pokeType)
    sitetype = sitetype.replace("?NAV?", createNavBar(data))
    sitetype = sitetype.replace("?TITLE?", TITLE)
    sitetype = sitetype.replace("?BODY?", makePage(pokeList, pokeType))
    sitetype = sitetype.replace("?PARAGRAPH?", pokeType)
    type1 = pokeType + ".html"
    f = open(type1, "w")
    f.write(sitetype)
    f.close()

def top10():
    site = '''
    <DOCTYPE HTML>
    <html>
        <head>
        <title>
          ?TITLE?
        </title>
        <link rel="stylesheet" href="stylesheet.css">
        <style>
          ?STYLE?
        </style>
      </head>
      <body>
        ?NAV?
        <h1>?HEADING?</h1>
        ?PARAGRAPH?
        ?BODY?
      </body>
    </html>'''
    end = ("<table>\n" + "<th>My Top</th>")
    count = 0
    i = 0
    end += ("<th>" + '''<img  src="img/front/0.png">''' + "</th>")
    end += ("<th>" + '''<img  src="img/back/0.png">''' + "</th>")
    while i < (len(data[0])):
        if i != 2:
            end += ("<th>")
            end += data[0][i]
            end += ("</th>")
            i += 1
        elif i == 2:
            end += ("<th>" + "Type(s)" + "</th>")
            i += 2
    for i in range(1, len(data)-1):
        if data[i][0] == '1' or data[i][0] == '4' or data[i][0] == '7' or data[i][0] == '25' or data[i][0] == '43' or data[i][0] == '113' or data[i][0] == '132' or data[i][0] == '143' or data[i][0] == '145' or data[i][0] == '133':
            x  = i
            y = 0
            end += ("<tr>")
            end += ("<td>" + "count1" + "</td>" + "<td>" + '''<img  src="img/front/imag2.png">''' + "</td>")
            end += ("<td>" + '''<img  src="img/back/imag2.png">''' + "</td>")
            end = end.replace("imag2", str(x))
            count += 1
            end = end.replace("count1", str(count))
            while y < (len(data[i])):
                if y != 2:
                    end += ("<td>")
                    end += (data[i][y])
                    end += ("</td>")
                    y += 1
                elif y == 2:
                    end += ("<td>" + "<div class = typpe> typpe </div>" + "<div class = tyee> tyee </div>" + "</td>")
                    end = end.replace("typpe", data[i][y])
                    end = end.replace("tyee", data[i][y+1])
                    y += 2
            end += ("</tr>")
    end += ("</table>")
    site = site.replace("?HEADING?", "Top 10")
    site = site.replace("?NAV?", createNavBar(data))
    site = site.replace("?TITLE?", TITLE)
    site = site.replace("?BODY?", end)
    site = site.replace("?PARAGRAPH?", '''<p>The first four listed pokemon are some of my favorites since they are very first starters,
                                             including Pikachu, which brings back a lot of nostalgia for me. For the others, I just chose
                                             the Pokemon I liked the most, as well as my favorite legendary from these 151 pokemon. Oddish
                                             used to be my favorite pokemon since I saw cute clips of it hopping up and down on YouTube.
                                             Then the others I based off of their iconicness, such as Chansey, being the nurses for the
                                             Pokecenters around the Pokemon universe. And then there's Snorlax, which almost everyone knows,
                                             and then Eevee, who has really cool evolutions that is unique about it.</p>''')
    return site
f = open("top.html", "w")
f.write(top10())
f.close()

#python yuen.jasmine.py
#python yuen.jasmine.py > all.html
