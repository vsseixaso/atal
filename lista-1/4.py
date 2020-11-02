def new_max(arr, chk):
    nmax = -1
    imax = -1
    for i in range(len(arr)):
        if arr[i] > nmax and not chk[i]:
            nmax = arr[i]
            imax = i
    return imax

def show_raylor(pop, dur, nmus, tmax):
    pop_dur = []
    for i in range(nmus):
        pop_dur.append(pop[i] / float(dur[i]))
        
    chk = [0 for n in range(nmus)]
    mus = [0 for n in range(nmus)]
        
    tmp = 0
    while tmp < tmax:
        imax = new_max(pop_dur, chk)
        chk[imax] = 1

        if tmp + dur[imax] <= tmax:
            mus[imax] = 1
            tmp += dur[imax]
        else:
            mus[imax] = (tmax - tmp) / float(dur[i])
            tmp = tmax
    
    return mus
               
    
pop = [96, 80, 45, 100, 80]
dur = [3, 4, 5, 2, 8]
nmus = 5
tmax = 15
mus = show_raylor(pop, dur, nmus, tmax)
print(" ".join(str(m) for m in mus))

# usei um algoritmo guloso