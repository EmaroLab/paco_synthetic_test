(define (domain joint_bar)
(:requirements :strips :equality :typing :adl)

(:types link joint angle)

(:predicates
	(Connected ?j - joint ?l - link) 
	(AngleOrd ?a - angle ?a1 - angle)
	(HasAngle ?a - angle ?j - joint)
)

(:action increase_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
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
)