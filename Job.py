import random

# 직업 - Warrior, Wizard, Archer, Tanker, Healer

# 일단 워리어만 
class Warrior(Player):
    def __init__(self):
        super().__init__("전사", 300, 50, 20, 5)
    def normal_attack(self):
        normal_damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - normal_damage, 0)
        print(f"\n {self.name}의 일반 공격! {monster.name}에게 {normal_damage}의 데미지를 입혔습니다!\n ")
    # 스킬 공격 (광역 공격)
    def skill_attack(self):
        skill_damage = random.randint(self.power - 4, self.power + 4)
        # 전사의 스킬공격 power기반으로 할까요 matic_power기반으로 할까요??
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - skill_damage, 0)
            print(f"\n {player.name}의 휠윈드! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {skill_damage}의 데미지를 입혔습니다!\n ")  
        else:
            print("\n 마나가 부족합니다. \n")

class Wizard(Player):
    def __init__(self):
        super().__init__()
    def normal_attack(self):
        normal_damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - normal_damage, 0)
        print(f"\n {self.name}의 일반 공격! {monster.name}에게 {normal_damage}의 데미지를 입혔습니다!\n ")
    # 스킬 공격 (광역 공격)
    def skill_attack(self):
        skill_damage = random.randint(self.power - 4, self.power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - skill_damage, 0)
            print(f"\n {player.name}의 메테오! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {skill_damage}의 데미지를 입혔습니다!\n ")
        else:
            print("\n 마나가 부족합니다. \n") 

class Archer(Player):
    def __init__(self):
        super().__init__()
    def normal_attack(self):
        normal_damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - normal_damage, 0)
        print(f"\n {self.name}의 일반 공격! {monster.name}에게 {normal_damage}의 데미지를 입혔습니다!\n ")
    # 스킬 공격 (광역 공격)
    def skill_attack(self):
        skill_damage = random.randint(self.power - 4, self.power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - skill_damage, 0)
            print(f"\n {player.name}의 화살엄청많이쏘기! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {skill_damage}의 데미지를 입혔습니다!\n ")
        else:
            print("\n 마나가 부족합니다. \n") 

class Tanker(Player):
    def __init__(self):
        super().__init__()
    def normal_attack(self):
        normal_damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - normal_damage, 0)
        print(f"\n {self.name}의 일반 공격! {monster.name}에게 {normal_damage}의 데미지를 입혔습니다!\n ")
    # 스킬 공격 (광역 버프)
    def skill_attack(self):
        if self.mp >= 10:
            pass
            # 탱커 스킬은 광역 버프 (공격력, 방어력 대폭 상승)
        else:
            print("\n 마나가 부족합니다. \n") 

class Healer(Player):
    def __init__(self):
        super().__init__()
    def normal_attack(self):
        normal_damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - normal_damage, 0)
        print(f"\n {self.name}의 일반 공격! {monster.name}에게 {normal_damage}의 데미지를 입혔습니다!\n ")
    # 스킬 공격 (광역 힐)
    def skill_attack(self):
        if self.mp >= 10:
            pass
            # 힐러는 스킬 = 광역 힐
        else:
            print("\n 마나가 부족합니다. \n") 


# -----------------테스트용 임시 몬스터 클래스--------------------

# class Monster:
    
#     def __init__(self, name, hp, power):
#         self.name = name
#         self.hp = hp
#         self.max_hp = hp
#         self.power = power

#     def monster_status(self):
#         monster_max_hp = self.max_hp
#         print(f""" 
#         {self.name}의 현재 상태창: 
#         <HP> {self.hp} / {monster_max_hp} 
#         <힘> {self.power}""")

#     def __str__(self): 
#         return self.name
    
#     def monster_attack(self):
#         monster_damage = random.randint(self.power - 2, self.power + 2)
#         player.hp = max(player.hp - monster_damage, 0) 
#         print(f"\n {self.name}의 공격! {monster_damage}의 데미지를 입었습니다!")
#         if player.hp == 0:
#             print(f"\n {player.name}이(가) 쓰러졌습니다. 전투 패배...\n")


# # ------------------TEST---------
# player = Warrior()
# monster_list = [Monster("고블린", 100, 10), Monster("트롤", 200, 20)]
# monster = random.choice(monster_list)

# player.normal_attack()
# player.skill_attack()
# monster.monster_status()


