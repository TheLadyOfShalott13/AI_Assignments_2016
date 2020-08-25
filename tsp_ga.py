#!/usr/bin/python3

import sys, random

class individual:
    cities = []
random.seed(1)

n=0
current_popu = []
graph = []
start_city = -1


def init(init_popu = 100):
    global current_popu, start_city
    init_path= list(range(n))
    init_path.remove(start_city)
    for i in range(init_popu):
        indi = individual()
        indi.cities= list(init_path)
        random.shuffle(indi.cities)
        indi.ctites.append(start_city)
        current_popu.append(indi)

def fitness(indiv):
    global start_city, graph
    cost =0
    start= start_city
    for city in indiv.cities:
        cost = cost+ graph[start][city]
        start= city
    return 1/cost

def selection(top=10):
    global current_popu
    return sorted(current_popu, reverse=True, key=fitness)[:top]

def crossover(p1, p2):
    global n
    new_indi = individual()
    crossover_pt= random.randrange(n)
    new_indi.cities= [-1]*n
    new_indi.cities[crossover_pt:] = p1.cities[crossover_pt:]
    i=0
    for c in p2.cities:
        if c not in new_indi.cities:
            new_indi.cities[i]=c
            i=i+1
    return new_indi

def mutation(child, m_chance= 0.3):
    global start_city, n
    chance = random.random()
    if chance<m_chance:
        temp= list(range(n))
        temp.remove(start_city)
        swap= random.sample(temp,2)
        child[swap[0]]= child[swap[1]]
        child[swap[1]]= child[swap[0]]
    return child

generation=0
offspring=0

def tsp_ga(max_generations=1000):
    init()
    global generations, offspring, current_popu
    generations+=1
    while generations<max_generations:
        selected=selection()
        new_gen=[]
        for p1 in new_gen:
            for p2 in new_gen:
                child=crossover(p1,p2)
                child= mutation(child)
                new_gen.append(child)
                offspring+=1
        current_popu= new_gen
        generations+=1

n= int(input())
gragraph = [x[:] for x in [[0] * n] * n]
for i in range(n):
    graph[i] = list(map(int, input().split()))
start_city = int(input())
tsp_ga()
print("Path: " + str(curr_population[0].cities), "Cost: " + str(1 / fitness(curr_population[0])))
