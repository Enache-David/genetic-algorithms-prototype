# Genetic Algorithms Prototype

This is a prototype that uses genetic algorithms for calculating the maximum value of a function.

## Features

* Customizable parameters
* Detailed results for the first population
* Summarized results for the next populations
* 2 versions

## Concepts Used

* Binary encoding/decoding
* Fitness proportionate selection
* Elitist selection
* One-point and two-point crossover
* Mutations

## About the versions
Version 1 features one-point crossover between two chromosomes.
<br>
Version 2 features two-point crossover between two or three chromosomes.

## Output Preview

<a href="https://github.com/Enache-David/genetic-algorithms-prototype/blob/main/featured_output.txt" target="_blank">See full output example</a>


### Populatia initiala

```
   1: 10110100011110000111001  x =  1.031340  f = 9.18595418501434
   2: 00100011001101010001011  x = -1.408626  f = 5.18249967851107
              ...
  20: 01110111010011001110001  x =  0.003873  f = 4.007806048821828
```

### Probabilitati selectie

```
cromozom    1 probabilitate 0.06254878535300633
cromozom    2 probabilitate 0.035288554198825484
              ...
cromozom   20 probabilitate 0.027289857576214542
```

### Intervale probabilitati selectie

```
0 0.06254878535300633 0.09783733955183181 ... 0.9727101424237854 1
```

```
u = 0.010327822243156537   selectam cromozomul 1
u = 0.5749403858194322     selectam cromozomul 11
              ...
u = 0.38538056446738456    selectam cromozomul 7
```

### Dupa selectie:


```
   1: 01110111010011001110001  x =  0.003873  f = 4.0078052306693985
   2: 10110100011110000111001  x =  1.031340  f = 9.185953001392296
              ...
  20: 10111110001010001001100  x =  1.194070  f = 10.05843666340318
```

### Probabilitate de incrucisare 0.25

```
   1: 01110111010011001110001 u = 0.2079107889845283   < 0.25 participa
   2: 10110100011110000111001 u = 0.1814713845304906   < 0.25 participa
              ...
  20: 10111110001010001001100 u = 0.8210824989549644  
```

### Recombinare dintre cromozomul 12 cu cromozomul 15:

```
10011110110101100010101 10010110100000000110101 puncte 2 13 - rezultat:
  ************            ************         
10010110100000100010101 10011110110101000110101
  ************            ************
```


### Dupa recombinare:

```
   1: 01110100010011001110001  x = -0.046518  f = 3.915615008311233
   2: 10111110011110000111001  x =  1.199309  f = 10.083158393812539
              ...
  20: 10111110001010001001100  x =  1.194070  f = 10.05843666340318
```

### Probabilitate de mutatie 0.1

```
Au fost modificati cromozomii:
  10: 10111110110100101000110 pozitia 13 - rezultat:
      10111110110101101000110
              ...
```

### Dupa mutatie:

```
   1: 01110100010011001110001  x = -0.046518  f = 3.915615008311233
   2: 10111110011110000111001  x =  1.199309  f = 10.083158393812539
              ...
  20: 10111110001010001001100  x =  1.194070  f = 10.05843666340318
```

### Evolutia maximului:

```
Generatia    1: f maxim = 10.895247652295772   f mediu = 7.343030683609257
Generatia    2: f maxim = 10.895247652295772   f mediu = 7.678339758940391
              ...
Generatia   50: f maxim = 10.849776849225748   f mediu = 9.97846228527954
```
