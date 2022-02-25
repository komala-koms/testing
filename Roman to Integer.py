class Solution:
    def romanToInt(self, s: str) -> int:
        output=0
        req_keys=dict()
        req_keys["I"]  = 1
        req_keys["IV"] = 4 
        req_keys["V"]  = 5 
        req_keys["IX"] = 9 
        req_keys["X"]  = 10
        req_keys["XL"] = 40
        req_keys["L"]  = 50 
        req_keys["XC"] = 90
        req_keys["C"]  = 100
        req_keys["CD"] = 400 
        req_keys["D"]  = 500
        req_keys["CM"] = 900
        req_keys["M"]  = 1000
        n= len(s)
        i=0
        while(i<n):
            if((i+1<n) and  req_keys[s[i]] < req_keys[s[i+1]]):
                output+= req_keys[s[i+1]]-req_keys[s[i]]
                i+=2
                
            else:
                output+=req_keys[s[i]]
                i+=1
            print("i", i)    
            print(output)
        return output
            
