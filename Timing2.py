import time
def convert_to_km(m):
    return m * 1.609

def compound(invest, interest, n_months):
    total = invest
    for i in range (n_months):
        total = total * interest
    return total

L_N = [1]
for i in range (7):
    L_N.append(L_N[-1]*10)
    
for N in L_N:
    t0 = time.perf_counter()
    convert_to_km(N)
    dt = time.perf_counter() - t0
    print(f"convert_to_km ({N}) took {dt} secs ({1/dt}/sec)")
    
for N in L_N:
    t = time.perf_counter()
    money = compound(N, 1.005, 12)
    dt = time.perf_counter() - t
    print (f"compound({N}) took {dt:.2e} seconds ({1/dt:.2f}/sec)")
    print (f"Your investment of (£{N}) is worth £{money:.2f}")
