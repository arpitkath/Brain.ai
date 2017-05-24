import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag.perceptron import PerceptronTagger
from AIAlarm import AlarmResponse
from AIConverter import ConversionResponse
from AISummarizer import SummarizerResponse
from AINews import NewsResponse
from AIMaps import MapsResponse
from AIModuleSelection import ModuleSelection
import spacy.en as spy
from semantic.units import ConversionService
import cPickle


STOP_WORDS = set(stopwords.words('english'))
STOP_WORDS.add('in')
STOP_WORDS.add('are')


class Brain:

	def __init__(self):
		
		self.tagger       = PerceptronTagger()
		self.alarm_ai     = AlarmResponse()
		self.converter_ai = ConversionResponse()
		self.summarize_ai = SummarizerResponse()
		self.news_ai      = NewsResponse()
		self.maps_ai      = MapsResponse()
		self.lemmatizer   = WordNetLemmatizer()
		self.parser       = spy.English()
		self.conversion   = ConversionService()
		self.ai           = {"alarm_api": self.alarm_ai, "unit_conversion": self.converter_ai, "summarization": self.summarize_ai, "news": self.news_ai, "maps_api": self.maps_ai}
		self.classifiers  = []
		with open('nb_dumped_classifier.pkl', 'rb') as fid:
			self.classifiers.append(cPickle.load(fid))
		with open('sgd_dumped_classifier.pkl', 'rb') as fid:
			self.classifiers.append(cPickle.load(fid))   
		with open('pla_dumped_classifier.pkl', 'rb') as fid:
			self.classifiers.append(cPickle.load(fid)) 
		self.previous_ents = {"PERSON": "", "GPE": ""}
		self.special_tags = {'PERSON': ['his', 'her', 'him', 'he', 'she'], 'GPE': ['it', 'there']}

	def response(self, plain_text):
		plain_text = plain_text.split()
		for ents in self.special_tags:
			for tag in self.special_tags[ents]:
				if tag in plain_text and self.previous_ents[ents] != "":
					plain_text[plain_text.index(tag)] = self.previous_ents[ents]
		plain_text = " ".join(plain_text)
		try:
			plain_text = unicode(plain_text, 'utf-8')
		except TypeError:
			pass
		parsed = self.parser(plain_text).ents
		for ents in parsed:
			if ents.label_ in self.previous_ents.keys():
				self.previous_ents[ents.label_] = ents.text

		tokens     = plain_text.lower().split()
		tags       = nltk.tag._pos_tag(tokens, None, tagger=self.tagger)
		modules    = ModuleSelection(plain_text, self.lemmatizer, STOP_WORDS, self.parser, self.conversion, self.classifiers).get_modules()
		for module in modules:
			if self.ai[module].can_response(tags=tags, plain_text=plain_text):
				return self.ai[module].respond(tags=tags, plain_text=plain_text)
		return "Something Wrong!"


'''
# For Unit Testing . . .
brain = Brain()
print "Ready!"
for _ in xrange(50):
	query = raw_input()
	print brain.response(query)

'''