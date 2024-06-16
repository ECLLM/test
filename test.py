# digits=[1,2,4]
# num=0
# for i in range(len(digits)):
#     print(digits[i])
#     print(len(digits)-1-i)
#     print(10^(len(digits)-1-i))
#     input()
#     num = num + digits[i]*(10^(len(digits)-1-i))
# #     print(num)
# # print(num)

# nums1=[4,5,6,0,0,0]
# nums2=[1,2,3]
# m = 3
# n = 3
# # nums1 = nums1[:m] + nums2
# # print(nums1)
# for i in range(m,m+n):
#     nums1[i]=nums2[i-m]
#     mid = nums1[i]
#     for j in range(m-1,-1,-1):
#         if mid<nums1[j]:
#             nums1[j+1]=nums1[j]
#             nums1[j]=mid
#         else:
#             break
#     print(nums1)
# print(nums1)

# nums=[1,3]
# left=0
# right=0

# sum=[]
# if len(nums) == 1:
#     sum.append(str(nums[0]))
# for i in range(len(nums)-1):
#     if nums[i]+1 == nums[i+1]:
#         right +=1
#         if right == len(nums)-1:
#             sum.append(str(nums[left]) + "->" + str(nums[right]))
#     elif nums[i]+1 != nums[i+1] and left==right:
#         sum.append(str(nums[left]))
#         left = i+1
#         right = i+1
        
#     elif nums[i]+1 != nums[i+1]:
#         sum.append(str(nums[left]) + "->" + str(nums[right]))
#         left = i+1
#         right = i+1
#         print(right)
#         print(len(nums)-1)
#         if right == len(nums)-1:
#             sum.append(str(nums[right]))
# print(sum)

# strs = ["flowers","flow"]
# strs.sort()
# for i in range(min(len(strs[0]),len(strs[-1]))):
#     print(str(strs[0])[0])
#     if strs[0][i] != str[-1][i]:
#         print(strs[0][:i])

    # def calPoints(self, operations: List[str]) -> int:
# operations = ["5","-2","4","C","D","9","+","+"]
# num = []
# for i in range(len(operations)):
#     if operations[i]=="C":
#         num.pop()
#         print(num)
#         input()
#     elif operations[i]=="D":
#         num.append(num[-1]*2)
#         print(num)
#         input()
#     elif operations[i]=="+":
#         num.append(sum(num))
#         print(num)
#         input()
#     else:
#         num.append(int(operations[i]))
#         print(num)
#         input()
# print(sum(num))

# import numpy as np
# mat=[[1,2],[3,4]]
# a = np.array(mat)
# b = a.reshape((1,4))
# print(b)
# c = a.reshape((4,1))
# print(c)
# print(list(c))


# from functools import reduce
# boxes= "110"
# index = []
# ans = []
# for i in range(len(boxes)):
#     # print(boxes[i])
#     if int(boxes[i])==1:
#         index.append(i)
# # print(index)
# for i in range(len(boxes)):
#     a = list(map(lambda x: abs(i-x),index))
#     print(a)
#     b = reduce(lambda x,y: x+y ,a)
#     print(b)
#     ans.append(b)
# print(ans)

# words = ["gin", "zen", "gig", "msg"]
# mo = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# print(len(mo))
# ans=[]
# for i in range(len(words)):
#     string=""
#     for j in range(len(words[i])):
#         print(ord(words[i][j])-92)
#         string += mo[ord(words[i][j])-92]
#     ans.append(string)
# print(len(set(ans)))

# expected =[]
# heights = [1,1,4,2,1,3]
# expected 
# num=0
# for i in range(len(heights)):
#     if heights[i]!=expected[i]:
#         num+=1
# print(num)

# height=[2,3,4,5,18,17,6]
# left = 0
# right = len(height)-1
# volumn = 0
# while left<right:
#     volumn = max(volumn,min(height[left],height[right])*(right-left))
#     if left<right:
#         print(left)
#         left +=1
#     else:
#         right-=1
# print(left)
# print(right)
# print(volumn)

# nums=[0,1,2]
# target = 0
# nums.sort()
# print("nums:",nums)
# ans = float("inf")
# for i in range(len(nums)-2):
#     L = i+1
#     R = len(nums)-1
#     while L<R:
#         print("L",L)
#         print("R",R)
#         if abs(nums[i]+nums[L]+nums[R]-target)<abs(ans-target):
#             ans = nums[i]+nums[L]+nums[R]
#             print()
#         if nums[i]+nums[L]+nums[R]>target:
#             R-=1
#         elif nums[i]+nums[L]+nums[R]<target:
#             L+=1
#         else:
#             print("target",target)

#         # if nums[i]>=target:
#         #     print("break")
#         #     break
# print("ans:",ans)


# 

# k =4

# import collections
# jewels = "aAA"
# stones = "abbA"
# x = collections.Counter(jewels)
# y = collections.Counter(stones)
# print(len(x&y)
# )

