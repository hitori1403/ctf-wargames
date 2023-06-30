# reversing.kr: position

found = False
for v6 in range(0x61, 0x7B):
    for v7 in range(0x61, 0x7B):
        v40 = (v6 & 1) + 5
        v48 = ((v6 & 0x10) != 0) + 5
        v42 = ((v6 & 2) != 0) + 5
        v44 = ((v6 & 4) != 0) + 5
        v46 = ((v6 & 8) != 0) + 5

        v32 = (v7 & 1) + 1
        v38 = ((v7 & 0x10) != 0) + 1
        v34 = ((v7 & 2) != 0) + 1
        v8 = ((v7 & 4) != 0) + 1
        v36 = ((v7 & 8) != 0) + 1

        first_part = [v40 + v8, v46 + v36, v42 + v38, v44 + v32, v48 + v34]

        if "".join(map(str, first_part)) == "76876":
            print(chr(v6) + chr(v7), end="")
            found = True
            break
    if found:
        break


v20 = ord("p")
for v19 in range(0x61, 0x7B):
    v41 = (v19 & 1) + 5
    v49 = ((v19 & 0x10) != 0) + 5
    v43 = ((v19 & 2) != 0) + 5
    v45 = ((v19 & 4) != 0) + 5
    v47 = ((v19 & 8) != 0) + 5
    v33 = (v20 & 1) + 1
    v39 = ((v20 & 0x10) != 0) + 1
    v35 = ((v20 & 2) != 0) + 1
    v21 = ((v20 & 4) != 0) + 1
    v37 = ((v20 & 8) != 0) + 1

    second_part = [v41 + v21, v47 + v37, v43 + v39, v45 + v33, v49 + v35]

    if "".join(map(str, second_part)) == "77776":
        print(chr(v19) + chr(v20), end="")
        exit()
