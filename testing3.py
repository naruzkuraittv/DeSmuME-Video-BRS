from tkinter import filedialog
file = filedialog.askopenfilename(title="Select a ROM", filetypes=(("NDS ROMs", "*.nds"), ("All files", "*.*")))
def read_rom_header(file):
    with open(file, "rb") as rom_file:
        header_data = rom_file.read(512)  # NDS header is typically 512 bytes
    # Extract information from the header
    title = header_data[12:28].decode("utf-8").rstrip('\x00')  # Title of the game
    print(title)
read_rom_header(file)