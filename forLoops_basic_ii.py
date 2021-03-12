#1 Biggie Size

def biggie_size(list_item):
    for x in range(len(list_item)):
        if list_item[x] > 0:
            list_item[x] = "big"
    return list_item

print(biggie_size([-1, 3, 5, -5]))

#2 Count Positives

def count_positives(list_item):
    newlist_item = []
    for x in range(len(list_item)):
        if list_item[x] > 0:
            newlist_item.append(list_item[x])
    list_item[len(list_item) - 1] = len(newlist_item)
    return list_item

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3 Sum Total

def sum_total(list_item):
    sum = 0
    for x in range(len(list_item)):
        sum += list_item[x]
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4 Average

def average(list_item):
    sum = 0
    for x in range(len(list_item)):
        sum += list_item[x]
    ave = sum / len(list_item)
    return ave

print(average([1,2,3,4]))

#5 Length

def length(list_item):
    return len(list_item)

print(length([37,2,1,-9]))
print(length([]))

#6 Minimum

def minimum(list_item):
    if len(list_item) == 0:
        return False
    else:
        min = list_item[0]
        for x in range(1, len(list_item)):
            if min > list_item[x]:
                min = list_item[x]
        return min

print(minimum([37,2,1,-9]))
print(minimum([]))

#7 Maximum

def maximum(list_item):
    if len(list_item) == 0:
        return False
    else:
        max = list_item[0]
        for x in range(1, len(list_item)):
            if max < list_item[x]:
                max = list_item[x]
        return max

print(maximum([37,2,1,-9]))
print(maximum([]))

#8 Ultimate Analysis

def ultimate_analysis(list_item):
    dict = {}
    
    sumTotal = 0
    min = list_item[0]
    max = list_item[0]

    for x in range(len(list_item)):
        sumTotal += list_item[x]
        average = sumTotal / len(list_item)

    for y in range(1, len(list_item)):
        if min > list_item[y]:
            min = list_item[y]
        if max < list_item[y]:
            max = list_item[y]
    
    dict.update({"sumTotal": sumTotal})
    dict.update({"average": average})
    dict.update({"minimum": min})
    dict.update({"maximum": max})
    dict.update({"length": len(list_item)})
    
    return dict

print(ultimate_analysis([37,2,1,-9]))

#9 Reverse list_item

def reverse_list_item(list_item):
    for x in range(int(len(list_item)/2)):
        temp = list_item[x]
        list_item[x] = list_item[len(list_item) - 1 - x]
        list_item[len(list_item) - 1 - x] = temp
    
    return list_item

print(reverse_list_item([37,2,1,-9]))