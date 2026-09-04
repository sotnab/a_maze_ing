# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  steps.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:17:56 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 22:18:08 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def add_steps(
    steps: list[tuple[int, int, int]],
    grid: list[list[int]],
    cell1: tuple[int, int],
    cell2: tuple[int, int]
) -> None:

    x1, y1 = cell1
    x2, y2 = cell2

    steps.append((x1, y1, grid[y1][x1]))
    steps.append((x2, y2, grid[y2][x2]))
