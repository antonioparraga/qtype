# QType
Framework To Ease Operating with Quantum Computers

## Concept

```python

# define an array of 15 cubits:
a = [Qubit() for i in range(15)]

# Iterate every cubit, superposing and entangling each one with the previous one:
for i in range(1, len(a)):
    a[i].hadamard().cnot(a[i - 1])

# Apply a gate to every qubit within the array    
for q in a: 
    q.not()

# Definying a Qubyte, a sequence of eight qubits operated on as a unit by a quantum computer.
q = Qubyte()

# 00001100 same as initialise q0 =  0, q1 = 0, q2 = 1, q3 = 1, q4 = 0, q5 = 0 … q7 = 0
q.status = 12;

# 11110011 same as apply not to every single qubit individually
q.not();

q.hadamard();  # same as apply hadamard to every single qubit individually
q.h()  # alias of hadamard

# define 3 qubits a, b and c (they are initialized to 0 by default)
a, b, c = Qubit()

a.status = 1  # setting the status of first qubit to 1
b.status = a.not()  # same as a a.cnot(b) (assign variable references is equivalent to entangle cubits themselve)

# initialize the qubit to 1 by setting the status matrix
a.status = [0, 1]  # density matrix

# superposing the cubit by setting its density matrix:
a.status = [1 / sqrt(2), 1 / sqrt(2)]

a.status = 0  # equivalent to a.status = [1, 0]
a.status = 1  # equivalent to a.status = [0, 1]

a.status.to_bloch().draw()  # draw Bloch sphere of status

c = int(a)  # that makes a to collapse to

c = a.read()  # same, read makes a to collapse to

c = a.read(1000)  # same, but with shots=1000

c = a.read()
d = a.read()  # circuit is being executed again, makes a to collapse to again.







```