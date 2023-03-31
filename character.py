import random

# 출력 색상 변경
R = "\033[91m"
B = "\033[94m"
W = "\033[0m"
G = "\033[92m"
M = "\033[95m"
YB = "\033[103m"

# 플레이어, 몬스터 부모 클래스
# 민경님
class Character:
    def __init__(self, name, hp=100, normal_power=100, mp=50):
        # 이름, hp, power, 일반 공격, 직업
        self.name = name
        self.max_hp = hp
        self.hp = max(hp, 0)
        self.mp = mp
        self.normal_power = normal_power
        self.alive = True

    def show_status(self):
        print("\n---------------------------스탯-----------------------------")
        print(f":::{G} {self.name}의 정보{W} {R}HP:{self.hp}/{self.max_hp}  MP:{self.mp}{W}")
        print(f":::[물리공격력]: {self.normal_power} [마법 공격력]: {self.magic_power}")
        print("-------------------------------------------------------------\n")
        return ""

    # 내가 조아하는 우리 팀장님!!! 제일 뼈대가 되는 구간을 너무 잘 짜신 것 같아요!!! 도움이 필요하면 언제든지 부르겠습니닷^ㅇ^ 화이팅 팀장님~~ - 묭
    def normal_attack(self, target):  # 기본 공격
        if target.hp > 0:
            critical_attack = random.random() < 0.3  # 10퍼센트 확률로 치명타 발동
            if critical_attack:
                damage = random.randint(int(self.normal_power * 0.8), int(self.normal_power * 1.2)) * 2
                print(f"{R}{YB}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{W}\n {R}{YB}!!!!!!!!치명타 발동!!!!!!!!{W}\n{R}{YB}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{W}")
                print(f"{M}치명타!! {target.name}에게 {damage}의 데미지를 입혔습니다.{W}")
                target.hp = max(target.hp - damage, 0)
            else:
                print(f"{YB}{self.name}의 일반공격!{W}")
                damage = random.randint(int(self.normal_power * 0.8), int(self.normal_power * 1.2))
                target.hp = max(target.hp - damage, 0)
                print(f"{M}{target.name}에게 {damage}의 데미지를 입혔습니다.{W}")

        if target.hp <= 0:
            print(f"{YB}{target.name}이 쓰러졌습니다.{W}")

    def check_alive(self):
        # 죽었는 지 살았는 지 확인 하는 코드
        if self.hp <= 0:
            self.alive = False
        return 1


# 혜민님
class Party(Character):
    def __init__(self, name, character, mp, hp, normal_power, magic_power, exp=0, level=1):
        super().__init__(name)
        self.max_hp = hp
        self.character = character
        self.mp = mp
        self.exp = exp
        self.level = level
        self.hp = hp
        self.normal_power = normal_power
        self.magic_power = magic_power

    def check_alive(self):
        # 죽었는 지 살았는 지 확인 하는 코드
        if self.hp <= 0:
            self.alive = False

    def show_choice_character(self):
        print(self.character)
    
    def level_exp(self, character_list):
        if self.exp == 100:
            print(f"{YB}!!**!!**!!**!!** 레 벨 업 **!!**!!**!!**!!{W}")
            for i in character_list:
                i.hp = i.max_hp
            self.level += 1
            self.exp = 0
            print(f"플레이어의 레벨이 {self.level}이 되었습니다!!")
        # 0 경험치에서 시작
        # 사냥할 때 마다 20씩 획득
        # 100경험치 달성시 레벨업!
        # 레벨업  -> 파워 2 증가, 체력 전부 회복
        # 다시 경험치는 0으로 설정


# items----------------------------
def steelsword(item_character):
    item_character.normal_power += 10
    print(f"{YB}!*!*!*!*!스틸소드 파워업!*!*!*!*!{W}")


def armor(item_character):
    item_character.max_hp += 50
    print(f"{YB}최대 체력이 50!! 증가했습니다!{W}")


def hp_portion(item_character):
    item_character.hp = item_character.max_hp
    print(f"{YB}!!!*****모든 hp를 회복했습니다*****!!!{W}")
    item_character.show_status()


def mp_portion(item_character):
    item_character.mp += 10
    print(f"{YB}마나가 10!! 증가했습니다.{W}")


def success_hunt_items(party_list):
        num_select = random.randint(1,4)
        if num_select == 1 : ##팀 리스트를 받아야 할 거 같음.
            print(f"{YB}모든 캐릭터 최대 체력 100 상승!{W}")
            for party_member in party_list:
                party_member.max_hp += 100
                party_member.show_status()
            
        elif num_select == 2 :
            print(f"{YB}모든 캐릭터 마나 10 상승!{W}")
            for party_member in party_list:
                party_member.mp += 10
                party_member.show_status()

        elif num_select == 3 :
            print(f"{YB}모든 캐릭터 일반공격력 100 상승!{W}")
            for party_member in party_list:
                party_member.normal_power += 100
                party_member.show_status()
        else:
            print(f"{YB}모든 캐릭터 마법공격력 10 상승!{W}")
            for party_member in party_list:
                party_member.magic_power += 10
                party_member.show_status()


