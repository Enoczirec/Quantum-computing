"""Script for preparing the Bell state |\Phi^{+}> in Cirq. """

# Import the Cirq library
import cirq

# Get qubits and circuit
qreg = [cirq.LineQubit(x) for x in range(2)]
circ = cirq.Circuit()

print(f"Entrada")
xy = input()

# Add the Bell state preparation circuit
circ.append([cirq.H(qreg[0]), cirq.CNOT(qreg[0], qreg[1])])

if xy == "01":
    circ.append(cirq.X(qreg[1]))
elif xy == "10":
    circ.insert(0, cirq.X(qreg[0]))
elif xy == "11":
    circ.append(cirq.X(qreg[1]))
    circ.insert(0, cirq.X(qreg[0]))
else:
    print("Corriendo valor por default 00")


# Display the circuit
print("Circuit")


sim = cirq.Simulator()
results = sim.simulate(circ)
# Print Bell State
print(results)


circ.append([cirq.CNOT(qreg[0], qreg[1]), cirq.H(qreg[0])])

# Add measurements
circ.append(cirq.measure(*qreg, key="z"))

print(circ)

# Simulate the circuit

res = sim.run(circ, repetitions=100)

# Display the outcomes
print("\nMeasurements:")
print(res.histogram(key='z'))
