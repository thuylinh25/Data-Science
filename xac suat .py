n = int(input("Nhập số n giai thừa: "))
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
print(giaiThua(n))

k = int(input("Nhập số k giai thừa: "))
def giaiThua(k):
    if k == 0:
        return 1
    return k * giaiThua(k - 1)
print(giaiThua(k))

h = n-k
def giaiThua(h):
    if h == 0:
        return 1
    return h * giaiThua(h - 1)

# Xác suất tổ hợp C: không có thứ tự, không lặp
C = giaiThua(n)/(giaiThua(k)*giaiThua(h))
print(f'Xac suat to hop C la {C}')

# Xác suất chỉnh hợp A: có thứ tự, không lặp
A = giaiThua(n)/giaiThua(h)
print(f'Xac suat chinh hop A la {A}')

# Xác suất chỉnh hợp A ngang: có thứ tự, có lặp
A_ngang = giaiThua(n)/n**k
print(f'Xac suat chinh hop lap A ngang  la {A_ngang}')

print(2**64)
print(18446744073709551616/2.3951146041928085e+37)
