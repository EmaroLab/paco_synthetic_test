(define (domain joint_bar)
(:requirements :strips :equality :typing :adl :conditional-effects)

(:types link angle)

(:predicates
	(AngleOrd ?a - angle ?a1 - angle)
	(HasAngle ?l - angle ?j - link)
	(Affected ?l1 - link ?l2 - link)
    (IsChildOf ?l1 - link ?l2 - link)
)

(:action increase_angle
:parameters (?child_link - link ?a1 ?a2 - angle)
:precondition (and 
	(HasAngle ?a1 ?child_link)
	(AngleOrd ?a1 ?a2)
	)
:effect 
    (and 
	    (not (HasAngle ?a1 ?child_link)) 
	    (HasAngle ?a2 ?child_link)
	    (forall (?ls - link ?a3 ?a4 - angle)
		    (when (and (Affected ?ls ?child_link) (HasAngle ?a3 ?ls) (AngleOrd ?a3 ?a4) )
		        (and
			        (not (HasAngle ?a3 ?ls))
			        (HasAngle ?a4 ?ls)
		        )
		    )
	    )
    )
)

(:action decrease_angle
:parameters (?child_link - link ?a2 ?a1 - angle)
:precondition (and 
	(HasAngle ?a2 ?child_link)
	(AngleOrd ?a1 ?a2)
	)
:effect 
    (and 
	    (not (HasAngle ?a2 ?child_link)) 
	    (HasAngle ?a1 ?child_link)
	    (forall (?ls - link ?a3 ?a4 - angle)
		    (when (and (Affected ?ls ?child_link) (HasAngle ?a4 ?ls) (AngleOrd ?a3 ?a4) )
		        (and
			        (not (HasAngle ?a4 ?ls))
			        (HasAngle ?a3 ?ls)
		        )
		    )
	    )
    )
)
)