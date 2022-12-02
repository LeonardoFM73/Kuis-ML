import random
import numpy as np
import string

gen = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
target = "GENETIKA"
population = 16
gen_length = 8
Epoch=100

def pop(population,length):
  individu = []
  for i in range(1,population+1):
      kromosome = []
      for j in range(1,length+1):
        temp=random.choice(gen)
        kromosome.append(temp)
      
      individu.append("".join(kromosome))
  return individu

def cal_fitness(parent):
    Fit=[]  
    for i in range(len(parent)):
        fitness=0
        Ex=0
        E=0
        for gs, gt in zip(parent[i], target):
            number = ord(gs)-64
            number1= ord(gt)-64
            E = abs(number-number1)
            Ex=Ex+E
        fitness=26*gen_length-Ex
        
        Fit.append(fitness)
    return Fit

def selection(parent,Fit):
    new_parent=[]
    k=0
    while k<4:
        maks=max(Fit)
        i=[i for i, j in enumerate(Fit) if j == maks]
        for j in range(len(i)):
            #print(i[j])
            new=i[j]
            new_parent.append(parent[new])
        k+=1
    return new_parent

def regenerate(parent):
  individu = parent
  for i in range(1,(population-len(parent))+1):
      kromosome = []
      for j in range(1,9):
        temp=random.choice(gen)
        kromosome.append(temp)
      
      individu.append("".join(kromosome))
  return individu    

def roulete_wheel(Fitness):
    Persen=[]
    Jfitness=sum(Fitness)
    for i in range(len(Fitness)):
        prosen=(Fitness[i]/Jfitness)*100
        prosen=int(prosen)
        Persen.append(prosen)

    
    return Jfitness,Persen


def multi_crossover(A,B,x,y):
    child1=[]
    child2=[]
    paret1=[]
    paret2=[]
    Parent1_new=[]
    Parent2_new=[]
    for gt,gs in zip(A,B):
        child1.append(gt)
        child2.append(gs)
    child1=np.append(A[:x],B[x:])
    child2=np.append(B[:x],A[x:])
    child1=np.append(child1[:y],child2[y:])
    child2=np.append(child2[:y],child1[y:])
    paret1.append("".join(child1))
    paret2.append("".join(child2))
    Parent1_new=list(paret1)
    Parent2_new=list(paret2)
    return Parent1_new,Parent2_new
    
def crossover(gnome):
    parent=[]
    for i in range(1,9):
        p=random.randint(0,7)
        q=random.randint(0,7)
        if p>q:
            A=p
            B=q
        else:
            A=q
            B=p
        Parent1_new,Parent2_new=multi_crossover(gnome[i-1],gnome[i*2-1],A,B)
        parent.append(Parent1_new[0])
        parent.append(Parent2_new[0])
    return parent
    
def mutate(parent):
    global gen
    gnome=[]
    for i in range(population):
        chromosome=[]
        for gt in zip(parent[i]):
            p=random.randint(0, 7)
            if p<4:
                chromosome.append(gt) 
            elif p<8:
                gene = random.choice(gen) 
                chromosome.append(gene)
        gnome.append(''.join(''.join(tup) for tup in chromosome))
    return gnome

def main():
    found = False
    generation=1
    parent = pop(population,gen_length)
    Fitness = cal_fitness(parent)
    JFitness,Persen = roulete_wheel(Fitness)
    while found is True or generation<=Epoch:
        print("Populasi ke",generation)
        for i in range(population):
            print("Individu: {}\tKromosom: {}\tFitness Score: {}\tProsen Score: {}".format(i+1, parent[i], Fitness[i], Persen[i]))
            if Fitness[i] == 260: 
                found = True
        print(JFitness)
        parent=crossover(parent)
        child=mutate(parent)
        child=selection(child,Fitness)
        parent=regenerate(child)
        Fitness = cal_fitness(parent)
        JFitness,Persen = roulete_wheel(Fitness)
        generation+=1

main()
# selection
# parent = pop(population,gen_length)
# Fitness = cal_fitness(parent)
# new_parent=selection(parent,Fitness)
# new1=regenerate(new_parent)
# print(new1)
# parent=crossover(parent)
# print(parent)