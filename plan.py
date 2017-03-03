"""
Module description.
"""

import sys
import time
from os.path import isfile, join, dirname, exists, realpath, normpath, isdir
from subprocess import check_call, STDOUT, CalledProcessError
from os import listdir, makedirs, devnull, rename

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2017, Alessio Capitanelli"
# __credits__ = []
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"

FNULL = open(devnull, 'w')


def plan_conditional(args):
    # Set source problems folder
    problems_path = makedir("/problems/conditional/")
    logs_path = makedir("/logs")
    if args.no_joint:
        problems_path += "simplified/"
        makedir("/plans/conditional/simplified/madagascar")
        makedir("/plans/conditional/simplified/probe")
    else:
        problems_path += "legacy/"
        makedir("/plans/conditional/legacy/madagascar")
        makedir("/plans/conditional/legacy/probe")
    problems_batches = [join(problems_path, f) for f in listdir(problems_path) if isdir(join(problems_path, f))]
    problems_batches.sort()

    # Set planners path
    local_path = dirname(realpath(__file__))
    probe_path = local_path + "/planners/probe/probe"
    madagascar_path = local_path + "/planners/madagascar/nplan"

    # get domain
    if args.no_joint:
        domain_path = local_path + "/domains/simplified/domain.pddl"
    else:
        domain_path = local_path + "/domains/legacy/domain.pddl"

    for batch in problems_batches:
        # get problem files and start planning
        problem_files = [join(batch, f) for f in listdir(batch) if isfile(join(batch, f))]

        # initialize output folders
        makedir("/plans/conditional/legacy/madagascar" + batch[batch.rfind("/"):])
        makedir("/plans/conditional/legacy/probe" + batch[batch.rfind("/"):])
        makedir("/plans/conditional/simplified/madagascar" + batch[batch.rfind("/"):])
        makedir("/plans/conditional/simplified/probe" + batch[batch.rfind("/"):])

        print "Planning legacy problems for batch {0}...".format(batch[batch.rfind("/"):])
        cur_file_num = 0
        total_file_num = len(problem_files)
        logs = []
        for problemFile in problem_files:
            cur_file_num += 1
            #  generate madagascar plan
            sys.stdout.write(
                "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
            sys.stdout.flush()

            plan_filename = problemFile[problemFile.rfind("/") + 9:-5]

            if args.no_joint:
                output_path = problemFile[:49] + "/plans/conditional/simplified/madagascar/" + batch[batch.rfind("/"):] + \
                              "/plan_" + plan_filename + ".plan"
            else:
                output_path = problemFile[:49] + "/plans/conditional/legacy/madagascar/" + batch[batch.rfind("/"):] + \
                              "/plan_" + plan_filename + ".plan"

            start_time = time.time()
            try:
                check_call([madagascar_path, domain_path, problemFile, "-o", output_path, "-Q"],
                           stdout=FNULL, stderr=STDOUT)
                madagascar_time = time.time() - start_time
                plan_file = open(output_path)
                madagascar_num_actions = sum(1 for line in plan_file)
                plan_file.close()
            except CalledProcessError, e:
                sys.stdout.write(
                    "Generating plan for File {0}/{1} ERROR: nplan fail\r".format(cur_file_num, total_file_num))
                sys.stdout.flush()
                madagascar_num_actions = "-"
                madagascar_time = "-"

            #  generate probe plan
            sys.stdout.write(
                "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
            sys.stdout.flush()

            if args.no_joint:
                output_path = problemFile[:49] + "/plans/conditional/simplified/probe" + batch[batch.rfind("/"):] + \
                              "/plan_" + plan_filename + ".plan"
            else:
                output_path = problemFile[:49] + "/plans/conditional/legacy/probe" + batch[batch.rfind("/"):] + \
                              "/plan_" + plan_filename + ".plan"

            start_time = time.time()
            try:
                check_call([probe_path, "-d", domain_path, "-i", problemFile, "-o", output_path],
                           stdout=FNULL, stderr=STDOUT)
                probe_time = time.time() - start_time
                rename(output_path + ".1", output_path)
                plan_file = open(output_path)
                probe_num_actions = sum(1 for line in plan_file)
                plan_file.close()
            except (CalledProcessError, OSError) as e:
                sys.stdout.write(
                    "Generating plan for File {0}/{1} ERROR: probe fail\r".format(cur_file_num, total_file_num))
                sys.stdout.flush()
                probe_num_actions = "-"
                probe_time = "-"

            logs.append("{0},{1},{2},{3},{4}\n".format(plan_filename,
                                                       madagascar_num_actions, madagascar_time,
                                                       probe_num_actions, probe_time))
        print "\nBatch legacy planning completed."
        logs.sort()
        if not isfile(logs_path + batch[batch.rfind("/"):]):
            test_results = open(logs_path + batch[batch.rfind("/"):], "w+")
            test_results.write("problem,np_actions,np_t,probe_actions,probe_t\n")
        else:
            test_results = open(logs_path + batch[batch.rfind("/"):], "a")
        for log in logs:
            test_results.write(log)
        test_results.close()
    print "Planning completed."


def plan_simple(args):
    # Set source problems folder
    problems_path = makedir("/problems/simple/")
    logs_path = makedir("/logs")
    if args.oriented:
        problems_path += "oriented/"
        makedir("/plans/simple/oriented/madagascar")
        makedir("/plans/simple/oriented/probe")
    else:
        problems_path += "relative/"
        makedir("/plans/simple/relative/madagascar")
        makedir("/plans/simple/relative/probe")
    problems_batches = [join(problems_path, f) for f in listdir(problems_path) if isdir(join(problems_path, f))]
    problems_batches.sort()

    # Set planners path
    local_path = dirname(realpath(__file__))
    probe_path = local_path + "/planners/probe/probe"
    madagascar_path = local_path + "/planners/madagascar/nplan"
    # get domain
    if args.oriented:
        domain_path = local_path + "/domains/oriented/domain.pddl"
    else:
        domain_path = local_path + "/domains/relative/domain.pddl"

    for batch in problems_batches:
        # get problem files and start planning
        problem_files = [join(batch, f) for f in listdir(batch) if isfile(join(batch, f))]

        # initialize output folders
        makedir("/plans/simple/relative/madagascar" + batch[batch.rfind("/"):])
        makedir("/plans/simple/relative/probe" + batch[batch.rfind("/"):])
        makedir("/plans/simple/oriented/madagascar" + batch[batch.rfind("/"):])
        makedir("/plans/simple/oriented/probe" + batch[batch.rfind("/"):])

        print "Planning relative problems for batch {0}...".format(batch[batch.rfind("/"):])
        cur_file_num = 0
        total_file_num = len(problem_files)
        logs = []
        for problemFile in problem_files:
            cur_file_num += 1
            #  generate madagascar plan
            sys.stdout.write(
                "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
            sys.stdout.flush()

            plan_filename = problemFile[problemFile.rfind("/") + 9:-5]

            if args.oriented:
                output_path = problemFile[:49] + "/plans/simple/oriented/madagascar" + batch[batch.rfind("/"):] +\
                              "/plan_" + plan_filename + ".plan"
            else:
                output_path = problemFile[:49] + "/plans/simple/relative/madagascar" + batch[batch.rfind("/"):] + \
                              "/plan_" + plan_filename + ".plan"

            start_time = time.time()
            try:
                check_call([madagascar_path, domain_path, problemFile, "-o", output_path, "-Q"],
                           stdout=FNULL, stderr=STDOUT)
                madagascar_time = time.time() - start_time
                plan_file = open(output_path)
                madagascar_num_actions = sum(1 for line in plan_file)
                plan_file.close()
            except CalledProcessError, e:
                sys.stdout.write(
                    "Generating plan for File {0}/{1} ERROR: nplan fail\r".format(cur_file_num, total_file_num))
                sys.stdout.flush()
                madagascar_num_actions = "-"
                madagascar_time = "-"

            # generate probe plan
            sys.stdout.write(
                "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
            sys.stdout.flush()

            if args.oriented:
                output_path = problemFile[:49] + "/plans/simple/oriented/probe/" + \
                              batch[batch.rfind("/"):] + "/plan_" + plan_filename + ".plan"
            else:
                output_path = problemFile[:49] + "/plans/simple/relative/probe/" + \
                              batch[batch.rfind("/"):] + "/plan_" + plan_filename + ".plan"

            start_time = time.time()
            try:
                check_call([probe_path, "-d", domain_path, "-i", problemFile, "-o", output_path],
                           stdout=FNULL, stderr=STDOUT)
                probe_time = time.time() - start_time
                rename(output_path + ".1", output_path)  # fix name probe plan name
                plan_file = open(output_path)
                probe_num_actions = sum(1 for line in plan_file)
                plan_file.close()
            except (CalledProcessError, OSError) as e:
                sys.stdout.write(
                    "Generating plan for File {0}/{1} ERROR: probe fail\r".format(cur_file_num, total_file_num))
                sys.stdout.flush()
                probe_num_actions = "-"
                probe_time = "-"

            logs.append("{0},{1},{2},{3},{4}\n".format(plan_filename,
                                                       madagascar_num_actions, madagascar_time,
                                                       probe_num_actions, probe_time))

        print "\nBatch completed."
        logs.sort()
        if not isfile(logs_path + batch[batch.rfind("/"):]):
            test_results = open(logs_path + batch[batch.rfind("/"):], "w+")
            test_results.write("problem,np_actions,np_t,probe_actions,probe_t\n")
        else:
            test_results = open(logs_path + batch[batch.rfind("/"):], "a")
        for log in logs:
            test_results.write(log)
        test_results.close()
    print("Planning relative problems completed.")


def makedir(name):
    plan_path = dirname(realpath(__file__))
    if not exists(plan_path + name):
        makedirs(plan_path + name)
    plan_path += name
    return plan_path


