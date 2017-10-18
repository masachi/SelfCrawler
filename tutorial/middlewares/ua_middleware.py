import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class UAMiddleWares(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        # print ua
        if ua:
            request.headers.setdefault('User-Agent', ua)

    user_agent_list = []
    with open('../file/user_agent', 'r') as f:
        for line in f.readlines():
            user_agent_list.append(line.strip())