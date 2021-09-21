import random

# 
# shivan ahmady
# 
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#######POPULATION SIZE#######
POPULATION_SIZE = 22     
######BITS PER INDIVIDUAL#######
GENOME_BITSIZE = 100     
#######GENERATIONS TO LIVE#######                << CONFIG >>>
GENERATIONS = 12  
#######TOURNAMENT SIZE#######
TOURNAMENT_SIZE = 3  
#######PROBABILITY OF MUTATION#######
MUTATION = 0.01  
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


#############################################--0--###########################################################################
### LOAD POPULATIONS -------------------------------------Returns population containing bitstrings.
def goGo(): # population comprises bitstrings
    return([(''.join(random.choice("01") for i in range(GENOME_BITSIZE))) for i in range(POPULATION_SIZE)])

### FITNESS ----------------------------------------------Fitness defined by # of 1s in each genome.
def fitness(individual): # fitness = number of 1s in individual
    return str(individual).count("1")

#############################################- DELTA -##############################################################
### TOURNAMENT SELECTION --------------------------------------------Individual selection & analysis.
def selection(population): # select one individual using tournament selection
    tournament = [random.choice(population) for i in range(TOURNAMENT_SIZE)]
    fitnesses = [fitness(tournament[i]) for i in range(TOURNAMENT_SIZE)]
    return tournament[fitnesses.index(max(fitnesses))] 

#def roulette(X, PROB):
#    x1 = list(X.copy())
#    x1.append(PROB)
#    x1 = sorted(x1)
#    return x1.index(PROB)


#############################################--HOPEFUL(?)ITERATION--########################################################
### i1 x i2 ----> SINGLE POINT CROSSOVER
def crossover(i1,i2):
    #####--------RANDOM MODIFIER--------------------------------------------------------------------------------
    RANDOMNESS_1=random.randint(1, GENOME_BITSIZE-1)
    #############################-------------------------------------------------------------------------------
    parent1,parent2=str(i1),str(i2)
    i1Xi2point=RANDOMNESS_1
    return([ parent1[0:i1Xi2point]+parent2[i1Xi2point:GENOME_BITSIZE], parent2[0:i1Xi2point]+parent1[i1Xi2point:GENOME_BITSIZE] ])

#def pairTechniqueX(elite, xtion, T='#'):
#    ii = [elite['#']]+xtion['#']
#    fitness = [elite['#']]+xtion['#']
#    if method == '#':
#        a1a2 = [[ii[x],ii[x+1]] 
#                   for x in range(len(ii)//2)]
#    if T == 'Chaos':
#        a1a2 = []
#        for x in range(len(ii)/2):

#############################################--MUTATION--#######################################################################
### MUTATION: HELPER-FUNCTION-1
def bitflip(bit): 
    bit=str(bit)
    if bit == "0": return "1"
    else: return "0"

### MUTATION 
def mutation(individual): # bitwise mutation with probability MUTATION
    individual=str(individual)
    for i in range(GENOME_BITSIZE):
        if random.random() < MUTATION:
            individual = individual[:i] + bitflip(i) + individual[i+1:]
    return(individual)        

#############################################--OUTPUT FORMATTING--#############################################
### DISPLAY OUTPUT            
def print_population(DATASET):            
    fitnesses=[fitness(DATASET[i]) for i in range(POPULATION_SIZE)]
    print(list(zip(DATASET,fitnesses)))
    print("========VARIABILITY/ELITISM ANALYSIS=========\n")


####################################################- -#############################################
####################################################-&-#############################################
####################################################- -#############################################
# INTERNAL STATE RANDOMNESS
random.seed() 
population= goGo() # generation 0

for gen in range(GENERATIONS):
    print("##GENERATION##", gen)
    print_population(population)
    if max([fitness(population[i]) for i in range(POPULATION_SIZE)]) == GENOME_BITSIZE: break;

    nextIteration=[]
    for i in range(int(POPULATION_SIZE/2)):
        parent1=selection(population)
        parent2=selection(population)
        offspring=crossover(parent1,parent2)
        nextIteration.append(mutation(offspring[0]))
        nextIteration.append(mutation(offspring[1]))

    population=nextIteration

####################################################- -#############################################
####################################################-1-#############################################
####################################################- -#############################################