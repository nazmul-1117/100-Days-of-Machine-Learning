# Day 74 | Logistic Regression | Gradient Descent
- Rows=m, Columns=n
- For each column their has `w+1` coefficiant

## Output Prediction
- $\hat{y_1}$ = $\sigma (w_0 + w_1 x_{11} + w_1 x_{12}) + ... + w_n x_{1n}$
- $\hat{y_2}$ = $\sigma (w_0 + w_1 x_{21} + w_2 x_{22}) + ... + w_n x_{2n}$
- ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...
- $\hat{y_m}$ = $\sigma (w_0 + w_1 x_{m1} + w_2 x_{m2}) + ... + w_n x_{mn}$

Build a Matrix form

- $\hat{Y}$ = $\begin{bmatrix}
    \hat{y_1}\\\
    \hat{y_2}\\\
    \hat{y_3}\\\
    ...\\\
    \hat{y_m}
\end{bmatrix}$ 

<!-- matrix build -->
- $\begin{bmatrix}
    \hat{y_1}\\\
    \hat{y_2}\\\
    \hat{y_3}\\\
    ...\\\
    \hat{y_m}
\end{bmatrix}$
=
$\begin{bmatrix}
 \sigma (w_0 + w_1 x_{11} + w_2 x_{12}) + ... + w_n x_{1n} \\\ 
 \sigma (w_0 + w_1 x_{21} + w_2 x_{22}) + ... + w_n x_{2n} \\\ 
 \sigma (w_0 + w_1 x_{31} + w_2 x_{32}) + ... + w_n x_{3n} \\\ 
 \sigma (w_0 + w_1 x_{..1} + w_2 x_{...2}) + ... + w_n x_{..n} \\\ 
 \sigma (w_0 + w_1 x_{m1} + w_2 x_{m2}) + ... + w_n x_{mn}
 \end{bmatrix}$
 - =
$\sigma \begin{bmatrix}
 (1 + x_{11} +  x_{12}) + ... + x_{1n} \\\ 
 (1 + x_{21} +  x_{22}) + ... + x_{2n} \\\ 
 (1 + x_{31} +  x_{32}) + ... + x_{3n} \\\ 
 (1 + x_{..1} + 2 x_{...2}) + ... x_n x_{..n} \\\ 
 (1 + x_{m1} +  x_{m2}) + ... + x_{mn}
 \end{bmatrix}$
 $\begin{bmatrix}
    w_0\\\
    w_1\\\
    w_2\\\
    ...\\\
    w_n
 \end{bmatrix}$

 - Matrix form, $\hat{Y} = \sigma(XW)$
 - Where,
   - X = $\begin{bmatrix}
 (1 + x_{11} +  x_{12}) + ... + x_{1n} \\\ 
 (1 + x_{21} +  x_{22}) + ... + x_{2n} \\\ 
 (1 + x_{31} +  x_{32}) + ... + x_{3n} \\\ 
 (1 + x_{..1} + 2 x_{...2}) + ... x_n x_{..n} \\\ 
 (1 + x_{m1} +  x_{m2}) + ... + x_{mn}
 \end{bmatrix}$
    
    -  $\hat{Y}$ = 
    $\begin{bmatrix}
    \hat{y_1}\\\
    \hat{y_2}\\\
    \hat{y_3}\\\
    ...\\\
    \hat{y_m}
\end{bmatrix}$
    
    - $W$ = 
    $\begin{bmatrix}
    w_0\\\
    w_1\\\
    w_2\\\
    ...\\\
    w_n
 \end{bmatrix}$

 ## Loss Function
 - $\displaystyle L=-\frac{1}{m} \sum y_i \log(\hat{y_i}) + (1-y_i) \log (1-\hat{y_I})$
 - $\displaystyle \frac{d}{dx} \sigma(x)$ $= \displaystyle \sigma(x) * [1- \sigma(x)]$

### Convert this equation into Matrix form
- $\sum y_i \log(\hat{y_i})$ = $y_1 \log(\hat{y_1}) + y_2 \log(\hat{y_2}) + y_3 \log(\hat{y_3}) + ... + y_m \log(\hat{y_m})$
- $\begin{bmatrix}
    y_1 & y_2 & y_3 & ... & y_m
\end{bmatrix}$
$\begin{bmatrix}
     \log(\hat{y_1})\\\
     \log(\hat{y_2})\\\
     \log(\hat{y_3})\\\
     .......... \\\
     \log(\hat{y_m})\\\
\end{bmatrix}$

- $\begin{bmatrix}
    y_1 & y_2 & y_3 & ... & y_m
\end{bmatrix}$
$\log \begin{bmatrix}
     \hat{y_1}\\\
     \hat{y_2}\\\
     \hat{y_3}\\\
     ... \\\
     \hat{y_m}\\\
\end{bmatrix}$
- $Y\log \hat{Y}$
- $Y\log (\sigma(WX))$
- Build the equation
- $\displaystyle L=-\frac{1}{m} [Y \log(\hat{Y}) + (1-Y) \log (1-\hat{Y})]$
- Where
  - $\hat{Y} = \sigma(WX)$

### Derivatives this equation
<span style = "color:red">$\displaystyle L=-\frac{1}{m} [Y \log(\hat{Y}) + (1-Y) \log (1-\hat{Y})]$<span>
- Assume
  - $T = Y \log(\hat{Y})$
  - $V = (1-Y) \log (1-\hat{Y})$
  - $L = \displaystyle-\frac{1}{m}[T+V]$

1. Now differentiation `T` with respect to `W`
   - $\displaystyle \frac{dT}{dW} = Y \log \hat{Y}$
   - $\displaystyle =\frac{Y}{\hat{Y}} \sigma(WX)[1-\sigma(WX)]X$
   - $\displaystyle =\frac{Y}{\hat{Y}} \hat{Y}[1-\hat{Y}]X$
   - $\displaystyle = Y (1-\hat{Y})X$

2.  Now differentiation `V` with respect to `W`
   - $\displaystyle V = (1-Y) \log (1-\hat{Y})$
   - $\displaystyle \frac{dV}{dW} = \frac{1-Y}{1-\hat{Y}} \sigma(WX) [1-\Sigma(WX)](-X)$
   - $\displaystyle = -\frac{1-Y}{1-\hat{Y}} \hat{Y} [1-\hat{Y}]X$
   - $\displaystyle = -\hat{Y}(1-Y)X$

### Build Final Equation
- $L = \displaystyle-\frac{1}{m}[T+V]$
- $L = \displaystyle-\frac{1}{m}[Y (1-\hat{Y})X -\hat{Y}(1-Y)X]$
- $= \displaystyle-\frac{1}{m}[Y-Y\hat{Y} -\hat{Y}+Y\hat{Y}]X$
- $= \displaystyle-\frac{1}{m}[Y-\hat{Y}]X$

## Gradient Descent Equation for Logistic Regression
<span style="color:#54f07d">$\displaystyle \frac{\Delta L}{\Delta W} = -\frac{1}{m}[Y-\hat{Y}]X$</span>

- Apply:
    - $W = W - \eta \frac{\Delta L}{\Delta W}$ 
    - 
    - $\displaystyle W = W + \frac{\eta}{m} [Y-\hat{Y}]X$ 