clc;clear;
syms x y; 
z=(sin(x)+2*cos(y)).*sqrt(x.^2+y.^2);
E=simplify((diff(z,x)^2+diff(z,y)^2+1)^0.5);
ans=int(z*E,y,0,pi);
las=int(ans,x,0,pi);
v=int(las,z,0,z);

