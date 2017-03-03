"""
Writes to file a problem file for the simple case.

"""

from random import randint
import numpy as np

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, Alessio Capitanelli"
__license__ = "GPLv3"
__version__ = "1.1.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"


def generate_simple_prob(file, angles, init, goal, oriented, file_id):

    joints = len(init)

    file.write("(define (problem joint_bar_{0})\n"
               "(:domain joint_bar)\n"
               "(:objects\n    ".format(file_id))

    if oriented:
        file.write("link_ground ")

    for link in range(1, joints + 1):
        file.write("link{0} ".format(link))
    file.write("- link\n    ")

    if oriented:
        file.write("joint_ground ")
    joints -= 1  # relative not oriented (j - 1)

    for joint in range(1, joints + 1):
        file.write("joint{0} ".format(joint))
    file.write("- joint\n    ")

    for angle in angles:
        file.write("angle{0} ".format(angle))
    file.write("- angle)\n")

    file.write("(:init\n")

    for angle in range(len(angles) - 1):
        file.write("    (AngleOrd angle{0} angle{1})\n".format(angles[angle], angles[angle + 1]))
    file.write("    (AngleOrd angle{0} angle{1})\n\n".format(angles[len(angles) - 1], angles[0]))

    if oriented:
        file.write("    (IsChildOf link1 link_ground)\n")
        file.write("    (IsParentOf link_ground link1)\n")
        for angle in range(1, joints + 1):
            file.write("    (IsChildOf link{0} link{1})\n".format(str(angle + 1), str(angle)))
            file.write("    (IsParentOf link{0} link{1})\n".format(str(angle), str(angle + 1)))
        file.write("\n")

        file.write("    (IsRoot joint_ground)\n\n")
        file.write("    (Connected joint_ground link_ground)\n")
        file.write("    (Connected joint_ground link1)\n")

    for joint in range(1, joints + 1):
        file.write("    (Connected joint{0} link{1})\n".format(joint, joint))
        file.write("    (Connected joint{0} link{1})\n".format(joint, joint + 1))
    file.write("\n")

    if oriented:
        file.write("    (HasAngle angle{0} joint_ground)\n".format(init[0]))
    for joint in range(int(oriented), joints + int(oriented)):
        file.write("    (HasAngle angle{0} joint{1})\n".format(init[joint], joint + int(not oriented)))

    file.write(")\n")
    file.write("(:goal\n")
    file.write("(and\n")

    if oriented:
        file.write("    (HasAngle angle{0} joint_ground)\n".format(goal[0]))
    for joint in range(int(oriented), joints + int(oriented)):
        file.write("    (HasAngle angle{0} joint{1})\n".format(goal[joint], joint + int(not oriented)))
    file.write("    )\n")

    file.write(")\n")
    file.write(")")


def generate_cond_prob(file, angles, init, goal, file_id):
    joints = len(init)

    file.write("(define (problem joint_bar_{0})\n"
               "(:domain joint_bar)\n"
               "(:objects\n    ".format(file_id))

    file.write("link_ground ")
    for link in range(1, joints + 1):
        file.write("link{0} ".format(link))
    file.write("- link\n    ")

    for joint in range(1, joints + 1):
        file.write("joint{0} ".format(joint))
    file.write("- joint\n    ")

    for angle in angles:
        file.write("angle{0} ".format(angle))
    file.write("- angle)\n")

    file.write("(:init\n")

    for angle in range(len(angles) - 1):
        file.write("    (AngleOrd angle{0} angle{1})\n".format(angles[angle], angles[angle + 1]))
    file.write("    (AngleOrd angle{0} angle{1})\n\n".format(angles[len(angles) - 1], angles[0]))

    curr_joint_index = 1
    while curr_joint_index <= joints:
        for joint_upstream in range(1, curr_joint_index):
            file.write(
                "    (Affected joint{0} link{1} joint{2})\n".format(curr_joint_index, joint_upstream, joint_upstream))
        for joint_downstream in range(curr_joint_index + 1, joints + 1):
            file.write(
                "    (Affected joint{0} link{1} joint{2})\n".format(curr_joint_index, joint_downstream - 1,
                                                                    joint_downstream))
        curr_joint_index += 1
    file.write("\n")

    file.write("    (Connected joint1 link_ground)\n")
    file.write("    (Connected joint1 link1)\n")
    for joint in range(2, joints + 1):
        file.write("    (Connected joint{0} link{1})\n".format(joint, joint - 1))
        file.write("    (Connected joint{0} link{1})\n".format(joint, joint))
    file.write("\n")

    file.write("    (Fixed link_ground)\n\n")

    for joint in range(0, joints):
        file.write("    (HasAngle angle{0} joint{1})\n".format(init[joint], joint + 1))
    file.write(")\n")

    file.write("(:goal\n")
    file.write("(and\n")

    for joint in range(0, joints):
        file.write("    (HasAngle angle{0} joint{1})\n".format(goal[joint], joint + 1))
    file.write("    )\n")

    file.write(")\n")
    file.write(")")


