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
	    self.transmissions = {} # this is t(e|f)
	    self.countef = {}
	    self.totalf = {}
	    self.totals = {}
	    self.data = data

	    
	    self.en_dict, self.en_words = self.convertArgsToTokens( self.data[1] )
	    self.de_dict, self.de_words = self.convertArgsToTokens( self.data[2] )
	    

	    self.dev_in = open(self.data[3], 'r')
	    self.dev_lines = self.dev_in.readlines()
	    self.dev_in.close()

	    for index in range(len(self.en_dict)):
	    	pair = (self.en_dict[index], self.de_dict[index])
	    	self.sent_pairs.append(pair)
	    # print "PAIRS:"
	    # print self.sent_pairs

	def printInfo(self):
		for line in self.dev_lines:
			self.dev_words += line.split()
		#print self.dev_words
		
		#print self.transmissions
		for word in self.dev_words:
			print "English Word:" + word
			print "German Words & Probabilities:"
			print self.transmissions[word]


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
		for word in self.en_words:
			word_poss = []
			# if word in sentence.. then 
			for sent in self.en_dict:
				if word in sent:
					matching = self.de_dict[ self.en_dict.index(sent)]
					word_poss = word_poss + matching.split()

			#remove the duplicates 
			word_poss = list( set(word_poss))
			#add the probable matches 
			probs[word] = word_poss

		self.probs = probs
			
		for word in self.en_words:
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
		# print self.transmission['sitzung']
			

	def iterateEM(self, count):
		

		for iter in range(count):
			print "ITERATION #("+str(iter + 1)+")\n"

			countef = {}
			totalf  = {}
			# set the count of the words to zero
			for word in self.en_words:
				
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

				for d in ds_split:
					self.totals[d] = 0
					for e in es_split:
						
						# print "E"
						# print e
						# print "D"
						# print d
						# print self.transmissions[e]
						
						e_trans = self.transmissions[e]
						

						if (d not in e_trans):
							continue

						# print "!!!"
						# print e_trans[d]
						# print "!!!"
						# print e_trans["sitzung"]
						self.totals[d] += e_trans[d]
						
					# print "!!!"
					# print self.totals
					for e in es_split:
						if (d not in self.transmissions[e]):
							continue
						self.countef[e][d] += self.transmissions[e][d] / self.totals[d]
						self.totalf[e] += self.transmissions[e][d] / self.totals[d]
						
						# print "!!!"
						# print self.countef
				# print "!!!"
				# print self.totalf
			for e in self.en_words:
				e_prob = self.probs[e]
				# print "!!!!"
				# print d_prob
				# print e
				for d in e_prob:
					self.transmissions[e][d] = self.countef[e][d]/self.totalf[e]


def main():
	print "WELCOME!"
	args = sys.argv
	if len(args) < 3:
	 	print "--*INCORRECT FORMAT*--"
	 	print "python model1.py <english corpus> <german corpus> <testfile>"
	 	exit()

	
	model1 = Model1(args)
	model1.initTef()
	model1.iterateEM(10)
	model1.printInfo()

if __name__=="__main__":
  main()
