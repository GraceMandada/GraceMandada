target=int(input("Please input the target number and list of integers:\n "))
nums=[]
element=0
while(element<10000):
    element=int(input())
    if element==10000:
        break
        
    nums.append(element)

#function definition as findTwoSum
def findTwoSum(nums,n,targ):
    for i in range(n):
        cur_sum=nums[i]
        
        j=i+1
        
        while j<n:
            cur_sum=cur_sum+nums[j]
            if cur_sum==targ:
                print("%d %d"%(i,j))
                
            else:
                cur_sum=cur_sum-nums[j]
                j=j+1
                
#calculating length of nums list 
n=len(nums)
#function call
findTwoSum(nums,n,target)