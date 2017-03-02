(define (problem joint_bar_9)
(:domain joint_bar)
(:objects
    link1 link2 link3 link4 link5 link6 link7 - link
    joint1 joint2 joint3 joint4 joint5 joint6 - joint
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
    (Connected joint3 link3)
    (Connected joint3 link4)
    (Connected joint4 link4)
    (Connected joint4 link5)
    (Connected joint5 link5)
    (Connected joint5 link6)
    (Connected joint6 link6)
    (Connected joint6 link7)

    (HasAngle angle180 joint1)
    (HasAngle angle270 joint2)
    (HasAngle angle270 joint3)
    (HasAngle angle270 joint4)
    (HasAngle angle0 joint5)
    (HasAngle angle270 joint6)
)
(:goal
(and
    (HasAngle angle0 joint1)
    (HasAngle angle90 joint2)
    (HasAngle angle0 joint3)
    (HasAngle angle0 joint4)
    (HasAngle angle90 joint5)
    (HasAngle angle270 joint6)
    )
)
)