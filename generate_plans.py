"""
Generates plans from PACO problems in the problem folders.

"""

import sys
import argparse
from plan import plan_conditional, plan_simple
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
                                     "Planning for ArtiCulated Objects (PACO) synthetic benchmark plans generator. \n"
                                     "Problem files must be located in the subfolder of"
                                     "/problems/conditional and /problems/simple.\n"
                                     "Results are stored in /plans")

    parser.add_argument('-s', '--simple_only', help="Plan simple problems only.", action='store_true')
    parser.add_argument('-c', '--conditional_only', help="Plan conditional problems only.", action='store_true')
    parser.add_argument('-o', '--oriented', help="Use oriented domain for relative plans", action='store_true')
    parser.add_argument('-n', '--no_joint', help="Use the alternative conditional domain with no joints.", action='store_true')
    parser.add_argument('-a', '--all',
                        help="Whenever a relative or conditional plan is generated, it generates both alternatives.",
                        action='store_true')
    args = parser.parse_args()

    # cleaning workspace
    print ("Cleaning /plans and /logs folders.")
    if isdir(dirname(realpath(__file__)) + "/plans"):
        shutil.rmtree(dirname(realpath(__file__)) + "/plans")
    if isdir(dirname(realpath(__file__)) + "/logs"):
        shutil.rmtree(dirname(realpath(__file__)) + "/logs")

    if not args.conditional_only:
        plan_simple(args)
    if not args.simple_only:
        plan_conditional(args)

    if args.all:
        args.oriented = not args.oriented
        args.no_joint = not args.no_joint

        if not args.conditional_only:
            plan_simple(args)
        if not args.simple_only:
            plan_conditional(args)

    print("Done! Results are stored in the /logs folder.")


if __name__ == "__main__":
    main(sys.argv[1:])
