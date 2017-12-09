原始模型

$$\frac{dx}{dt}=a_1+\frac{b_1x^n}{K_1^n+x^n+({\gamma}y)^p}-d_1x$$

$$\frac{dy}{dt}=a_2+\frac{b_2x^m}{K_2^m+x^m}-d_2y$$

```mermaid
graph LR
	x-->x
	x--active-->y
	y-.repress.->x
```

简化一下，否则无法求出解析解

$$n=1;m=1;p=1$$

$$a_1=0;a_2=0$$

$$f(x,y)=\frac{b_1x}{K_1+x+({\gamma}y)}-d_1x$$

$$g(x,y)=\frac{b_2x}{K_2+x}-d_2y$$

先求一下稳定点

$$\frac{dx}{dt}=f(x,y)=0$$

$$\frac{dy}{dt}=f(x,y)=0$$

有三个稳定点$(x_k,y_k)$

$$(x_0,y_0)=(0,0)$$

$$(x_1,y_1)=(\frac{b_1-d_1K_1}{d_1}-\frac{b_1d_2-d_1d_2(K_1-K_2)}{2d_1d_2}+P,\frac{b_1d_2+b_2d_1\gamma-d_1d_2(K_1-K_2)}{2d_1d_2\gamma}-{\gamma}P)$$

$$(x_2,y_2)=(\frac{b_1-d_1K_1}{d_1}-\frac{b_1d_2-d_1d_2(K_1-K_2)}{2d_1d_2}-P,\frac{b_1d_2+b_2d_1\gamma-d_1d_2(K_1-K_2)}{2d_1d_2\gamma}+{\gamma}P)$$

其中

$$P=\frac{\sqrt{b_1^2d_2^2-2b_1b_2d_1d_2\gamma-2b_1d_1d_2^2(K_1-K_2)+b_2^2d_1^2\gamma^2+2b_2d_1^2d_2{\gamma}(K_1+K_2)+d_1^2d_2^2(K_1-K_2)^2}}{2d_1d_2}$$

在三个稳定点附近做泰勒展开，只保留一次项

$$f(x_k+{\delta}x,y_k+{\delta}y)=\frac{{\partial}f(x_k,y_k)}{{\partial}x}{\delta}x+\frac{{\partial}f(x_k,y_k)}{{\partial}y}{\delta}y$$

$$g(x_k+{\delta}x,y_k+{\delta}y)=\frac{{\partial}g(x_k,y_k)}{{\partial}x}{\delta}x+\frac{{\partial}g(x_k,y_k)}{{\partial}y}{\delta}y$$

$$\frac{{\partial}f(x_k,y_k)}{{\partial}x}=\frac{b_1}{(K_1+x+{\gamma}y)}-d_1-\frac{b_1x}{(K_1+x+{\gamma}y)^2}$$

$$\frac{{\partial}f(x_k,y_k)}{{\partial}y}=-\frac{b_1{\gamma}x}{(K_1+x+{\gamma}y)^2}$$

$$\frac{{\partial}g(x_k,y_k)}{{\partial}x}=\frac{b_2}{K_2+x}-\frac{b_2x}{(K_2+x)^2}$$

$$\frac{{\partial}g(x_k,y_k)}{{\partial}y}=-d_2$$

$$\left(\begin{matrix}f(x_k+{\delta}x,y_k+{\delta}y)\\g(x_k+{\delta}x,y_k+{\delta}y)\end{matrix}\right)=\left(\begin{matrix}\frac{{\partial}f(x_k,y_k)}{{\partial}x}&\frac{{\partial}f(x_k,y_k)}{{\partial}y}\\\frac{{\partial}g(x_k,y_k)}{{\partial}x}&\frac{{\partial}g(x_k,y_k)}{{\partial}y}\end{matrix}\right)\left(\begin{matrix}{\delta}x\\{\delta}y\end{matrix}\right)$$

$$J=\left(\begin{matrix}\frac{{\partial}f(x_k,y_k)}{{\partial}x}&\frac{{\partial}f(x_k,y_k)}{{\partial}y}\\\frac{{\partial}g(x_k,y_k)}{{\partial}x}&\frac{{\partial}g(x_k,y_k)}{{\partial}y}\end{matrix}\right)$$

求出特征根$\lambda$

$$\left|\begin{matrix}{\lambda}I-J\end{matrix}\right|=0$$

$$\left|\begin{matrix}{\lambda}-\frac{{\partial}f(x_k,y_k)}{{\partial}x}&-\frac{{\partial}f(x_k,y_k)}{{\partial}y}\\-\frac{{\partial}g(x_k,y_k)}{{\partial}x}&{\lambda}-\frac{{\partial}g(x_k,y_k)}{{\partial}y}\end{matrix}\right|=0$$

将三个稳定点带入含$\lambda$的二次方程，要求

$$Re\lambda\leq0$$

$$Im\lambda\neq0$$

