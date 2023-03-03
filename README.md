# parse-ubx-data-hexa-to-binary

The first 6 bytes are a header forget about it and this indicates the beginning of a new message
Then the green bytes are the (itow, gps fix, flags, fixstat) also forget about them
The. U will have ur 7th byte which is highlighted in red
For example when it is (10) in hex. in binary is 0001 0000

The forth bit is 1 which means spoofed this what i need