#### ------------------------Monster 시작
#### -----------------------------------

# 1. monster에서 쓰고 있던 normal_attack 제거중... 완료
# 2. Character에서 상속받을 수 있는 건 받게 만드는 중...
# __init__ 완료
# 3. 코드 간소화 중...
class Monster(Character):
    # 몬스터 스킬 사용 코드 -> 랜덤을 사용 하거나, mp나 sp도 좋을 듯!
    # 1차 목표 스킬 구현.
    # 가능하면 여러 가지 스킬 구현.
    # 몬스터 스킬의 필요한 mp량 나중에 수정을 쉽게 하기 위해 변수로 추가해 둠.
    monster_skill_mp = [10, 20, 30]  # 약공 강공 힐

    def __init__(self, name, hp, normal_power, mp, magic_power, exp):  # normal attack 제거 job도 일단 제거
        # 이름, hp, nomral_power, 일반 공격, 직업
        # 따로 함수로..고민중!()

        super().__init__(name, hp, normal_power, mp)
        # self.normal_attack = normal_attack
        # self.job = job
        self.magic_power = magic_power
        self.exp = exp
        self.alive = True
        

    # Character class에 추가 예정!
    def enough_mp(self, required_mp):  # mp가 충분한지 확인하는 함수. 좀 짧게 만드려고 추가.
        skill_attack_flag = 1
        if self.mp < required_mp:
            skill_attack_flag = 0
        return skill_attack_flag

    def choose_skill(self):
        possible_skill_list = [0, 0, 0]  # 스킬이 사용가능한 상황인지 체크하려고 만듦. + 숫자를 추가해서 확률을 높이려고 함.
        for index in range(len(Monster.monster_skill_mp) - 1):
            if Monster.enough_mp(self, Monster.monster_skill_mp[index]) == 1:
                possible_skill_list[index] = 1
        if (self.hp <= (self.max_hp // 2)) and (
        Monster.enough_mp(self, Monster.monster_skill_mp[2])):  # 체력이 50%이하 + mp가 충분하면 힐 할 확률 생성
            possible_skill_list[2] += 1
        if self.mp >= (Monster.monster_skill_mp[1] * 5):
            possible_skill_list[1] += 2  # mp가 강공보다 5배 많다면 2만큼 확률 추가
        elif self.mp >= (Monster.monster_skill_mp[1] * 3):
            possible_skill_list[1] += 1  # mp가 강공보다 3배 많다면 1만큼 확률 추가
        elif self.mp >= (Monster.monster_skill_mp[0] * 5):
            possible_skill_list[0] += 2  # mp가 강공보다 3배 많다면 1만큼 확률 추가
        elif self.mp >= (Monster.monster_skill_mp[0] * 3):
            possible_skill_list[0] += 1  # mp가 강공보다 3배 많다면 1만큼 확률 추가

        total_chance = 0
        for chance in possible_skill_list:
            total_chance += chance
        choose_chance = random.randint(1, total_chance)
        choose_result = 0  # 선택할 스킬
        for chance in possible_skill_list:
            choose_result += 1
            if choose_chance <= chance:
                break
            else:
                choose_chance -= chance
        return choose_result

    def skill_attack(self, other):
        # 랜덤 추가 고려중!~~~^ㅇ^ ##했습니다. :D
        skill_type = Monster.choose_skill(self)

        if skill_type == 1:  # 1은 약한 스킬 2는 강한 스킬 3은 회복. 3이 획복이라면 함수 이름 변경 필요할 듯.
            damage = random.randint(self.normal_power, self.normal_power * 2 + 1)  # 데미지가 nomral_power ~ nomral_power*2
            if self.mp < 10:
                self.normal_attack(other)
            else:
                other.hp = max(other.hp - damage, 0)
                print(f"{YB}{self.name}의 몸!통!박!치!기! {other.name}에게 {damage}의 데미지를 입혔습니다.{W}")  # 쉬발쉬발 -팀장왈 진정하세요 팀장님 -팀원A 팀장님~컴다운~=묭
                print(f"{M}{other.name}의 남은 체력은 {other.hp}{W}")
                if other.hp == 0:
                    self.alive = False
                    print(f"{YB}{other.name}이(가) 쓰러졌습니다.{W}")
        elif skill_type == 2:
            damage = random.randint(self.normal_power * 2,
                                    self.normal_power * 3 + 1)  # 데미지가 nomral_power*2 ~ nomral_power*3
            if self.mp < 20:
                self.normal_attack(other)
            else:
                other.hp = max(other.hp - damage, 0)
                print(f"{YB}{self.name}의 휘둘러치기!!! {other.name}에게 {damage}의 데미지를 입혔습니다.{W}")
                print(f"{M}{other.name}의 남은 체력은 {other.hp}{W}")
                if other.hp == 0:
                    self.alive = False
                    print(f"{YB}{other.name}이(가) 쓰러졌습니다.{W}")
        elif skill_type == 3:
            heal = random.randint(self.normal_power // 2, self.normal_power + 1)  # 1/2~1만큼 회복
            if self.mp < 10:
                self.normal_attack(other)
            else:
                self.hp += heal
                print(f"{YB}{self.name}이 {heal}만큼 회복해 hp가 {self.hp}가 되었다!{W}")


# 몬스터를 그룹화 해서 묶어주기. 아마 리스트나 딕셔너리로 구현하게 될 것 같음.
# Monster 클래스는 단일 몬스터의 객체로 남겨두려고 함.
# 그래서 따로 그룹을 형성하는 함수를 만들려고 함.
# 리스트로 생성하려고 함. 처음에는 딕셔너리로 생성하려고 했지만 이미 필요한 정보들이 생성될 몬스터 객체에 들어있어서 리스트로 구성원 체크.
test_fl = 1
test_gd = 1


def monster_generation(floor_level, game_difficulty):  # 몬스터 인자 생성
    monster_name = ''
    named_monster_flag = 0  # 네임드 몬스터 결정하는 flag
    name_named_monster_list = ['우두머리 ', '대장 ']
    name_first_adjective_list = ['크고', '', '작고']
    name_second_adjective_list = ['강인한', '평범한', '나약한', '병든']
    name_monster_variation_list = ['주영', '경민', '영미', '민혜', '호기']

    name_first_adjective_int = random.randint(0, 2)
    name_second_adjective_int = random.randint(0, 3)
    name_monster_variation_int = random.randint(0, len(name_monster_variation_list)-1)

    check_named_monster_int = random.randint(0, 9)
    if check_named_monster_int == 0:  # 1/10 확률로 네임드 몬스터
        named_monster_flag = 1
    name_named_monster_int = random.randint(0, 1)
    if name_first_adjective_int == 1:
        monster_name = name_second_adjective_list[name_second_adjective_int] + ' '
    else:
        monster_name = name_first_adjective_list[name_first_adjective_int] + ' ' + name_second_adjective_list[
            name_second_adjective_int] + ' '
    if named_monster_flag == 1:
        monster_name += name_named_monster_list[name_named_monster_int]
    monster_name += name_monster_variation_list[name_monster_variation_int]

    monster_base_hp = random.randint(20, 30)  # 몬스터 기본체력
    monster_add_hp = ((3 - name_first_adjective_int) + (4 - name_second_adjective_int) + (
                len(name_monster_variation_list) - name_monster_variation_int) + floor_level) * 10 * game_difficulty  # 이름에 따른 추가 체력. 레벨상승시 lvl*10*난이도
    monster_total_hp = (monster_base_hp + monster_add_hp) * (named_monster_flag + 1)  # 네임드일 경우 체력 2배

    monster_base_power = random.randint(4, 6)  # 몬스터 기본파워
    monster_add_power = ((3 - name_first_adjective_int) + (4 - name_second_adjective_int) + (
                len(name_monster_variation_list) - name_monster_variation_int) + floor_level) * game_difficulty  # 이름에 따른 추가 파워. 레벨상승시 lvl*난이도
    monster_total_power = (monster_base_power + monster_add_power) * (named_monster_flag + 1)  # 네임드일 경우 2배의 파워

    # 일단은 mp랑 magic_power는 hp랑 normal_power그대로 가져옴.
    monster_base_mp = random.randint(40, 80)  # 몬스터 기본mp
    monster_add_mp = ((3 - name_first_adjective_int) + (4 - name_second_adjective_int) + (
                len(name_monster_variation_list) - name_monster_variation_int) + floor_level) * 10 * game_difficulty  # 이름에 따른 추가 체력. 레벨상승시 lvl*10*난이도
    monster_total_mp = (monster_base_hp + monster_add_mp) * (named_monster_flag + 1)  # 네임드일 경우 체력 2배

    monster_base_magic_power = random.randint(2, 4)  # 몬스터 기본파워
    monster_add_magic_power = ((3 - name_first_adjective_int) + (4 - name_second_adjective_int) + (
                len(name_monster_variation_list) - name_monster_variation_int) + floor_level) * game_difficulty  # 이름에 따른 추가 파워. 레벨상승시 lvl*난이도
    monster_total_magic_power = (monster_base_magic_power + monster_add_magic_power) * (
                named_monster_flag + 1)  # 네임드일 경우 2배의 파워

    monster_base_xp = random.randrange(4, 6)  # 몬스터 경험치
    monster_add_xp = ((3 - name_first_adjective_int) + (4 - name_second_adjective_int) + (
                len(name_monster_variation_list) - name_monster_variation_int) + floor_level) * game_difficulty  # 이름에 따른 추가 파워. 레벨상승시 lvl*난이도
    monster_total_xp = (monster_base_xp + monster_add_xp) * (named_monster_flag + 1)  # 네임드일 경우 2배의 파워
    # , monster_total_xp
    return Monster(monster_name, monster_total_hp, monster_total_power, monster_total_mp,
                    monster_total_magic_power, monster_total_xp)  # name, hp=100, normal_power=100, mp=50


def monster_group():  # 몬스터 리스트 생성
#def monster_group(game_difficulty, level):  # 몬스터 리스트 생성
    number_of_group = random.randint(1, 3) + (2) // 2  # 1~3마리 랜덤 생성 + 난이도와 도달한 층에 따라 그룹원 추가
    monster_list = []
    for index in range(number_of_group):
        new_monster = monster_generation(1, 1)  # Monster()안에 난이도와 계층 변수 필요.
        #new_monster = monster_generation(game_difficulty, level)  # Monster()안에 난이도와 계층 변수 필요.
        monster_list.append(new_monster)
    return monster_list


def monster_print(monster_list):
    for a in monster_list:
        a.show_status()
    return 1


#### ------------------------Monster 끝
#### -----------------------------------


#### --------------------------------------------------Job 시작
# 직업 - Warrior, Wizard, Archer, Tanker, Healer
# normal_attack은 Character쪽으로! -> MP사용하는 애들은 오버라이딩!

class Warrior(Party):
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, monster_list, party_list):
        magic_damage = random.randint(self.magic_power + 100, self.magic_power + 100)
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0)  # 스킬공격은 마나를 소모함
            for monsters in monster_list:
                monsters.hp = max(monsters.hp - magic_damage, 0)
            print(f"\n{YB}{self.name}의 휠윈드$!$!$ MP10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!{W}\n")
        else:
            print(f"\n{R}마나가 부족합니다.{W}\n")

    

