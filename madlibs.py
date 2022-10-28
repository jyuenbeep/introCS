import random

text = '''
As President of the {NAME6} Law {PLACE}, she {VERB} a certain amount of respect among her peers;
as a legacy student bearing the {NAME1} name, she commands even more among the faculty, most of whom
{VERB} her {NOUN} and her {NOUN} before her. {NAME2} has the sort of presence that makes all other
people in the room stop and {VERB} attention; a {ADJECTIVE}, {ADJECTIVE}, {ADJECTIVE} presence,
bred into her by her bloodline and {VERB} into her by her mother’s discipline. Yes, she commands respect.

Or at least she does around most {NOUN}, she mumbles to herself as {NAME3} {VERB} a {NOUN} that
hits {NAME4} square in the eye, yelling something about {NOUN} while {NAME5} tries to {VERB} her in to
little avail. {NAME3} shouldn’t even be in here. She’s {ADVERB} even enrolled in {PLACE}, let alone law
{PLACE}, but nothing stops {NAME5}’s little {NOUN} from doing whatever she wants. {NAME2} almost envies
them, watching {NAME5} {VERB} the kid around and {VERB} {NOUN} away from her. There’s something nice about
siblings. But then {NAME3} skids under a {PLACE} and connects two of the {NOUN} and there’s the {ADJECTIVE},
{ADJECTIVE} sound of a spark and {NAME2} decides maybe she’s okay with being an only child.
'''

nounList = ['book', 'statue', 'pen', 'president', 'woman', 'man', 'bottle', 'computer', 'headphones']
verbList = ['ran', 'jumped', 'hopped', 'give', 'dash', 'eat', 'smother', 'smack', 'carry']
adjectiveList = ['beautiful', 'cute', 'pretty', 'adventurous', 'calm', 'excited', 'slick', 'intellectual', 'talented']
nameList = ['James','Kallen','Jean','Ayura','Misaki','Karl','Jessi','Olivia','Ari','Matthew','Kiana']
adverbList = ['quickly', 'loudly', 'slowly', 'awkwardly', 'extremely', 'barely', 'terribly', 'deftly', 'very']
placeList = ['school', 'hospital', 'bank', 'bedroom', 'bathroom', 'garage', 'deskspace', 'park', 'intersection']

def replaceWords(text,nounList,verbList,adjectiveList,nameList):
    for i in text:
        text = text.replace('{ADJECTIVE}', random.choice(adjectiveList), 1)
        text = text.replace('{NOUN}', random.choice(nounList), 1)
        text = text.replace('{VERB}', random.choice(verbList), 1)
        text = text.replace('{ADVERB}', random.choice(adverbList), 1)
        text = text.replace('{PLACE}', random.choice(placeList), 1)
    string = '{NAMEX}'
    x = 1
    while x <= 9:
        string =  string.replace('X', str(x))
        temp = random.choice(nameList)
        while string in text:
            if temp in text:
                temp = random.choice(nameList)
            else:
                text = text.replace(string, temp)
        x += 1
        string = '{NAMEX}'
    return text

print(replaceWords(text,nounList,verbList,adjectiveList,nameList))
