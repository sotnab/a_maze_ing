# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  types.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 00:30:16 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 00:35:18 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import TypeAlias

Cell: TypeAlias = tuple[int, int]

Step: TypeAlias = tuple[int, int, int]

Grid: TypeAlias = list[list[int]]
