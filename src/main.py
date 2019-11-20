from enum import Enum
import sys

from enums import Command
from controllers import ParkingLotController


class ExecutionEngine(Enum):
    CLI = "cli"
    FILE = "file"

    def execute(self, filepath=None):
        if self.value == self.FILE.value:
            if not filepath: raise ValueError("The filepath can't be None")
            return self.execute_from_file(filepath)
        return self.cli_loop()

    def execute_from_file(self, filepath):
        parking_lot = None
        with open(filepath) as file:
            for line in file.readlines():
                parking_lot, output = self.parse_and_execute(parking_lot, line)
                print(output)

    def cli_loop(self):
        parking_lot = None
        while True:
            parking_lot, output = self.parse_and_execute(parking_lot, input())
            print(output)

    @staticmethod
    def parse_and_execute(parking_lot, line: str):
        input_params = line.split()
        command, args = Command(input_params[0]), input_params[1:]
        return ParkingLotController.execute_command(parking_lot, command, args)


if __name__ == '__main__':
    engine, fpath = None, None
    if len(sys.argv) == 2:
        engine = ExecutionEngine("file")
        fpath = sys.argv[1]
    else:
        engine = ExecutionEngine("cli")
    engine.execute(fpath)


