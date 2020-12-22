import subprocess, os


#Execute Mosquitto and save Output
out = subprocess.Popen(['mosquitto_sub', '-t', 'iotkit/temp', '-C', '1'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
data = stdout.split(",")
message = data[1]

#String to Integer
check = int(float(message))

curl = ('curl' + ' -X' + ' POST' + ' -H' + ' "Content-Type: application/json"' + ' -d' + "'" + '{"value1":%d}' + "'" + ' https://maker.ifttt.com/trigger/Receive_event/with/key/i8Cm9hDvanFDIplLj9kDDahWokZ9mWEt5ZA2lQdkMv0')% (check)

if check < 30:
    os.system(curl)
    print ("Today is a good day")
    print(message)
else:
    print ("Today is a hot day")
    print(message)
