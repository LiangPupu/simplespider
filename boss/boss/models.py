# class ProxyModel(object):
#     def __init__(self, data):
#         self.ip = data['ip']
#         self.port = data['port']
#         self.expire_time_str = data['expire_time']
#         self.proxy = 'https://{}:{}'.format(self.ip, self.port)
#
#     @property
#     def expire_time