"""
Generates plans from PACO problems in the problem folders.

"""

import sys
import argparse
from plan import plan_conditional, plan_simple, merge_results

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, Alessio Capitanelli"
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"


def main(argv):

    parser = argparse.ArgumentParser(description=
                                     "Planning for ArtiCulated Objects (PACO) synthetic benchmark plans generator. \n"
                                     "By default, plans from the problems stored in "
                                     "/problems/conditional and /problems/simple.\n"
                                     "Results are stored by default in /plans")

    parser.add_argument('-so', '--simple_only', help="Plan simple problems only.", action='store_true')
    parser.add_argument('-co', '--conditional_only', help="Plan conditional problems only.", action='store_true')
    parser.add_argument('-pp', '--plan_path', help="Path where to store plans.", type=str)
    parser.add_argument('-ss', '--simple_source_path', help="Path where to store simple plans.", type=str)
    parser.add_argument('-cs', '--conditional_source_path', help="Path where to store conditional plans.", type=str)
    args = parser.parse_args()

    if not args.conditional_only:
        simple_results = plan_simple(args)
    if not args.simple_only:
        conditional_results = plan_conditional(args)


    if args.conditional_only or args.simple_only:
        pass
    else:
        print("Merging results in plan folder...")
        merge_results(simple_results, conditional_results)
    print("Complete.")

if __name__ == "__main__":
    main(sys.argv[1:])
