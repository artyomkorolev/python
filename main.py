firstList = [2, 8,   3,  6, 7,  3, 5, 10,2]
fIndexMax = firstList.index(max(firstList))


def lastMin(list):
    minlist = []
    for i in range(0, len(list)):
        if list[i] == min(list):
            minlist.append(i)
    fIndexmin = minlist[len(minlist) - 1]
    return fIndexmin


def task(list, firstmax, lastminimum):
    finishlist = []
    if lastminimum<firstmax:
        return 0;
    for i in range(0, firstmax+1):
        finishlist.append(list[i])
    list1=list[firstmax+1:lastminimum]
    for i in range(0,len(list1)):
        finishlist.append(list1[len(list1)-i-1])
    for i in range(lastMin(list),len(list)):
        finishlist.append(list[i])
    return finishlist





finishList = task(firstList, fIndexMax, lastMin(firstList))
print(finishList)
