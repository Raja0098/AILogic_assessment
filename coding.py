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




