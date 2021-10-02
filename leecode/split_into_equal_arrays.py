class Solution:
    def __init__(self):
        self.res = []
        pass
    def getPart(self, nums):
        result = []
        sumValue = sum(nums)
        print(f'sum = {sumValue}')
        if ( sumValue % 2 == 1):
            return result
        currentList = []
        toBeProcessList = []
        toBeProcessList.extend(nums)
        self.getPartWrapper(toBeProcessList, currentList, 0, int(sumValue/2))
        return self.res
    def cloneNextProcessed(self, toBeProcessList, value):
        newList = []
        newList.extend(toBeProcessList)
        for i in newList[::-1]:
            if (i == value):
                newList.remove(value)
        return newList
    def cloneCurrentList(self, currentList,  value):
        newList = []
        newList.extend(currentList)
        newList.append(value)
        return newList

    def getPartWrapper(self, toBeProcessList, currentList, currentSum, target):
        print("########################")
        print(f'toBeProcessList: {toBeProcessList}')
        print(f'currentList: {currentList}')
        if (len(self.res) > 0):
            return
        if (currentSum == target):
            print(f">>>>>>>>>>>>>>>>>>>>>> find result: {currentList}")
            self.res = currentList
            return
        for item in toBeProcessList:
            self.getPartWrapper(self.cloneNextProcessed(toBeProcessList, item),
                           self.cloneCurrentList(currentList, item),
                           currentSum + item,
                           target)
        return

sol = Solution()
#Array[] = {0,1,7,4,6,3,9,2};
input = [0, 1, 2, 3,  4, 6, 7, 9]
res = sol.getPart(input)
if (len(res) > 0):
    print(f'The answer is : {res}')
else:
    print(f"the original array can't be split")