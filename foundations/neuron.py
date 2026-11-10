import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        z=np.dot(w,x)+b
        # sigmoid of z activation
        if activation=='sigmoid':
            y=1/(1+np.exp(-z))
        # relu activation
        elif activation=="relu":
            y=max(0,z)
        else:
            y=z
        return float(np.round(y,5))
