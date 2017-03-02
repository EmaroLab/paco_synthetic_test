(define (problem joint_bar_1)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 link4 link5 link6 link7 link8 link9 link10 - link
    joint1 joint2 joint3 joint4 joint5 joint6 joint7 joint8 joint9 joint10 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (IsChildOf link1 link_ground)
    (IsChildOf link2 link1)
    (IsChildOf link3 link2)
    (IsChildOf link4 link3)
    (IsChildOf link5 link4)
    (IsChildOf link6 link5)
    (IsChildOf link7 link6)
    (IsChildOf link8 link7)
    (IsChildOf link9 link8)
    (IsChildOf link10 link9)

    (Affected joint2 link1 joint1)
    (Affected joint3 link1 joint1)
    (Affected joint3 link2 joint2)
    (Affected joint4 link1 joint1)
    (Affected joint4 link2 joint2)
    (Affected joint4 link3 joint3)
    (Affected joint5 link1 joint1)
    (Affected joint5 link2 joint2)
    (Affected joint5 link3 joint3)
    (Affected joint5 link4 joint4)
    (Affected joint6 link1 joint1)
    (Affected joint6 link2 joint2)
    (Affected joint6 link3 joint3)
    (Affected joint6 link4 joint4)
    (Affected joint6 link5 joint5)
    (Affected joint7 link1 joint1)
    (Affected joint7 link2 joint2)
    (Affected joint7 link3 joint3)
    (Affected joint7 link4 joint4)
    (Affected joint7 link5 joint5)
    (Affected joint7 link6 joint6)
    (Affected joint8 link1 joint1)
    (Affected joint8 link2 joint2)
    (Affected joint8 link3 joint3)
    (Affected joint8 link4 joint4)
    (Affected joint8 link5 joint5)
    (Affected joint8 link6 joint6)
    (Affected joint8 link7 joint7)
    (Affected joint9 link1 joint1)
    (Affected joint9 link2 joint2)
    (Affected joint9 link3 joint3)
    (Affected joint9 link4 joint4)
    (Affected joint9 link5 joint5)
    (Affected joint9 link6 joint6)
    (Affected joint9 link7 joint7)
    (Affected joint9 link8 joint8)
    (Affected joint10 link1 joint1)
    (Affected joint10 link2 joint2)
    (Affected joint10 link3 joint3)
    (Affected joint10 link4 joint4)
    (Affected joint10 link5 joint5)
    (Affected joint10 link6 joint6)
    (Affected joint10 link7 joint7)
    (Affected joint10 link8 joint8)
    (Affected joint10 link9 joint9)

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
    (Connected joint8 link7)
    (Connected joint8 link8)
    (Connected joint9 link8)
    (Connected joint9 link9)
    (Connected joint10 link9)
    (Connected joint10 link10)

    (HasAngle angle90 joint1)
    (HasAngle angle90 joint2)
    (HasAngle angle270 joint3)
    (HasAngle angle180 joint4)
    (HasAngle angle270 joint5)
    (HasAngle angle180 joint6)
    (HasAngle angle90 joint7)
    (HasAngle angle270 joint8)
    (HasAngle angle270 joint9)
    (HasAngle angle0 joint10)
)
(:goal
(and
    (HasAngle angle180 joint1)
    (HasAngle angle180 joint2)
    (HasAngle angle180 joint3)
    (HasAngle angle0 joint4)
    (HasAngle angle0 joint5)
    (HasAngle angle0 joint6)
    (HasAngle angle0 joint7)
    (HasAngle angle270 joint8)
    (HasAngle angle90 joint9)
    (HasAngle angle270 joint10)
    )
)
)