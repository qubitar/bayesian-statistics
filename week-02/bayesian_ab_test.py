import numpy as np

rng = np.random.default_rng(42)  # Create a random number generator with a fixed seed for reproducibility
N=1000000

A = rng.beta(101, 901, size=N)  # Generate N samples from a Beta distribution with parameters alpha=2 and beta=5
B =rng.beta(121,881,size=N)  # Generate N samples from a Beta distribution with parameters alpha=3 and beta=7

delta=B-A
relative_lift= delta/A

prob_b_better = np.mean(delta>0)
credible_interval = np.percentile(delta, [2.5, 97.5])


#Expected regret per visitor
regret_choose_B= np.mean(np.maximum(B-A,0))
regret_choose_A= np.mean(np.maximum(A-B,0))

#Regret per 100000 visitors
print(regret_choose_B*100000)
print(regret_choose_A*100000)

