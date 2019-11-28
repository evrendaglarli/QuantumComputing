# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:04:44 2019

@author: Evren Dağlarlı
"""

import qiskit
import numpy as np
from qiskit import(QuantumCircuit,QuantumRegister,ClassicalRegister,execute,Aer)
from qiskit.visualization import plot_histogram
from qiskit import IBMQ
# MY_API_TOKEN = '10c9f8c082b4a92d552b9b27f33678b295cffd88dd81476b0dc6f1acac46316687c9b948c57b5ee34de862e9a982909ac44bcb3f6f7941cfb7a19b57efe704e7'
# IBMQ.save_account('MY_API_TOKEN')
IBMQ.load_account()

#######################
## System Design  #####
#######################
## Define a two-qubit quantum circuit
q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(q, c)
## Apply the quantum gates
circuit.h(q[0])
circuit.cx(q[0], q[1])
## Finish off with the measurements
circuit.measure(q, c)
## Draw the circuit
%matplotlib inline
circuit.draw(output="mpl")

#######################
## Run on Simulator ###
#######################
## First, simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend=simulator, shots=1024)
result = job.result()
## Then, plot a histogram of the results
counts = result.get_counts(circuit)
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)

############################
## Run on Quantum Device ###
############################
# Next, find the least-busy IBM device
from qiskit.providers.ibmq import least_busy
lb_device = least_busy(IBMQ.backends())
# And run the circuit on that device
job = execute(circuit, backend=lb_device, shots=1024)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
result = job.result()
# Finally, plot a histogram of the results
counts = result.get_counts(circuit)
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)
