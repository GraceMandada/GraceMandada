class Solution(object):
    def restoreString(self,s, indices): #function declared
        shuffled = list(s) #creating the list from the string
        for i in range(len(indices)): #iterating the indices list
            shuffled[indices[i]] = s[i] #place the character at s[i] to its correct position that is shuffled[indices[i]]
        srestored=''.join(shuffled) #restore the string by concatination using the join function
        return srestored #return the restored string




s=input("Enter string: ")
indices=[]
for i in range(len(s)):
    indices.append(int(input()))
solution= Solution()
print(solution.restoreString(s,indices))