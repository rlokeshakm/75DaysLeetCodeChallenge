class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        #s=s.replace(",","").replace(":","").replace(" ","").replace(".","").lower().replace("/","").replace("@","").replace("#","").replace("_","").replace("")
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        sa=s[::-1]
        if s == sa:
            return True
        return False
        