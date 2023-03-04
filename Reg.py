class Register:
    """
    A class representing a 32-bit general-purpose register in an 8086 CPU.

    Attributes:
        value (int): The current value of the register.

    Methods:
        set(value): Sets the value of the register to the specified value.
        get(): Returns the current value of the register.
        add(value): Adds the specified value to the register.
        sub(value): Subtracts the specified value from the register.
        mul(value): Multiplies the register by the specified value.
        div(value): Divides the register by the specified value.
        and_op(value): Performs a bitwise AND operation with the specified value.
        or_op(value): Performs a bitwise OR operation with the specified value.
        xor_op(value): Performs a bitwise XOR operation with the specified value.
        shl(value): Shifts the bits in the register left by the specified number of bits.
        shr(value): Shifts the bits in the register right by the specified number of bits.
        rol(value): Rotates the bits in the register left by the specified number of bits.
        ror(value): Rotates the bits in the register right by the specified number of bits.
    """

    def __init__(self, value=0):
        self.value = value

    def set(self, value):
        """Sets the value of the register to the specified value."""
        self.value = value

    def get(self):
        """Returns the current value of the register."""
        return self.value

    def add(self, value):
        """Adds the specified value to the register."""
        self.value += value

    def sub(self, value):
        """Subtracts the specified value from the register."""
        self.value -= value

    def mul(self, value):
        """Multiplies the register by the specified value."""
        self.value *= value

    def div(self, value):
        """Divides the register by the specified value."""
        self.value //= value

    def and_op(self, value):
        """Performs a bitwise AND operation with the specified value."""
        self.value &= value

    def or_op(self, value):
        """Performs a bitwise OR operation with the specified value."""
        self.value |= value

    def xor_op(self, value):
        """Performs a bitwise XOR operation with the specified value."""
        self.value ^= value

    def shl(self, value):
        """Shifts the bits in the register left by the specified number of bits."""
        self.value <<= value

    def shr(self, value):
        """Shifts the bits in the register right by the specified number of bits."""
        self.value >>= value

    def rol(self, value):
        """Rotates the bits in the register left by the specified number of bits."""
        self.value = ((self.value << value) | (self.value >> (32 - value))) & 0xFFFFFFFF

    def ror(self, value):
        """Rotates the bits in the register right by the specified number of bits."""
        self.value = ((self.value >> value) | (self.value << (32 - value))) & 0xFFFFFFFF


def main():
    # Create new registers with initial values of 0
    eax = Register()
    ebx = Register()
    ecx = Register()
    edx = Register()
    esp = Register()
    ebp = Register()

    # Set the value of the EAX register to 0x12345678
    eax.set(0x12345678)

    # Add 0x87654321 to the EBX register
    ebx.add(0x87654321)

    # Multiply the ECX register by 0x1234
    ecx.mul(0x1234)

    # Divide the EDX register by 0x100
    edx.div(0x100)

    # Set the ESP register to 0x7FFFD000
    esp.set(0x7FFFD000)

    # Subtract 0x100 from the EBP register
    ebp.sub(0x100)

    # Perform a bitwise AND between EAX and EBX
    eax.and_op(ebx.get())

    # Perform a bitwise OR between ECX and EDX
    ecx.or_op(edx.get())

    # Perform a bitwise XOR between EAX and ECX
    eax.xor_op(ecx.get())

    # Shift the bits in the ESP register left by 12 bits
    esp.shl(12)

    # Shift the bits in the EBP register right by 4 bits
    ebp.shr(4)

    # Rotate the bits in the EAX register left by 8 bits
    eax.rol(8)

    # Rotate the bits in the EBX register right by 4 bits
    ebx.ror(4)

    # Print the final values of all the registers
    print("EAX:", hex(eax.get()))
    print("EBX:", hex(ebx.get()))
    print("ECX:", hex(ecx.get()))
    print("EDX:", hex(edx.get()))
    print("ESP:", hex(esp.get()))
    print("EBP:", hex(ebp.get()))


if __name__ == "__main__":
    main()
