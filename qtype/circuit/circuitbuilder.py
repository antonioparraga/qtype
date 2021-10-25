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
from qtype.circuit.circuitcommand import CircuitCommand


class CircuitBuilder:

    def __init__(self):
        self.commands = []

    def add_command(self, command: CircuitCommand):
        self.commands.append(command)

    def build(self, circuit):
        for command in self.commands:
            command.execute(circuit)
