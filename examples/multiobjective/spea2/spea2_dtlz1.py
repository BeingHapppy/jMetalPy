from jmetal.algorithm.multiobjective.spea2 import SPEA2
from jmetal.operator import SBXCrossover, PolynomialMutation
from jmetal.problem import DTLZ2
from jmetal.util.solution import read_solutions, print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == '__main__':
    problem = DTLZ2()
    problem.reference_front = read_solutions(filename='resources/reference_front/DTLZ2.3D.pf')

    max_evaluations = 20000
    algorithm = SPEA2(
        problem=problem,
        population_size=20,
        offspring_population_size=20,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max=max_evaluations)
    )

    algorithm.run()
    front = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.label)
    print_variables_to_file(front, 'VAR.'+ algorithm.label)

    print(f'Algorithm: ${algorithm.get_name()}')
    print(f'Problem: ${problem.get_name()}')
    print(f'Computing time: ${algorithm.total_computing_time}')
