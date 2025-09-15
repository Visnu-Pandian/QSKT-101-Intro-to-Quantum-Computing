# ================================
# 			DO NOT EDIT
# ================================

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Set number of simulations
SIM = 100

def test_one_qubit_circuit(your_circuit: QuantumCircuit, check="0"):
	"""
	Test the student's circuit against multiple initial states.
	The value qubits should be set to is represented by check.
	"""
	
	print(f"\nRunning test for qubit |{check}> setter...\n")
	
	simulator = AerSimulator()

	# Initialize test cases
	test_cases = [
		("|0>", QuantumCircuit(1, 1)),
		("|1>", QuantumCircuit(1, 1)),
		("|H>", QuantumCircuit(1, 1))]
	
	test_cases[1][1].x(0) # |1>
	test_cases[2][1].h(0) # Superposition
	
	# Add measurements to all circuits
	for _, circuit in test_cases:
		circuit.measure(0, 0)
	
	# Show students their circuits
	print_circuit(your_circuit, "Your circuit:")

	# Create completed circuits
	success = True
	for test_name, test_circuit in test_cases:
		student_circuit = your_circuit
		
		combined_circuit = test_circuit.copy()
		combined_circuit = combined_circuit.compose(student_circuit, qubits=[0])
		
		print_circuit(combined_circuit, "Testing circuit...")
		
		combined_circuit.measure(0, 0)
		
		# Run simulation
		compiled_circuit = transpile(combined_circuit, simulator)
		job = simulator.run(compiled_circuit, shots=SIM)
		results = job.result().get_counts()
		
		if results.get(check, 0) == SIM:
			print(f"\n{test_name} PASSED | results: {results}")
		else:
			print(f"\n{test_name} FAILED | results: {results}")
			success = False
   
	return_status(success)

def test_two_qubit_circuit(your_circuit: QuantumCircuit, check="00"):
	"""
	Test the student's circuit against multiple initial states.
	The value qubits should be set to is represented by check.
	"""

	print(f"\nRunning test for qubit |{check}> setter...\n")

	simulator = AerSimulator()

	# Initialize test cases
	test_cases = [
		("|00>", QuantumCircuit(2, 2)), # 0
		("|01>", QuantumCircuit(2, 2)), # 1
  		("|10>", QuantumCircuit(2, 2)), # 2
  		("|11>", QuantumCircuit(2, 2)), # 3
		("|H0>", QuantumCircuit(2, 2)), # 4
		("|H1>", QuantumCircuit(2, 2)), # 5
	 	("|0H>", QuantumCircuit(2, 2)), # 6
	 	("|1H>", QuantumCircuit(2, 2)), # 7
		("|HH>", QuantumCircuit(2, 2))] # 8
	
	# |00> exists by default
	test_cases[1][1].x(1) # |01>
	test_cases[2][1].x(0) # |10>
	test_cases[3][1].x([0, 1]) # |11>
	test_cases[4][1].h(0) # |H0>
	test_cases[5][1].h(0) # |HX>
	test_cases[5][1].x(1) # |H1>
	test_cases[6][1].h(1) # |0H>
	test_cases[7][1].x(0) # |1X>
	test_cases[7][1].h(1) # |1H>
	test_cases[8][1].h([0, 1]) # |HH>
 
	# Adding measurement to all circuits
	for _, circuit in test_cases:
		circuit.measure(range(2), range(2))
	
	# Show students their circuit
	print_circuit(your_circuit, "Your circuit:")
 
	# Create completed circuit
	success = True
	for test_name, test_circuit in test_cases:
		combined_circuit = test_circuit.copy()
		combined_circuit = combined_circuit.compose(your_circuit, qubits=[0, 1])
  
		print_circuit(combined_circuit, "Testing circuit...")
  
		combined_circuit.measure(range(2), range(2))
  
		# Run simulation
		compiled_circuit = transpile(combined_circuit, simulator)
		job = simulator.run(compiled_circuit, shots=SIM)
		results = job.result().get_counts()
  
		if results.get(check, 0) == SIM:
			print(f"\n{test_name} PASSED | results: {results}")
		else:
			print(f"\n{test_name} FAILED | results: {results}")
			success = False
   
	return_status(success)

def return_status(status: bool):
    
    if status:
        print(f"\nCongratulations! You circuit works for all cases!")
    else:
        print(f"\nKeep trying! Hint: Consider which gates help flip qubit states.")
    
    return True

def print_circuit(qc: QuantumCircuit, msg: str):
	"""
	Helper function to print the student's circuit
	"""
	print(f"\n{msg}")
	print(qc.draw(output='text'))
	return qc
