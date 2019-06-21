# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('twitter_template'))
template = env.get_template('twitter.html')
with open('./twitter_template/test.html', 'w+', encoding='utf-8') as f:
    f.write(template.render(tweet_text='这里是推文内容', time='这里是发送时间', re='这里是转发次数', like='这里是喜欢次数', reply='这里是回复数'))