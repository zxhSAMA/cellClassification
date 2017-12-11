clear;clc;
syms b1 b2 k1 k2 d1 d2 gamma x y;

dxdt=(b1*x)/(k1+x+gamma*y)-d1*x==0;
dydt=(b2*x)/(k2+x)-d2*y==0;

sol=solve(dxdt,dydt,x,y);
xsol=sol.x;
ysol=sol.y;

diff(dxdt,x)
diff(dxdt,y)
