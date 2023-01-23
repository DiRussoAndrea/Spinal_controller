# Spinal controller

SCONE scenario scripts containing experiments carried using the spinal controller.

**spinal_controller_main.scone**: optimied gait using the spinal controller

**spinal_controller_imitate.scone**: optimized from a reference solution using imitation.

**ong_main.scone**: optimized gait with the controller proposed by Ong et al. (2019).

**delay**: colder containing the neural delay for the muscles modeled.

**import**:
+ **initializations**: folder containing par files used to initializze the optimization and files containing initial states of the model.
+ **measures**: folder containing scone files with the implementation of the cost function to optimize.
+ **models**: folder containing osim models.
+ **CMA_settings.scone**: scone file defining optimizer's parameters.
+ **ModelAndIntegrationSettings.scone**: scone file defining teh integration method and accuracy.


**ong_controller**:
+ **ong_2019.scone**: implementation of Ong's controller (2019).
+ **ong_2019.scone**: implementation of the balance controller from Ong et al. (2019).

**scripts**: folder containing python scripts to generate graphs and perform the correlation analysis
+ **spinal_modulation**: folder containing the experiments and scripts used for the correlation analysis.
+ **plot_neural_input.py**: generate a graph checking the contribution of CPGs, reflexes, and balance to the motoneuron activity.
+ **plot_sim.py**: plot kinematics, GRFs, and muscle activation.
+ **utils.py**: python file where we implemented the functions used in the other scripts.
	
**spinal_controller**:
+ **spinal_cntroller.scone**: controller implementation.
+ **spinal_cntroller_no_cpgs.scone**: controller implementation without CPGs parameters.
+ **spinal_disable_controller**: spinal controller where all parameters are set to 0 (necessary to obtain the imitation solution).
	
**stastes**: folder containing initial states to imitate. 


## Instruction to perform the three optmizations steps

If you want to try obtaining a new solution from scratch with the proposed controller. However, these step are not necessary if you use the solution already provided (import/initializations/spinal.par).

1. Optimize the scenario ong_main.scone to obtain a solution to imitate from Ong's controller (2019).
2. Save the evaluated storage solution (.sto) into the state folder.
3. In spinal_controller_imitate.scone, replace the .sto file with the solution you obtained at line 9 and 41 (file = states/your_file_name.sto)
4. Optimize the scenario spinal_controller_imitate.scone.
5. Save the parameter file (.par) representing the solution where the optimization converged into the folder import/initializations.
6. In spinal_controller.scone, use the parameter file obtained from the previous step to initialize the optimiztion (init_file = import/initializations/your_file_imitation_name.par), comment "<< import/measures/measure.scone >>" at line 102 and uncomment "<< import/measures/measure_mimic_unstable.scone >>" at line 103.
7. Optimize the scenario spinal_controller.scone to obtain a first stable solution.
8. Save the parameter file representing your stable solution into the folder import/initializations.
9. In spinal_controller.scone, use the parameter file obtained from the previous step to initialize the optimiztion (init_file = import/initializations/your_file_stable_name.par), comment "<< import/measures/measure_mimic_unstable.scone >>" at line 103 and uncomment "<< import/measures/measure.scone >>" at line 102.
10. Optimize again the scenario spinal_controller.scone to obtain your final solution.

Once a good solution is found, it can be used as initialization to perform other experimets (e.g. speed modulation).
