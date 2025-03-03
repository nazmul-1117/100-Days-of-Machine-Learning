# Day 051 | Simple Linear Regression | Mathmetically find (m, c) | Custume Regression Algorithm
We can calculate (M, C) using 2 ways
1. Closed form (Direct math formula)
   1. Method: OLS (`LinearRegression`)
2. Non-Closed form (assumption)
   1. Gradiant Descent (`SGDRegression`)

# Error calculate
![image](assets/3.jpg)
E = ∑ d<sub>i</sub><sup>2</sup></br>
- Here d is basically y-y<sup>^</sup>
  - Here y is `should be` point
  - y <sup>^</sup> is `Prdicted/Estimate` point

E = ∑ (y-y<sup>^</sup>)<sup>2</sup></br>
- Here, y<sup>^</sup> is Prdicted point
  - y<sup>^</sup> = mx+c

So E = ∑ (y-mx+c)<sup>2</sup></br>

When C=0(constrant)</br>
E = ∑ (y-mx)<sup>2</sup></br>
![image](assets/parabola.png)
Here, X-axis = X, y-axis = E

Again, When m=1
E = ∑ (y-x+c)<sup>2</sup></br
![image](assets/parabola.png)>
Here, X-axis = X, y-axis = E

**Draw 3D curve**
![image](assets/lr01.jpg)
Here,
- Low(Blue) point is Minimum Error
- High(Red) point is maximum Error

## From This curve and Equation apply Pertial Differentiation
In mathematics, "maxima and minima" refer to the highest and lowest points of a function, respectively. These points are also known as extrema.
![image](assets/mx1.webp)
![image](assets/mx2.webp)
![image](assets/mx3.png)

**Equation**
Pertial Derivatives: f(x, y)
- ∂f/∂x
- ∂f/∂y

In my case,</br>
- f = E
- x = m
- y = c

### Partial Differentiation with respect to `c`
- ∂E/∂c = ∂/∂x &sum;(y-mx+c)<sup>2</sup> = 0
-  &sum; 2(y-mx+c)(-1) = 0
-  &sum; -2(y-mx+c) = 0
-  &sum; y-mx+c = 0 
-  &sum;y/n - &sum;mx/n + &sum;c/n = 0 
-  y&#x304; - mx&#x304; + nc/n = 0
-  y&#x304; - mx&#x304; + c = 0
- **<span style="color:#FF5722">c = y&#x304; - mx&#x304; (ans)**</span>

Put this `c` value in `E`
- E = ∑ (y-mx+c)<sup>2</sup></br>
- E = ∑ (y-mx-y&#x304; - mx&#x304;)<sup>2</sup></br>

### Partial Differentiation with respect to `m`
- ∂E/∂c = ∂/∂x ∑ (y-mx-y&#x304; - mx&#x304;)<sup>2</sup> = 0
- ∑ 2(y-mx-y&#x304; - mx&#x304;)(-x + x&#x304;) = 0
- ∑ -2(y-mx-y&#x304; - mx&#x304;)(x - x&#x304;) = 0
- ∑ (y-mx-y&#x304; - mx&#x304;)(x - x&#x304;) = 0
- ∑ [ (y-y&#x304;) -m(x - x&#x304;) ] (x - x&#x304;) = 0
- ∑ (y-y&#x304;)(x - x&#x304;) - m(x - x&#x304;)<sup>2</sup> = 0
- ∑ m(x - x&#x304;)<sup>2</sup> = ∑ (y-y&#x304;)(x - x&#x304;) 
- **<span style="color:#FF5722">m = ∑ (y-y&#x304;)(x - x&#x304;)/∑ (x - x&#x304;)<sup>2</sup> (ans)**</span>


**Here**,
  - `X` is Features(Input) (X<sub>1</sub>, X<sub>2</sub> ... X<sub>n</sub>)
  - `Y` is Label(Output) (Y<sub>1</sub>, Y<sub>2</sub> ... Y<sub>n</sub>)
  - `M` is constrant `slop`.
  - `C` is constrant `intercept`.

