import random

class MarkovChain:
	def __init__(self, corpus):
		self.corpus = corpus
		self.vocablo = []
		self.ret = ""
		self.count = 0
	def train(self, h):
		if h:
			self.vocablo = []
		esekas = []
		for sentence in self.corpus:
			keys = []
			sp = sentence.split(" ")
			sk = []
			for k in sp:
				if k in sk:
					pass
				else:
					sk.append(k)
			for i in sk:
				key = []
				for x in sp:
					if (i + " " + x) in sentence:
						key.append(x)
				keys.append((i, key)) #estructura datos : ("palabra", ["siguiente 1".....])
			esekas.append(keys)
		claves = []
		for x in esekas:
			for y in x:
				clave = y[0]
				valor = y[1]
				if clave in claves:
					for z in self.vocablo:
						if clave == z[0]:
							z[1].extend(valor)
				else:
					claves.append(clave)
					self.vocablo.append((clave, valor))
		print(str(self.vocablo))
	def gen(self, seed):
		self.counted -= 1
		for i in self.vocablo:
			if i[0] == seed:
				self.ret += " " + seed
				if self.counted == 0:
					return seed
				try:
					current = self.gen(random.choice(i[1]))
				except Exception:
					current = seed
				return current
	def ultigen(self, seed, counted):
		self.counted = counted
		self.ret = ""
		self.gen(seed)
		return self.ret
