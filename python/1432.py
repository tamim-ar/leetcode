class Solution:
    def maxDiff(self, num):
        s = str(num)
        
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break
        else:
            max_s = s
        
        if s[0] != '1':
            min_s = s.replace(s[0], '1')
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_s = s.replace(ch, '0')
                    break
            else:
                min_s = s

        return int(max_s) - int(min_s)
