import requests
from bs4 import BeautifulSoup


class NewsResponse:

    def __init__(self):
        pass

    def can_response(self, **kwargs):

        tags       = kwargs.get('tags')
        plain_text = kwargs.get('plain_text').lower().split()

        check      = [('news', 'JJ'),
                       ('news', 'NN')
                      ]

        for tag in tags:
            if tag in check:
                return True

        return False

    def respond(self, **kwargs):

        URL       = "http://indiatoday.intoday.in/news.html"
        news      = []
        data      = ""
        n_attempt = 0
        for i in range(5):
            try:
                print "Attempt #%d" % (i + 1)
                data = requests.get(URL)
                break
            except:
                n_attempt += 1
        if n_attempt > 4:
            return "Try again later ..."
        soup = BeautifulSoup(data.text, 'html.parser')
        news_ul = soup.find('div', {'class': 'normaltaxt'}).ul

        for _news in news_ul.find_all('li'):
            news.append(_news.find('a').contents[0])

        return "news " + "...".join(news)
'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = "latest news"
print(sentence)
text_input = sentence.lower()
#print(text_input)
tokens = nltk.word_tokenize(text_input)
#print(tokens)
perceptron_tagger = PerceptronTagger()
tags = nltk.tag._pos_tag(tokens, None, tagger=perceptron_tagger)
print(tags)
cr = NewsResponse()
if cr.can_response(tags=tags, plain_text=text_input):
    print cr.respond(tags=tags, plain_text=text_input)
else:
    print "something wrong"
'''