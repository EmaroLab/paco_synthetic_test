"""
Writes to file a problem file for the simple case.

"""

__author__ = "Alessio Capitanelli"
__copyright__ = "Copyright 2016, Alessio Capitanelli"
__license__ = "GNU"
__version__ = "1.1.0"
__maintainer__ = "Alessio Capitanelli"
__email__ = "alessio.capitanelli@dibris.unige.it"
__status__ = "Development"


def generate_simple_prob(file, angles, init, goal, oriented, file_id):

    joints = len(angles)

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
        file.write("    (angle-before angle{0} angle{1})\n".format(angles[angle], angles[angle + 1]))
    file.write("    (angle-before angle{0} angle{1})\n\n".format(angles[len(angles) - 1], angles[0]))

    if oriented:
        file.write("    (ground link_ground)\n\n")
        file.write("    (connected joint_ground link_ground)\n")
        file.write("    (connected joint_ground link1)\n")

    for joint in range(1, joints + 1):
        file.write("    (connected joint{0} link{1})\n".format(joint, joint))
        file.write("    (connected joint{0} link{1})\n".format(joint, joint + 1))
    file.write("\n")

    if oriented:
        file.write("    (angle-joint angle{0} joint_ground)\n".format(init[0]))
    for joint in range(int(oriented), joints + int(oriented)):
        file.write("    (angle-joint angle{0} joint{1})\n".format(init[joint], joint + int(not oriented)))

    file.write(")\n")
    file.write("(:goal\n")
    file.write("(and\n")

    if oriented:
        file.write("    (angle-joint angle{0} joint_ground)\n".format(goal[0]))
    for joint in range(int(oriented), joints + int(oriented)):
        file.write("    (angle-joint angle{0} joint{1})\n".format(goal[joint], joint + int(not oriented)))
    file.write("    )\n")

    file.write(")\n")
    file.write(")")


def generate_cond_prob(file, angles, init, goal, file_id):
    joints = len(angles)

    file.write("(define (problem joint_bar_{0})\n"
               "(:domain joint_bar)\n"
               "(:objects\n    ".format(file_id))

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
        file.write("    (angle-before angle{0} angle{1})\n".format(angles[angle], angles[angle + 1]))
    file.write("    (angle-before angle{0} angle{1})\n\n".format(angles[len(angles) - 1], angles[0]))

    curr_joint_index = 1
    while curr_joint_index <= joints:
        for joint_upstream in range(1, curr_joint_index):
            file.write(
                "    (affected joint{0} link{1} joint{2})\n".format(curr_joint_index, joint_upstream, joint_upstream))
        for joint_downstream in range(curr_joint_index + 1, joints + 1):
            file.write(
                "    (affected joint{0} link{1} joint{2})\n".format(curr_joint_index, joint_downstream - 1, joint_downstream))
        curr_joint_index += 1
    file.write("\n")

    file.write("    (connected joint1 link1)\n")
    for joint in range(2, joints + 1):
        file.write("    (connected joint{0} link{1})\n".format(joint, joint - 1))
        file.write("    (connected joint{0} link{1})\n".format(joint, joint))

    file.write("\n")
    for joint in range(0, joints):
        file.write("    (angle-joint angle{0} joint{1})\n".format(init[joint], joint + 1))
    file.write(")\n")

    file.write("(:goal\n")
    file.write("(and\n")

    for joint in range(0, joints):
        file.write("    (angle-joint angle{0} joint{1})\n".format(goal[joint], joint + 1))
    file.write("    )\n")

    file.write(")\n")
    file.write(")")