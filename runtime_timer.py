import timeit
import random
from multiselect_sort import pre_sort


def test_sorting_algorithms(list_size, run_count, mode="random"):

    list_of_numbers = []

    # Vyber postup podle zvoleného módu
    if mode == "random":
        # Pole obsahující daný počet (list_size) různých čísel od 1 do list_size
        list_of_numbers = random.sample(range(1, list_size + 1), list_size)
    elif mode == "reversed":
        # Pole seřazených čísel v opačném směru, než ve kterém algoritmy řadí
        list_of_numbers = [x for x in range(list_size + 1, 1, -1)]
    elif mode == "nearly-sorted":
        # Pole obsahující daný počet (list_size) různých čísel od 1 do list_size
        list_of_numbers = random.sample(range(1, list_size + 1), list_size)
        # Předřaď pole (dvakrát pro téměř seřazené)
        list_of_numbers = pre_sort(list_of_numbers)
        list_of_numbers = pre_sort(list_of_numbers)
    else:
        print("Error: Incorrect mode name. Choose from: 'random', 'reversed'.")
        exit()

    # Pole algoritmů, které mají být podrobeny testu
    algorithms = ["bubble_sort", "selection_sort", "insertion_sort",  "merge_sort", "quick_sort", "multiselect_sort"]

    # Proveď test pro každý algoritmus
    for alg in algorithms:
        setup = "from {0} import {0}".format(alg)
        statement = "{0}({1})".format(alg, list_of_numbers)
        # Vypiš výsledek testu
        print("{0} na {1} čísel proběhl {2}krát za {3} sekund".format(
            alg, list_size, run_count, round(timeit.timeit(stmt=statement, setup=setup, number=run_count), 3)
        ))


if __name__ == '__main__':
    test_sorting_algorithms(10000, 1, mode="random")
