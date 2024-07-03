# Bachelor Thesis : Machine learning methods for studies of quantum mechanical many-body  systems


### General information
This repository contains all the code written in Python to build a VMC algorithm. The VMC algorithm is made to run with regular metropolis sampling, as well as using the Metro-Hastings (importance sampling). There are 3 possible trial-wavefunction that can be used : Single Paramter Trial Wavefunction (SPTW), Restricted Boltzmann Machine (RBM) and the general Neural Network (NN). The first model can be found in the directory "Single_param_WFT" while the NN based approaches can be found in the directory named "NN_based_WFT" .Most of the code is written in [JAX](https://jax.readthedocs.io/en/latest/index.html) - which offers a high performing compilation of the Python-code - as well as automatic differentiation. Most of the same code have been however built using [NumPy](https://numpy.org) aswell, mostly to benchmark, and for simplicity when creating the programs. 

### Requirements
Necessary dependencies can be found in the pyproject.toml file - and is easily handled by [Poetry](https://python-poetry.org/). Feel free to install them manually using Pip if you dislike simplicity (or have any other reason to not use Poetry).

### Running the VMC algorithm
Running the VMC implementation is simple, and straightforward. For SPTW and RBM you can choose your system specific parameters inside the config.py file in the specific directory (either "Single_param_WFT" or NN_based_WFT" ) located in src/simulation_scripts, 

which offers the following tune-able parameters to change the quantum system:
- Number of particles.
- Number of dimensions.
- Number of samples.
- Number of chains (for parallelisation). NOTE: Number of samples will then be the same _on each chain_
- Using JAX or Numpy
- Learning rate (eta) and number of training cycles
- Termination tolerance for optimisation.
- Optimisation scheme
- Batch size in the training
- MCMC algorithm of choice (with/without importance sampling)
- Type of Hamiltonian (harmonic)
- Interaction (None or Coulomb)
- The max degree of the hermite polynomial
- The particle type

Only for the SPTW case:
- Initial guess for the variational parameter, alpha ()

Only for the RBM case:
- Number of hidden nodes.
- Initialisaton scale of variational parameters.
- Harmonic oscillator frequency.
- A parameter which lets you choose the relation between the wave-function and Boltzmann machine.
- Sampling scale.

Also for the Importance sampling there are  two additional parameters
- Time step.
- Diffusion coefficient.



After setting these parameters to reflect the quantum system one wishes to study, the entire program is ran using '>  ./vmc.sh' (located in Single_param_WFT/ or NN_based_WFT/). This will automatically start the VMC algorithm through src/simulation_scripts/vmc_playground.py. Different flags following ./vmc.sh will have the following effect
- No flag or vmc: Runs src/simulation_scripts/vmc_playground.py
- grid: Runs src/simulation_scripts/vmc_playground.py
- int: Runs src/simulation_scripts/interaction_vs_particles.py
- energy: Runs src/simulation_scripts/energy_particle.py
- boot: Runs src/simulation_scripts/bootstrap.py
- plot: Runs src/simulation_scripts/plot_producer.py

... so on and so forth , you can check all the flags in the vmc.sh of interest ( they are not the same throughout the different models). If any other flag is put, denoted "$1", vmc.sh will attempt to run src/simulation_scripts/"$1" in the terminal. 


For the NN case, you can choose between the NonInteractiveNN ( made for testing) and the InteractiveNN (the final product) once chosen , just open the NaiveNN_Optimization file (either .ipynb or .py) and run the programm.