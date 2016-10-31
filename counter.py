import re
from collections import Counter

str = "When sent by the client, this method acknowledges one or more messages delivered via the Deliver or Get-Ok methods. When sent by server, this method acknowledges one or more messages published with the Publish method on a channel in confirm mode. The acknowledgement can be for a single message or a set of messages up to and including a specific message"

words = re.findall(r'\w+',str)
count = Counter(words)
print count
print count.most_common(3)
