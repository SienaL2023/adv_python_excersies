# exercise # 1
# build a function that takes two parameters
# parameters: list(int), num(int)
# from the list of ints, find the two numbers
# that adds up to the num
# if an answer exist: return True
# if no possible answer: return False

list = [1, 2, 3, 4, 5]
num = 6
def twoSum(num_list, sum):
    # for x in range(len(num_list)):
    #     for y in range(x+1, len(list)):
    #         answer = y + num_list[x]
    #         if answer == sum:
    #             return True
    # return False
    num_list.sort()
    left = 0
    right = len(num_list) - 1
    while left < right:
        answer = num_list[left] + num_list[right]
        if(answer==sum):
            return True
        elif(answer > sum):
            right -= 1
        else:
            left+= 1
    return False

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


