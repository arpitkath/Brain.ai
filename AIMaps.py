import spacy.en


class MapsResponse:

    def __init__(self):

        self.parser = spacy.en.English()
        self.special_check = ['atm', "atm's", 'restaurants', 'restaurant']

    def can_response(self, **kwargs):

        tags       = kwargs.get('tags')
        plain_text = kwargs.get('plain_text')

        check      = [('path', 'NN'),
                       ('route', 'NN'),
                       ('distance', 'NN')
                      ]

        other_check = [('nearest', 'JJS'), ('nearby', 'JJS'), ('nearby', 'RB')]
        if any(i in other_check for i in tags):
            plain_text = unicode(plain_text, 'utf-8')
            parsed = self.parser(plain_text).ents
            return len(parsed) == 1 or any(s in self.special_check for s in str(plain_text).lower().split())

        if 'from' in plain_text.split() and 'to' in plain_text.split():
            plain_text = unicode(plain_text, 'utf-8')
            parsed = self.parser(plain_text).ents
            print parsed
            return len(parsed) == 2

        for tag in tags:
            if tag in check:
                plain_text = unicode(plain_text, 'utf-8')
                parsed = self.parser(plain_text).ents
                return len(parsed) == 2

        return False

    def respond(self, **kwargs):

        plain_text = unicode(kwargs.get('plain_text'), 'utf-8')
        parsed = self.parser(plain_text).ents
        location = "map "
        if any(s in self.special_check for s in str(plain_text).lower().split()):
            for i in self.special_check:
                if i in str(plain_text).lower().split():
                    location += i
                    break
        elif len(parsed) == 1:
            place = str(parsed[0]).lower()
            if len(place.split()) == 2:
                place = "_".join(str(i) for i in place.split())
            location += place
        elif len(parsed) == 2:
            place_1 = str(parsed[0]).lower()
            place_2 = str(parsed[1]).lower()
            if len(place_1.split()) == 2:
                place_1 = "_".join(str(i) for i in place_1.split())
            if len(place_2.split()) == 2:
                place_2 = "_".join(str(i) for i in place_2).split()
            location += place_1 + " " + place_2
        else:
            return "Oops! .. Having some problem!"

        return location


'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = "nearby atms"
print(sentence)
text_input = sentence
#print(text_input)
tokens = nltk.word_tokenize(text_input)
#print(tokens)
perceptron_tagger = PerceptronTagger()
tags = nltk.tag._pos_tag(tokens, None, tagger=perceptron_tagger)
print(tags)

cr = MapsResponse()
if cr.can_response(tags=tags, plain_text=text_input):
    print cr.respond(tags=tags, plain_text=text_input)
else:
    print "something wrong"
'''