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
        self.status = status
        self.is_collapsed = False

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if type(status) == QuantumStatus:
            self._status = status
        else:
            self._status = QuantumStatus(status)

    def read(self):
        return self.collapse()

    def collapse(self):
        self.is_collapsed = True
        return self._status.collapse()

    def __int__(self):
        return self.collapse()
