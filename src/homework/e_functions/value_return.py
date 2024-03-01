def get_hour(epoch_seconds):
    ansH = 0
    ansH = int(epoch_seconds/3600)
    return ansH
def get_minutes(epoch_seconds):
    ansM = 0
    ansM = int(epoch_seconds/60)
    ansM %= 60
    return ansM
def get_seconds(epoch_seconds):
    ansS = 0
    ansS += epoch_seconds%3600
    ansS %= 60
    return ansS