#!/usr/bin/env python

"""
Generates random configurations for the PDDL PACO domains specified in the domains folder:

EASY - Angles between joints are expressed relatively (child respect to root)
CONDITIONAL - Angles are absolute, when an angle is modified all upstream and downstream ones are modified too

"""

import sys
import argparse
import os
from problem_generators import flush_files, generate_configurations
from os.path import dirname, realpath, isdir
import shutil

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, Alessio Capitanelli"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"


def main(argv):

    parser = argparse.ArgumentParser(description=
                                     "Planning for ArtiCulated Objects (PACO) synthetic benchmarks generator. \n"
                                     "By default, it generates both relative and conditional problems and "
                                     "stores them in the /problems folder.\n")

    parser.add_argument('N_LINKS', help="Number of links of the articulated objects.", type=int)
    parser.add_argument('N_SAMPLES', help="Number of samples to generate.", type=int)
    parser.add_argument('-r', '--resolution', help="Sets angle resolution, default: 4 (0, 90, 180, 270).", type=int)
    parser.add_argument('-s', '--simple_only', help="Generate simple problems only.", action='store_true')
    parser.add_argument('-c', '--conditional_only', help="Generate conditional problems only.", action='store_true')
    parser.add_argument('-a', '--all',
                        help="Whenever a relative or conditional problem is generated, it generates both alternatives.",
                        action="store_true")
    parser.add_argument('-d', '--distance', help="Minimum average distance between a joint initial and goal state. "
                                                 "Used to generate more realistic datasets.", type=int)
    parser.add_argument('-o', '--oriented',
                        help="Generates spatially oriented configurations for the relative case, default: false",
                        action='store_true')
    parser.add_argument('-n', '--no_joint', help="Use the alternative conditional domain with no joints.",
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

    confs = generate_configurations(args.N_SAMPLES, joints, angles, resolution, args.distance)

    # Print to file
    tag = ""
    if args.distance:
        tag = tag + "_d" + str(args.distance)
    tag = "{0}_{1}{2}".format(joints, resolution, tag)

    if not args.conditional_only or args.simple_only:
        path = os.path.dirname(os.path.realpath(__file__))

        if args.oriented:
            d_type = "oriented"
            alt_type = "relative"
        else:
            d_type = "relative"
            alt_type = "oriented"

        if not os.path.exists(path + "/problems/simple/" + d_type + "/" + tag):
            os.makedirs(path + "/problems/simple/" + d_type + "/" + tag)
        path += ("/problems/simple/" + d_type + "/" + tag)

        print("Writing {0} simple problem files to {1}...".format(args.N_SAMPLES, path))
        flush_files(angles, confs, d_type, tag, path)
        print("Done.")

        if args.all:
            path = os.path.dirname(os.path.realpath(__file__))
            if not os.path.exists(path + "/problems/simple/" + alt_type + "/" + tag):
                os.makedirs(path + "/problems/simple/" + alt_type + "/" + tag)
            path += ("/problems/simple/" + alt_type + "/" + tag)

            print("Writing {0} simple problem files to {1}...".format(args.N_SAMPLES, path))
            flush_files(angles, confs, alt_type, tag, path)
            print("Done.")

    if not args.simple_only or args.conditional_only:
        path = os.path.dirname(os.path.realpath(__file__))

        if args.no_joint:
            d_type = "simplified"
            alt_type = "legacy"
        else:
            d_type = "legacy"
            alt_type = "simplified"

        if not os.path.exists(path + "/problems/conditional/" + d_type + "/" + tag):
            os.makedirs(path + "/problems/conditional/" + d_type + "/" + tag)
        path += ("/problems/conditional/" + d_type + "/" + tag)

        print("Writing {0} conditional problem files to {1}...".format(args.N_SAMPLES, path))
        flush_files(angles, confs, d_type, tag, path)
        print("Done.")

        if args.all:
            path = os.path.dirname(os.path.realpath(__file__))
            if not os.path.exists(path + "/problems/conditional/" + alt_type + "/" + tag):
                os.makedirs(path + "/problems/conditional/" + alt_type + "/" + tag)
            path += ("/problems/conditional/" + alt_type + "/" + tag)

            print("Writing {0} conditional problem files to {1}...".format(args.N_SAMPLES, path))
            flush_files(angles, confs, alt_type, tag, path)
            print("Done.")

    print("All operations completed. Happy planning!")


if __name__ == "__main__":
    main(sys.argv[1:])