class Wizard(Party):
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, monster_list, party_list):
        magic_damage = random.randint(self.magic_power - 4, self.magic_power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0)  # 스킬공격은 마나를 소모함
            for monsters in monster_list:
                monsters.hp = max(monsters.hp - magic_damage, 0)
            print(f"\n{YB}{self.name}의 메테오!&!&! MP10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!{W}\n ")
        else:
            print(f"\n{R}마나가 부족합니다.{W}\n")


class Archer(Party):
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 공격)
    def magic_attack(self, monster_list, party_list):
        magic_damage = random.randint(self.magic_power - 4, self.magic_power + 4)
        # 스킬공격
        if self.mp >= 10:
            self.mp = max(self.mp - 10, 0)  # 스킬공격은 마나를 소모함
            for monsters in monster_list:
                monsters.hp = max(monsters.hp - magic_damage, 0)
            print(
                f"\n{YB}{self.name}의 화살엄청!!!많이쏘기!!! MP10을 소모해 {len(monster_list)}마리의 몬스터에게 각각 {magic_damage}의 데미지를 입혔습니다!{W}\n")
        else:
            print(f"\n{R}마나가 부족합니다.{W}\n")


class Tanker(Party):
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 버프)
    def magic_attack(self, target, party_list):
        if self.mp >= 10:
            for party_member in party_list:
                party_member.normal_power += 10
                party_member.magic_power += 10
            print(f"\n{YB}{self.name}의 광역 버프!! 파티원의 모든 공격력 스탯이 상승했습니다!!^!^!^!^!^!{W}\n")
        else:
            print(f"\n{R}마나가 부족합니다.{W} \n")


class Healer(Party):
    # normal_attack은 Character클래스로 이동
    # 스킬 공격 (광역 힐)
    def magic_attack(self, target, party_list):
        if self.mp >= 10:
            for party_member in party_list:
                party_member.hp = party_member.max_hp
            print(f"\n{YB}{self.name}의 광역 회복!! 파티원의 모든 HP와 MP가 회복되었습니다!!**!!**!!**!!{W}\n")
        else:
            print(f"\n{R}마나가 부족합니다.{W}\n")

