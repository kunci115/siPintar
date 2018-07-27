import numpy as np


def forwardPass(inputs, weight, bias, activation='softmax'):
    w_sum = np.dot(inputs, weight) + bias

    if activation is 'relu':
        act = np.maximum(w_sum, 0)
        print(act)
    elif activation is 'softmax':
        act_exp = np.exp(w_sum)
        act_sum = np.sum(act_exp, axis=1, keepdims=True)
        act = act_exp/act_sum
    else:
    # Linear Activation f(x) = x
        act = w_sum

    return act


# Pre-Trained Weights & Biases after Training

W_H = np.array([[0.00192761, -0.78845304, 0.30310717, 0.44131625, 0.32792646, -0.02451803, 1.43445349, -1.12972116]])
b_H = np.array([-0.02657719, -1.15885878, -0.79183501, -0.33550513, -0.23438406, -0.25078532, 0.22305705, 0.80253315])

W_o = np.array([[-0.77540326], [0.5030424 ], [0.37374797], [-0.20287184], [-0.35956827], [-0.54576212], [1.04326093], [0.8857621]])
b_o = np.array([0.04351173])

# Initialize Input Data
inputs = np.array([[-2], [0], [2]])

#Output of Hidden Layer
h_out = forwardPass(inputs, W_H, b_H, 'softmax')

print('Hidden Layer Output (ReLU)')
print('================================')
print(h_out, "\n")

# Output of Output Layer
o_out = forwardPass(h_out, W_o, b_o, 'linear')

print('Output Layer Output (Linear)')
print('================================')
print(o_out, "\n")