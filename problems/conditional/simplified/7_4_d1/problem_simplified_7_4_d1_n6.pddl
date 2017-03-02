(define (problem joint_bar_6)
(:domain joint_bar)
(:objects
    link1 link2 link3 link4 link5 link6 link7 - link
    angle0 angle90 angle180 angle270 - angle)
(:init
    (AngleOrd angle0 angle90)
    (AngleOrd angle90 angle180)
    (AngleOrd angle180 angle270)
    (AngleOrd angle270 angle0)

    (IsChildOf link2 link1)
    (IsChildOf link3 link2)
    (IsChildOf link4 link3)
    (IsChildOf link5 link4)
    (IsChildOf link6 link5)
    (IsChildOf link7 link6)

    (Affected link2 link1)
    (Affected link3 link1)
    (Affected link3 link2)
    (Affected link4 link1)
    (Affected link4 link2)
    (Affected link4 link3)
    (Affected link5 link1)
    (Affected link5 link2)
    (Affected link5 link3)
    (Affected link5 link4)
    (Affected link6 link1)
    (Affected link6 link2)
    (Affected link6 link3)
    (Affected link6 link4)
    (Affected link6 link5)
    (Affected link7 link1)
    (Affected link7 link2)
    (Affected link7 link3)
    (Affected link7 link4)
    (Affected link7 link5)
    (Affected link7 link6)

    (HasAngle angle0 link1)
    (HasAngle angle90 link2)
    (HasAngle angle90 link3)
    (HasAngle angle180 link4)
    (HasAngle angle0 link5)
    (HasAngle angle0 link6)
    (HasAngle angle0 link7)
)
(:goal
(and
    (HasAngle angle0 link1)
    (HasAngle angle180 link2)
    (HasAngle angle180 link3)
    (HasAngle angle270 link4)
    (HasAngle angle270 link5)
    (HasAngle angle180 link6)
    (HasAngle angle270 link7)
    )
)
)