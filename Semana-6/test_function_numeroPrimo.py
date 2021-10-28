def multiplo (n,m):
    i = 1
    multi = (m+1) * i
    while(multi != 0):
        if multi > n:
            print("Computador começa")
            break
        if multi == n:
            print("Você começa:")
            break
        i = i+1
        multi = (m+1) * i
