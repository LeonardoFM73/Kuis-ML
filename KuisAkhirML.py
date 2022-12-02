import random
import string

gen = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
target = "GENETIKA"
population = 16
gen_length = 8
Epoch=5

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

def roulete_wheel(Fitness):
    Persen=[]
    Jfitness=sum(Fitness)
    for i in range(len(Fitness)):
        prosen=(Fitness[i]/Jfitness)*100
        prosen=int(prosen)
        Persen.append(prosen)
    
    return Jfitness,Persen

#def roulete_wheel():

def crossover(gnome):
    parent=[]
    child_chromosome=[]
    for i in range(population):

        if j<16 and i%2==0:
            j=j+1
            for gp1,gp2 in zip(gnome[i],gnome[j]):
                p = random.random()
        
                if p <45:
                    child_chromosome.append(gp1) 
                elif p<90:
                    child_chromosome.append(gp2)
                else:
                    child_chromosome.append(mutate())   
        parent=child_chromosome 
    return parent
    
def mutate(parent):
    global gen
    gnome=[]
    for i in range(population):
        chromosome=[]
        for gt in zip(parent[i]):
            p=random.random()
            if p <45:
                chromosome.append(gt) 
            elif p<90:
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
    while found is not True or generation<=Epoch:
        print("Populasi ke",generation)
        for i in range(population):
            print("Individu: {}\tKromosom: {}\tFitness Score: {}\tProsen Score: {}".format(i+1, parent[i], Fitness[i], Persen[i]))
            if Fitness !=260: 
                found = True
        print(JFitness)
        parent=mutate(parent)
        Fitness = cal_fitness(parent)
        JFitness,Persen = roulete_wheel(Fitness)
        generation+=1


main()