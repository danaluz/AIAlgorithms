function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

g = 1 ./ (1 + exp(-z));

% a./b perform right-array division by dividing each element of a by the corresponding element of b.
% If inputs a and b are not the same size, one of them must be a scalar value. 

% =============================================================

end
