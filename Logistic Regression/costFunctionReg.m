function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


prediction = X * theta;
%product of X with theta
% hypothesis using sigmoid function 
hypothesis = sigmoid(prediction);

first = -(y .* log(hypothesis));
%first term of J theta
diff = 1 - hypothesis;
second = (( 1 - y) .* log( diff ));
%second term of J theta

reg_param = ((sum(theta(2:size(theta,1),1).^2))*(lambda/(m*2)));

J = (((sum(first-second))/m)+ reg_param);


tranpose = X';
gra_diff = hypothesis - y;

gra_prod = tranpose*gra_diff;
alpha = 1;

grad_param = zeros(size(theta,1),1);
grad_param(1,1) = theta(1,1);
grad_param(2:size(grad_param,1),1) = (theta((2:size(theta,1)),1).*(lambda/m));

grad = (alpha*(gra_prod/m));
 grad(2:size(grad,1),1) = grad(2:size(grad,1),1)+grad_param(2:size(grad_param,1),1);




% =============================================================

end
