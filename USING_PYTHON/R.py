lookup={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
class process:
    
    def R_TO_I(self,s):
       
        N=len(s)
        i=N-1
        integer=0
        while i>=0:
            if i < N-1 and lookup[s[i]] < lookup[s[i+1]]:
                integer-=lookup[s[i]]
            else:
                integer+=lookup[s[i]]
                i-=1
        return integer
    def get_key(self,val):
        for key, value in lookup.items():
            if val == value:
                return key
       
if __name__ == '__main__':
    p=process()
    val=p.R_TO_I('XXXVVIIIIIIIIII')
    
    print(p.get_key(val))

