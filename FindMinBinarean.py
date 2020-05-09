#Problem statement:
'''
A nonempty array A consisting of N non-negative integers is given.
Its Binarean is defined as 
pow2(A[0])+pow2(A[1])+....+pow2(A[N-1])
pow2(k) = 2^k

for Example, the binarean of array A such that:
A[0]= 1
A[1] = 5
A[2] = 4

Bin(A) = 2 + 32 + 4 = 50

Write an efficient algorithm for the following assumptions.
1.N is an integer within the range of [1...100000]
2. Each element of array A is an integer within range [0...10000]

Return the length of the shortest array that has the same binarian as array A. 
for example:
A[0] = 1
A[1] = 0
A[2] = 2
A[3] = 0
A[4] = 0
A[5] = 2

the function should return 3 because 
-- The binarian of A is 13.
-- Array B such that B[0] = 3 , B[1]=2 and B[2]=0 also has binarian of 13.
-- there is no shorter array with a binarian of 13. 
'''

def solution(A):
    # write your code in Python 3.6
    #Step1: Find bbinarian value of A.
    BinValue = 0
    ShortArray = []
    for item in A:
        BinValue += 2**item
    #step2: Find the shortest array which gives equal binarian value as A.
    #To do that we need to find the binary representation of BinValue and count the number of set bits.
    #convert BinValue to binary represntation.
    while(BinValue):
        ShortArray.append(BinValue%2)
        BinValue = int(BinValue/2)
    
    #ShortestArray contains total number of set bits in Binarian Value of A.
    #The total number of set bits in a number is the minimum number of element needed to represent the same number in binarean array. 
    return ShortArray.count(1)
	
if __name__ == "__main__":
    #assuming A as given array.
	A= [1,0,2,0,0,2]
    print(solution(A))
