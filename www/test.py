import orm
from models import User, Blog, Comment
import asyncio
import logging

async def test(loop):
    await orm.create_pool(loop=loop, user='xushubo', password='kxc_2011', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destroy_pool()

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()