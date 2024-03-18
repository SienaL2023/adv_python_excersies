# exercise # 1
# build a function that takes two parameters
# parameters: list(int), num(int)
# from the list of ints, find the two numbers
# that adds up to the num
# if an answer exist: return True
# if no possible answer: return False

def twoSum(num_list, sum):
    # for x in range(len(num_list)):
    #     for y in range(x+1, len(list)):
    #         answer = y + num_list[x]
    #         if answer == sum:
    #             return True
    # return False
    # num_list.sort()
    # left = 0
    # right = len(num_list) - 1
    # while left < right:
    #     answer = num_list[left] + num_list[right]
    #     if(answer==sum):
    #         return True
    #     elif(answer > sum):
    #         right -= 1
    #     else:
    #         left += 1
    # return False

    # to put every number into dictionary (key = index, number = value)
    num_dict = {}
    for x in range(len(num_list)):
        num_dict[num_list[x]] = x # adds list stuff to dictionary number NOT key
    for x in range(len(num_list)):
        dif = sum - num_list[x] # subtracts num from sum, the finds dif in the dictionary and makes sure it not itself
        if dif in num_dict and x != num_dict[dif]:
            return True
    return False # if all fails :)

# print(twoSum(list, num))
#
# twoSum(list,num)

# nested for loop
# for each element in list:
#   for each element in list:
#       current element +

result = twoSum([1,2,5], 3)
assert result == True

result1 = twoSum([2,6,8], 27)
assert result1 == False

result2 = twoSum([4,2,67], 71)
assert result2 == True


# exercise #2
# given list of strings: ["hello", "help", "hell"]
# find the longest common prefix string amongst the list of strings

def longestCommonPrefix(strings): # return the longest prefix string
    # shortest = 9999
    # for x in strings:
    #     if len(x)< shortest:
    #         shortest = len(x)
    # # by here shortest word length is found
    # prefix = ""
    # for y in range(shortest):
    #     letter_y = strings[1][y]
    #
    #     for x in range(len(strings)):
    #         # print(strings[x][y])
    #         temp = strings[x][y]
    #         if temp != letter_y:
    #             return prefix
    #     prefix += letter_y

    strings.sort() # nlogn # sort alphabetically
    prefix = "" # creates blank string to put letter of prefixes in
    for x in range(len(strings[0])): # o(n) # for x in range of the len of the first letter
        temp = strings[len(strings) - 1][x] # temp = the x letter in the last word of list
        if temp != strings[0][x]: # compare temp and x letter of first word
            return prefix # return gets u out of the function
        prefix += temp # add letter

    # create empty string
    # go through each character in shortest word -->  for loop
    # go through each word in list --> for loop
    # check if letter equals to the next
    # if not: return string (prefix)
    # if so: add to empty string

    # more optimal solution
    # 1. sort the list of strings alphabetically list.sort()
    # 2. check first and last word fro longest common prefix
    # 3. return longest

# strings = ["hello", "help", "hell", "heeeee", "heel", "hi"]
# print(strings[0][0]) # gets first letter of hello
# print(strings[1][0])
# print(strings[2][0])

solution = longestCommonPrefix(["hello", "help", "hell", "heeeee", "heel", "hi"])
assert solution == "h"

solution = longestCommonPrefix(["nemo", "neighbor", "nick"])
assert solution == "n"

# exercise # 3
# best time to buy/sell stock
# input: list of integers --> price of that stock per day
# output: find maximum profit where you will buy from the cheapest and sell at a later time

