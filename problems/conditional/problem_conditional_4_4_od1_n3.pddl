(define (problem joint_bar_3)
(:domain joint_bar)
(:objects
    link1 link2 link3 link4 - link
    joint1 joint2 joint3 joint4 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (angle-before angle0 angle90)
    (angle-before angle90 angle180)
    (angle-before angle180 angle270)
    (angle-before angle270 angle0)

    (affected joint1 link1 joint2)
    (affected joint1 link2 joint3)
    (affected joint1 link3 joint4)
    (affected joint2 link1 joint1)
    (affected joint2 link2 joint3)
    (affected joint2 link3 joint4)
    (affected joint3 link1 joint1)
    (affected joint3 link2 joint2)
    (affected joint3 link3 joint4)
    (affected joint4 link1 joint1)
    (affected joint4 link2 joint2)
    (affected joint4 link3 joint3)

    (connected joint1 link1)
    (connected joint2 link1)
    (connected joint2 link2)
    (connected joint3 link2)
    (connected joint3 link3)
    (connected joint4 link3)
    (connected joint4 link4)

    (angle-joint angle270 joint1)
    (angle-joint angle0 joint2)
    (angle-joint angle90 joint3)
    (angle-joint angle90 joint4)
)
(:goal
(and
    (angle-joint angle180 joint1)
    (angle-joint angle0 joint2)
    (angle-joint angle0 joint3)
    (angle-joint angle180 joint4)
    )
)
)