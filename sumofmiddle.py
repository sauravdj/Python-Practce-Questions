def sumMiddle(list):
    lengthOfList = len(list)
    sliceToSum = list[1:lengthOfList-1]
    middleSum = sum(sliceToSum)
    list[1:lengthOfList-1] = [middleSum]
    return list

dataList = [2,4,6,8,10]
sl = sumMiddle(dataList)
print(sl)


