class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = HashTable(len(s))
        th = HashTable(len(t))
        
        for i in s:
            sh.set_val(i,1)
        for i in t:
            th.set_val(i,1)

        if sh.get_freq() == th.get_freq():
            return True
        else:
            return False
        

class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, record_val) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, record_val+1)
                return
        bucket.append((key,val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return True
        return False

    def get_freq(self):
        output=set()
        for bucket in self.hash_table:
            for key,val in bucket:
                output.add((key,val))
        return output
