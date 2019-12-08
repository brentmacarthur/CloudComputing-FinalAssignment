# Create SQL Insert script

import os

path = 'D:\\My Documents\\Education\\Cloud Computing\\CloudComputing-FinalAssignment'
write_file = os.path.join(path, 'insert_time_zones.sql')
read_file = os.path.join(path, 'tz.csv')

# with open(path + 'insert_time_zones.sql', 'w') as file_w:
# with open(read_file, 'w') as file_r:
#    for line in file_r:
#        print(line)
print(read_file)
file_r = open(read_file)
for line in file_r:
    line = line.rstrip()
    print(line)
