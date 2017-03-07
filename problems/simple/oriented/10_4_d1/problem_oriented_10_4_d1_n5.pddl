(define (problem joint_bar_5)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 link4 link5 link6 link7 link8 link9 link10 - link
    joint_ground joint1 joint2 joint3 joint4 joint5 joint6 joint7 joint8 joint9 - joint
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (IsChildOf link1 link_ground)
    (IsParentOf link_ground link1)
    (IsChildOf link2 link1)
    (IsParentOf link1 link2)
    (IsChildOf link3 link2)
    (IsParentOf link2 link3)
    (IsChildOf link4 link3)
    (IsParentOf link3 link4)
    (IsChildOf link5 link4)
    (IsParentOf link4 link5)
    (IsChildOf link6 link5)
    (IsParentOf link5 link6)
    (IsChildOf link7 link6)
    (IsParentOf link6 link7)
    (IsChildOf link8 link7)
    (IsParentOf link7 link8)
    (IsChildOf link9 link8)
    (IsParentOf link8 link9)
    (IsChildOf link10 link9)
    (IsParentOf link9 link10)

    (IsRoot joint_ground)

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
    (Connected joint7 link7)
    (Connected joint7 link8)
    (Connected joint8 link8)
    (Connected joint8 link9)
    (Connected joint9 link9)
    (Connected joint9 link10)

    (HasAngle angle90 joint_ground)
    (HasAngle angle180 joint1)
    (HasAngle angle90 joint2)
    (HasAngle angle90 joint3)
    (HasAngle angle270 joint4)
    (HasAngle angle90 joint5)
    (HasAngle angle0 joint6)
    (HasAngle angle90 joint7)
    (HasAngle angle0 joint8)
    (HasAngle angle270 joint9)
)
(:goal
(and
    (HasAngle angle0 joint_ground)
    (HasAngle angle90 joint1)
    (HasAngle angle0 joint2)
    (HasAngle angle90 joint3)
    (HasAngle angle0 joint4)
    (HasAngle angle0 joint5)
    (HasAngle angle270 joint6)
    (HasAngle angle0 joint7)
    (HasAngle angle90 joint8)
    (HasAngle angle0 joint9)
    )
)
)