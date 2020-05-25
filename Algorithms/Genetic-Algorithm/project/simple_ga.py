from __future__ import annotations
import random
import string
from typing import Collection
from fuzzywuzzy import fuzz

POPULATION = 30
GENERATIONS = 1000
TARGET_STRING = "Hello"
TARGET_LENGTH = len(TARGET_STRING)


class Agent:
    def __init__(self, length: int) -> None:
        self.value = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1
    
    def __str__(self) -> str:
        return f"{self.value}"


class Population:
    def __init__(self, agents: Collection[Agent] = None) -> None:
        if agents:
            self.agents = list(agents)
        else:
            self.agents = []
    
    @classmethod
    def init_agents(cls, population_size: int, length: int) -> Population:
        return cls(agents=[Agent(length) for _ in range(population_size)])

    def fitness(self) -> None:
        for agent in self.agents:
            agent.fitness = fuzz.ratio(agent.value, TARGET_STRING)
    
    def selection(self) -> None:
        self.agents.sort(key=lambda agent: agent.fitness, reverse=True)
        # print("\n".join(list(f"{i}: {str(val)}" for i, val in enumerate(self.agents))))
        self.agents = self.agents[:int(0.2 * len(self.agents))] # take 20% of agents

    def crossover(self) -> None:
        offspring = []
        for _ in range((POPULATION - len(self.agents)) // 2):
            parent1 = random.choice(self.agents)
            parent2 = random.choice(self.agents)

            child1 = Agent(TARGET_LENGTH)
            child2 = Agent(TARGET_LENGTH)

            split = random.randint(0, TARGET_LENGTH)
            child1.value = parent1.value[split:] + parent2.value[:split]
            child2.valie = parent1.value[:split] + parent2.value[split:]
            offspring.extend([child1, child2])
        self.agents.extend(offspring)

    def mutation(self) -> None:
        for agent in self.agents:
            for idx, letter in enumerate(agent.value):
                if random.uniform(0, 1) <= 0.02:
                    agent.value = agent.value[:idx] + random.choice(string.ascii_letters) + agent.value[idx+1:]

def main():
    population = Population.init_agents(POPULATION, TARGET_LENGTH)
    for generation in range(GENERATIONS):
        if generation % 100 == 0:
            print(f'Generation: {generation} Best value: {str(population.agents[0])}')
        population.fitness()
        population.selection()
        population.crossover()
        population.mutation()

        if any(agent.fitness >= 90 for agent in population.agents):
            print("Threshold met!")
            print(f"Result: {population.agents[0]}")
            return


if __name__ == "__main__":
    main()
