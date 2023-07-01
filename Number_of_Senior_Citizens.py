class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for i in details:
            age =int(i[11:13])
            if age>60:
                ans+=1
        return ans
            
