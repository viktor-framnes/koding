n = int(input())
sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum -= i**2
    else:
        sum += i**2
        if sum > n:
            sum -= i**2
            print(f"summen før det ble større enn n var {sum} som skjedde i runde {i-1}")