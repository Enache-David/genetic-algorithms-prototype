import math
import random

def binary_search(l, x):
    left = 0
    right = len(l) - 2
    
    while left <= right:
        mid = (left + right) // 2
      
        if x < l[mid]:
            right = mid - 1
            
        elif l[mid + 1] <= x:
            left = mid + 1
            
        else:
            return mid
    
    return 'x nu a fost gasit.'

def f(coef, x):
    return coef[0] * x**4 + coef[1] * x**3 + coef[2] * x**2 + coef[3] * x + coef[4]

in_file = open('input2.txt')
out_file = open('out2.txt', 'w')

population_size = int(in_file.readline())
a, b = map(float, in_file.readline().split())
coef = list(map(float, in_file.readline().split()))
precision = int(in_file.readline())
pc = float(in_file.readline())
pm = float(in_file.readline())
generations = int(in_file.readline())

l = math.ceil(math.log(((b - a) * 10**precision), 2))
d = (b - a) / 2**l

n = 2**l # numarul de intervale
binary_format = f'0{l}b' # string pentru a formata reprezentarea binara pe l biti
float_format = f' .{precision}f' # string pentru a formata afisarea numerelor reale
# ^ spatiul din f-string afiseaza spatiu inaintea numerelor pozitive

encoding_intervals = [a + i * d for i in range(n)]
encoding_intervals.append(b)

print(population_size)
print(a, b)
print(coef)
print(precision)
print(pc)
print(pm)
print(generations)
print()

print(f'l = {l}')
print(f'd = {d}')
print(f'Intervale: {encoding_intervals[:20]}')
print()

P = []

out_file.write('Populatia initiala\n')

for i in range(population_size):
    x = (b - a) * random.random() + a # aleg aleator un numar din domeniu
    index = binary_search(encoding_intervals, x) # codific numarul in sir binar
    P = P + [f'{index:{binary_format}}']

    out_file.write(f'{i + 1:>4}: {P[i]}  x = {x:{float_format}}  ')
    out_file.write(f'f = {f(coef, x)}\n')

