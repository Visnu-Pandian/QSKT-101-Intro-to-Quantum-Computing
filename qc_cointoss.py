#!/usr/bin/env python

# Use "python qc_cointoss.py" from your cmd line to run this file.
# Install requirements using "pip install -r requirements.txt"

from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import os, shutil

# Uncomment if facing stdout text formatting issues.
""" 
# Adjust system text and print formatting
original_stdout = sys.stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 
"""

# Set number of simulations
SIM = 10000

# Cleaning image directory
images = "qasm_images"
if not os.path.exists(images):
	os.makedirs(images)
else:
	for file in os.scandir(images):
		if file.is_file() or file.is_symlink():
			os.unlink(file.path)
		elif file.is_dir():
			shutil.rmtree(file.path)

print("\n=====================================")
print("\tQuantum Coin Toss Demo")
print("=====================================\n")

# 1. Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

print("\nOur initial circuit:")
print(qc.draw(output='text'))

# 2. Apply Hadamard gate to push qubit 0 into superposition
qc.h(0)

print("Circuit after adding H-gate:")
print(qc.draw(output='text'))
print("The qubit is now akin to a coin spinning in the air.")

# 3. Measure the qubit to see the result
qc.measure(0, 0)

print("\nFinal circuit: ")
print(qc.draw(output='text'))

try:
	qc.draw('mpl')
	plt.title("Final Quantum Circuit")
	plt.savefig("qasm_images/final_circuit.png")
	print(f"Circuit saved to: {images}/...")
	plt.close
except:
	print("Matplotlib visualization not available!")

# 4. Run the experiment on a quantum simulator
simulator = AerSimulator()

print(f"\nRunning simulation {SIM} times...\n")
circuit = transpile(qc, simulator)
job = simulator.run(circuit, shots=SIM)
result = job.result().get_counts()

print("Simulation complete!")    
print(f"Results: {result}")

try: 
	plot_histogram(result)
	plt.title(f"Results of {SIM} Quantum Coin Tosses")
	plt.savefig("qasm_images/simulation_results.png")
	print(f"Results saved to: {images}/...")
	plt.close
except:
	print("Matplotlib visualization not available!")

## Uncomment if facing stdout text formatting issues.
"""
# Restore stdout settings
sys.stdout = original_stdout
"""
