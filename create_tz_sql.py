# Create SQL Insert script

import os

path = 'D:\\My Documents\\Education\\Cloud Computing\\CloudComputing-FinalAssignment'
write_file = os.path.join(path, 'insert_time_zones.sql')
read_file = os.path.join(path, 'tz_nh.csv')

with open(write_file, 'w') as outfile:
    outfile.write('INSERT INTO time_zones\n')
    outfile.write(
        '\t(tz_id,tz_abbreviation,time_zone_name,tz_location,utc_offset)\n')
    outfile.write('VALUES')
    with open(read_file, 'r') as infile:
        for line in infile:
            outfile.write('\t({}),\n'.format(line.rstrip()))
