class ModuleSelection:

	def __init__(self, query, lemmatizer, stopwords, parser, conversion_service, classifiers):
		self.lemmatizer = lemmatizer
		self.stopwords = stopwords
		self.conversion_service = conversion_service
		self.parser = parser
		self.classifiers = classifiers
		self.modules = self.select_the_module(query)

	# This does the magic
	def do_the_magic(self, query):
		import re
		print query + " ---> ",
		query = " ".join([self.lemmatizer.lemmatize(e) for e in query.split()])
		try:
			query = unicode(query, 'utf-8')
		except TypeError:
			pass
		query = re.sub('(((\d{1,2}:\d{1,2}|\d+)\s(a\.?m|A\.?M|p\.?m|P\.?M))|seconds?|hours?|minutes?)', 'TIME', query) # RE for time tagging
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
		print query,
		return str(query)

	def select_the_module(self, query):
		modules = {}
		query = self.do_the_magic(query)
		for classifier in self.classifiers:
			result = classifier.predict([query])[0]
			modules[result] = modules.setdefault(result, 0) + 1
		modules = modules.items()
		modules.sort(reverse=True, key=lambda x: x[1])
		modules = list(map(lambda x: x[0], modules))
		print modules
		return modules

	def get_modules(self):
		return self.modules