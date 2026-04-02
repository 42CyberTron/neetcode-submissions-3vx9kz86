class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hashtable = defaultdict(list)
            for str in strs:
                freq = [0]*26
                for c in str:
                    freq[ord(c) - ord('a')] += 1
                freq = tuple(freq)
                hashtable[freq].append(str) 
            return list(hashtable.values())   