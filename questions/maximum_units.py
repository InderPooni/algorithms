def maximum_units(boxTypes, truckSize):
    s = sorted(boxTypes, key=lambda x: x[1], reverse=True)

    res = 0

    for numBoxes, unitPerBox in s:
        if truckSize <= 0:
            return res
        
        elif truckSize < numBoxes:
            res += (truckSize * unitPerBox)
            truckSize = 0
        
        else:
            res += (numBoxes * unitPerBox)
            truckSize -= numBoxes
    
    return res

print(maximum_units([[1,3],[2,2],[3,1]], 4))