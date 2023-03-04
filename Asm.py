class RAM:
    def __init__(self, size):
        self.data = bytearray(size)

    def write_byte(self, address, value):
        self.data[address] = value

    def read_byte(self, address):
        return self.data[address]


class Registers:
    def __init__(self):
        self.eax = 0
        self.ebx = 0
        self.ecx = 0
        self.edx = 0
        self.esp = 0
        self.ebp = 0
        self.esi = 0
        self.edi = 0


class MyASM:
    def __init__(self, ram_size):
        self.ram = RAM(ram_size)
        self.registers = Registers()

    def parse_instruction(self, instruction):
        # Split the instruction into its component parts
        parts = instruction.split()

        # Extract the opcode and operands
        opcode = parts[0]
        operands = parts[1:]

        # Dispatch to the appropriate instruction handler
        if opcode == "mov":
            self.handle_mov(operands)
        elif opcode == "add":
            self.handle_add(operands)
        elif opcode == "sub":
            self.handle_sub(operands)
        elif opcode == "push":
            self.handle_push(operands)
        elif opcode == "pop":
            self.handle_pop(operands)
        else:
            raise Exception(f"Unknown opcode: {opcode}")

    def handle_mov(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid operands for mov")
        dest, src = operands  # for example [ (mov) eax, [0x12345678] ]
        setattr(self.registers, dest, self.get_operand_value(src))  # set register using get operand value

    def handle_add(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid operands for add")
        dest, src = operands
        setattr(self.registers, dest, getattr(self.registers, dest) + self.get_operand_value(src))

    def handle_sub(self, operands):
        if len(operands) != 2:
            raise Exception("Invalid operands for sub")
        dest, src = operands
        setattr(self.registers, dest, getattr(self.registers, dest) - self.get_operand_value(src))

    def handle_push(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid operands for push")
        value = self.get_operand_value(operands[0])
        self.registers.esp -= 4
        self.ram.write_byte(self.registers.esp, value)

    def handle_pop(self, operands):
        if len(operands) != 1:
            raise Exception("Invalid operands for pop")
        value = self.ram.read_byte(self.registers.esp)
        setattr(self.registers, operands[0], value)
        self.registers.esp += 4

    def get_operand_value(self, operand):
        if operand.startswith("[") and operand.endswith("]"):
            address = int(operand[1:-1], 16)
            return self.ram.read_byte(address)
        elif operand in self.registers.__dict__:
            return getattr(self.registers, operand)
        else:
            return int(operand, 16)

    def execute_program(self, program):
        instructions = program.strip().split("\n")
        for instruction in instructions:
            self.parse_instruction(instruction)

    def dump_registers(self):
        print(f"eax: {self.registers.eax}")
        print(f"ebx: {self.registers.ebx}")
        print(f"ecx: {self.registers.ecx}")
        print(f"edx: {self.registers.edx}")
        print(f"esi: {self.registers.esi}")
        print(f"edi: {self.registers.edi}")
        print(f"ebp: {self.registers.ebp}")
        print(f"esp: {self.registers.esp}")


if __name__ == "__main__":
    # Create a new instance of MyASM with a RAM size of 1024 bytes
    my_asm = MyASM(1024)

    # Define a sample assembly program
    program = """
    mov eax 0x10
    mov ebx 0x20
    add eax ebx
    sub ebx 0x5
    push eax
    pop ecx
    """

    # Execute the program
    my_asm.execute_program(program)

    # Print the register values
    my_asm.dump_registers()
