(define (problem joint_bar_6)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 - link
    joint1 joint2 joint3 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (Affected joint1 link1 joint2)
    (Affected joint1 link2 joint3)
    (Affected joint2 link1 joint1)
    (Affected joint2 link2 joint3)
    (Affected joint3 link1 joint1)
    (Affected joint3 link2 joint2)

    (Connected joint1 link_ground)
    (Connected joint1 link1)
    (Connected joint2 link1)
    (Connected joint2 link2)
    (Connected joint3 link2)
    (Connected joint3 link3)

    (Fixed link_ground)

    (HasAngle angle0 joint1)
    (HasAngle angle90 joint2)
    (HasAngle angle90 joint3)
)
(:goal
(and
    (HasAngle angle270 joint1)
    (HasAngle angle0 joint2)
    (HasAngle angle180 joint3)
    )
)
)