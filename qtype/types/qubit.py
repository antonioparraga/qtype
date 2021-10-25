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
from qtype.types.qtype import QType
from qtype.types.quantumstatus import QuantumStatus


class Qubit(QType):

    def __init__(self, status=None):
        if status is None:
            self.status = QuantumStatus(0)
        else:
            super(status)
