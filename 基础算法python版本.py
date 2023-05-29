
# # 双指针，若是则更新长度值，若不是则重置初始下标
# # 特点，用哈希表辅助判断
# s = input()
# # 输入
#
# ans = 0
# # 存储答案
#
# begin=0
# # 存储更新的第一个位置连续子串下标
#
# setyuan =set ("aeiouAEIOU")
# # 用哈希表存储元音的字符
#
# for i,ch in enumerate(s):
#     # enumerate函数 第一个值为函数，第二个值下标开始，默认为0
#
#     if ch in setyuan:
#         ans=max(ans,i-begin+1)
#     #     存在，更新长度
#     else:
#         begin = i
#     #     不存在，重置开头
#
# print(ans)
# # 输出答案




# 分类讨论+贪心：a.停在最左/右的边上  b.停在两个1的正中间
# # 注意距离计算：车停后的最大距离
# s = list(map(int,input().split(",")))
# # 数据初始化处理，map(int,....) 将每个字符转为整数类型  ；   list，存储到列表中
#
# l = 0
# r = len(s)-1
# # 最开始的l与r的位置
#
# ans = 0
# # 答案初始值为0
#
# for i,ch in enumerate(s):
#     if ch == 1 :
#         ans = max(ans,i)
#         l=i
#         break
# # 若停左边的最大距离
#
# for i,ch in enumerate(s[::-1],r):
# enumerate( 可迭代对象【列表，元组，字符串...】，start = 0 起始索引值 ) 函数:获取元素和元素下标
#     if ch == 1:
#         ans = max(ans,r-i)
#         r = i
#         break
# # 若停右边的最大距离
#
# for i,ch in enumerate(s[l+1:r+1],l+1):
#     if ch == 1:
#         ans = max(ans,(i-l)//2)
#         l = i
# # 若停两个1中间的最大距离---- 奇数要取整 ≈ ( 数值+1 )/2   四舍五入 ≈ int( 数值+0.5 )
#
# print(ans)
# # 输出答案

# #哈希表【不包含重复元素=set】无序，若要排序需转化为list+sort
# n = eval(input())
# # 输入一个整数
#
# num_set = set ()
# # 初始化一个哈希集合num_set，用于存储所有不重复元素
#
# for _ in range(n):
#     num_set.add(eval(input()))
# # _ 表示一个占位符，用于表示当前遍历的元素值在循环中不需要使用，只需要执行循环体N次
# # 遍历n次，依次输入数字
#
# # while (n):
# #     num_set.add(eval(input()))
# #     n-=1
# # 或者用 while 实现
#
# num_lst = list(num_set)
# # 哈希集合是无序的数据结构，所以要把哈希转化为列表后再排序
#
# num_lst.sort()
# # 对列表进行排序
#
# for num in num_lst:
#     print(num,end=" ")
# # 遍历输出答案


# # 最小覆盖子串 问题 步骤：1.字典储存，字符与值  ； 2.滑动窗口技巧：右指针先滑动  ； 满足条件下，左指针移动，找最优解
#
# s = input()
# t = input()
# # 输入字符串和查找的字串
#
# t_dict = {}
# # 字典dict来存储字串每个字符的数量
# # map（str，[1,2,3]) 表示将[1,2,3]中的每个元素转为字符串类型  ----类型转换
#
# for ch in t:
#     t_dict[ch] = t_dict.get(ch,0)+1
# #dict遍历初始化
#
# min_len = 100000000000
# # 目前找到的最小覆盖子串的长度
#
# count = len(t)
# #t中还未被覆盖的字符数量
#
# ans = ""
# # 初始化答案的字符串
#
# l,r = 0,0
# # 双指针滑动遍历，初始化为0，0
#
# while r < len(s):
#     if s[r] in t_dict :
#         if t_dict[s[r]] > 0:
#             count -=1
#         t_dict[s[r]] -=1
#     r +=1
#     # 移动右指针r，直到窗口包含t中所有的字符【count == 0】
#     # 若右指针指向的字符在t中出现，则对应的字典值-1.若字典值仍大于0，说明还需要覆盖这个字符，count值-1
#
#
#     while count == 0:
#         if r-l < min_len:
#             min_len = r-l
#             ans=s[l:r]
#         if s[l] in t_dict:
#             t_dict[s[l]] += 1
#             if t_dict[s[l]] >0:
#                 count += 1
#         l += 1
# #         满足包含所有的字符的条件，左指针l右移，满足则更新min值与ans。对应的t_dict 和 count值【在t_dict > 0的情况】要改变
#
# print(min_len,ans)
#
# # 输出答案



用函数来
from collections import Counter
from math import inf

def check (cnt_win, cnt_sub):
    return all(cnt_win[k] >= cnt_sub[k] for k in cnt_sub)

s = input()

num = len(s)//4
# 获得每个字符的出现次数

cnt_s = Counter(s)
print(cnt_s,end='\n')
# 获得原来字符中所有字符的出现次数

cnt_sub = {k:v - num for k,v in cnt_s.items() if v > num}
#获得需要覆盖的字串字符以及出现次数

if len(cnt_sub) == 0:
    print(0)

else:
    cnt_win = Counter()
    ans = inf
    l = 0

    for r,ch in enumerate(s) :
        cnt_win[ch] += 1

        while check (cnt_win,cnt_sub) :
            ans = min(ans,r-l+1)
            cnt_win[s[l]] -= 1
            l += 1

    print(ans)








