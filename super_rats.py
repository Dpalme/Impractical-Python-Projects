import time
import random
import statistics

# constants
GOAL = 50000
NUM_RATS = 100
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.1
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):
    return [int(random.triangular(min_wt, max_wt, mode_wt))
            for _ in range(num_rats)]


def fitness(population, goal):
    ave = statistics.mean(population)
    return ave / goal


def select(population, to_retain):
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain // 2
    members_by_sex = len(sorted_population) // 2
    females = sorted_population[:members_by_sex]
    males = sorted_population[members_by_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females


def breed(males, females):
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(LITTER_SIZE):
            child = random.randint(female, male)
            children.append(child)
    return children


def mutate(children):
    for index, rat in enumerate(children):
        if MUTATE_ODDS >= random.random():
            children[index] = round(rat * random.uniform(MUTATE_MIN,
                                                         MUTATE_MAX))
    return children


def main():
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
                       INITIAL_MODE_WT)
    print("Initial population weights = " + str(parents))
    popl_fitness = fitness(parents, GOAL)
    print("Initial population fitness = %d" % popl_fitness)
    print("number to retain = %d" % NUM_RATS)

    ave_wt = int(statistics.mean(parents))

    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = mutate(breed(selected_males, selected_females))
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print("Generation %d fitness = %.4f" % (generations, popl_fitness))
        ave_wt = int(statistics.mean(parents))
        generations += 1
        print("average weight per generation = %d" % ave_wt)
        print("\nnumber of generations = %d" % generations)
        print("number of years = %d" % int(generations/LITTERS_PER_YEAR))


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was %f seconds" % duration)
