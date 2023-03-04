import requests
import bs4

url = ''

src = requests.get(url)
soup = bs4.BeautifulSoup(src.text, 'html.parser')

keyWordList = soup.text
keyWordList = keyWordList.split()

soundexChar = {0: ['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y'], 1: ['b', 'f', 'p', 'v'], 2: ['c', 'g', 'j', 'k', 'k', 'q', 's', 'x', 'z'], 3: ['d', 't'], 4: ['l'], 5: ['m', 'n'], 6: ['r']}

res = set([token.lower() for token in keyWordList if token.isalpha()])

answer = dict()

for i in list(res):
    recent = ''
    code = i[0]
    for c in i[1:]:
        for k, v in soundexChar.items():
            if c.lower() in v and c != recent:
                recent = c
                code = code + str(k)
        code = code.replace('0', '')
    if len(code) < 4:
        code = code + '000'
    if code[:4] not in answer.keys():
        answer.setdefault(code[:4], [i])
    else:
        answer[code[:4]].append(i)

for k,v in answer.items():
    print(k, v)
