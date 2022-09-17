class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word_idx = -1
        self.palindrome_word_idx = []

    @staticmethod
    def is_palinderome(word):
        return word == word[::-1]

    def insert(self, word, index):
        node = self
        # make trie with reversed words
        for idx, char in enumerate(reversed(word)):
            # check if rest of word is a palindrome
            if self.is_palinderome(word[: len(word) - idx]):
                node.palindrome_word_idx.append(index)
            node = node.children[char]
        # mark index when traverse ends
        node.word_idx = index

    def search(self, word, index):
        res = []
        node = self
        while word:
            # Case 1. Check rest of the word is a palindrome
            if node.word_idx >= 0:
                if self.is_palinderome(word):
                    res.append(node.word_idx)
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]
        # Case 2. palindrome_word_idx already contains
        # every palindrome's indices.
        if node.word_idx >= 0:
            res.append(node.word_idx)
        res.extend(node.palindrome_word_idx)

        return res
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        node = Trie()
        for i, word in enumerate(words):
            node.insert(word, i)
        res = []
        for i, word in enumerate(words):
            res.extend([[i, cand] for cand in node.search(word, i) if i != cand])
        return res
        