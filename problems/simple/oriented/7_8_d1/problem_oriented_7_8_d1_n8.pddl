(define (problem joint_bar_8)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 link4 link5 link6 link7 - link
    joint_ground joint1 joint2 joint3 joint4 joint5 joint6 - joint
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

    (IsChildOf link1 link_ground)
    (IsChildOf link2 link1)
    (IsChildOf link3 link2)
    (IsChildOf link4 link3)
    (IsChildOf link5 link4)
    (IsChildOf link6 link5)
    (IsChildOf link7 link6)

    (Connected joint_ground link_ground)
    (Connected joint_ground link1)
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

    (HasAngle angle0 joint_ground)
    (HasAngle angle45 joint1)
    (HasAngle angle45 joint2)
    (HasAngle angle180 joint3)
    (HasAngle angle90 joint4)
    (HasAngle angle180 joint5)
    (HasAngle angle0 joint6)
)
(:goal
(and
    (HasAngle angle315 joint_ground)
    (HasAngle angle180 joint1)
    (HasAngle angle270 joint2)
    (HasAngle angle45 joint3)
    (HasAngle angle180 joint4)
    (HasAngle angle135 joint5)
    (HasAngle angle90 joint6)
    )
)
)