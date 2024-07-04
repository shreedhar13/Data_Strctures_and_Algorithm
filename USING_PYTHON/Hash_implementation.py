#in array for accessing any element O(n) time complexity is there
#but python supports dictionary which internally implements Hash mapping,,,so accessing is fast O(1)
#but how hash map is implemented see

class hashtable:
    def  __init__(self):
        self.MAX=100  #assuming we have 100 data values
        self.arr=[None for i in range(self.MAX)]  #empty list,,with 100 cells ,,index(0,99)
    def get_hash_val(self,key):
        h=0
        for char in key:
            h+=ord(char)#ex->"march 6" is a key then ,for each element of key ASCII value is extracted and add all this value and store in h
        return h % self.MAX  #and we have 100 cells in array and index is given to  each value w.r.t its key ,and index is b/n 0 to 99
        #bcz modulus with 100 gives 100-1 ie;99 from 0 to 99 remainder is produced.and this is used as index
    def add(self,key,value):
        index=self.get_hash_val(key)
        self.arr[index]=value
    def get(self,key):
        index=self.get_hash_val(key)
        return self.arr[index]
temp=hashtable()
temp.add('march 6',310)
temp.add('march 7',430)
print(temp.arr)
print(temp.get('march 7'))
sum=0
for i in 'march 6':
    sum+=ord(i)
    if ord(i) == 32:
        print('space',ord(i))
    else :
        print(i,ord(i))
print('sum is=',sum)
print('index/hash value is generated is =',sum % 100)#thus u see 310 value is stored at index 9 of arr

#note->2 keys can have same ascii sum of characters then COLLISION occurs,,so use COLIISION RESOLUTION TECH ie;mainly linear probing is used

    

