# QSKT 101: Intro to Quantum Computing

This project is part of an introductory lecture on Quantum Computing.

The project seeks to explore the practical uses of Quantum Computing by integrating it into a familiar programming language such as Python. This is done via [IBM's Qiskit library](https://www.ibm.com/quantum/qiskit).

This project is maintained by [@Visnu-Pandian](@Visnu-Pandian). Please contact me via email for any inquiries, issues, or additional material regarding this project.

Project contact email: <visnupandian1@gmail.com>

## Contents

1. [Installation](#installation)
2. [Lecture slides](#lecture-slides)
3. [Cointoss experiment](#coin-toss-experiment)
4. [Biased coin challenge](#biased-coin-challenge)
5. [Solutions](#solutions)

## Installation

### Using requirements.txt

```bash
pip install -r requirements.txt
```

### Using pyproject.toml

```bash
pip install .
```

## Lecture Slides

This lecture was originally designed for members of [CyberWVU](https://wvuengage.wvu.edu/organization/cyberwvu). It was designed to span one hour with the activity and challenge included.

The lecture slides accompanying this project are present in the [docs](docs/QSKT%20101_%20Intro%20to%20Quantum%20Computing.pptx) folder.

## Coin toss experiment

The goal of [this program](/qc_cointoss.py) is to show how Qiskit can be used in Python. This is done via a coin-toss simulation.

Run this file

```terminal
C:\foo@bar\QSKT-101-Intro-to-Quantum-Computing>python qc_cointoss.py
```

Students are introduced to Quantum Circuits, measurement and Hadamard Gates. They are shown how quantum circuits are built and how they can be visualized in the terminal. Matplotlib is used to generate an image of the final circuit used for the experiment.

## Biased coin challenge

This [challenge](/qc_challenge.py) exists to give students a sandbox and test their understanding on applying logic gates using Qiskit.

Students should only attempt this after understanding the [coin-toss demo](#coin-toss-experiment) and familiarizing themselves with the basics of [IBM's Qiskit library](https://www.ibm.com/quantum/qiskit).

Run this file

```terminal
C:\foo@bar\QSKT-101-Intro-to-Quantum-Computing>python qc_challenge.py
```

The goal of this challenge is to create a circuit that takes any single-qubit input and converts it into a |0> output. Alternatively, changing the TEST parameter to '1' changes the target output to |1>.

## Solutions

This [text file](solutions/solutions.txt) contains the answers to the [biased coin challenge](#biased-coin-challenge).

Students are advised to only open this file after attempting to solve the challenge by themselves and discussing it with peers.
