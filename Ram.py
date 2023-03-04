import tkinter as tk


class RAM:
    """
    A class representing the RAM memory in an 8086 CPU.

    Attributes:
        memory (bytearray): The memory contents, represented as a bytearray.

    Methods:
        read_byte(segment, offset): Reads a byte from the specified memory location.
        write_byte(segment, offset, value): Writes a byte to the specified memory location.
        read_word(segment, offset): Reads a 16-bit word from the specified memory location.
        write_word(segment, offset, value): Writes a 16-bit word to the specified memory location.
        read_dword(segment, offset): Reads a 32-bit double word from the specified memory location.
        write_dword(segment, offset, value): Writes a 32-bit double word to the specified memory location.
    """

    def __init__(self, size):
        self.memory = bytearray(size)

    def read_byte(self, segment, offset):
        """Reads a byte from the specified memory location."""
        address = (segment << 4) + offset
        return self.memory[address]

    def write_byte(self, segment, offset, value):
        """Writes a byte to the specified memory location."""
        address = (segment << 4) + offset
        self.memory[address] = value

    def read_word(self, segment, offset):
        """Reads a 16-bit word from the specified memory location."""
        address = (segment << 4) + offset
        return (self.memory[address + 1] << 8) | self.memory[address]

    def write_word(self, segment, offset, value):
        """Writes a 16-bit word to the specified memory location."""
        address = (segment << 4) + offset
        self.memory[address] = value & 0xFF
        self.memory[address + 1] = (value >> 8) & 0xFF

    def read_dword(self, segment, offset):
        """Reads a 32-bit double word from the specified memory location."""
        address = (segment << 4) + offset
        return (self.memory[address + 3] << 24) | (self.memory[address + 2] << 16) | (self.memory[address + 1] << 8) | \
            self.memory[address]

    def write_dword(self, segment, offset, value):
        """Writes a 32-bit double word to the specified memory location."""
        address = (segment << 4) + offset
        self.memory[address] = value & 0xFF
        self.memory[address + 1] = (value >> 8) & 0xFF
        self.memory[address + 2] = (value >> 16) & 0xFF
        self.memory[address + 3] = (value >> 24) & 0xFF


class RAMViewer:
    def __init__(self, ram):
        self.ram = ram

        # Create the main window
        self.window = tk.Tk()
        self.window.title("RAM Viewer")

        # Create a text area to display the memory contents
        self.text = tk.Text(self.window, font=("Courier", 12), state="disabled", width=64, height=32)
        self.text.pack()

        # Create a button to refresh the display
        self.button = tk.Button(self.window, text="Refresh", command=self.refresh)
        self.button.pack()

        # Refresh the display initially
        self.refresh()

        # Start the main event loop
        self.window.mainloop()

    def refresh(self):
        # Clear the text area and enable editing
        self.text.configure(state="normal")
        self.text.delete("1.0", tk.END)

        # Print the memory contents to the text area
        for segment in range(0, 0xFFFF, 0x10):
            for offset in range(0x10):
                byte = self.ram.read_byte(segment >> 4, offset)
                self.text.insert(tk.END, f"{byte:02X} ")
            self.text.insert(tk.END, "\n")

        # Disable editing of the text area
        self.text.configure(state="disabled")


def main():
    # Create a new RAM object with 64 kilobytes of memory
    ram = RAM(64 * 1024)

    # Write some initial data to the memory
    for i in range(0, 256):
        ram.write_byte(0, i, i)

    # Read some data from the memory
    for i in range(0, 256):
        data = ram.read_byte(0, i)
        print(f"Data at address 0x{i:02X}: {data:02X}")

    # Perform some arithmetic operations on the data
    for i in range(0, 256, 2):
        a = ram.read_byte(0, i)
        b = ram.read_byte(0, i + 1)
        c = a + b
        d = a - b
        e = a * b
        f = a // b
        print(f"{a:02X} + {b:02X} = {c:02X}")
        print(f"{a:02X} - {b:02X} = {d:02X}")
        print(f"{a:02X} * {b:02X} = {e:02X}")
        print(f"{a:02X} // {b:02X} = {f:02X}")

        # Launch a RAMViewer GUI to view and modify the memory
        viewer = RAMViewer(ram)


if __name__ == "__main__":
    main()
