class Solution:
    def intToRoman(self, num: int) -> str:
        output=""
        req_keys=dict()
        req_keys[1]    = "I"
        req_keys[4]    = "IV"
        req_keys[5]    = "V"
        req_keys[9]    = "IX"
        req_keys[10]   = "X"
        req_keys[40]   = "XL"
        req_keys[50]   = "L"
        req_keys[90]   = "XC"
        req_keys[100]  = "C"
        req_keys[400]  = "CD"
        req_keys[500]  = "D"
        req_keys[900]  = "CM"
        req_keys[1000] = "M"
        for key,value in reversed(req_keys.items()):
            quotient,num = divmod(num,key)
            if(quotient>0):
                output+=req_keys[key]*quotient
                print(output)      
        return output
