import spacy.en

'''
Caution:
Not working if entity's initials are lower case.
'''

class MapsResponse:

    def __init__(self):

        self.parser = spacy.en.English()

    def can_response(self, **kwargs):

        tags       = kwargs.get('tags')
        plain_text = kwargs.get('plain_text')
        parsed = self.parser(plain_text).ents
        return len(parsed) in [1, 2]

    def respond(self, **kwargs):

        plain_text = kwargs.get('plain_text')
        parsed = self.parser(plain_text).ents
        location = ""
        if len(parsed) == 1:
            location = "map2 "
            place = str(parsed[0]).lower()
            if len(place.split()) == 2:
                place = "_".join(str(i) for i in place.split())
            location += place
        elif len(parsed) == 2:
            location = "map3 "
            place_1 = str(parsed[0]).lower()
            place_2 = str(parsed[1]).lower()
            if len(place_1.split()) == 2:
                place_1 = "_".join(str(i) for i in place_1.split())
            if len(place_2.split()) == 2:
                place_2 = "_".join(str(i) for i in place_2).split()
            location += place_1 + " " + place_2
        else:
            return "Something Wrong!"

        return location


'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = "directions to Chandigarh"
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