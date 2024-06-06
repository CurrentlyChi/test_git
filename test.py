# number_list = []
# x = -121
# for digit in str(x):
#     number_list.append(digit)

# reversed_digit = number_list[::-1]

# def check(list_one, list_two):
#     for i in range (len(list_one)):
#         if number_list[i] != list_two[i]:
#             return False
#     return True

# a = check(number_list,reversed_digit)

# print(a)

# class Solution:
#     def isPalindrome(self, x:int):
#         list_one = []
#         for digit in str(x):
#             list_one.append(digit)
#         list_two = list_one[::-1]

#         for i in range(len(list_one)):
#             if list_one[i] != list_two[i]:
#                 return False
#         return True

# so = Solution()

# print(so.isPalindrome(-121))

#first
# class Solution:
#     def isPalidrome(self, x:int):
#         str_x = str(x)
        
#         return str_x == str_x[::-1]
    
# so = Solution()

# print(so.isPalidrome(-121))

# append to list one, is it smaller than the next value? then move to the left

class Solution:
    def mergeTwoLists(self, list1, list2):
        new_list = []
        i,j = 0,0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                new_list.append(list1[i])
                i += 1
            else:
                new_list.append(list2[j])
                j +=1
        
        while i < len(list1):
            new_list.append(list1[i])
            i += 1
        
        while j < len(list2):
            new_list.append(list2[j])
            j +=1

        return new_list
        
list1 = [1,2,4]
list2 = [1,3,4]

so = Solution()

for number in so.mergeTwoLists(list1,list2):
    print(number)


