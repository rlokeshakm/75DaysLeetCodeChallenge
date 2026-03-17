class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
    
        for i in nums:
            d[i]=d.get(i,0)+1
        
        p = [(freq, i) for i, freq in d.items()]
        p.sort(reverse=True)

        res=[]
        for i in range(k):
            res.append(p[i][1])
        return res
        