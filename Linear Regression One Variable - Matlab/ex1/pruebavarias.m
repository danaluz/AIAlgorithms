data = load('ex1data1.txt');

X = data(:, 1); y = data(:, 2);
m = length(y); % number of training examples
theta = zeros(2, 1); % initialize fitting parameters

% Some gradient descent settings
iterations = 1500;
alpha = 0.01;
% Plot Data
% Note: You have to complete the code in plotData.m
plotData(X, y);
fprintf('Program paused. Press enter to continue.\n');
pause;

X = [ones(m, 1), data(:,1)]; % Add a column of ones to x

n=0;
for i=1:m
    n = n+(theta(1,1)+theta(2,1)*X(i,2)-y(i))^2;
end;    
fprintf('Value.\n %f',n);
pause;

J= (0.5*m)*n;
fprintf('Value.\n %f',J);
pause;
