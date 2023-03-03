from pyubx2 import UBXReader, SET, GET, POLL, UBXMessage
from datetime import datetime
from pytz import timezone, all_timezones
import pandas as pd

data_arr = []
with open("1.gps_20dB.ubx", 'rb') as file:
    ubr = UBXReader(file, protfilter=2, msgmode=GET, parsebitfield=1, validate=0)
    # raw_data, parsed_data = ubr.read()
    for raw_data, parsed_data in ubr.iterate():
        # print(raw_data)
        # data_arr.append(parsed_data)
        # print(parsed_data)

        if parsed_data.identity == "NAV-STATUS":
            # print(parsed_data)
            data_arr.append(parsed_data)
        #     # print(datetime.fromtimestamp(parsed_data.iTOW/100).astimezone(timezone('Asia/Dubai')).strftime("%H:%M:%S"), parsed_data.msss)
        #     try:
        #         temp_dict = {
        #             "iTOW": parsed_data.iTOW,
        #             "gpsFix": parsed_data.gpsFix,
        #             "gpsFixOk": parsed_data.gpsFixOk,
        #             "diffSoln": parsed_data.diffSoln,
        #             "wknSet": parsed_data.wknSet,
        #             "towSet": parsed_data.towSet,
        #             "diffCorr": parsed_data.diffCorr,
        #             "carrSolnValid": parsed_data.carrSolnValid,
        #             "mapMatching": parsed_data.mapMatching,
        #             "psmState": parsed_data.psmState,
        #             "spoofDetState": parsed_data.spoofDetState,
        #             "carrSoln": parsed_data.carrSoln,
        #             "ttff": parsed_data.ttff,
        #             "msss": parsed_data.msss
        #         }
        #         data_arr.append(temp_dict)
        #         # with open("msg.txt", 'a', encoding='utf8') as new:
        #         #     new.write(str(parsed_data) + '\n')
        #     except Exception as e:
        #         pass
print(len(data_arr))
df = pd.DataFrame(data_arr)
df.to_csv("output.csv", index=False)
'''
-----------------------------
The first 6 bytes are a header forget about it and this indicates the beginning of a new message
Then the green bytes are the (itow, gps fix, flags, fixstat) also forget about them
The. U will have ur 7th byte which is highlighted in red
For example when it is (10) in hex in binary is
0001 0000

The forth bit is 1 which means spoofed this what i need
------------------------------
I want to parse ubx data from ublox receiver
There is a message of the ubx called nav_status
I need only to parse this message
[In page 142 u will the message details(in pdf)]
-----------------
To read the ubx u need Hex editor neo cause the message in binary form
-----------------------
Ubx_Nav_status
Just to check the flags 2 (spoofing detection)
--------------------------------------------------------
U parsed the Nav_Status not the Nav_Sat right?


'''
