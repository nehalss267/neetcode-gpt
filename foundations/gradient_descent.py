class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    
        x = init
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:   
        for i in range(iterations):
            grad = 2 * x
            x_new = x - learning_rate * grad
            x = x_new
        # Round final answer to 5 decimal places
        return round(x, 5)