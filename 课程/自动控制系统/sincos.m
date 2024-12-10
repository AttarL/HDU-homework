subplot(1,2,1);
x = linspace(0,2*pi);
y1 = sin(x);
plot(x,y1,'b')
hold on
scatter(x,y1,'r','o')
hold off

subplot(1,2,2); 
y2 = cos(x);
plot(x,y2)
hold on
scatter(x,y2,'b','*')
hold off

