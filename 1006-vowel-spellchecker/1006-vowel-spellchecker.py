class Solution:
    def replace(self, word):
        result = []
        for ch in word:
            if ch in 'aeiou':
                result.append('*')
            else:
                result.append(ch)
        return ''.join(result)
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        set_words = set(wordlist)
        cap = {}
        vowel = {}
        
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in cap:
                cap[lower_word] = word
            replaced_word = self.replace(lower_word)
            if replaced_word not in vowel:
                vowel[replaced_word] = word
                
        ans = []
        for query in queries:
            if query in set_words:
                ans.append(query)
                continue
            lower_query = query.lower()
            if lower_query in cap:
                ans.append(cap[lower_query])
                continue
            replaced_query = self.replace(lower_query)
            if replaced_query in vowel:
                ans.append(vowel[replaced_query])
                continue
            ans.append("")
            
        return ans