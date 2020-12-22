from twython import Twython

import subprocess
from keys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

#executes command and filters data out
out = subprocess.Popen(['mosquitto_sub', '-t', 'iotkit/temp', '-C', '1'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
data = stdout.split(",")
message = data[1]

#sends tweet message
twitter.update_status(status="It's %s right now in zurich"% (data[1]))
print("Tweeted: %s" % message)
