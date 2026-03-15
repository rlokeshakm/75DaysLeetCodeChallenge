class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num =set(nums)
        ran=len(nums)

        an=[]
        for i in range(1,ran+1):
            if i not in num:
                an.append(i)
            
        return an
        

      
        

        