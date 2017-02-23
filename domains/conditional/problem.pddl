(define (problem joint_bar_01)
(:domain joint_bar)
(:objects
	link1 link2 link3 - link
	joint1 joint2 - joint
	angle90 angle0 angle180 angle270 - angle)
(:init
	(angle-before angle0 angle90)
	(angle-before angle90 angle180)
	(angle-before angle180 angle270)
	(angle-before angle270 angle0)

	(affected_as_child joint1 link2)
    (affected_as_child joint2 link2)

	(connected joint1 link1)
	(connected joint1 link2)
	(connected joint2 link2)
	(connected joint2 link3)
	
	(angle_joint angle0 joint1)
	(angle_joint angle0 joint2)
	)

(:goal
(and
	(angle_joint angle270 joint1)
	(angle_joint angle90 joint2)
	)
)
)
