import duckduckgo


class SummarizerResponse:

    def __init__(self):
        pass

    def can_response(self, **kwargs):
        # Always return something, maybe useful 
        return True
    def respond(self, **kwargs):

        plain_text = kwargs.get('plain_text').lower()

        try:
            for i in range(5):
                print "Attempt #%d"%(i + 1)
                try:
                    result = str(duckduckgo.get_zci(plain_text))#.split()
                    return result
                except:
                    pass
        except:
            return "Oops! .. Having some problem!"
        return "Oops! .. Having some problem!"


'''
# For Unit Testing . . .
import nltk
from nltk.tag.perceptron import PerceptronTagger

sentence = raw_input()
print(sentence)
text_input = sentence.lower()
#print(text_input)
tokens = nltk.word_tokenize(text_input)
#print(tokens)
perceptron_tagger = PerceptronTagger()
tags = nltk.tag._pos_tag(tokens, None, tagger=perceptron_tagger)
print(tags)
cr = SummarizerResponse()
if cr.can_response(tags=tags, plain_text=text_input):
    print cr.respond(tags=tags, plain_text=text_input)
else:
    print "something wrong"
'''
