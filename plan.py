"""
Module description.
"""

import sys
import time
import csv
from os.path import isfile, join, dirname, exists, realpath, normpath
from subprocess import check_call, STDOUT, CalledProcessError
from os import listdir, makedirs, devnull, rename

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, ArmorPy"
# __credits__ = []
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"

FNULL = open(devnull, 'w')


def plan_conditional(args):
    # Set output plans folder
    if args.plan_path is not None:
        plan_path = args.plan_path
    else:
        plan_path = makedir("/plans/conditional/")

    probe_plan_path = makedir("/plans/conditional/probe/")
    madagascar_plan_path = makedir("/plans/conditional/madagascar/")

    # Set source problems folder
    if args.conditional_source_path is not None:
        problems_path = args.conditional_source_path + "/"
    else:
        problems_path = makedir("/problems/conditional/")

    # Set planners path
    local_path = dirname(realpath(__file__))
    probe_path = local_path + "/planners/probe/probe"
    madagascar_path = local_path + "/planners/madagascar/nplan"

    # get domain
    domain_path = local_path + "/domains/conditional/domain.pddl"

    # get problem files and start planning
    problem_files = [f for f in listdir(problems_path) if isfile(join(problems_path, f))]

    print "Planning conditional problems..."
    cur_file_num = 0
    total_file_num = len(problem_files)
    logs = []
    for problemFile in problem_files:
        cur_file_num += 1
        #  generate madagascar plan
        sys.stdout.write(
            "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
        sys.stdout.flush()
        start_time = time.time()
        output_path = madagascar_plan_path + normpath(problemFile)[8:-5] + ".plan"

        try:
            check_call([madagascar_path, domain_path, problems_path + problemFile, "-o", output_path, "-Q"],
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
        start_time = time.time()
        output_path = probe_plan_path + normpath(problemFile)[8:-5] + ".plan"
        try:
            check_call([probe_path, "-d", domain_path, "-i", problems_path + problemFile, "-o", output_path],
                       stdout=FNULL, stderr=STDOUT)
            probe_time = time.time() - start_time
            rename(output_path + ".1", output_path)  # fix name probe plan name
            plan_file = open(output_path)
            probe_num_actions = sum(1 for line in plan_file)
            plan_file.close()
        except CalledProcessError, e:
            sys.stdout.write(
                "Generating plan for File {0}/{1} ERROR: probe fail\r".format(cur_file_num, total_file_num))
            sys.stdout.flush()
            probe_num_actions = "-"
            probe_time = "-"

        logs.append("{0},{1},{2},{3},{4}\n".format(normpath(problemFile),
                           madagascar_num_actions, madagascar_time,
                           probe_num_actions, probe_time))

    print "\nDone!"
    logs.sort()
    test_results = open(plan_path + "/conditional_planning_results.txt", "w+")
    for log in logs:
        test_results.write(log)
    test_results.close()
    return plan_path


def plan_simple(args):
    # Set output plans folder
    if args.plan_path is not None:
        plan_path = args.plan_path
    else:
        plan_path = makedir("/plans/simple/")

    probe_plan_path = makedir("/plans/simple/probe/")
    madagascar_plan_path = makedir("/plans/simple/madagascar/")

    # Set source problems folder
    if args.simple_source_path is not None:
        problems_path = args.simple_source_path + "/"
    else:
        problems_path = makedir("/problems/simple/")

    # Set planners path
    local_path = dirname(realpath(__file__))
    probe_path = local_path + "/planners/probe/probe"
    madagascar_path = local_path + "/planners/madagascar/nplan"
    # get domain
    domain_path = local_path + "/domains/simple/domain.pddl"

    # get problem files and start planning
    problem_files = [f for f in listdir(problems_path) if isfile(join(problems_path, f))]

    print "Planning simple problems..."
    cur_file_num = 0
    total_file_num = len(problem_files)
    logs = []
    for problemFile in problem_files:
        cur_file_num += 1
        #  generate madagascar plan
        sys.stdout.write(
            "Generating plan for File {0}/{1}                  \r".format(cur_file_num, total_file_num))
        sys.stdout.flush()
        start_time = time.time()
        output_path = madagascar_plan_path + normpath(problemFile)[8:-5] + ".plan"

        try:
            check_call([madagascar_path, domain_path, problems_path + problemFile, "-o", output_path, "-Q"],
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
        start_time = time.time()
        output_path = probe_plan_path + normpath(problemFile)[8:-5] + ".plan"
        try:
            check_call([probe_path, "-d", domain_path, "-i", problems_path + problemFile, "-o", output_path],
                       stdout=FNULL, stderr=STDOUT)
            probe_time = time.time() - start_time
            rename(output_path + ".1", output_path)  # fix name probe plan name
            plan_file = open(output_path)
            probe_num_actions = sum(1 for line in plan_file)
            plan_file.close()
        except CalledProcessError, e:
            sys.stdout.write(
                "Generating plan for File {0}/{1} ERROR: probe fail\r".format(cur_file_num, total_file_num))
            sys.stdout.flush()
            probe_num_actions = "-"
            probe_time = "-"

        logs.append("{0},{1},{2},{3},{4}\n".format(normpath(problemFile),
                                                          madagascar_num_actions, madagascar_time,
                                                          probe_num_actions, probe_time))

    print "\nDone!"
    logs.sort()
    test_results = open(plan_path + "/simple_planning_results.txt", "w+")
    for log in logs:
        test_results.write(log)
    test_results.close()
    return plan_path


def makedir(name):
    plan_path = dirname(realpath(__file__))
    if not exists(plan_path + name):
        makedirs(plan_path + name)
    plan_path += name
    return plan_path


def merge_results(simple_path, conditional_path):
    merged_file = open(simple_path[:-7] + "results.txt", "w+")
    simple = open(simple_path + "/simple_planning_results.txt").readlines()
    conditional = open(conditional_path + "conditional_planning_results.txt").readlines()

    merged_file.write("problem, s_np_a, s_np_t, s_probe_a, s_probe_t,"
                      "c_np_a, c_np_t, c_probe_a, c_probe_t\n")

    assert len(simple) == len(conditional)
    for line in range(0, len(simple)):
        values_simple = list(csv.reader([simple[line]], skipinitialspace=True, delimiter=','))
        values_conditional = list(csv.reader([conditional[line]], skipinitialspace=True, delimiter=','))
        merged_file.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(
            values_simple[0][0], values_simple[0][1], values_simple[0][2], values_simple[0][3], values_simple[0][4],
            values_conditional[0][1], values_conditional[0][2], values_conditional[0][3], values_conditional[0][4]
        ))
    merged_file.close()

