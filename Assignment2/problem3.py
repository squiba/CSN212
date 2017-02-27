'''
The Lucky Draw
Longest Increasing Subsequence
https://www.codechef.com/problems/D2/ 

'''
def long_increasing_subseq(A,index,N):
    dp=[1 for i in range(N)]
    for i in range(index+1,index+N):
        for j in range(index,i):
            if A[j]<A[i]:
                dp[i-index]=max(dp[i-index],dp[j-index])
    return max(dp[i-index])


    
def main():
    no_of_tests = int(raw_input())
    for test in range(no_of_tests):
        N = int(raw_input())
        a = map(int,raw_input().strip().split())

        answer = 0
        for i in range(N):
            answer = max(answer,long_increasing_subseq(a,i,N))
        print answer
