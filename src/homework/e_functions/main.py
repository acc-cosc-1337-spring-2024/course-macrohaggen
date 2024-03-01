from value_return import get_hour
from value_return import get_minutes
from value_return import get_seconds
intOK = int(input("Provide a UNIX time parameter:\n"))
print(get_hour(intOK),":",get_minutes(intOK),":",get_seconds(intOK), sep='')
