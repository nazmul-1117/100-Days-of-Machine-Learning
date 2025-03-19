# Day 64 | Ridge Regression Gradient Descent
from previous lecture we know the derivatives function:
- $\frac {δL}{δ\omega}$ = $2X^TXW - 2X^TY + 2\lambda W$
- $\frac {δL}{δ\omega}$ = $X^TXW - X^TY + \lambda W$

for graadient descent update the `W`'s value

  -  W = $\begin{bmatrix}\omega_0 &\omega_1 &\omega_2 &... &\omega_n\\ 0 &1 &1 &... &1\end{bmatrix}$
  - <span style="color:#e50000">$W$ = $W-\eta\frac {δL}{δ\omega}$ </span>