# nums=[5,4,-1,7,8]
# if len(nums) == 1:
#     print(nums[0])
# sum = 0
# max = float("-inf")
# for i in range(len(nums)):
#     sum = sum + nums[i]
#     # print(sum)
#     if sum > max:
#         max = sum
#     if sum < 0:
#         sum = 0
# print(max)

# import collections
# nums=[1,2,3,1]
# a = collections.Counter(nums)
# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())
# if max(a.values())>1:
#     print(True)
# else:
#     print(False) 

# nums = [2,6,2,5,4,15,1]
# nums.sort(reverse = True)
# print(nums)
# for i in range(len(nums)-2):
#     if nums[i] - nums[i+1] < nums[-1]:
#         j = i + 2
#         while nums[i] - nums[i+1] > nums[j]:
#             j += 1
#         print(nums[i] + nums[i+1] + nums[j]) 
# print(0)

# nums=[1,2,3,4,5,6,7]
# print(nums[0:1])
# k=3
# n = len(nums)-1
# k = k % len(nums)
# print(n)
# print(nums[n-k+1:n])
# print(nums[0:n-k])
# nums[0:k-1],nums[k:n] = nums[n-k+1:n],nums[0:n-k]

# import collections
# a = [2,3,4,5,5]
# print(set(a))
# print(collections.Counter(a))
# for k,v in collections.Counter(a):
#     print(k)

# a = [1,2,3]
# b=[3,5]
# c= zip(a,b)
# print(list(c))

# input = -123

# if input >= 0:
#   ans = int(str(input)[::-1])
# else :
#   ans = -int(str(input)[:0:-1])

# if ans > 2**32 or ans < -2**32:
#   print(false)
# else:
#   print(ans)


# import collections

# p = "abc"
# s = "cbaebabacd"

# ans = []
# wl = len(p)
# ll = len(s)
# dict_2 = collections.Counter(list(p))
# print(dict_2)
# if ll < wl:
#     print("[]") 

# dict_1 = collections.Counter(list(s[0:wl]))
# print(dict_1)
# if dict_1 == dict_2:
#         ans.append(0)

# for i in range(1, ll-wl+1):
#     dict_1[s[i-1]] -= 1
#     dict_1[s[i+wl-1]] += 1
#     print(dict_1)
#     if dict_1 == dict_2:
#         ans.append(i)
        
# print(ans)
# precision = 1
# recall = 0.32
# if precision + recall == 0:
#     print(0.0)
# else:
#     f1 = 2 * (precision * recall) / (precision + recall)
#     print(f1)

#########################################################################################################################
# def calculate_metrics(true_positive, false_positive, false_negative):
#     """
#     计算 Precision、Recall 和 F1 分数
    
#     参数:
#     true_positive (int): 真正例数量
#     false_positive (int): 假正例数量
#     false_negative (int): 假反例数量
    
#     返回值:
#     precision (float): 精确率
#     recall (float): 召回率
#     f1 (float): F1 分数
#     """
#     if true_positive + false_positive == 0:
#         precision = 0.0
#     else:
#         precision = true_positive / (true_positive + false_positive)
    
#     if true_positive + false_negative == 0:
#         recall = 0.0
#     else:
#         recall = true_positive / (true_positive + false_negative)
    
#     if precision + recall == 0:
#         f1 = 0.0
#     else:
#         f1 = 2 * (precision * recall) / (precision + recall)
    
#     return precision, recall, f1

# def sum_other_values(my_dict, key_to_exclude, idx):
#     total = 0
#     for k,v in my_dict.items():
#         if k != key_to_exclude:
#             total += v[idx]

#     return total 

# def get_item_positive(target, alldata):
#     true_positive = alldata[target][1]
#     false_positive = sum_other_values(alldata,target,idx=1)
#     false_negative = alldata[target][2]
#     true_netative = sum_other_values(alldata,target,idx=2)
#     all = sum_other_values(alldata,None,idx=0)
#     return true_positive, false_positive, false_negative, true_netative, all

# def get_item_negative(target,alldata):
#     true_positive = sum_other_values(alldata,target,idx=2)
#     false_positive = alldata[target][2]
#     false_negative = sum_other_values(alldata,target,idx=1)

#     return true_positive, false_positive, false_negative

# def processing_dict(my_dict,target):
#     for k,v in my_dict.items():
#         if k == 'mmlu':
#             v = [it * 2 for it in v]
#         elif k == 'drop':
#             v = [round(it / 10 * 3.5) for it in v]
#         elif k == 'gsm8k':
#             v = [round(it * 2.5) for it in v]
#         my_dict[k] = v
#     for k,v in my_dict.items():
#         if k != target:
#             v = [round(it / 3 / 2) for it in v]
#             my_dict[k] = v

#     return my_dict


# target = 'boolq'
# alldata = ['boolq','mmlu','drop','gsm8k']
# alldata={'boolq':[3270,2755,515],
#         'mmlu':[1528,565,963],
#         'drop':[9536,7817,1719],
#         'gsm8k':[1319,28,1291]}

