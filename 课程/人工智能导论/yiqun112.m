 % 定义函数 
 fitnessfcn = @(x) 20 + x(1).^2 + x(2).^2 - 10.*(cos(2.*pi.*x(1))+cos(2.*pi.*x(2))); 
 % 定义x和y的范围
 x = linspace(-5, 5); y = linspace(-5, 5); 
 % 计算截面
 [X, Y] = meshgrid(x, y);
 Z = zeros(length(y), length(x));
 for i = 1:length(x) 
     for j = 1:length(y) 
         Z(j, i) = fitnessfcn([x(i), y(j)]);
     end
 end
 % 绘制截面图
 contourf(X, Y, Z, 100, 'LineStyle', 'none') 
 colorbar 
 xlabel('x') 
 ylabel('y') 
 title('Fitness Function Contour Plot')