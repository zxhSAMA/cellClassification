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

有三个稳定点$(x_k,y_k)$，在三个稳定点附近做泰勒展开，只保留一次项

$$f(x_k+{\delta}x,y_k+{\delta}y)=\frac{{\partial}f(x_k,y_k)}{{\partial}x}{\delta}x+\frac{{\partial}f(x_k,y_k)}{{\partial}y}{\delta}y$$

$$g(x_k+{\delta}x,y_k+{\delta}y)=\frac{{\partial}g(x_k,y_k)}{{\partial}x}{\delta}x+\frac{{\partial}g(x_k,y_k)}{{\partial}y}{\delta}y$$

$$\left(\begin{matrix}f(x_k+{\delta}x,y_k+{\delta}y)\\g(x_k+{\delta}x,y_k+{\delta}y)\end{matrix}\right)=\left(\begin{matrix}\frac{{\partial}f(x_k,y_k)}{{\partial}x}&\frac{{\partial}f(x_k,y_k)}{{\partial}y}\\\frac{{\partial}g(x_k,y_k)}{{\partial}x}&\frac{{\partial}g(x_k,y_k)}{{\partial}y}\end{matrix}\right)\left(\begin{matrix}{\delta}x\\{\delta}y\end{matrix}\right)$$

