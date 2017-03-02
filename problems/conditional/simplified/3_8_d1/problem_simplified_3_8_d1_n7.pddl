(define (problem joint_bar_7)
(:domain joint_bar)
(:objects
    link1 link2 link3 - link
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

    (IsChildOf link2 link1)
    (IsChildOf link3 link2)

    (Affected link2 link1)
    (Affected link3 link1)
    (Affected link3 link2)

    (HasAngle angle270 link1)
    (HasAngle angle45 link2)
    (HasAngle angle225 link3)
)
(:goal
(and
    (HasAngle angle0 link1)
    (HasAngle angle90 link2)
    (HasAngle angle180 link3)
    )
)
)