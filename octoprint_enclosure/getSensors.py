import sys
import subprocess


def error():
    print('-1 | -1')
    sys.exit(1)


def readValue(sensor_name):
    cmd = "sensors | grep -e " + sensor_name
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    lines = output.split('\n')
    lines = filter(None, lines)
    value = -1
    if len(lines) <> 1:
        error()
    if lines[0].find(sensor_name) >= 0:
        values = lines[0].split()
        numeric = ''.join(i for i in values[1] if i.isdigit() or i == '.')
        value = float(numeric)
    return value

#temp_name = "???"
#humidity_name = "???"

# if len(sys.argv) == 3:
#    temp_name = sys.argv[1]
#    humidity_name = sys.argv[2]
# else:
#    error()


#cTemp = readValue(temp_name)
#humidity = readValue(humidity_name)
cTemp = -1
humidity = -1

print('{0:0.1f} | {1:0.1f}'.format(cTemp, humidity))
