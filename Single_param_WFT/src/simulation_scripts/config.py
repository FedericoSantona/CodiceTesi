# Config
output_filename = "../data/vmc_playground.csv"

nparticles = 2
dim = 2


nsamples =  int(2**16) #  2**18 = 262144
scale = 1 + (dim-1)*0.1
nchains = 4# number of Markov chains.
mcmc_alg = "mh" # eiteer "mh" or "m"
backend = "jax" # or "numpy" but jax should go faster because of the jit

eta =0.01
training_cycles = 1000 #this is cycles for the ansatz
optimizer = "adam" #  ither "adam" or "gd
batch_size =  400
tol = 10**-12

particle_type = "bosons" # either "bosons" or "fermions"
max_degree = nparticles //2
hamiltonian = "ho" 
beta = 1 #2.82843

interaction = "Coulomb" # either Coulomb or Hardshell or None
radius =0.0043

#only important for Metropolis hastings:

time_step = 0.05
diffusion_coeff = 0.5

detailed = True
wf_type = "vmc" 
seed = 142
alpha = 0.55