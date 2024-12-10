% ������Ӧ�Ⱥ���
fitnessfcn = @(x) -(20 + x(1).^2 + x(2).^2 - 10.*(cos(2.*pi.*x(1))+cos(2.*pi.*x(2))));

% ����PSO������
nvars = 2; % number of variables
lb = [-5, -5]; % lower bounds for each variable
ub = [5, 5]; % upper bounds for each variable
options = optimoptions('particleswarm','MaxIterations',100,'SwarmSize',50);

% ����PSO����
[x,fval] = particleswarm(fitnessfcn,nvars,lb,ub,options);

% Display the results
disp(['Minimum value found: ',num2str(fval)]);
disp(['x1: ',num2str(x(1))]);
disp(['x2: ',num2str(x(2))]);