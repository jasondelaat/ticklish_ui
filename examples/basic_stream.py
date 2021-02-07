# This example creates a stream which filters out odd numbers and
# prints only the even ones.

from ticklish_ui import Stream

stream = Stream()

(stream
 .filter(lambda n: n % 2 ==0)
 .map(print)
)

stream.insert(1)
stream.insert(2)
stream.insert(3)
stream.insert(4)
stream.insert(5)
stream.insert(6)
stream.insert(7)
stream.insert(8)
stream.insert(9)
stream.insert(10)

# Expected output:
# 2
# 4
# 6
# 8
# 10
