'''문제 설명
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.'''

# 나의 풀이
def get_bit_counts(n):
    bit = ""
    while(n!=1):
        a = n % 2
        bit = str(a) + bit
        n = n // 2
    array = "1"+bit
    result = array.count('1')
    return result

def solution(n):
    value = get_bit_counts(n)
    while(True):
        n += 1
        if(get_bit_counts(n) == value):
            break
    return n

# bin함수를 이용한 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n


# bin()함수는 "0b"접두사가 붙은 문자열 형식의 이진 표현으로
# 변환하는데 사용된다. ex) bin(5) -> '0b101' 반환