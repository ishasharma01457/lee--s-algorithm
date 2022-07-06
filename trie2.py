class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
	
		return TrieNode()

	def _charToIndex(self,ch):
		
		return ord(ch)-ord('a')


	def insert(self,key):
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])

			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]
		pCrawl.isEndOfWord = True

	def search(self, key):
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]

		return pCrawl.isEndOfWord

def main():

	keys = ["the","a","there","why","any",
			"by","their"]
	output = [" present ",
			"Present "]

	
	t = Trie()

	
	for key in keys:
		t.insert(key)

	
	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("yes",output[t.search("yes")]))
	print("{} ---- {}".format("there",output[t.search("there")]))

if __name__ == '__main__':
	main()