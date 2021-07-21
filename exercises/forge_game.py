# 五行石分为1-8级，商人处只能购买1级石头，玩家处可以购买所有等级的石头
# 高级石头能通过低级石头的合成获得
# 货币：金币
# 合成系统：
# 合成过程消耗 1.金币 2.钻石 3.体力
# 购买1级五行石（商人）：消耗金币、钻石
# 1级-3级：消耗金币、体力和1级五行石
# 3级-4级：消耗金币、体力和1级五行石（一定概率）
# 4级-6级：消耗金币、体力和4级五行石

'''
    level 1 stone
'''
l1_gold = 0.75
l1_diamond = 8

'''
    level 1 to level 3
'''
l1_to_l3 = 12       # consumes 12 level 1 stones
l1_to_l3_gold = 0.39
l1_to_l3_vit = 10   # 10 vitality

'''
    level 3 to level 4
'''
l3_to_l4 = 16       # consumes 16 level 1 stone
l3_to_l4_gold = 0.897
l3_to_l4_vit = 10
l3_to_l4_prob = 0.4878      # fail to forge would lose 
                            # 16 level 1 stones and gold, but not vit

'''
    level 4 to level 6
'''
l4_to_l6 = 12       # consumes 12 level 4 stones
l4_to_l6_gold = 19.75
l4_to_l6_vit = 10

'''
    The price of a level 6 stone from other players is 750 gold
    Also:
        1 diamond equals to 0.05 gold
        1 vit equals to 1 gold
    Which method costs less? Purchase the level 6 stone directly from the player
    or forge it from level 1 by myself?
'''

## ANSWER
import random

## the value of n pieces of level 1 stones
def value_l1(n):
    one_l1 = l1_gold + l1_diamond * 0.05
    v1 = n * one_l1
    return v1

## the value of n pieces of level 3 stones
def value_l3(n):
    one_l3 = value_l1(l1_to_l3) + l1_to_l3_gold + l1_to_l3_vit * 1
    v3 = n * one_l3
    return v3

## the value of n pieces of level 4 stones
def value_l4(n):

    # probability
    success_prob = l3_to_l4_prob
    failure_prob = 1 - l3_to_l4_prob

    # prob of failure/sccuess upgrade
    success_cost = (value_l3(1) + value_l1(16) + l3_to_l4_gold + l3_to_l4_vit * 1)
    failure_cost = (value_l1(16) + l3_to_l4_gold)

    # vale of successfully obtaining n level 4 stone
    v4 = n * (success_cost + (failure_prob)/(success_prob) * failure_cost)

    return v4

## the value of n pieces of level 6 stones
def value_l6(n):
    one_l6 = value_l4(12) + l4_to_l6_gold + l4_to_l6_vit * 1
    v6 = n * one_l6
    return v6

## Is it worth?
v6_from_player = 750

print('the value of a level 1 stone is', value_l1(1))
print('the value of a level 3 stone is', value_l3(1))
print('the value of a level 4 stone is', value_l4(1))
print('the value of a level 6 stone is', value_l6(1))

if value_l6(1) >= v6_from_player:
    print('Forge a level 6 stone will cost you', value_l6(1), 
    'gold, it is not worth')
else:
    print('Forge a level 6 stone only cost you', value_l6(1),
    'gold, screw other players!')
