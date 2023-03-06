import pandas as pd
import subprocess

file_name = "hq_gps_gal_16022023_1110.ubx"
result = subprocess.run(
    f'gnssdump --filename {file_name} --protfilter 2 --msgfilter NAV-STATUS --format 4 --msgmode 0 --quitonerror 1',
    shell=True,
    capture_output=True, text=True)
# print(result.stdout)
# print(result.stderr)

with open("data.txt", 'w', encoding='utf8') as data:
    data.write(result.stdout, )

header = ''
hex_arr = []
# b56201031000 703cb50703df00 0c 63030000ebe00800 a3e0
with open("data.txt", 'r', encoding='utf8') as file:
    hexdata = file.readlines()
    for flat_hex in hexdata[2:-2]:
        main_hex = " ".join(flat_hex[k:k + 2] for k in range(0, len(flat_hex), 2))

        if header == '':
            header = flat_hex[0:12]

        print(main_hex.replace("\n", ""))

        if len(flat_hex) >= 49:
            # check header(first 12 hex data)
            if header == flat_hex[0:12]:
                hex_data = flat_hex[26:28]
                binary_format1 = "{0:04b}".format(int(str(hex_data[0]), 16))
                binary_format2 = "{0:04b}".format(int(str(hex_data[1]), 16))
                print(f"{hex_data}:{str(binary_format1) + str(binary_format2)}")

                with open("new_output.txt", 'a', encoding='utf8') as new:
                    new.write(f"{main_hex}{hex_data}:{str(binary_format1) + str(binary_format2)}")

        # hex_arr.append({"hex": hex_data, "binary": str(binary_format1) + str(binary_format2)})

# df = pd.DataFrame(hex_arr)
# df.to_excel("hex_to_binary.xlsx", index=False)

'''
I dont want to be convert
I want a code to go through the hex

1) first check the header is there ( the one highlighted in green at the beginning)==done
it is always the same and it keep repeating==done
2) then the on one highlighted in green just count the places
3) if 1 is true go to byte number 14 and check it
4) convert byte 14 to binary and see

The red highlighted always need to be check after checking the beginning of the message
Its a recorded message sent again and again u need the header to know that this is ur message 
cause the header never changes and the message have the same structure
'''
