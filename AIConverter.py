from semantic.units import ConversionService
import inflect
import re


class ConversionResponse:

    def __init__(self):
        pass

    def can_response(self, **kwargs):

        tags = kwargs.get('tags')
        plain_text = kwargs.get('plain_text').lower()

        check = [('convert', 'VB'),
                 ('convert', 'NN'),
                 ('much', 'JJ'),
                 ('many', 'JJ')
                 ]

        for tag in tags:
            if tag in check:
                service = ConversionService()
                units = service.extractUnits(plain_text)
                #print units
                if len(units) > 1:
                    return True

        return False

    def respond(self, **kwargs):

        plain_text = kwargs.get('plain_text').lower()
        service    = ConversionService()
        units      = service.extractUnits(plain_text)

        inf_eng    = inflect.engine()

        try:
            original_num = re.findall(r'\d+', plain_text)

            if len(original_num) == 0:
                try:
                    converted_num = service.convert(plain_text)
                    return "Your ans is " + "%.2f"%(float(str(service.convert(plain_text)).split()[0])) + " " + units[1]
                except TypeError:
                    plain_text = "one " + units[0] + " to " + units[1]
                    original_num = [1]

            converted_num = float("%.2f"%(float(str(service.convert(plain_text)).split()[0])))

            output = str(inf_eng.number_to_words(original_num[0])) + " " + units[0] + " equals " + str(inf_eng.number_to_words(converted_num)) + " " + units[1]
            return output


        except TypeError:

            return "Sorry, I cannot convert these units."

        except:

            return "Oops! .. Having some problem!"


'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = "convert 3.5 kilometers to miles"
print(sentence)
text_input = sentence.lower()
#print(text_input)
tokens = nltk.word_tokenize(text_input)
#print(tokens)
perceptron_tagger = PerceptronTagger()
tags = nltk.tag._pos_tag(tokens, None, tagger=perceptron_tagger)
print(tags)
cr = ConversionResponse()
if cr.can_response(tags=tags, plain_text=sentence):
    print cr.respond(tags=tags, plain_text=sentence)
else:
    print "something wrong"
'''

