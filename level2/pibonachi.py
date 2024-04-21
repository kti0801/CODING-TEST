"""
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
"""

# 나의 풀이(runtime error)
def solution(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return solution(n-1) + solution(n-2)

"""
해결법: 동적계획법(Dynamic Programming)
1번 가정: 큰 문제를 작은 문제로 나눌 수 있다.
2번 가정: 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
"""
# 공부 후 풀이(runtime error)
def solution2(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

# 신박한 풀이
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
    