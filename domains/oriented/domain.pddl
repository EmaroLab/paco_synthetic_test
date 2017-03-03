(define (domain joint_bar)
(:requirements :strips :equality :typing :adl)

(:types link joint angle)
(:predicates
    (Connected ?j - joint ?l - link) 
    (AngleOrd ?a - angle ?a1 - angle)
    (HasAngle ?a - angle ?j - joint)
    (IsChildOf ?child - link ?parent - link)
    (IsParentOf ?child - link ?parent - link)
    (IsRoot ?j - joint)
)

(:action increase_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
    (IsChildOf ?link1 ?link2)
    (Connected ?joint ?link1)
    (Connected ?joint ?link2)
    (not (= ?link1 ?link2))
    (HasAngle ?a1 ?joint)
    (AngleOrd ?a1 ?a2)
    )
:effect (and 
    (not (HasAngle ?a1 ?joint)) 
    (HasAngle ?a2 ?joint)
    )
)

(:action decrease_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
    (IsChildOf ?link1 ?link2)
    (Connected ?joint ?link1)
    (Connected ?joint ?link2)
    (not (= ?link1 ?link2))
    (HasAngle ?a1 ?joint)
    (AngleOrd ?a2 ?a1)
    )
:effect (and 
    (not (HasAngle ?a1 ?joint)) 
    (HasAngle ?a2 ?joint)
    )
)

(:action increase_angle
:parameters (?link1 ?link2 - link ?joint ?root - joint ?a1 ?a2 ?ar1 ?ar2 - angle)
:precondition (and 
    (IsParentOf ?link1 ?link2)
    (IsRoot ?root)
    (not (= ?joint ?root))
    (Connected ?joint ?link1)
    (Connected ?joint ?link2)
    (not (= ?link1 ?link2))
    (HasAngle ?a1 ?joint)
    (AngleOrd ?a1 ?a2)
    (HasAngle ?ar1 ?root)
    (AngleOrd ?ar1 ?ar2)
    )
:effect (and 
    (not (HasAngle ?a1 ?joint)) 
    (HasAngle ?a2 ?joint)
    (not (HasAngle ?ar1 ?root))
    (HasAngle ?ar2 ?root)
    )
)

(:action decrease_angle
:parameters (?link1 ?link2 - link ?joint ?root - joint ?a1 ?a2 ?ar1 ?ar2 - angle)
:precondition (and 
    (IsParentOf ?link1 ?link2)
    (IsRoot ?root)
    (not (= ?joint ?root))
    (Connected ?joint ?link1)
    (Connected ?joint ?link2)
    (not (= ?link1 ?link2))
    (HasAngle ?a1 ?joint)
    (AngleOrd ?a2 ?a1)
    (HasAngle ?ar1 ?root)
    (AngleOrd ?ar2 ?ar1)
    )
:effect (and 
    (not (HasAngle ?a1 ?joint)) 
    (HasAngle ?a2 ?joint)
    (not (HasAngle ?ar1 ?root))
    (HasAngle ?ar2 ?root)
    )
)
)