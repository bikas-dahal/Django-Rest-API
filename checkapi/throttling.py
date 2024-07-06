from rest_framework.throttling import UserRateThrottle

class SyamRateThrottle(UserRateThrottle):
    scope = 'syam'
    rate = '4/minute'