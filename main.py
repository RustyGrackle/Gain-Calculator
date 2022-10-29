import math as m
inp_voltage = input("Input voltage: \n").split()
out_voltage = input("Output voltage: \n").split()

len = len(inp_voltage)
i = 0
Gain = []

for n in range(len):
    gain = 20 * (m.log((float(out_voltage[i]) / float(inp_voltage[i])), 10))
    Gain.append(gain)
    i += 1

print(Gain)

#1.55 1.58 1.62 1.60 1.64 1.61 1.68 1.57 1.64 1.64 1.75 1.67 1.73 1.71 1.74 1.61 1.51
#1.53 1.56 1.62 1.58 1.60 1.37 1.24 1.14 1.05 0.777 0.912 1.27 1.39 1.59 1.65 1.18 0.731