def generate_cond_prob_no_joint(file, angles, init, goal, file_id):
    links = len(init)

    file.write("(define (problem joint_bar_{0})\n"
               "(:domain joint_bar)\n"
               "(:objects\n    ".format(file_id))

    for link in range(1, links + 1):
        file.write("link{0} ".format(link))
    file.write("- link\n    ")

    for angle in angles:
        file.write("angle{0} ".format(angle))
    file.write("- angle)\n")

    file.write("(:init\n")

    for angle in range(len(angles) - 1):
        file.write("    (AngleOrd angle{0} angle{1})\n".format(angles[angle], angles[angle + 1]))
    file.write("    (AngleOrd angle{0} angle{1})\n\n".format(angles[len(angles) - 1], angles[0]))

    for angle in range(1, links):
        file.write("    (IsChildOf link{0} link{1})\n".format(str(angle + 1), str(angle)))
    file.write("\n")

    curr_link_index = 1
    while curr_link_index <= links:
        for link_upstream in range(1, curr_link_index):
            file.write(
                "    (Affected link{0} link{1})\n".format(curr_link_index, link_upstream))
        curr_link_index += 1

    file.write("\n")
    for joint in range(0, links):
        file.write("    (HasAngle angle{0} link{1})\n".format(init[joint], joint + 1))
    file.write(")\n")

    file.write("(:goal\n")
    file.write("(and\n")

    for joint in range(0, links):
        file.write("    (HasAngle angle{0} link{1})\n".format(goal[joint], joint + 1))
    file.write("    )\n")

    file.write(")\n")
    file.write(")")


def convert_angles_rel2abs(angles):
    previous_angle = 0
    new_angles = []
    for angle in angles:
        angle += previous_angle
        if angle > 359:
            angle -= 360
        new_angles.append(angle)
        previous_angle = angle
    return new_angles


def flush_files(angles, confs, d_type, tag, path):
    file_id = 1
    for probf in range(0, len(confs), 2):
        filename = "/problem_{0}_{1}_n{2}.pddl".format(d_type, tag, file_id)
        file = open(path + filename, "w+")
        if d_type == "relative":
            generate_simple_prob(file, angles, confs[probf], confs[probf + 1], False, file_id)
        elif d_type == "oriented":
            generate_simple_prob(file, angles, confs[probf], confs[probf + 1], True, file_id)
        else:
            init = convert_angles_rel2abs(confs[probf])
            goal = convert_angles_rel2abs(confs[probf + 1])
            if d_type == "legacy":
                generate_cond_prob(file, angles, init, goal, file_id)
            if d_type == "simplified":
                generate_cond_prob_no_joint(file, angles, init, goal, file_id)
        file.close()
        file_id += 1


def generate_configurations(n_samples, n_joints, angles, resolution, distance):
    confs = []
    for prob in range(0, n_samples):

        state = []
        for joint in range(0, n_joints):
            state.append(angles[randint(0, resolution - 1)])

        goal = []
        if distance is not None:
            realism = -1

            while realism < n_joints * distance:
                goal = []
                for link in range(0, n_joints):
                    goal.append(angles[randint(0, resolution - 1)])
                realism = abs(sum(list(np.array(state) - np.array(goal))))
        else:
            for link in range(0, n_joints):
                goal.append(angles[randint(0, resolution - 1)])

        confs.append(state)
        confs.append(goal)

    return confs
