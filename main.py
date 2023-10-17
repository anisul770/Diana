# I tried but couldn't manage; need more efficient way


def isprime(n):
    p = True
    for i in range(2, (n//2)+1):
        if n % i == 0:
            p = False
            break
    return p


def strtoint_q(fixed, variable):
    variable = str(variable)
    n = fixed + variable
    return int(n)


def strtoint_p(variable, fixed):
    variable = str(variable)
    n = variable + fixed
    return int(n)


def pq_list():
    p_prime_set = set()
    q_prime_set = set()
    q_fixed = ['34157', '834157', '9834157', '19834157', '219834157']
    p_fixed = ['34157', '341572', '3415721', '341572198', '341572198']
    for i in range(len(q_fixed)):
        for j in range(int(str('1')+('0'*(4-i)))):
            if isprime(strtoint_q(q_fixed[i], j)):
                q_prime_set.add(strtoint_q(q_fixed[i], j))
    for i in range(len(p_fixed)):
        for j in range(int(str('1')+('0'*(4-i)))):
            if isprime(strtoint_p(j, p_fixed[i])):
                p_prime_set.add(strtoint_p(j, p_fixed[i]))
    p_prime_list = sorted(list(p_prime_set))
    q_prime_list = sorted(list(q_prime_set))
    return p_prime_list, q_prime_list


def compare_pq(p_prime_list, q_prime_list):
    given = '34157219834157'
    p_primary = set()
    q_primary = set()
#    for i in p_prime_list:


def main():
    print(pq_list()[0], pq_list()[1])


if __name__ == '__main__':
    main()

# 34157   219834157
# 341572198   34157
# q = (34157)0 - (34157)9999
# p = 1(34157) - 9999(34157)
