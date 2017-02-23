#!/usr/bin/env python

"""
Generates random configurations for the PDDL PACO domains specified in the domains folder:

EASY - Angles between joints are expressed relatively (child respect to root)
CONDITIONAL - Angles are absolute, when an angle is modified all upstream and downstream ones are modified too

"""

import sys
import argparse
import os
from random import randint
import numpy as np
from problem_generators import generate_simple_prob, generate_cond_prob
from convert_angles import convert_angles_rel2abs

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, Alessio Capitanelli"
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"


def main(argv):

    parser = argparse.ArgumentParser(description=
                                     "Planning for ArtiCulated Objects (PACO) synthetic benchmarks generator. \n"
                                     "By default, it generates both relative and conditional problems and "
                                     "stores them in the problems folder.\n")

    parser.add_argument('N_LINKS', help="Number of links of the articulated objects.", type=int)
    parser.add_argument('N_SAMPLES', help="Number of samples to generate.", type=int)
    parser.add_argument('-r', '--resolution', help="Sets angle resolution, default: 4 (0, 90, 180, 270).", type=int)
    parser.add_argument('-so', '--simple_only', help="Generate simple problems only.", action='store_true')
    parser.add_argument('-co', '--conditional_only', help="Generate conditional problems only.", action='store_true')
    parser.add_argument('-sp', '--simple_path', help="Path where to generate simple problems.", type=str)
    parser.add_argument('-cp', '--conditional_path', help="Path where to generate conditional problems.", type=str)
    parser.add_argument('-d', '--distance', help="Minimum average distance between a joint initial and goal state. "
                                                 "Used to generate more realistic datasets.", type=int)
    parser.add_argument('-o', '--oriented',
                        help="Generates spatially oriented configurations for the relative case, default: false",
                        action='store_true')
    args = parser.parse_args()

    # Generating available angles configurations
    step = 90
    resolution = 4

    if args.resolution is not None:
        if 360 % args.resolution == 0:
            step = 360/args.resolution
            resolution = args.resolution
        else:
            print('Resolution must be a divisor of 360. Aborting.')
            return

    if args.N_LINKS < 3:
        print('There must be at least 3 links. Aborting.')
        return

    angles = range(0, 359, step)

    joints = args.N_LINKS  # later, -1 if not oriented
    if args.oriented:
        print('Generating oriented configurations for the relative case. Considering virtual link with the ground.')

    # Generate initial and final configurations
    confs = []

    for prob in range(0, args.N_SAMPLES):

        state = []
        for joint in range(0, joints):
            state.append(angles[randint(0, resolution - 1)])

        goal = []
        if args.distance is not None:
            realism = -1

            while realism < joints * args.distance:
                goal = []
                for link in range(0, joints):
                    goal.append(angles[randint(0, resolution - 1)])
                realism = abs(sum(list(np.array(state) - np.array(goal))))
        else:
            for link in range(0, joints):
                goal.append(angles[randint(0, resolution - 1)])

        confs.append(state)
        confs.append(goal)

    # Print to file
    tag = ""
    if args.oriented or args.distance:
        tag += "_"
    if args.oriented:
        tag += "o"
    if args.distance:
        tag = tag + "d" + str(args.distance)

    if not args.conditional_only or args.simple_only:

        path = os.path.dirname(os.path.realpath(__file__))
        if args.simple_path is not None:
            path = args.simple_path
        else:
            if not os.path.exists(path + "/problems/simple"):
                os.makedirs(path + "/problems/simple")
            path += "/problems/simple"

        print("Writing {0} simple problem files to {1}...".format(args.N_SAMPLES, path))
        file_id = 1
        for probf in range(0, len(confs), 2):
            filename = "/problem_simple_{0}_{1}{2}_n{3}.pddl".format(joints, resolution, tag, file_id)
            file = open(path + filename, "w+")
            generate_simple_prob(file, angles, confs[probf], confs[probf + 1], args.oriented, file_id)
            file.close()
            file_id += 1

        print("Done.")

    if not args.simple_only or args.conditional_only:

        path = os.path.dirname(os.path.realpath(__file__))
        if args.conditional_path is not None:
            path = args.conditional_path
        else:
            if not os.path.exists(path + "/problems/conditional"):
                os.makedirs(path + "/problems/conditional")
            path += "/problems/conditional"

        print("Writing conditional problem files to {0}...".format(path))
        file_id = 1
        for probf in range(0, len(confs), 2):
            filename = "/problem_conditional_{0}_{1}{2}_n{3}.pddl".format(joints, resolution, tag, file_id)
            file = open(path + filename, "w+")
            init = convert_angles_rel2abs(confs[probf])
            goal = convert_angles_rel2abs(confs[probf + 1])
            generate_cond_prob(file, angles, init, goal, file_id)
            file.close()
            file_id += 1

        print("Done.")
    print("All operations completed. Happy planning!")


if __name__ == "__main__":
    main(sys.argv[1:])

