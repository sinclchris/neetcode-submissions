class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = HashTable(len(nums))

        for i in nums:
            if ht.get_val(i) == True:
                return True
            else:
                ht.set_val(i,i)
        return False

class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return
        bucket.append((key,val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return True
        return False
