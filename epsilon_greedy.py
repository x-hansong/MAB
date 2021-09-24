#Epsilon 贪心算法

import random

class ArmBandit():
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability
        self.pull_times = 1
        self.profit = 0
    
    #模拟摇臂，按照概率返回，1代表有收益，0代表没有收益
    def pull(self):
        self.pull_times += 1
        if random.random() < self.probability:
            self.profit += 1
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
epsilon = 0.01
#摇老虎机的机会
total_chance = 10000

#构造老虎机实例
bandits = []
for x in range(bandits_num):
    bandits.append(ArmBandit(x, bandit_propability[x]))

#初始化老虎机收益
bandits_result = {}
for bandit in bandits:
    bandits_result[bandit] = 0

#获取当前赢钱概率最高的老虎机
def get_max_profit_bandit():
    max_bandit = bandits[0]
    max_profit = 0
    for bandit, profit in bandits_result.items():
        #遍历比较
        if (max_profit / max_bandit.get_pull_times()) < (profit / bandit.get_pull_times()):
            max_profit = profit
            max_bandit = bandit
    return max_bandit

total_profit = 0
for _ in range(total_chance):
    if random.random() < epsilon:
        #概率小于epsilon，随机选一个老虎机
        random_bandit = bandits[random.randint(0, 9)]
        random_bandit_profit = bandits_result[random_bandit]
        random_bandit_profit += random_bandit.pull()
        #更新收益
        bandits_result[random_bandit] = random_bandit_profit
    else:
        #概率大于等于epsilon，选赢钱概率最大的
        max_profit_bandit = get_max_profit_bandit()
        max_bandit_profit = bandits_result[max_profit_bandit]
        max_bandit_profit += max_profit_bandit.pull()
        #更新收益
        bandits_result[max_profit_bandit] = max_bandit_profit

for bandit, profit in bandits_result.items():
    print(f"{bandit}，收益为：{profit}")
    total_profit += profit

print("最终收益：%d" % total_profit)
