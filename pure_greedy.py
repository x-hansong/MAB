#朴素贪心算法

import random

class ArmBandit():
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability
        self.pull_times = 1
    
    #模拟摇臂，按照概率返回，1代表有收益，0代表没有收益
    def pull(self):
        self.pull_times += 1
        if random.random() < self.probability:
            return 1
        else:
            return 0
    
    def get_pull_times(self):
        return self.pull_times
            
    def __str__(self) -> str:
        return f"{self.name}号老虎机的概率为：{self.probability}"

#初始化老虎机概率
bandit_propability = [0.1355416916306045, 0.5939514278183152, 0.6589668115166952, 0.6755337560094611, 0.2913420268334277,
0.32445103069055126, 0.5447695432679104, 0.5142948397820707, 0.6631081989312548, 0.1570983569528034]

#老虎机个数
bandits_num = 10
#探索次数
explore_times = 100
#摇老虎机的机会
total_chance = 10000
#利用次数
exploit_times = total_chance - bandits_num * explore_times

#构造老虎机实例
bandits = []
for x in range(bandits_num):
    bandits.append(ArmBandit(x, bandit_propability[x]))

#每个老虎机探索一定的次数
bandits_result = {}
for bandit in bandits:
    profit = 0
    for _ in range(explore_times):
        profit += bandit.pull()
    bandits_result[bandit] = profit

#计算赢钱概率最高的老虎机，每个老虎机的探索次数相等，所以赢钱的概率只要比较收益大小就行
max_bandit = None
max_profit = 0
total_profit = 0
for bandit, profit in bandits_result.items():
    print(f"{bandit}，摇{explore_times}次收益为：{profit}")
    if max_profit < profit:
        max_profit = profit
        max_bandit = bandit
        total_profit += profit
#最后把剩下的机会都留给赢钱概率最高的老虎机
print(f"收益最高的估算是：{max_bandit}")
exploit_profit = 0
for _ in range(exploit_times):
    exploit_profit += max_bandit.pull()

total_profit += exploit_profit

print("最终收益：%d" % total_profit)
