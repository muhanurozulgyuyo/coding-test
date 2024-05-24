while True:
    n = int(input())

    if n == -1:
        break

    divisors = [i for i in range(1, n) if n % i == 0]
    sum_divisors = sum(divisors)

    if sum_divisors == n:
        divisors_str = ' + '.join(map(str, divisors))
        print(f"{n} = {divisors_str}")
    else:
        print(f"{n} is NOT perfect.")
