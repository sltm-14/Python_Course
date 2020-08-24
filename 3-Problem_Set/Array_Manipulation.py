from sys import stdin

if __name__ == '__main__':
    (n,m) = [int(i) for i in stdin.readline().split()]

    vals  = [0] * (n+1)

    m_sum = 0
    aux   = 0

    for _ in range(m):
        (a, b, k) = [int(n) for n in stdin.readline().split()]
        vals[a-1] += k
        if b <= n:
            vals[b] -= k



    for i in (vals):
        aux += i
        if m_sum < aux:
            m_sum = aux

    print(m_sum)
