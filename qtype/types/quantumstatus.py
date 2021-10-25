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
from qtype.errors.quantumstatusexception import QuantumStatusException


class QuantumStatus:

    def __init__(self, status=None):
        if type(status) == list:
            self.status = status
        elif type(status) == int:
            self.status = self.transformToStatusMatrix(status)
        else:
            raise QuantumStatusException

    def transformToStatusMatrix(self, status: int):
        status_matrix = []
        binary_representation = format(status, "b")
        for bit in binary_representation:
            status_matrix.append(int(bit))

        return status_matrix
