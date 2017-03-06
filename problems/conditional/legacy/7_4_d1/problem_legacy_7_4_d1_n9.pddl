(define (problem joint_bar_9)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 link4 link5 link6 link7 - link
    joint1 joint2 joint3 joint4 joint5 joint6 joint7 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (Affected joint1 link1 joint2)
    (Affected joint1 link2 joint3)
    (Affected joint1 link3 joint4)
    (Affected joint1 link4 joint5)
    (Affected joint1 link5 joint6)
    (Affected joint1 link6 joint7)
    (Affected joint2 link1 joint1)
    (Affected joint2 link2 joint3)
    (Affected joint2 link3 joint4)
    (Affected joint2 link4 joint5)
    (Affected joint2 link5 joint6)
    (Affected joint2 link6 joint7)
    (Affected joint3 link1 joint1)
    (Affected joint3 link2 joint2)
    (Affected joint3 link3 joint4)
    (Affected joint3 link4 joint5)
    (Affected joint3 link5 joint6)
    (Affected joint3 link6 joint7)
    (Affected joint4 link1 joint1)
    (Affected joint4 link2 joint2)
    (Affected joint4 link3 joint3)
    (Affected joint4 link4 joint5)
    (Affected joint4 link5 joint6)
    (Affected joint4 link6 joint7)
    (Affected joint5 link1 joint1)
    (Affected joint5 link2 joint2)
    (Affected joint5 link3 joint3)
    (Affected joint5 link4 joint4)
    (Affected joint5 link5 joint6)
    (Affected joint5 link6 joint7)
    (Affected joint6 link1 joint1)
    (Affected joint6 link2 joint2)
    (Affected joint6 link3 joint3)
    (Affected joint6 link4 joint4)
    (Affected joint6 link5 joint5)
    (Affected joint6 link6 joint7)
    (Affected joint7 link1 joint1)
    (Affected joint7 link2 joint2)
    (Affected joint7 link3 joint3)
    (Affected joint7 link4 joint4)
    (Affected joint7 link5 joint5)
    (Affected joint7 link6 joint6)

    (Connected joint1 link_ground)
    (Connected joint1 link1)
    (Connected joint2 link1)
    (Connected joint2 link2)
    (Connected joint3 link2)
    (Connected joint3 link3)
    (Connected joint4 link3)
    (Connected joint4 link4)
    (Connected joint5 link4)
    (Connected joint5 link5)
    (Connected joint6 link5)
    (Connected joint6 link6)
    (Connected joint7 link6)
    (Connected joint7 link7)

    (Fixed link_ground)

    (HasAngle angle0 joint1)
    (HasAngle angle90 joint2)
    (HasAngle angle90 joint3)
    (HasAngle angle180 joint4)
    (HasAngle angle0 joint5)
    (HasAngle angle270 joint6)
    (HasAngle angle90 joint7)
)
(:goal
(and
    (HasAngle angle270 joint1)
    (HasAngle angle0 joint2)
    (HasAngle angle90 joint3)
    (HasAngle angle90 joint4)
    (HasAngle angle270 joint5)
    (HasAngle angle0 joint6)
    (HasAngle angle0 joint7)
    )
)
)