def maxProfit(prices):
    # profit = 0
    # for each number in prices:
    #   temp = number
    #   for every number after temp:
    #       get diff between number and temp
    #       update profit variable
    # return profit
    # 0(n*m)
    # profit = 0
    # for x in range(len(prices)): #0(n)
    #     temp = prices[x]
    #
    #     for y in range(x+1, len(prices)): # 0(m)
    #         diff = prices[y] - temp
    #         if diff > profit:
    #             profit = diff
    # return profit

    # Goal: 0(n)
    # loop through each number in list,
    # at each iteration, update maximum profit and find out minimum price
    # maximum profit = max(profit, number-minimum)
    profit = 0
    minimum = 10000000000000 # very big so no number can beat it
    for x in range(len(prices)): # 0(n)
        if prices[x] < minimum: # if ur current min is bigger then this price, change
            minimum = prices[x]
        profit = max(profit, prices[x] - minimum) # max(profit, current number - min), sets new profit incase this new number is better
    return profit
# print(min(5,7))
# print(max(5,7))
profit = maxProfit([3,4,1,8,5,3])
assert profit == 7

profit = maxProfit([7,6,4,3,1])
assert profit == 0

# exercise #4
# merge and sort two lists
# given two lists, merge them into one list and sort it


def bubbleSort(final_list):# O(n^2)
    for x in range(len(final_list)):  # going through every list
        for y in range(len(final_list) - x - 1):  # minus 1 bc u dont wanna be out of bounds in the list and minus x bc it may be next iteration
            if final_list[y] > final_list[y + 1]:  # if #y is greater then nxt num
                # temp = final_list[y+1] # put number in extra hand
                # final_list[y+1] = final_list[y] # overwrite that number bc it is already stored in extra hand
                # final_list[y] = temp # stuff in extra hand goes to empty hand
                final_list[y], final_list[y + 1] = final_list[y + 1], final_list[y]
    return final_list

def selectionSort(list): # O(n^2)
    # repeatedly selects the smallest element from list and swaps it with first element (or index)
    # loop through input list
    for x in range(len(list)):
        smallest = x # set smallest as the index num , so basically x
        # find smallest element to swap
        for y in range(x+1, len(list)): # range(next one, end of list)
            if(list[smallest] > list[y]): # compare the current num to the list[y]
                smallest = y # update variable
        list[x], list[smallest] = list[smallest], list[x] # a,b = b,a
    return list

def insertionSort(list): # o(n^2)
    for x in range(1, len(list)):
        key = list[x] # stays constant in the while loop
        index = x-1 # will change in while loop
        while key < list[index]:
            # loop to move element to proper place
            list[index+1] = list[index] # the bigger and smaller num
            index -= 1 # moves to the next num to the left
        list[index+1] = key # puts the key wherever it got stuck
    return list
# index = 2
# key =5
# 5 < list[2] --> yes
# list[3] = 13
# index -= 1 --> index =1
# 5 <list[index] --> yes
# list[2] = 12
# index -= 1 --> index = 0

# [11,12,13,5,6]

def mergeSort(list):
    if len(list) > 1: # if the list is already at one u cant keep dividing
        mid = len(list)//2 # finds midpoint to spilt list
        left = list[0:mid] # creates left side of list
        right = list[mid:] # creates right side of list
        mergeSort(left) # makes that part of the list go back into the function to split again
        mergeSort(right) # makes part of list go back and split
        # split until its one, then go onto next part!
        #### algorithm of mergesort
        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] <= right[y]: # if x is less then y, x would be first on the list
                list[z] = left[x] # adds to final list
                x += 1 # now out of while loop
            else:
                list[z] = right[y] # same but for y or right side
                y += 1
            z += 1
        while x < len(left): # same but for left if it didnt qualify last time
            list[z] = left[x]
            x += 1
            z += 1
        while y < len(right): # same but right if u didnt qualify last time
            list[z] = right[y]
            y += 1
            z += 1
    return list


def mergeSortList(list1, list2):
    final_list = list1 + list2 #merge two lists
    return mergeSort(final_list)



# mergeSortList([1,3,5,7], [2,4,6,8])
answer = mergeSortList([1,3,5,7], [2,4,6,8])
assert answer == [1,2,3,4,5,6,7,8]

def sort(list):
    for x in range(len(list)):
        for y in range(len(list) - x -1):
            if list[y] > list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
    return list
