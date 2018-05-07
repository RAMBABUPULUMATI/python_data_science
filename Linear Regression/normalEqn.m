function [theta] = normalEqn(X, y)
%NORMALEQN Computes the closed-form solution to linear regression 
%   NORMALEQN(X,y) computes the closed-form solution to linear 
%   regression using the normal equations.

theta = zeros(size(X, 2), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the code to compute the closed form solution
%               to linear regression and put the result in theta.
%

% ---------------------- Sample Solution ----------------------


transpose_of_x = X';
prod_of_x_and_transpose =  transpose_of_x * X;
inverse_of_prod = inv(prod_of_x_and_transpose);
prod_of_y_and_transpose = transpose_of_x * y;
theta = inverse_of_prod * prod_of_y_and_transpose;

% -------------------------------------------------------------


% ============================================================

end