for g in range(generations):
    P1 = []
    f_max = 0
    F = 0
    sel_intervals = [0]
    crossover = []
    P1_indexes = []
    
    for i in range(population_size):
        x = a + int(P[i], 2) * d # decodific numarul
        
        if f_max < f(coef, x):
            f_max = f(coef, x)
            elitist = f'{index:{binary_format}}'
            
        F = F + f(coef, x)
    
    if g == 0:
        out_file.write('\nProbabilitati selectie\n')
        
        for i in range(population_size):
            x = a + int(P[i], 2) * d # decodific numarul
            out_file.write(f'cromozom {i + 1:>4} probabilitate {f(coef, x) / F}\n')
        
    for i in range(population_size - 1):
        x = a + int(P[i], 2) * d # decodific numarul
        sel_intervals.append(sel_intervals[-1] + f(coef, x) / F)  
    
    sel_intervals.append(1)
    
    if g == 0:
        out_file.write('\nIntervale probabilitati selectie\n')
            
        for i in range(population_size + 1):
            out_file.write(f'{sel_intervals[i]} ')
    
        out_file.write('\n\n')
        
    P1.append(elitist)
        
    for i in range(population_size - 1):
        u = random.random()
        index = binary_search(sel_intervals, u)
        # ^ fiindca P incepe de la 0 este corect sa folosesc indexul capatului din stanga
        P1.append(P[index])
        
        if g == 0:
            out_file.write(f'u = {u:<22} selectam cromozomul {index + 1}\n')
        
    if g == 0:
        out_file.write('\nDupa selectie:\n')
        
        for i in range(population_size):
            x = a + int(P1[i], 2) * d # decodific numarul
            out_file.write(f'{i + 1:>4}: {P1[i]}  x = {x:{float_format}}  ')
            out_file.write(f'f = {f(coef, x)}\n')
            
    if g == 0:
        out_file.write(f'\nProbabilitate de incrucisare {pc}\n')
            
    for i in range(population_size):
        u = random.random()
        
        if u < pc:
            crossover.append(P1[i])
            P1_indexes.append(i)
            
        if g == 0:
            out_file.write(f'{i + 1:>4}: {P1[i]} u = {u:<20}')
            
            if u < pc:
                out_file.write(f' < {pc} participa\n')
                
            else:
                out_file.write('\n')
            
    while len(crossover) > 1:
        # ^ nu vrem sa facem incrucisare daca in crossover a ajuns doar un individ
        
        cp1 = random.randrange(l) # aleg aleator pozitia unui bit
        cp2 = random.randrange(l) # aleg aleator pozitia unui bit
        
        spaces = ' ' * l
        stars = '*' * l
        
        if cp1 > cp2:
            aux = cp1
            cp1 = cp2
            cp2 = aux
        
        if len(crossover) % 2 == 0:
            x0, x1 = crossover[0], crossover[1]
            
            if g == 0:
                out_file.write(f'\nRecombinare dintre cromozomul {P1_indexes[0] + 1} cu cromozomul {P1_indexes[1] + 1}:\n')
                out_file.write(f'{x0} {x1} puncte {cp1} {cp2} - rezultat:\n')
                
                if cp2 < l - 1:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]}')
                    
                else:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}')
            
            aux = x0
            if cp2 < l - 1:
                x0 = x0[:cp1] + x1[cp1:cp2+1] + x0[cp2+1:]
                x1 = x1[:cp1] + aux[cp1:cp2+1] + x1[cp2+1:]
            
            else:
                x0 = x0[:cp1] + x1[cp1:cp2+1]
                x1 = x1[:cp1] + aux[cp1:cp2+1]
            
            if g == 0:
                out_file.write(f'\n{x0} {x1}\n')
                if cp2 < l - 1:
                    # out_file.write(f'\n{x0[:cp1]}|{x0[cp1:cp2+1]}|{x0[cp2+1:]} ')
                    # out_file.write(f'{x1[:cp1]}|{x1[cp1:cp2+1]}|{x1[cp2+1:]}\n')
                
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]}')
                    
                else:
                    # out_file.write(f'\n{x0[:cp1]}|{x0[cp1:cp2+1]}| ')
                    # out_file.write(f'{x1[:cp1]}|{x1[cp1:cp2+1]}|\n')
                    
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}')
            
            P1[P1_indexes[0]] = x0
            P1[P1_indexes[1]] = x1
            
            crossover = crossover[2:]
            P1_indexes = P1_indexes[2:]
            
        else:
            x0, x1, x2 = crossover[0], crossover[1], crossover[2]
            
            if g == 0:
                out_file.write(f'\nRecombinare dintre cromozomul {P1_indexes[0] + 1} cu cromozomul {P1_indexes[1] + 1} si cromozomul {P1_indexes[2] + 1}:\n')
                out_file.write(f'{x0} {x1} {x2} puncte {cp1} {cp2} - rezultat:\n')
                
                if cp2 < l - 1:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]}')
                    
                else:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}')
            
            aux = x0
            if cp2 < l - 1:
                x0 = x0[:cp1] + x1[cp1:cp2+1] + x0[cp2+1:]
                x1 = x1[:cp1] + x2[cp1:cp2+1] + x1[cp2+1:]
                x2 = x2[:cp1] + aux[cp1:cp2+1] + x2[cp2+1:]
            
            else:
                x0 = x0[:cp1] + x1[cp1:cp2+1]
                x1 = x1[:cp1] + x2[cp1:cp2+1]
                x2 = x2[:cp1] + aux[cp1:cp2+1]
            
            if g == 0:
                out_file.write(f'\n{x0} {x1} {x2}\n')
                
                if cp2 < l - 1:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}{spaces[cp2+1:]}')
                    
                else:
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]} ')
                    out_file.write(f'{spaces[:cp1]}{stars[cp1:cp2+1]}')
            
            P1[P1_indexes[0]] = x0
            P1[P1_indexes[1]] = x1
            P1[P1_indexes[2]] = x2
            
            crossover = crossover[3:]
            P1_indexes = P1_indexes[3:]
            
    if g == 0:
        out_file.write('\nDupa recombinare:\n')
        
        for i in range(population_size):
            x = a + int(P1[i], 2) * d # decodific numarul
            out_file.write(f'{i + 1:>4}: {P1[i]}  x = {x:{float_format}}  ')
            out_file.write(f'f = {f(coef, x)}\n')
    
    if g == 0:
        out_file.write(f'\nProbabilitate de mutatie {pm}\n')
        out_file.write(f'Au fost modificati cromozomii:\n')
    
    for i in range(population_size):
        u = random.random()
        
        if u < pm:
            x = P1[i]
            
            p = random.randrange(l) # aleg aleator pozitia unui bit
            
            mutated_x = x[:p] + str(int(not int(x[p]))) + x[p+1:]
            
            P1[i] = mutated_x
            
            if g == 0:
                out_file.write(f'{i + 1:>4}: {x} pozitia {p} - rezultat:\n')
                out_file.write(f'      {P1[i]}\n')
                
    if g == 0:
        out_file.write(f'\nDupa mutatie:\n')
                
        for i in range(population_size):
            x = a + int(P1[i], 2) * d # decodific numarul
            out_file.write(f'{i + 1:>4}: {P1[i]}  x = {x:{float_format}}  ')
            out_file.write(f'f = {f(coef, x)}\n')
            
        out_file.write(f'\nEvolutia maximului:\n')
        
    out_file.write(f'Generatia {g + 1:>4}: f maxim = {f_max:<20} f mediu = {F/population_size}\n')
        
    P = P1.copy()