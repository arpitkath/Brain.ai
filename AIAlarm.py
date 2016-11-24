from dateutil import parser
from datetime import datetime


class AlarmResponse:

    def __init__(self):
        pass

    def can_response(self, **kwargs):

        tags = kwargs.get('tags')
        plain_text = kwargs.get('plain_text').split()

        check = [("alarm", "NN"),
                 ("alarm", "JJ")
                 ]

        for tag in tags:
            if tag in check and ("create" in plain_text or "set" in plain_text):
                return True

        return False

    def respond(self, **kwargs):

        plain_text = kwargs.get('plain_text')
        _time = []

        for word in plain_text.split():
            try:
                parser.parse(word)
                _time.append(word)
            except:
                pass

        if len(_time) == 0:
            return "Oops! .. Having some problem!"

        _time = " ".join(_time)

        if "pm" in plain_text.split() or "p.m" in plain_text.split():
            _time += "pm"

        try:
            _time = int(parser.parse(_time).strftime("%s"))
            _time -= int(datetime.now().strftime("%s"))
        except:
            return "Oops! .. Having some problem!"

        if "tomorrow" in plain_text.split():
            _time += int(24 * 60 * 60)

        if _time <= 0:
            return "I do not have time machine..:P"
        return "alarm " + str(_time)

'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = "create an alarm for wednesday 5:45 pm"
print(sentence)
text_input = sentence.lower()
#print(text_input)
tokens = nltk.word_tokenize(text_input)
#print(tokens)
perceptron_tagger = PerceptronTagger()
tags = nltk.tag._pos_tag(tokens, None, tagger=perceptron_tagger)
print(tags)
cr = AlarmResponse()
if cr.can_response(tags=tags, plain_text=text_input):
    print cr.respond(tags=tags, plain_text=text_input)
else:
    print "something wrong"
'''