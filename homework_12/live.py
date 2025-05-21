import multiprocessing as mp
import random
from typing import List, Optional, Tuple


class Organism:
    def __init__(self, energy: float = 10, age: int = 0) -> None:
        """
        Ініціалізує організм з початковою енергією та віком.

        :param energy: Початкова енергія організму.
        :param age: Початковий вік організму.
        """
        self.energy: float = energy
        self.age: int = age

    def live(self) -> Tuple['Organism', Optional['Organism'], bool]:
        """
        Симулює один крок життя організму.

        Організм шукає їжу, витрачає енергію на життя, може розмножуватися,
        зазнає випадкових подій та може померти.

        :return: Кортеж з оновленим організмом, новонародженим організмом (або None),
                 та булевим значенням, чи живий організм.
        """
        food_found: float = random.uniform(0, 5)
        self.energy += food_found
        self.energy -= 1  # витрати на життя
        self.age += 1

        offspring: Optional[Organism] = None
        if self.energy > 15:
            self.energy /= 2
            offspring = Organism(energy=self.energy)

        self.random_events()

        alive: bool = self.energy > 0 and self.age < 50
        return self, offspring, alive

    def random_events(self) -> None:
        """
        Симулює випадкові події, що впливають на енергію та вік організму.
        """
        if random.random() > 0.7:  # катаклізм
            self.energy -= 1
            self.age += 1

        if random.random() > 0.5:  # хороший урожай
            self.energy += 1


def process_organism(org: Organism) -> Tuple[Organism, Optional[Organism], bool]:
    """
    Обробляє один крок життя організму.

    :param org: Організм для симуляції кроку.
    :return: Кортеж (оновлений організм, потомство або None, чи живий організм).
    """
    return org.live()


def simulate_population(initial_population: List[Organism], steps: int = 100) -> None:
    """
    Симулює життя популяції організмів протягом певної кількості кроків.

    :param initial_population: Початкова популяція організмів.
    :param steps: Кількість кроків симуляції.
    """
    population: List[Organism] = initial_population

    for step in range(steps):
        with mp.Pool(processes=mp.cpu_count()) as pool:
            results: List[Tuple[Organism, Optional[Organism], bool]] = pool.map(process_organism, population)

        new_population: List[Organism] = []
        for org, offspring, alive in results:
            if alive:
                new_population.append(org)
            if offspring:
                new_population.append(offspring)

        population = new_population
        print(f"Step {step + 1}: Population size = {len(population)}")

        if len(population) == 0:
            print("Популяція вимерла.")
            break


if __name__ == "__main__":
    initial_population: List[Organism] = [Organism() for _ in range(20)]
    simulate_population(initial_population, steps=50)
