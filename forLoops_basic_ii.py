#1 Biggie Size

def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list

print(biggie_size([-1, 3, 5, -5]))

#2 Count Positives

def count_positives(list):
    newList = []
    for x in range(len(list)):
        if list[x] > 0:
            newList.append(list[x])
    list[len(list) - 1] = len(newList)
    return list

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3 Sum Total

def sum_total(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4 Average

def average(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    ave = sum / len(list)
    return ave

print(average([1,2,3,4]))

#5 Length

def length(list):
    return len(list)

print(length([37,2,1,-9]))
print(length([]))

#6 Minimum

def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for x in range(1, len(list)):
            if min > list[x]:
                min = list[x]
        return min

print(minimum([37,2,1,-9]))
print(minimum([]))

#7 Maximum

def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for x in range(1, len(list)):
            if max < list[x]:
                max = list[x]
        return max

print(maximum([37,2,1,-9]))
print(maximum([]))

#8 Ultimate Analysis

def ultimate_analysis(list):
    dict = {}
    
    sumTotal = 0
    min = list[0]
    max = list[0]

    for x in range(len(list)):
        sumTotal += list[x]
        average = sumTotal / len(list)

    for y in range(1, len(list)):
        if min > list[y]:
            min = list[y]
        if max < list[y]:
            max = list[y]
    
    dict.update({"sumTotal": sumTotal})
    dict.update({"average": average})
    dict.update({"minimum": min})
    dict.update({"maximum": max})
    dict.update({"length": len(list)})
    
    return dict

print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List

def reverse_list(list):
    for x in range(int(len(list)/2)):
        temp = list[x]
        list[x] = list[len(list) - 1 - x]
        list[len(list) - 1 - x] = temp
    
    return list

print(reverse_list([37,2,1,-9]))