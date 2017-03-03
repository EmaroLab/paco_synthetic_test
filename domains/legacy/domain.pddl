(define (domain joint_bar)
(:requirements :strips :equality :typing :adl :conditional-effects)

(:types link joint angle)

(:predicates
	(Connected ?j - joint ?l - link) 
	(AngleOrd ?a - angle ?a1 - angle)
	(HasAngle ?a - angle ?j - joint)
	(Affected ?j - joint ?l - link ?j1 - joint)
	(Fixed ?l - link)
)

(:action increase_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
	(Connected ?joint ?link1)
	(Connected ?joint  ?link2)
	(not (Fixed ?link1))
	(not (= ?link1 ?link2))
	(HasAngle ?a1 ?joint)
	(AngleOrd ?a1 ?a2)
	)
:effect 
    (and 
	    (not (HasAngle ?a1 ?joint)) 
	    (HasAngle ?a2 ?joint)
	    (forall (?js - joint ?a3 ?a4 - angle )
		    (when (and (Affected ?js ?link1 ?joint) (not (= ?js ?joint)) (HasAngle ?a3 ?js) (AngleOrd ?a3 ?a4))
		        (and
			        (not (HasAngle ?a3 ?js))
			        (HasAngle ?a4 ?js)
		        )
		    )
	    )
    )
)


(:action decrease_angle
:parameters (?link1 ?link2 - link ?joint - joint ?a1 ?a2 - angle)
:precondition (and 
	(Connected ?joint ?link1)
	(Connected ?joint  ?link2)
	(not (Fixed ?link1))
	(not (= ?link1 ?link2))
	(HasAngle ?a1 ?joint)
	(AngleOrd ?a2 ?a1)
	)
:effect 
    (and 
	    (not (HasAngle ?a1 ?joint)) 
	    (HasAngle ?a2 ?joint)
	    (forall (?js - joint ?a3 ?a4 - angle )
		    (when (and (Affected ?js ?link1 ?joint) (not (= ?js ?joint)) (HasAngle ?a3 ?js) (AngleOrd ?a4 ?a3))
		        (and
			        (not (HasAngle ?a3 ?js))
			        (HasAngle ?a4 ?js)
		        )
		    )
	    )
    )
)
)