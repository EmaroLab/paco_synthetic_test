(define (problem joint_bar_8)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 - link
    joint_ground joint1 joint2 - joint
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
    (IsParentOf link_ground link1)
    (IsChildOf link2 link1)
    (IsParentOf link1 link2)
    (IsChildOf link3 link2)
    (IsParentOf link2 link3)

    (IsRoot joint_ground)

    (Connected joint_ground link_ground)
    (Connected joint_ground link1)
    (Connected joint1 link1)
    (Connected joint1 link2)
    (Connected joint2 link2)
    (Connected joint2 link3)

    (HasAngle angle135 joint_ground)
    (HasAngle angle315 joint1)
    (HasAngle angle90 joint2)
)
(:goal
(and
    (HasAngle angle225 joint_ground)
    (HasAngle angle315 joint1)
    (HasAngle angle45 joint2)
    )
)
)