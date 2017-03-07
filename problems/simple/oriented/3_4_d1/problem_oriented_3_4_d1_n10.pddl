(define (problem joint_bar_10)
(:domain joint_bar)
(:objects
    link_ground link1 link2 link3 - link
    joint_ground joint1 joint2 - joint
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

    (IsRoot joint_ground)

    (Connected joint_ground link_ground)
    (Connected joint_ground link1)
    (Connected joint1 link1)
    (Connected joint1 link2)
    (Connected joint2 link2)
    (Connected joint2 link3)

    (HasAngle angle0 joint_ground)
    (HasAngle angle270 joint1)
    (HasAngle angle270 joint2)
)
(:goal
(and
    (HasAngle angle180 joint_ground)
    (HasAngle angle0 joint1)
    (HasAngle angle0 joint2)
    )
)
)