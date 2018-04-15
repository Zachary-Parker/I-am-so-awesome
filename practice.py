import numpy
import redis

import six
import hmac
value = 'abc'
if isinstance(value, six.text_type):
    value = value.encode(encoding='utf-8')
mymac = hmac.new(value)
print(mymac)