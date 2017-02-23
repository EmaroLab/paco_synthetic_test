(define (problem joint_bar_9)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 link4 - link
    joint_ground joint1 joint2 joint3 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (angle-before angle0 angle90)
    (angle-before angle90 angle180)
    (angle-before angle180 angle270)
    (angle-before angle270 angle0)

    (ground link_ground)

    (connected joint_ground link_ground)
    (connected joint_ground link1)
    (connected joint1 link1)
    (connected joint1 link2)
    (connected joint2 link2)
    (connected joint2 link3)
    (connected joint3 link3)
    (connected joint3 link4)

    (angle-joint angle270 joint_ground)
    (angle-joint angle0 joint1)
    (angle-joint angle90 joint2)
    (angle-joint angle0 joint3)
)
(:goal
(and
    (angle-joint angle90 joint_ground)
    (angle-joint angle180 joint1)
    (angle-joint angle180 joint2)
    (angle-joint angle270 joint3)
    )
)
)