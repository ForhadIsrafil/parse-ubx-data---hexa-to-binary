import pandas as pd
import subprocess

result = subprocess.run(
    'gnssdump --filename 1.gps_20dB.ubx --protfilter 2 --msgfilter NAV-STATUS --format 4 --msgmode 0 --quitonerror 1',
    shell=True,
    capture_output=True, text=True)
# print(result.stdout)
# print(result.stderr)

with open("data.txt", 'w', encoding='utf8') as data:
    data.write(result.stdout, )

hex_arr = []
with open("data.txt", 'r', encoding='utf8') as file:
    scale = 16
    hexdata = file.readlines()
    for flat_hex in hexdata[2:-2]:
        if len(flat_hex) == 49:
            hex_data = flat_hex[26:28]
            binary_format1 = "{0:04b}".format(int(str(hex_data[0]), 16))
            binary_format2 = "{0:04b}".format(int(str(hex_data[1]), 16))
            print(f"Hex Format: {hex_data} | Binary Format: {str(binary_format1)+str(binary_format2)}")
            hex_arr.append({"hex": hex_data, "binary": str(binary_format1)+str(binary_format2)})

df = pd.DataFrame(hex_arr)
df.to_excel("hex_to_binary.xlsx", index=False)
