import sys

class Model1(object):
	
	def __init__(self, data):
	    

	    self.de_words = []
	    self.de_dict = []
	    self.en_words = []
	    self.en_dict = []
	    self.dev_words = []
	    self.sent_pairs = []

	    self.probs = {}
	    self.transmissions = {}
	    self.countef = {}
	    self.totalf = {}
	    self.totals = {}
	    self.data = data

	    
	    self.de_dict, self.de_words = self.convertArgsToTokens( self.data[1] )
	    self.en_dict, self.en_words = self.convertArgsToTokens( self.data[2] )

	    self.dev_in = open(self.data[3], 'r')
	    self._dev_lines = self.dev_in.readlines()
	    self.dev_in.close()

	    for index in range(len(self.en_dict)):
	    	pair = (self.en_dict[index], self.de_dict[index])
	    	self.sent_pairs.append(pair)
	    # print "PAIRS:"
	    # print self.sent_pairs

	    

	def convertArgsToTokens(self, data):
		"""
		this converts the readin lines from
		sys to useable format, returns list
		of token and dict of tokens
		"""

		tdict  = []
		tokens = []
		
		d = open(data, 'r')
		for line in d.readlines():
			tdict.append( line.rstrip() )
			tokens +=  line.split()
	      		  	
	  	d.close() 
	  	tokens = list( set(tokens) )    
	  	# print "!!!!"
	  	# print tokens
	  	return tdict, tokens

	def initTef(self):
		''' 
		get all probable matches
		and then initialize t(f|e)
		'''
		probs = {}
		transmissions = {}

		# go through each german word
		for word in self.de_words:
			word_poss = []
			# if word in sentence.. then 
			for sent in self.de_dict:
				if word in sent:
					matching = self.en_dict[ self.de_dict.index(sent)]
					word_poss = word_poss + matching.split()

			#remove the duplicates 
			word_poss = list( set(word_poss))
			#add the probable matches 
			probs[word] = word_poss

		self.probs = probs
			
		for word in self.de_words:
			#print self.probs
			word_probs = self.probs[word]
			if (len(word_probs) == 0):
				print word, word_probs
			uniform_prob = 1.0/ len(word_probs)

			word_probs = dict( [(w, uniform_prob) for w in word_probs] )
			
			#print word_probs
			transmissions[word] = word_probs 
				
		self.transmissions = transmissions
		# print "!!!!"
		# print self.transmissions
			

	def iterateEM(self, count):
		

		for iter in range(count):
			print "ITERATION #("+str(iter + 1)+")\n"

			countef = {}
			totalf  = {}
			# set the count of the words to zero
			for word in self.de_words:
				
				word_probs = self.probs[word]
				
				count = dict( [(w, 0) for w in word_probs] )
				countef[word] = count
				totalf[word] = 0
			
			self.countef = countef
			
			self.totalf = totalf

			# print "!!!"
			# print self.countef
			 
			
			for (es, ds) in self.sent_pairs:
				es_split = es.split()
				ds_split = ds.split()
				
				
				# print es_split
				# print ds_split

				for e in es_split:
					self.totals[e] = 0
					for d in ds_split:
						#print self.transmissions
						d_trans = self.transmissions[d]
						
						if (e not in d_trans):
							continue

						self.totals[e] += d_trans[e]
						# print "!!!"
						# print self.totals

					for d in ds_split:
						if (e not in self.transmissions[d]):
							continue
						self.countef[d][e] += self.transmissions[d][e] / self.totals[e]
						self.totalf[d] += self.transmissions[d][e] / self.totals[e]
						
						# print "!!!"
						# print self.countef
				# print "!!!"
				# print self.totalf
			for d in self.de_words:
				d_prob = self.probs[d]
				# print "!!!!"
				# print d_prob
				# print e
				for e in d_prob:
					self.transmissions[d][e] = self.countef[d][e]/self.totalf[d]


def main():
	print "WELCOME!"
	args = sys.argv
	if len(args) < 3:
	 	print "--*INCORRECT FORMAT*--"
	 	print "python model1.py <foreign corpus> <english corpus> <testfile>"
	 	exit()

	
	model1 = Model1(args)
	model1.initTef()
	model1.iterateEM(10)
	model1._printInfo()

if __name__=="__main__":
  main()
