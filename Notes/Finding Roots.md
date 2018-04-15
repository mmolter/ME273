% Root Finding
% M. Molter
% 27 March 2018

# Introduction

In the simplest analytical case, 

$$a x^2 + b x + c = 0$$ 

...produces the roots... 

$$x=\frac{-b\pm\sqrt{b^2 - 4ac}}{2a}$$

We are essentially asking the question, "When does...,

$$ f(x) = 0 $$

Now it *is* possible to find roots graphically (i.e. where the function crosses the x--axis); however, it is difficult to find a precise solution. 

The numerical techniques we will now discuss are conceptually simply, but can by tricky to implement properly in code.

# Bracketing Methods
## Bisection Method
{
First, choose brackets

$$x_l = 4$$
$$x_u = 6$$

Now perform the test, "does the function changes signs within the bracket?", essentially,

$$f(x_u)f(x_l) < 0$$

If true, you can be certain if there is a root within the interval; however, if false, the interval can still contain a root.

Now approximate the root by **bisecting** the interval.

$$x_r=\frac{x_u + x_l}{2}$$

Now perform the bracket test between $x_l$ and $x_r$; and $x_u$ and $x_r$. Bisect the interval containing the root and continue.

## False Position Method

A faster way to approach the root is with the **false position method**. This uses a line between $x_u$ and $x_l$ and chooses the next $x_r$ where this line crosses zero.

Simplified:

$$x_r = x_u - \frac{f(x_u)(x_l-x_u)}{f(x_l)-f(x_u)}$$

The same bracket--checking conditions apply.

$$f(x_u)f(x_r) < 0$$
$$f(x_l)f(x_r) < 0$$

## Simple Fixed Point Iteration

The **simple fixed point iteration** method is a better technique when an understanding of the function behavior is not available. First rearrange $f(x)=0$ into the form $x=g(x)$. This can be done by simply adding $x$ to both sides.

$$f(x) + x = 0 + x = x$$

Now iterate according to,

$$x_{i+1}=g(x_i)$$

While watching the **approximate error**,

$$\varepsilon_a = \left| \frac{x_{i+1}-x_i}{x_i}\right|$$

If the error is getting smaller, the computation is converging on a root. If not, try a different initial point. 

As stated above, this method is not guaranteed to converge.

## Newton--Raphson Method

The **Newton--Raphson method** is similar to the simple fixed point iteration method, but uses the slope of the function (i.e. $f^\prime(x_i)$) to find the next location to iterate.

$$f^\prime(x_i)=\frac{f(x_i) - 0}{x_i - x_{i+1}}$$

Your next guess becomes,

$$x_{i+1}=x_i - \frac{f(x_i)}{f^\prime(x_i)}$$


