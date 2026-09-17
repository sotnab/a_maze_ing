# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  types.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 00:30:16 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 14:32:37 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import TypeAlias

Cell: TypeAlias = tuple[int, int]
Step: TypeAlias = tuple[int, int, int]
Grid: TypeAlias = list[list[int]]
MazeData: TypeAlias = list[str]
