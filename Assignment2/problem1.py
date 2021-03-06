'''
Longest Zigzag Subsequence of a given sequence

https://community.topcoder.com/stat?c=problem_statement&pm=1259

'''

def long_zz_subsequence(A):
    # Given sequence A
    # L[i][0] => length of longest_zz_subsequence ending at i and last character greater than previous
    # L[i][1] => length of longest_zz_subsequence ending at i and last character smaller than previous
    N = len(A)

    L = [[1 for i in range(2)] for j in range(N)]
    answer = 1

    for i in range(1,N):
        for j in range(i):
            if A[j]<A[i] and L[i][0]<L[j][1]+1:
                L[i][0] = L[j][1] +1
            if A[j]>A[i] and L[i][1]<L[j][0]+1:
                L[i][1] = L[j][0] +1

        answer = max(answer,L[i][0],L[i][1])
    return answer

print(long_zz_subsequence([1,7,4,9,2,5]))
print(long_zz_subsequence([1,17,5,10,13,15,10,5,16,8]))
print(long_zz_subsequence([44]))
print(long_zz_subsequence([1,2,3,4,5,6,7,8,9]))
