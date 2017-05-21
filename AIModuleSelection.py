class AIModuleSelection:

	def __init__(self, query, lemmatizer, stopwords, parser, conversion_service, classifiers):
		self.lemmatizer = lemmatizer
		self.stopwords = stopwords
		self.conversion_service = conversion_service
		self.parser = parser
		self.classifiers = classifiers
		return self.select_the_module(query)

	# This does the magic - preprocessing
	def do_the_magic(self, query):
		import re
		query = " ".join([self.lemmatizer.lemmatize(e) for e in query.split()])
		try:
			query = unicode(query, 'utf-8')
		except TypeError:
			pass
		query = re.sub('(((\d{1,2}:\d{1,2}|\d+)\s(a\.m|A\.M|p\.m|P\.M))|seconds?|hours?|minutes?)', 'TIME', query) # RE for time tagging
		units = self.conversion_service.extractUnits(query)
		for unit in units:
			if unit not in self.stopwords:
				query = re.sub('\w*%s\w*'%(unit), 'QUANTITY', query)
		parsed = self.parser(query).ents
		for entity in parsed:
			try:
				_ = int(entity.text)
				query = query.replace(entity.text, entity.label_)
			except ValueError:
				if entity.text not in self.stopwords and entity.text.upper() != entity.text:
					query = query.replace(entity.text, entity.label_)
		
		return str(query)

	def select_the_module(self, query):
		modules = {}
		for classifier in self.classifiers:
			result = classifier.predict([do_the_magic(query)])[0]
			modules[result] = modules.setdefault(result, 0) + 1
		for module in modules:
			if modules[module] == max(modules.values()):
				return module
