class Solution:
    

    def insertion_sort(self, bucket):
        for i in range(1,len(bucket)):
            key = bucket[i]
            j=i-1
            while j >= 0 and bucket[j] > key:
                bucket[j+1] = bucket[j]
                j -= 1
            bucket[j+1] = key
            
    def bucketsort(self, arr, freqs):
        n = len(arr)+1
        buckets = [[] for _ in range(n)]
        print(buckets)

        for num in freqs:
            bucket_index = freqs[num] - 1
            print(num, bucket_index)
            buckets[bucket_index].append(num)
        
        print(buckets)

        for bucket in buckets:
            self.insertion_sort(bucket)

        print(buckets)

        index = 0
        for bucket in buckets:
            for num in bucket:
                arr[index] = num
                index += 1
        print('arr is', arr)
        output = [i for j in buckets for i in j]
        print('output', output)
        return [i for j in buckets for i in j]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in freqs :
                freqs[key] += 1
            else:
                freqs[key] = 1
        print('frequencies', freqs.items())
        return self.bucketsort(nums,freqs)[-k:]