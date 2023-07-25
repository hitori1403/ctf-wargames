# rootme: ELF x86 - No software breakpoints

enc = bytes.fromhex("1ecd2ad53487fc7864359decde15ac9799af96da79264f32e0")

with open("ch20.bin", "rb") as f:
    program = f.read()

edx = 0
for i in range(0xA3):
    edx = edx ^ edx & 0xFF | (edx + program[0x80 + i] & 0xFF) & 0xFFFFFFFF
    edx = (edx << 3 | edx >> 29) & 0xFFFFFFFF

flag = []
for c in enc[::-1]:
    edx = (edx & 1) << 31 | edx >> 1
    flag.append(c ^ edx & 0xFF)

print(bytes(flag)[::-1])
