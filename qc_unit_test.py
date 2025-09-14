from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import pylatexenc

# Set number of simulations
SIM = 100

def test_circuit(your_circuit: QuantumCircuit, check='0'):
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
    
    if success:
        print("\nCongratulations! Your circuit works for all cases!")
    else:
        print("\nKeep trying! Hint: Consider which gate flips the state of a qubit.")

    return success

def print_circuit(qc: QuantumCircuit, msg: str):
    """
    Helper function to print the student's circuit
    """
    print(f"\n{msg}")
    print(qc.draw(output='text'))
    return qc
