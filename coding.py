Coding Q1 - 
  
#  Question 1 Solution 
nums = [5,2,6,1]

result = []
for i in range(len(nums)-1):
    count = 0
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j] :
            count += 1
    result.append(count)
result.append(0)
print(result)


# updated code for question 1

sort_nums = sorted(nums)
print(sort_nums)

def get_index(nums,sort_nums):
    n = len(sort_nums)
    
    mid = len(sort_nums)//2
    
    if nums == sort_nums[mid]:
        return n-mid
    elif nums > sort_nums[mid] :
        return get_index(nums,sort_nums[mid:])
    else :
        return get_index(nums,sort_nums[:mid])
    
    
            
result = []
for i in range(len(nums)-1):
    check = get_index(sort_nums,nums[i])
    result.append(check)
    
print(result)


#  Question 3 Solution 

def num_array(nums,k):
    n = len(nums)
    result = []
    count = 0
    b = 0
    
    for i in range(n):
        count += nums[i]
        if count == k :
            result.append(count)
            count -= nums[b]
            b += 1
    return len(result)
solution =num_array([1,1,1],2) 
print(solution)



# Question 2 solution 

def longest_string(st,k):
    count = k
    distinct = 1
    num = 0
    check = set()
    for i in st:
        if i not in check :
            
            if count > 0 or distinct == 1 :
                
                num += 1
                count -= 1
            else :
                return num
        else :
            num +=1
        check.add(i)
        print(check)
            
    return num
print(longest_string("ABAB",2))




