function [J, grad] = lrCostFunction(theta, X, y, lambda)
%LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
%regularization
%   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
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
%
% Hint: The computation of the cost function and gradients can be
%       efficiently vectorized. For example, consider the computation
%
%           sigmoid(X * theta)
%
%       Each row of the resulting matrix will contain the value of the
%       prediction for that example. You can make use of this to vectorize
%       the cost function and gradient computations. 
%
% Hint: When computing the gradient of the regularized cost function, 
%       there're many possible vectorized solutions, but one solution
%       looks like:
%           grad = (unregularized gradient for logistic regression)
%           temp = theta; 
%           temp(1) = 0;   % because we don't add anything for j = 0  
%           grad = grad + YOUR_CODE_HERE (using the temp variable)
%

prediction = X * theta;  %product of X with theta
hypothesis = sigmoid(prediction); % hypothesis using sigmoid function 

first = -(y .* log(hypothesis)); %first term of J theta
diff = 1 - hypothesis;
second = (( 1 - y) .* log( diff )); %second term of J theta

J_unreg = ((sum(first-second))/m); %unregularised cost funtion

reg_param = ((sum(theta(2:size(theta,1),1).^2))*(lambda/(m*2))); % calculating regularization parameter

J = J_unreg + reg_param; %adding regularization to the cost function


tranpose = X';  %computing transpose matrix for gradient of cost
gra_diff = hypothesis - y;

gra_prod = tranpose*gra_diff;
alpha = 1;

grad_param = zeros(size(theta,1),1); %use a temperory variable to calculate regularization parameter for gradient
grad_param(1,1) = theta(1,1);
grad_param(2:size(grad_param,1),1) = (theta((2:size(theta,1)),1).*(lambda/m)); 

grad = (alpha*(gra_prod/m)); % gradient with out regularization parameter

grad(2:size(grad,1),1) = grad(2:size(grad,1),1)+grad_param(2:size(grad_param,1),1);

% gradient with regularization parameter added


% =============================================================

grad = grad(:);

end
