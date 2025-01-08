class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root 
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root 
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False 
            current = current.children[index]
        return current.isLeaf and current
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root 
        for letter in prefix:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return True
class Solution:
    def recursion(self, s, wordDict, max_len, flag):
        if s == "":
            flag[0] = True
            return True
        if flag[0] == True:
            return True
        tmp = ""
        idx = min(max_len-1, len(s)-1)
        tmp_result = False
        while(idx >= 0):
            tmp = s[0:idx+1]
            if tmp in wordDict:
                tmp_result = self.recursion(s[idx+1:], wordDict, max_len, flag)
                if tmp_result == True:
                    return True
            idx -= 1
        #return tmp_result
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie_dict = Trie()
        max_len = 0
        flag = [False]
        for word in wordDict:
            if len(word) > max_len:
                max_len = len(word)
            trie_dict.insert(word)
        visited_set = set()
        
        queue = []
        for i in range(max_len):
            if s[:i+1] in wordDict:
                if i+1 == len(s):
                    return True
                queue.append(i)
        while (len(queue)>0):
            idx = queue.pop()
            if idx in visited_set:
                continue
            visited_set.add(idx)
            idx += 1
            for i in range(max_len):
                if s[idx:idx+i+1] in wordDict:
                    if idx+i+1 == len(s):
                        return True
                    queue.append(idx+i)
        return False
        #x = self.recursion(s, wordDict, max_len, flag)
        #if x == True:
        #    return x
        #return False
    
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s = "a"
wordDict = ["a"]
sol = Solution()
print(sol.wordBreak(s, wordDict))