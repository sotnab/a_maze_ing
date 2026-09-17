# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  test_maze_config.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/17 18:35:19 by wbaran          #+#    #+#               #
#  Updated: 2026/09/17 20:45:22 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import unittest
from mazegen import MazeConfig

test_files_path = "./tests/test_files/"


class TestMazeConfig(unittest.TestCase):

    def test_invalid_configs(self) -> None:

        files = [
            "invalid_configs/invalid_entry.txt",
            "invalid_configs/invalid_exit.txt",
            "invalid_configs/invalid_perfect.txt",
            "invalid_configs/missing_property.txt",
            "invalid_configs/same_entry_exit.txt",
            "invalid_configs/too_big_maze.txt",
            "invalid_configs/too_small_maze.txt",
        ]

        for file in files:
            with self.assertRaises(ValueError):
                MazeConfig.from_file(test_files_path + file)

    def test_valid_configs(self) -> None:

        files = [
            "valid_configs/big_maze.txt",
            "valid_configs/small_maze.txt",
            "valid_configs/non_perfect.txt",
            "valid_configs/with_seed.txt",
        ]

        for file in files:
            MazeConfig.from_file(test_files_path + file)

    def test_parses_from_file(self) -> None:
        config = MazeConfig.from_file(
            test_files_path + "valid_configs/big_maze.txt")

        self.assertEqual(config.entry, (0, 0))
        self.assertEqual(config.exit, (89, 69))
        self.assertEqual(config.output_file, "maze.txt")
        self.assertTrue(config.perfect)
        self.assertEqual(config.seed, 42)


if __name__ == "__main__":
    unittest.main()
