(define (problem joint_bar_2)
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

    (Affected joint1 link1 joint2)
    (Affected joint1 link2 joint3)
    (Affected joint1 link3 joint4)
    (Affected joint1 link4 joint5)
    (Affected joint1 link5 joint6)
    (Affected joint1 link6 joint7)
    (Affected joint1 link7 joint8)
    (Affected joint1 link8 joint9)
    (Affected joint1 link9 joint10)
    (Affected joint2 link1 joint1)
    (Affected joint2 link2 joint3)
    (Affected joint2 link3 joint4)
    (Affected joint2 link4 joint5)
    (Affected joint2 link5 joint6)
    (Affected joint2 link6 joint7)
    (Affected joint2 link7 joint8)
    (Affected joint2 link8 joint9)
    (Affected joint2 link9 joint10)
    (Affected joint3 link1 joint1)
    (Affected joint3 link2 joint2)
    (Affected joint3 link3 joint4)
    (Affected joint3 link4 joint5)
    (Affected joint3 link5 joint6)
    (Affected joint3 link6 joint7)
    (Affected joint3 link7 joint8)
    (Affected joint3 link8 joint9)
    (Affected joint3 link9 joint10)
    (Affected joint4 link1 joint1)
    (Affected joint4 link2 joint2)
    (Affected joint4 link3 joint3)
    (Affected joint4 link4 joint5)
    (Affected joint4 link5 joint6)
    (Affected joint4 link6 joint7)
    (Affected joint4 link7 joint8)
    (Affected joint4 link8 joint9)
    (Affected joint4 link9 joint10)
    (Affected joint5 link1 joint1)
    (Affected joint5 link2 joint2)
    (Affected joint5 link3 joint3)
    (Affected joint5 link4 joint4)
    (Affected joint5 link5 joint6)
    (Affected joint5 link6 joint7)
    (Affected joint5 link7 joint8)
    (Affected joint5 link8 joint9)
    (Affected joint5 link9 joint10)
    (Affected joint6 link1 joint1)
    (Affected joint6 link2 joint2)
    (Affected joint6 link3 joint3)
    (Affected joint6 link4 joint4)
    (Affected joint6 link5 joint5)
    (Affected joint6 link6 joint7)
    (Affected joint6 link7 joint8)
    (Affected joint6 link8 joint9)
    (Affected joint6 link9 joint10)
    (Affected joint7 link1 joint1)
    (Affected joint7 link2 joint2)
    (Affected joint7 link3 joint3)
    (Affected joint7 link4 joint4)
    (Affected joint7 link5 joint5)
    (Affected joint7 link6 joint6)
    (Affected joint7 link7 joint8)
    (Affected joint7 link8 joint9)
    (Affected joint7 link9 joint10)
    (Affected joint8 link1 joint1)
    (Affected joint8 link2 joint2)
    (Affected joint8 link3 joint3)
    (Affected joint8 link4 joint4)
    (Affected joint8 link5 joint5)
    (Affected joint8 link6 joint6)
    (Affected joint8 link7 joint7)
    (Affected joint8 link8 joint9)
    (Affected joint8 link9 joint10)
    (Affected joint9 link1 joint1)
    (Affected joint9 link2 joint2)
    (Affected joint9 link3 joint3)
    (Affected joint9 link4 joint4)
    (Affected joint9 link5 joint5)
    (Affected joint9 link6 joint6)
    (Affected joint9 link7 joint7)
    (Affected joint9 link8 joint8)
    (Affected joint9 link9 joint10)
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

    (Fixed link_ground)

    (HasAngle angle270 joint1)
    (HasAngle angle270 joint2)
    (HasAngle angle180 joint3)
    (HasAngle angle180 joint4)
    (HasAngle angle270 joint5)
    (HasAngle angle270 joint6)
    (HasAngle angle180 joint7)
    (HasAngle angle90 joint8)
    (HasAngle angle180 joint9)
    (HasAngle angle180 joint10)
)
(:goal
(and
    (HasAngle angle90 joint1)
    (HasAngle angle0 joint2)
    (HasAngle angle180 joint3)
    (HasAngle angle270 joint4)
    (HasAngle angle180 joint5)
    (HasAngle angle90 joint6)
    (HasAngle angle270 joint7)
    (HasAngle angle90 joint8)
    (HasAngle angle0 joint9)
    (HasAngle angle90 joint10)
    )
)
)