import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag.perceptron import PerceptronTagger
from AIAlarm import AlarmResponse
from AIConverter import ConversionResponse
from AISummarizer import SummarizerResponse
from AINews import NewsResponse
from AIMaps import MapsResponse

'''
def lemmatize(query):
    wnl = WordNetLemmatizer()
    tokens = [token.lower() for token in word_tokenize(query)]
    lemmatized_query = [wnl.lemmatize(token) for token in tokens]
    return lemmatized_query
'''


class Brain:

    def __init__(self):
        
        self.tagger       = PerceptronTagger()
        self.alarm_ai     = AlarmResponse()
        self.converter_ai = ConversionResponse()
        self.summarize_ai = SummarizerResponse()
        self.news_ai      = NewsResponse()
        self.maps_ai      = MapsResponse()
        self.ai           = [self.alarm_ai, self.converter_ai, self.summarize_ai, self.news_ai, self.maps_ai]

    def response(self, plain_text):
        #tokens = lemmatize(plain_text)
        tokens     = plain_text.lower().split()
        #plain_text = " ".join(tokens)
        tags       = nltk.tag._pos_tag(tokens, None, tagger=self.tagger)
        for ai in self.ai:
            if ai.can_response(tags=tags, plain_text=plain_text):
                return ai.respond(tags=tags, plain_text=plain_text)
        return "Oh .. Don't ask me that!!"


'''
# For Unit Testing . . .
query = "CONVERT MILES TO KM"
brain = Brain()
print brain.response(query)
'''