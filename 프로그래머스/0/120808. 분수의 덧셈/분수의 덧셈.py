import math

def solution(numer1, denom1, numer2, denom2):
    # 두 분수를 통분하여 합하기
    common_denom = denom1 * denom2
    new_numer1 = numer1 * denom2
    new_numer2 = numer2 * denom1
    sum_numer = new_numer1 + new_numer2
    
    # 기약 분수로 만들기 위해 분자와 분모의 최대공약수 구하기
    gcd = math.gcd(sum_numer, common_denom)
    
    # 분자와 분모를 최대공약수로 나누어 기약 분수 만들기
    reduced_numer = sum_numer // gcd
    reduced_denom = common_denom // gcd
    
    return [reduced_numer, reduced_denom]