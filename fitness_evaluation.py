def is_result_correct(result, color):
    return all(element == color for element in result)

def calculate_fitness(hits, total_runs):
    return hits/total_runs