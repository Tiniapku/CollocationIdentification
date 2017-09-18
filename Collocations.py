#Tianyi Liu | tianyil | 16069542
from collections import defaultdict


class collocation(object):
	def __init__(self):
		self.unigram = defaultdict(int)
		self.bigram = defaultdict(int)
	def readData(self, data):
		for s in data.readlines():
			s = s.lower()
			s = s.strip()
			words = s.split(" ")
			lastword = ""
			for w in words:
				if len(w) == 1 and (ord(w) < 97 or ord(w) > 112):
					# get rid of punctuations
					continue

				# add to unigram
				self.unigram[w] += 1
				if lastword:
					bigram = (lastword, w)
					self.bigram[bigram] += 1
				lastword = w

	def ignoreLessThan5(self):
		for word1, word2, count in self.bigram.values():
			if count < 5:
				del self.bigram[(word1, word2)]

	def chiSquare(self):
		pass

	def PMI(self):
		pass

if __name__ == '__main__':
	obj = collocation()
	method = sys.argv[1]
	if method == "chi-square":
		print obj.chiSquare()
	elif method == "PMI":
		print obj.PMI()
	else:
		print "Wrong method!!"
