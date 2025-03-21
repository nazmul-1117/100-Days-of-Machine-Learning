# Day 067 | Lasso Regression Mathematical Part


##  Mathematical Prove
Loss function for Linear Regression
- Loss Function L = $\sum_{i=1}^{n} (y_i-\hat{y_i})^2$
- $\hat{y_i} = mx_i - c$
- c = $\bar{y} - m \bar{x}$

<!-- - $\frac {δL}{δ\beta_0}$ = $\frac{1}{m}$ $[2*(y_1-\hat{y_1})(-1) + 2(y_2-\hat{y_2})(-1)]$ -->

Loss function for Lasso Regression
- Loss Function L = $\sum_{i=1}^{n} (y_i-\hat{y_i})^2 + 2\lambda |m|$ [`2` for simplyfy the quation]
- Loss Function L = $\sum_{i=1}^{n} (y_i - m x_i - c)^2 + 2\lambda |m|$
- Loss Function L = $\sum_{i=1}^{n} (y_i - m x_i - \bar{y} - m \bar{x})^2 + 2\lambda |m|$

> Here `|m|` is not differentiable function. so break |m| into 3 part<br>
> `m > 0`, |m| = m<br>
> `m = 0`, |m| = 0<br>
> `m < 0`, |m| = -m<br>

Derivatives this with respect to `m`
- L = $\sum_{i=1}^{n} (y_i - m x_i - \bar{y} + m \bar{x})^2 + \lambda |m|$
- L = $\sum_{i=1}^{n} (y_i - m x_i - \bar{y} + m \bar{x})^2 + \lambda m$
- $\frac {δL}{δm}$ = $2\sum(y_i - m x_i - \bar{y} + m \bar{x})(-x_i + \bar{x}) + 2\lambda$
- $\frac {δL}{δm}$ = $-2\sum(y_i - m x_i - \bar{y} + m \bar{x})(x_i - \bar{x}) + 2\lambda$

Now this equation will be `0` for find the `minima` slop
- $-2\sum(y_i - m x_i - \bar{y} + m \bar{x})(x_i - \bar{x}) + 2\lambda$ = $0$
- $-\sum(y_i - m x_i - \bar{y} + m \bar{x})(x_i - \bar{x}) + \lambda$ = $0$
- $\lambda -\sum(y_ - m x_i - \bar{y} + m \bar{x})(x_i - \bar{x})$ = $0$

- $\lambda -\sum[(y_i- \bar{y}) + m (x_i - \bar{x})](x_i - \bar{x})$ = $0$
- $\lambda -\sum[(y_i- \bar{y})(x_i - \bar{x}) + m (x_i - \bar{x})^2]$ = $0$
- $\lambda -\sum(y_i- \bar{y})(x_i - \bar{x}) +\sum m (x_i - \bar{x})^2$ = $0$
- $\sum m (x_i - \bar{x})^2$ = $\sum(y_i- \bar{y})(x_i - \bar{x})-\lambda$


- <span style="color:#54ff82"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})-\lambda}{(x_i - \bar{x})^2}$ </span>

<!-- - <span style="color:#f654ff"> $m ∝ \frac{1}{X}$ </span> -->

### When , M>0
- <span style="color:#4287f5"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})-\lambda}{(x_i - \bar{x})^2}$ </span>
  
### When , M=0
- <span style="color:#8ce8fa"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})}{(x_i - \bar{x})^2}$ </span>

### When , M<0
- <span style="color:#9ffa0c"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})+\lambda}{(x_i - \bar{x})^2}$ </span>

## Ridge vs Lasso Regression
- Ridge Regression
- - <span style="color:#54ff82"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})-\lambda}{(x_i - \bar{x})^2}$ </span>
> if $\sum(y_i- \bar{y})(x_i - \bar{x})$ = $\lambda$ then `m` is `0(Zero)` <br>
> if $\sum(y_i- \bar{y})(x_i - \bar{x})$ < $\lambda$ then `m` is `Negative (-m))` which is impossible<br>
> it can be `Zero(0)`

- Lasso Regression
> - <span style="color:#54ff82"> $m$ = $\frac{\sum(y_i- \bar{y})(x_i - \bar{x})}{\sum (x_i - \bar{x})^2 + \lambda }$ </span><br>
> 
> It cannot be `Zero(0)`<br>

## Images
![image1](assets/1.jpg)
![image2](assets/2.png)