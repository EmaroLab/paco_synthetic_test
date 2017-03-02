(define (problem joint_bar_4)
(:domain joint_bar)
(:objects
    link1 link2 link3 link4 link5 link6 link7 link8 link9 link10 - link
    joint1 joint2 joint3 joint4 joint5 joint6 joint7 joint8 joint9 - joint
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
    (Connected joint3 link3)
    (Connected joint3 link4)
    (Connected joint4 link4)
    (Connected joint4 link5)
    (Connected joint5 link5)
    (Connected joint5 link6)
    (Connected joint6 link6)
    (Connected joint6 link7)
    (Connected joint7 link7)
    (Connected joint7 link8)
    (Connected joint8 link8)
    (Connected joint8 link9)
    (Connected joint9 link9)
    (Connected joint9 link10)

    (HasAngle angle315 joint1)
    (HasAngle angle135 joint2)
    (HasAngle angle0 joint3)
    (HasAngle angle45 joint4)
    (HasAngle angle135 joint5)
    (HasAngle angle0 joint6)
    (HasAngle angle270 joint7)
    (HasAngle angle180 joint8)
    (HasAngle angle135 joint9)
)
(:goal
(and
    (HasAngle angle135 joint1)
    (HasAngle angle270 joint2)
    (HasAngle angle45 joint3)
    (HasAngle angle270 joint4)
    (HasAngle angle180 joint5)
    (HasAngle angle270 joint6)
    (HasAngle angle45 joint7)
    (HasAngle angle0 joint8)
    (HasAngle angle0 joint9)
    )
)
)