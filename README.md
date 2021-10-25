# QType
Framework To Ease Operating with Quantum Computers

## Concept

```python

a = [Qubit() for i in range(15)]

for i in range(0, len(a)):
    a[i].hadamard().cnot(a[i-1])

for q in a:
    q.not()

q = Qubyte()

q.status = 12; # 00001100 same as initialise q0 =  0, q1 = 0, q2 = 1, q3 = 1, q4 = 0, q5 = 0 … q7 = 0

q.not(); # 11110011 same as apply not to every single qubit individually

q.hadamard(); # same as apply hadamard to every single qubit individually
q.h() # alias of hadamard

a, b, c = Qubit() #initialized to 0 by default

a.status = 1
b.status = a.not() # same as a a.cnot(b) (assign variable references is equivalent to entangle cubits itself.
a.status = 0 # because b is entangle, b is 1
a.status = 1 # due to entanglement, b is 0


a.status = [0, 1] #status matrix

a.status = [ 1 / sqrt(2), 1 / sqrt(2) ]

a.status = 0 #equivalent to a.status = [1, 0]
a.status = 1 #equivalent to a.status = [0, 1]

a.status.to_bloch().draw() #draw Bloch sphere of status

c = int(a) #that makes a to collapse to

c = a.read() #same, read makes a to collapse to

c = a.read(1000) #same, but with shots=1000

c = a.read()
d = a.read() #circuit is being executed again, makes a to collapse to again.







```