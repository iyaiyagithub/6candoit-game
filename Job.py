import random

#------------------------임시로 main 가져오기-----------------------



#--------------------임시로 가져온 main 끝!-----------------------


# 영주님 벌써 이렇게 많이 작성하시다니....!!!!!!!!!!! 사랑스러워 죽겠어용ㅎㅎㅎㅎㅎ 남은 시간도 화이팅하구!! 잘부탁드려용^ㅇ^ - 묭
# 감사합니닿ㅎ 저도 잘부탁드려요. 부족하지만 열심히 해보겠습니다(_ _)
# 점심먹기 전 변경사항
# 1. normal_attack 함수 제거(Character클래스에 공통으로)
# 2. skill 명칭 magic으로 일괄 변경
# 3. 탱커와 힐러 magic_attack을 각각 버프와 힐로 추가
# 4. Party클래스 상속 받아오는 것으로 변경
# main.py는 손대지 않았습니다.

# 직업 - Warrior, Wizard, Archer, Tanker, Healer

# normal_attack은 Character쪽으로! -> MP사용하는 애들은 오버라이딩!

class Warrior(Party):
    def __init__(self):
        super().__init__("전사", 300, 50, 30, 5)
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, party):
        magic_damage = random.randint(self.magic_power - 4, self.magic_power + 4)
        # 전사의 스킬공격 power기반으로 할까요 matic_power기반으로 할까요??
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - magic_damage, 0)
            print(f"\n {party.name}의 휠윈드! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!\n ")  
        else:
            print("\n 마나가 부족합니다. \n")

class Wizard(Party):
    def __init__(self):
        super().__init__("마법사", 150, 100, 10, 40)
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, party):
        magic_damage = random.randint(self.magic_power - 4, self.magic_power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - magic_damage, 0)
            print(f"\n {party.name}의 메테오! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!\n ")
        else:
            print("\n 마나가 부족합니다. \n") 


class Archer(Party):
    def __init__(self):
        super().__init__("궁수", 200, 80, 20, 10)
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, party):
        magic_damage = random.randint(self.magic_power - 4, self.magic_power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0) # 스킬공격은 마나를 소모함
            for monster in monster_list:
                monster.hp = max(monster.hp - magic_damage, 0)
            print(f"\n {party.name}의 화살엄청많이쏘기! mp 10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!\n ")
        else:
            print("\n 마나가 부족합니다. \n") 


class Tanker(Party):
    def __init__(self):
        super().__init__("탱커", 500, 30, 20, 5)
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 버프)
    def magic_attack(self, party):
        if self.mp >= 10:
            for member in party:
                member.normal_power += 30
                member.magic_power += 30
            print(f"\n {party.name}의 광역 버프! 파티원의 모든 공격력 스탯이 상승했습니다! \n")
        else:
            print("\n 마나가 부족합니다. \n") 


class Healer(Party):
    def __init__(self):
        super().__init__("힐러", 150, 100, 5, 30)
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 힐)
    def magic_attack(self, party):
        if self.mp >= 10:
            for member in party:
                member.hp = member.max_hp
                member.mp = member.max_mp
            print(f"\n {party.name}의 광역 회복! 파티원의 모든 HP와 MP가 회복되었습니다! \n")
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


