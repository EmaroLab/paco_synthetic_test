(define (problem joint_bar_9)
(:domain joint_bar)
(:objects
    link1 link2 link3 - link
    joint1 joint2 - joint
    angle0 angle45 angle90 angle135 angle180 angle225 angle270 angle315 - angle)
(:init
    (AngleOrd angle0 angle45)
    (AngleOrd angle45 angle90)
    (AngleOrd angle90 angle135)
    (AngleOrd angle135 angle180)
    (AngleOrd angle180 angle225)
    (AngleOrd angle225 angle270)
    (AngleOrd angle270 angle315)
    (AngleOrd angle315 angle0)

    (Connected joint1 link1)
    (Connected joint1 link2)
    (Connected joint2 link2)
    (Connected joint2 link3)

    (HasAngle angle0 joint1)
    (HasAngle angle0 joint2)
)
(:goal
(and
    (HasAngle angle315 joint1)
    (HasAngle angle45 joint2)
    )
)
)