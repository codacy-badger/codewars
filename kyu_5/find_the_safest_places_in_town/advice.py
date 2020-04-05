#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import Dict
from kyu_5.find_the_safest_places_in_town.cell import Cell


def create_map(n: int):
    """
    Generate city map with coordinates
    :param n: defines the size of the city that Bassi needs to hide in,
              in other words the side length of the square grid
    :return:
    """
    return [(row, col) for row in range(0, n) for col in range(0, n)]


def agents_cleanup(agents, n):
    """
    Remove all agents that are outside of the city boundaries
    :param agents: is an array of agent coordinates
    :param n: defines the size of the city that Bassi needs to hide in,
              in other words the side length of the square grid
    :return:
    """
    return [agent for agent in agents if agent[0] < n and agent[1] < n]


def advice(agents: list, n: int) -> list:
    """
    The function should return a list of coordinates that are the
    furthest away (by Manhattan distance) from all agents.

    Edge cases:
        - If there is an agent on every grid cell, there is no safe space, so return an empty list.
        - If there are no agents, then every cell is a safe spaces, so return all coordinates.
        - if n is 0, return an empty list.
        - If agent coordinates are outside of the map, they are simply not considered.
        - There are no duplicate agents on the same square.

    :param agents: is an array of agent coordinates
    :param n: defines the size of the city that Bassi needs to hide in,
    in other words the side length of the square grid
    :return:
    """
    # if n is 0, return an empty list
    if n == 0:
        return list()

    # If there is an agent on every grid cell, there is no safe space,
    # so return an empty list
    agents_cleanup(agents, n)
    if len(agents) == n * n:
        return []

    # If there are no agents, then every cell is a safe spaces,
    # so return all coordinates
    COORDINATES = list()

    if not agents:
        for row in range(0, n):
            for col in range(0, n):
                COORDINATES.append((row, col))
        return COORDINATES

    DISTANCES: Dict[int, list] = dict()
    create_map(n, agents, COORDINATES, DISTANCES)

    if DISTANCES:
        return DISTANCES[max(DISTANCES.keys())]
    else:
        return COORDINATES
