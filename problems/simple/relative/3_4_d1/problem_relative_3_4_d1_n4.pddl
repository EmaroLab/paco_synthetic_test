(define (problem joint_bar_4)
(:domain joint_bar)
(:objects
    link1 link2 link3 - link
    joint1 joint2 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (Connected joint1 link1)
    (Connected joint1 link2)
    (Connected joint2 link2)
    (Connected joint2 link3)

    (HasAngle angle90 joint1)
    (HasAngle angle0 joint2)
)
(:goal
(and
    (HasAngle angle90 joint1)
    (HasAngle angle90 joint2)
    )
)
)