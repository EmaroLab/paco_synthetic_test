(define (problem joint_bar_3)
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

    (IsChildOf link1 link_ground)
    (IsChildOf link2 link1)
    (IsChildOf link3 link2)

    (Affected joint2 link1 joint1)
    (Affected joint3 link1 joint1)
    (Affected joint3 link2 joint2)

    (Connected joint1 link_ground)
    (Connected joint1 link1)
    (Connected joint2 link1)
    (Connected joint2 link2)
    (Connected joint3 link2)
    (Connected joint3 link3)

    (HasAngle angle270 joint1)
    (HasAngle angle0 joint2)
    (HasAngle angle0 joint3)
)
(:goal
(and
    (HasAngle angle90 joint1)
    (HasAngle angle270 joint2)
    (HasAngle angle180 joint3)
    )
)
)