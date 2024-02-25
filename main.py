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
    profit = 0
    for x in range(len(prices)):
        temp = prices[x]

        for y in range(x+1, len(prices)):
            diff = prices[y] - temp
            if diff > profit:
                profit = diff
    return profit

print(min(5,7))
print(max(5,7))
profit = maxProfit([7,1,5,3,6,4])
assert profit == 5

profit = maxProfit([7,6,4,3,1])
assert profit == 0