# alldata={'boolq':[3270,1339,1931],
#         'mmlu':[1528,314,1214],
#         'drop':[9536,2190,7346],
#         'gsm8k':[1319,0,1319]}

# alldata={'boolq':[3270,2971,199],
#         'mmlu':[1528,430,1098],
#         'drop':[9536,498,9038],
#         'gsm8k':[1319,5,1314]}

# # target = 'mmlu'
# # alldata={'boolq':[3270,2498,772],
# #         'mmlu':[1528,1178,350],
# #         'drop':[9536,8211,1325],
# #         'gsm8k':[1319,675,644]}

# # alldata={'boolq':[3270,37,3233],
# #         'mmlu':[1528,63,1464],
# #         'drop':[9536,95,9441],
# #         'gsm8k':[1319,0,1319]}

# # alldata={'boolq':[3270,220, 3050],
# #         'mmlu':[1528,1139,389],
# #         'drop':[9536,111,9425],
# #         'gsm8k':[1319,29,1290]}

# target = 'drop'
# alldata={'boolq':[3270,89,3181],
#         'mmlu':[1528,20,1508],
#         'drop':[9536,7221,1815],
#         'gsm8k':[1319,0,1319]}

# alldata={'boolq':[3270,19,3251],
#         'mmlu':[1528,1,1527],
#         'drop':[9536,3177,6359],
#         'gsm8k':[1319,0,1319]}

# alldata={'boolq':[3270,44,3226],
#         'mmlu':[1528,10,1518],
#         'drop':[9536,8191,1345],
#         'gsm8k':[1319,0,1319]}

# # target = 'gsm8k'
# # alldata={'boolq':[3270,266,3004],
# #         'mmlu':[1528,53,1475],
# #         'drop':[9536,4871,4665],
# #         'gsm8k':[1319,1117,202]}

# # alldata={'boolq':[3270,1519,1751],
# #         'mmlu':[1528,661,867],
# #         'drop':[9536,2202,7334],
# #         'gsm8k':[1319,525,794]}

# # alldata={'boolq':[3270,148,3121],
# #         'mmlu':[1528,57,1471],
# #         'drop':[9536,103,9433],
# #         'gsm8k':[1319,1310,9]}

# alldata = processing_dict(alldata, target)
# print(alldata)

# true_positive, false_positive, false_negative, true_negative, all = get_item_positive(target, alldata)
# precision, recall, f1_1 = calculate_metrics(true_positive, false_positive, false_negative)

# # print(f"Precision: {precision:.2f}")
# # print(f"Recall: {recall:.2f}")
# print(f"accuracy: {(true_negative+true_positive)/all:.4f}")
# print(f"F1 Score: {f1_1:.4f}")


# true_positive, false_positive, false_negative = get_item_negative(target, alldata)

# precision, recall, f1_2 = calculate_metrics(true_positive, false_positive, false_negative)

# # print(f"Precision: {precision:.2f}")
# # print(f"Recall: {recall:.2f}")
# print(f"F1 Score: {f1_2:.4f}")
# print((f1_1+f1_2)/2)

#########################################################################################################################

# class BinaryTreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def build_binary_tree(values, index=0):
#     if index >= len(values):
#         return None

#     value = values[index]
#     if value is None:
#         return None

#     node = BinaryTreeNode(value)
#     node.left = build_binary_tree(values, 2 * index + 1)
#     node.right = build_binary_tree(values, 2 * index + 2)

#     return node


# def dfs(root,res):
#     if not root:
#         return 
#     res.append(root.val)
#     dfs(root.left,res)
#     dfs(root.right,res)
#     return res

# def clear(root):
#     if not root:
#         return
#     root = None

# def rdfs(root,res):
#     if not res:
#         return None
#     if not root:
#         root = BinaryTreeNode(res[0])
#     print("res",res)
#     root.val = res[0]
#     res.pop(0)
#     clear(root.left)
#     if not root.right:
#         print("yesss")
#         root.right = BinaryTreeNode(None)
#     rdfs(root.right,res)

# values = [1,2,5,3,4,None,6]
# root = build_binary_tree(values)
# res = dfs(root, res=[])
# print("aaaaaaaaaaaaa", res)
# rdfs(root,res)
# print(dfs(root,[]))

import math

nums= [6,6]
target = 8

left = 0
right = len(nums)-1
ans = [-1,-1]

while left <= right and target >= left and target <= right:
    
    mid = int((left + right) / 2)
    print(mid)
    # print(left,right,nums[mid])
    # input()
    if nums[mid] < target:
        left = mid + 1
    elif nums[mid] >= target:
        right = mid - 1 
# print(left)
if nums[left] == target:
    ans[0] = left
    right = len(nums)-1

    while left <= right :
        mid = math.ceil((left + right) / 2)
        if nums[mid] <= target:
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1
    ans[1] = right
    print(ans)
else:
    print(ans)
