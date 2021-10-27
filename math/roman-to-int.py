'''
Self explanatory, transform a roman number to int
'''


class Solution:
    def romanToInt(s):
        s = list(s)
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s = [dict[i] for i in s]

        result = 0
        i = 0
        leng = len(s)
        while (i < leng):
            if (i+1) < leng and s[i] < s[i+1]:
                result += s[i+1]-s[i]
                i += 2
            else:
                result += s[i]
                i += 1
        return result
