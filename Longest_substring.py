class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        empty_str =""
        if len(strs)==0: #length of the string
            return empty_str
    
        for i in range(len(min(strs))): #length of the shortest string in strs
            c=strs[0][i] #iterate through shortest string characters
            if all(a[i]==c for a in strs): 
                empty_str+=c
            else:
                break
        return empty_str
