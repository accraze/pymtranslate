import sys
#import string

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
