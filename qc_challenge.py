#!/usr/bin/env python

from qiskit import QuantumCircuit
from qc_unit_test import test_circuit
import sys, io

# Adjust system text and print formatting
original_stdout = sys.stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 

# Test parameter. Edit to change the qubit value being tested for.
TEST='0'

def create_custom_circuit():
    f"""
    YOUR TASK: Create a circuit that resets any single-qubit state to |{TEST}>.
    
    Available gates:
    - qc.x(0) # Pauli-X gate (bit flip)
    - qc.h(0) # Hadamard gate (creates superposition)
    - qc.id(0) # Identity gate (does nothing)
    
    Available conditional statements:
    - with qc ...
    - qc.if_test((...))
    
    Test states:
    - |0>
    - |1>
    - |H>
    
    Returns:
    qc: Your Quantum Circuit
    """
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    
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
    test_circuit(qc, TEST)