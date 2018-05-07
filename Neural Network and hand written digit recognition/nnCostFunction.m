function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

%Adding ones(biased unit) to X
X = [ones(size(X,1),1), X];

% Naming input layer to a1 for ease and computing hypothesis
a1 = X;
prod1 = a1*Theta1';
a2 = sigmoid(prod1);
% Adding ones(biased unit) to a2
a2 = [ones(size(a2,1),1), a2];
prod2 = a2*Theta2';
hypothesis = sigmoid(prod2);
a3 = hypothesis;

% Vectorizing the labels for Y for cost computation
op = zeros(m, num_labels);
for i = 1:m
	for j = 1:num_labels
		if( j == y(i) )
			op(i,j) = 1;
			break;
		end
	end
end

% Cost computation J( Theta )
First_term = -( op .* log(hypothesis));
diff = ( 1 - op );
second_term = diff .* log( 1 - hypothesis );
J = sum(sum((First_term - second_term)))/m;


% Cost function J added with Regularization
First_Reg=(sum(sum(Theta1(:,2:size(Theta1,2)).^2))*lambda)/(2*m);
Second_Reg=(sum(sum(Theta2(:,2:size(Theta2,2)).^2))*lambda)/(2*m);
Reg = First_Reg + Second_Reg;

J = J + Reg;

%Computing back propagation for each example in the training set. 
%since step1 - step4 is computation and step1 is done above 
%We are starting with step2 

delta_3 = a3 - op;  %step2
delta_2 = ( delta_3 * Theta2 ) .* ( a2 .* ( 1 - a2)); %step3
delta_2 = delta_2(:,2:end);

% Now calculating Theta1_grad and Theta2_grad

Theta1_grad = (a1' * delta_2)'/m;
Theta2_grad = (a2' * delta_3)'/m;

% Now computing gradients w/ regularization

reg_sub_theta1 =  Theta1(:,2:end)*(lambda/m);
reg_sub_theta2 =  Theta2(:,2:end)*(lambda/m);

r
% ------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
