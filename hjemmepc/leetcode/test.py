
strs=["act","pots","tops","cat","stop","hat"]
y = []

strs = ["",""]

sorted(strs[0]) == sorted(strs[1]) # ja






sorted(strs[0]) == sorted(strs[1]) #nei
sorted(strs[0]) == sorted(strs[2]) #nei
sorted(strs[0]) == sorted(strs[3]) #ja
sorted(strs[0]) == sorted(strs[4]) #nei
sorted(strs[0]) == sorted(strs[5]) #nei
y.append([strs[0],strs[3]]) # strs[0] & strs[3]

sorted(strs[1]) == sorted(strs[2]) #ja
# sorted(strs[1]) == sorted(strs[3])
sorted(strs[1]) == sorted(strs[4]) #ja
sorted(strs[1]) == sorted(strs[5]) #nei
y.append([strs[1],strs[2],strs[4]]) # strs[1] & strs[2] & strs[4]

# sorted(strs[2]) == sorted(strs[3])
# sorted(strs[2]) == sorted(strs[4])
# sorted(strs[2]) == sorted(strs[5])

# sorted(strs[3]) == sorted(strs[4])
# sorted(strs[3]) == sorted(strs[5])

# sorted(strs[4]) == sorted(strs[5])

y.append(strs[5])
print(y)