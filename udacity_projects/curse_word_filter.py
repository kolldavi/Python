from urllib import request, parse

def read_text():
    quotes = open("./message.txt")
    content = quotes.read()

    quotes.close()
    check_curse_word(content)



def check_curse_word(txt):
    url = f'http://www.wdylike.appspot.com/?q={parse.quote(txt)}'
    
    req = request.urlopen(url)
    answer = req.read()
    print(answer)
    req.close()

read_text()