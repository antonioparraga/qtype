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
from qtype.types.quantumstatus import QuantumStatus


class QType:

    def __init__(self, status=None):
        if type(status) == QuantumStatus:
            self.status = status
        else:
            self.status = QuantumStatus(status)

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status

    def read(self):
        return self.collapse()

    def collapse(self):
        pass

    def __int__(self):
        return self.collapse()
