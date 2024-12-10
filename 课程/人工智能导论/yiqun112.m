 % ���庯�� 
 fitnessfcn = @(x) 20 + x(1).^2 + x(2).^2 - 10.*(cos(2.*pi.*x(1))+cos(2.*pi.*x(2))); 
 % ����x��y�ķ�Χ
 x = linspace(-5, 5); y = linspace(-5, 5); 
 % �������
 [X, Y] = meshgrid(x, y);
 Z = zeros(length(y), length(x));
 for i = 1:length(x) 
     for j = 1:length(y) 
         Z(j, i) = fitnessfcn([x(i), y(j)]);
     end
 end
 % ���ƽ���ͼ
 contourf(X, Y, Z, 100, 'LineStyle', 'none') 
 colorbar 
 xlabel('x') 
 ylabel('y') 
 title('Fitness Function Contour Plot')