import time

def twoSum(nums,target):
    start = time.perf_counter()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                stop = time.perf_counter()
                times = str(stop - start)
                print(times)
                return [i,j]


def twoSum_hashmap(nums,target):
    start = time.perf_counter()

    hashmap = {}
    for i,num in enumerate(nums):
        hashmap[num] = i
    for i,num in enumerate(nums):
        j = hashmap[target - num]
        if j != None and j != i :
            stop = time.perf_counter()
            print(stop - start)
            return[i,j]



if __name__ == '__main__':
    nums = [1,5,3,7,8]
    print(twoSum(nums,8))
    print(twoSum_hashmap(nums,8))