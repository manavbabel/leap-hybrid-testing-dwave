# function to solve QUBOs with D-Wave

from dimod import BinaryQuadraticModel, ExactSolver
from dwave.samplers import SimulatedAnnealingSampler
from dwave.system import LeapHybridSampler

def solve_qubo_dwave(linear_terms, quadratic_terms, method):
    # Takes
    # * linear_terms: dict {"x0":2,...}
    # * quadratic terms: dict {("x0","x1"):-3,...}
    # * method: str, as below
    # Returns a dict of the optimal result {"x0":0,...}

    # initialises the QUBO
    qubo = BinaryQuadraticModel(linear_terms, quadratic_terms, "BINARY")

    if method == "exact":
        # brute-force the qubo (only up to 18 vars)
        result = ExactSolver().sample(qubo)

    elif method == "simulated-annealing":
        # solve by simulated annealing
        result = SimulatedAnnealingSampler().sample(qubo, num_reads=200, randomise_order=True)
    
    elif method == "leap-hybrid":
        # solve using Leap hybrid solver
        # this is untested
        result = LeapHybridSampler().sample(qubo)

    else:
        print("ERROR: method "+method+" is unrecognised.")
        quit()

    return result.first.sample, result.first.energy
