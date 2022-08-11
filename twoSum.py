def twoSum(nums: list[int], target: int) -> list[int]:
    comp = {}
    for i in range(len(nums)):
        val_list = list(comp.values())
        if (nums[i]) in val_list:
            # return [val_list.index(nums[i] - target), i]
            print([val_list.index(nums[i]), i])
        else:
            comp.update({i: (target - nums[i])})

ex1 = [2,7,11,15]
t1 = 9
ex2 = [3,2,4]
t2 = 6

twoSum(ex1,t1)
twoSum(ex2,t2)