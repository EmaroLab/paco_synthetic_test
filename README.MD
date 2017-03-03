# PACO - Planning fo ArtiCulated Objects

Problem generator and planners benchmark based on the manipulation of articulated objects.

Before running the scripts, you can check the sample problems and plans that we have already generated in
the `problems`, `plans` and `logs` folders.

## Domains

**Simple**:

+ **Relative**: a domain modelling an articulated object with a set of links and joints. Each joint 
 has an angle associated representing the difference in orientation between the precedent link and the 
 successive one.
+ **Oriented**: as above, but with an extra `link_ground` and `joint_ground`. It is used
when it is necessary to discriminate among configurations by their absolute orientation as a whole 
(e.g., the end orientation of the object is important too, not just the *"shape"*).

**Conditional**:
+ **Legacy**: a domain using absolute orientations instead of relative ones, modelled using conditional
operators. Each joint represent the angle of the link that follows.
+ **Simplified**: similar to the one above, but simplified for use in robotics. Links are ordered
and only downstream propagation is allowed. Angles are assigned directly to links and joints are
eliminated.

In general, actions assume that the first `link` argument is acted upon while somehow constraining the second one, 
to change the state of the `joint` angle.

**Note**: given a joint, it is possible to change its state by acting either on the precedent link or 
the successive one. The physical interpretation of actions may change from one model to another.
The only exception is the **simplified** domain which only allows acting on a link while constraining
the precedent one.

## Scripts

+ `generate_problems.py` generates by default problems for both the simple and conditional case with 
equivalent initial and final states. Includes options to generate alternative domains, the number of samples, joints,
and the average difference between joint angles in the initial and final states. Problems are stored
in the `problems` folder by batch with a tag indicating resolution, number of links and average difference.

+ `generate_plans.py` plans all the batches in `problems` and stores the results in `plans` folder.
It uses both *[Madagascar](https://users.ics.aalto.fi/rintanen/jussi/satplan.html)* and 
*[Probe](http://www.ai.upf.edu/software/probe-classical-planner)* planners. 
A log of planning time and number of actions is stored in the `logs` folder. 
*Please note* that when this script is launched, the `plan` folder is cleaned of
all its content before generating new plans.
 
* `run.sh` generates six batches differing by resolution and number of joints for each domain,
then it launches the planners. Can be a long process on slower machines.

Run `--help` to have more detailed information about Python scripts options.

## Contacts

[Alessio Capitanelli](mailto:alessio.capitanelli@dibris.unige.it)

[Fulvio Mastrogiovanni](mailto:fulvio.mastrogiovanni@unige.it)

[Marco Maratea](mailto:marco@dibris.unige.it)

[Mauro Vallati](m.vallati@hud.ac.uk)

## References

### Planners

[Madagascar](https://users.ics.aalto.fi/rintanen/jussi/satplan.html)

[Probe](http://www.ai.upf.edu/software/probe-classical-planner)
