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
    pass
    # create empty string
    # go through each character in shortest word -->  for loop
    # go through each word in list --> for loop
    # check if letter equals to the next
    # if not: return string (prefix)
    # if so: add to empty string

strings = ["hello", "help", "hell", "heeeee", "heel", "hi"]
print(strings[0][0]) # gets first letter of hello
print(strings[1][0])
print(strings[2][0])