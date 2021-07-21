# The damage of skill1 and skill2

def dmg(skill1, skill2):
    dmg1 = basic_dmg + skill1 * 1.5
    dmg2 = basic_dmg + skill2 * 3.0
    return dmg1, dmg2

basic_dmg = int(input('basic damage: '))
dmg_of_skill1 = int(input('damage of skill1: '))
dmg_of_skill2 = int(input('damage of skill2: '))

skill1_dmg, skill2_dmg = dmg(dmg_of_skill1, dmg_of_skill2)  # 使用两个有意义的变量名称接收返回结果
total_dmg = skill1_dmg + skill2_dmg
print('Your total damage on enemy is ' + str(total_dmg))
