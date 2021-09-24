#UCB算法

import math
import cmath
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
    
    def get_profit(self):
        return self.profit
    
    def get_ucb_score(self, currentTotalTimes):
        probability = (self.profit / self.pull_times)
        ucb = ((2 * math.log(currentTotalTimes)) / self.pull_times) ** 0.5
        return probability + ucb
            
    def __str__(self) -> str:
        return f"{self.name}号老虎机的概率为：{self.probability}，收益为：{self.profit}，被选择次数为：{self.pull_times}"

#初始化老虎机概率
bandit_propability = [0.1355416916306045, 0.5939514278183152, 0.6589668115166952, 0.6755337560094611, 0.2913420268334277,
0.32445103069055126, 0.5447695432679104, 0.5142948397820707, 0.6631081989312548, 0.1570983569528034]
#摇老虎机的机会
total_chance = 10000
#老虎机个数
bandits_num = 10
#构造老虎机实例
bandits = []
for x in range(bandits_num):
    bandits.append(ArmBandit(x, bandit_propability[x]))

def get_max_profit_bandit(currentTotalTimes):
    max_bandit = bandits[0]
    for bandit in bandits:
        if max_bandit.get_ucb_score(currentTotalTimes) < bandit.get_ucb_score(currentTotalTimes):
            max_bandit = bandit
    return max_bandit

for i in range(total_chance):
    #这里注意log0是非法的，要加1
    max_bandit = get_max_profit_bandit(i + 1)
    max_bandit.pull()

total_profit = 0
for bandit in bandits:
    total_profit += bandit.get_profit()
    print(bandit)

print("最终收益：%d" % total_profit)
