# This code is part of QType.
#
# Copyright 2021 Antonio Párraga Navarro
#
# This code is licensed under the MIT License. You may obtain
# a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at https://opensource.org/licenses/MIT.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
from qtype.errors.quantumindexoutofboundsexception import QuantumIndexOutOfBoundsException
from qtype.errors.quantumstatusexception import QuantumStatusException


class QuantumStatus:

    """Contains the status of 1 or more qubits

       self.status contains an array of individual qubits density matrixes

       e.g. [ [0, 1], [1, 0], [ 0.7071, 0.7071], ... ]

    """

    CONST_ZERO = [1, 0]
    CONST_ONE = [0, 1]

    def __init__(self, status=None, number_of_qubits=None):
        if type(status) == list and len(status) == 2:
            self.qubits_status = [status]
        elif type(status) == int:
            self.qubits_status = self.transform_to_qubits_density_matrixes(status)
        else:
            raise QuantumStatusException

        if number_of_qubits is not None:
            if number_of_qubits > len(self.qubits_status):
                for i in range(len(self.qubits_status), number_of_qubits):
                    self.qubits_status.insert(0, self.CONST_ZERO)
            elif number_of_qubits < len(self.qubits_status):
                raise QuantumIndexOutOfBoundsException

    def transform_to_qubits_density_matrixes(self, status: int):
        density_matrixes = []
        binary_representation = format(status, "b")
        for bit in binary_representation:
            if bit == "0":
                density_matrixes.append(self.CONST_ZERO)
            elif bit == "1":
                density_matrixes.append(self.CONST_ONE)
        return density_matrixes

    def qubits_count(self):
        return len(self.qubits_status)

    @property
    def qubits_status(self):
        return self.qubits_status