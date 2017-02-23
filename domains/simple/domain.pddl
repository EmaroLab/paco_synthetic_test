(define (domain joint_bar)
(:requirements :strips :equality :typing :adl)

(:types link joint angle)

(:predicates
	(connected ?j - joint ?l - link) 
	(angle-before ?a - angle ?a1 - angle)
	(angle-joint ?a - angle ?j - joint)
	(ground ?l - link) 
)

(:action increase_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
	(connected ?joint ?link1)
	(connected ?joint ?link2)
	(not (= ?link1 ?link2))
	(not (ground ?link1))
	(angle-joint ?a1 ?joint)
	(angle-before ?a1 ?a2)
	)
:effect (and 
	(not (angle-joint ?a1 ?joint)) 
	(angle-joint ?a2 ?joint)
	)
)

(:action decrease_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
	(connected ?joint ?link1)
	(connected ?joint ?link2)
	(not (= ?link1 ?link2))
	(not (ground ?link1)) 
	(angle-joint ?a1 ?joint)
	(angle-before ?a2 ?a1)
	)
:effect (and 
	(not (angle-joint ?a1 ?joint)) 
	(angle-joint ?a2 ?joint)
	)
)
)