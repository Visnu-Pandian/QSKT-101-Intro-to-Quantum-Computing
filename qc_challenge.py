#!/usr/bin/env python

from qiskit import QuantumCircuit
from qc_unit_test import test_one_qubit_circuit, test_two_qubit_circuit
import sys, io

# Adjust system text and print formatting
original_stdout = sys.stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_custom_circuit():
	f"""
	YOUR TASK: Create a circuit that resets any qubit state to |0> (|00> in case of two-qubit system).
	
	Available gates:
	- qc.x(0) # Pauli-X gate (bit flip)
	- qc.h(0) # Hadamard gate (creates superposition)
	- qc.id(0) # Identity gate (does nothing)
	
	Available conditional statements:
	- with qc ...
	- qc.if_test((...))
	
	Test states:
 
	One-qubit
	- |0>
	- |1>
	- |H>
 
	Two-qubit
	- |00>
 	- |01>
  	- |10>
   	- |11>
	- |0H>
	- |H0>     
	- |1H>
 	- |H1>
  	- |HH>
    
	Returns:
	qc: Your Quantum Circuit
	"""
 
	# One-qubit initializers
	qc = QuantumCircuit(1, 1)
	qc.measure(0, 0)
	
	# Two-qubit initializers
	# qc = QuantumCircuit(2, 2)
	# qc.measure(range(2), range(2))
 
	# ============ YOUR CODE HERE ==========
	# Try different gates to see what works!
	# ======================================
	
	return qc

# ======= MAIN =======
if __name__ == "__main__":
	
	print("\n===========================================")
	print("\tQuantum Coin Toss Challenge")
	print("===========================================\n")
	
	qc = create_custom_circuit()
 
	# Uncomment whichever test you want to run.
	test_one_qubit_circuit(qc)
	# test_two_qubit_circuit(qc)
