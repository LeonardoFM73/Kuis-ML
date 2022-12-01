import random
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

def roulete_wheel(Fitness):
    Persen=[]
    Jfitness=sum(Fitness)
    for i in range(len(Fitness)):
        prosen=(Fitness[i]/Jfitness)*100
        prosen=int(prosen)
        Persen.append(prosen)
    
    return Jfitness,Persen

#def roulete_wheel():
    


def main():
    parent = pop(population,gen_length)
    Fitness = cal_fitness(parent)
    JFitness,Persen = roulete_wheel(Fitness)
    for epoch in range(Epoch):
        print("Populasi ke",epoch+1)
        for i in range(population):
            print("Individu: {}\tKromosom: {}\tFitness Score: {}".format(i+1, parent[i], Fitness[i]))
        print(JFitness)
        print(Persen) 


main()