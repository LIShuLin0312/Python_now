import redis
import time
from gjc import gjc
from APP_UA import APP_UA
pool = redis.ConnectionPool(host='localhost', port=6379, db=1,decode_responses=True)
redis = redis.Redis(connection_pool=pool)
# redis.set("IP_URL","http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=100017&port=1&pack=63643&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions=&gm=4")
# redis.set("IP_URL","http://api.hailiangip.com:8422/api/getIp?type=1&num=1&pid=-1&unbindTime=300&cid=-1&orderId=O19091112293850909682&time=1570764667&sign=89044b2ba42ecaeac98efcda6a0ea7d1&noDuplicate=1&dataType=1&lineSeparator=0&singleIp=0")
# for i in APP_UA:
#     s = redis.sadd("APP_UA",i)
# for i in gjc:
#     s = redis.lpush("GJC",i)
# # print(s)
# s = redis.lrange("GJC",0,-1)
# for i in s:
#     print(i)
# for i in range(10):
#     s = redis.srandmember(name="APP_UA")
#     print(s)
#     time.sleep(1)
redis.lpush("PBC","molixianhua")