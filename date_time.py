__author__ = 'lyndsay.beaver'
import datetime
start = datetime.datetime.now()

i = 0
while i < 1000000:
    i += 1

end = datetime.datetime.now()

print(end - start)