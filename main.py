import random
import sys
# import Job as j

# 플레이어, 몬스터 부모 클래스
# 민경님
class Character:
    def __init__(self, name, hp=100, normal_power=100, mp=50):
        # 이름, hp, power, 일반 공격, 직업
        self.name = name
        self.max_hp = 100
        self.hp = max(hp, 0)
        self.mp = mp
        self.normal_power = normal_power
        self.alive = True

    def show_status(self):
        print(f"{self.name}의 정보 hp : {self.hp} / {self.max_hp}")
        pass

    # 내가 조아하는 우리 팀장님!!! 제일 뼈대가 되는 구간을 너무 잘 짜신 것 같아요!!! 도움이 필요하면 언제든지 부르겠습니닷^ㅇ^ 화이팅 팀장님~~ - 묭
    def normal_attack(self, target):  # 기본 공격
        if monster.hp > 0:
            print(f"{self.name}의 일반공격!")
            damage = random.randint(int(self.normal_power * 0.8), int(self.normal_power * 1.2))
            target.hp -= damage
            print(f"{target.name}에게 {damage}의 데미지를 입혔습니다.")

        if target.hp <= 0:
            print(f"{target.name}이 쓰러졌습니다.")

    def check_alive(self):
        # 죽었는 지 살았는 지 확인 하는 코드
        if self.hp == 0:
            self.alive = False



#기호님
class Monster(Character):
    # 몬스터 스킬 사용 코드 -> 랜덤을 사용 하거나, mp나 sp도 좋을 듯!
    def skill_attack(self):
        pass

    def monster_group(self):
        pass

    # 몬스터 능력치 관리 코드
    def monster_level(self):
        # 다음 층으로 갈수록 몬스터가 강해 지며 수가 많아 집니다.
        pass


# 혜민님
class Party(Character):
    def __init__(self, name, character, mp=100, hp=100):
        super().__init__(name, normal_power=1)
        self.character = character
        self.mp = mp
        self.exp = 0
        self.level = 1
        self.hp = hp

    def check_alive(self):
        # 죽었는 지 살았는 지 확인 하는 코드
        if self.hp <= 0:
            self.alive = False

    def show_choice_character(self):
        print(self.character)

    # 혜민님~~~ 여기 파트 엄청 많죠ㅠㅠ 저도 얼른 끝내고 도와 드리러 오겠습니당ㅎㅎㅎㅎ 화이팅 하시고 고민있으면 바로 디엠 고고!! 혜민님 메세지는 바로 달려가서 볼께요^ㅇ^ - 묭
    def item(self, num):
        # 강철검 : 착용 시 파워 5 증가
        # 갑옷 : 착용 시 HP 50 증가
        # HP 포션 : 획득(사용) 시 HP 전부 회복
        # MP 포션 : 획득(사용) 시 MP 전부 회복
        pass


    def success_hunt(self):
        # 몬스터 사냥에 성공 시 다음중 하나 또는 전부를 획득 합니다.
        # ex) 체력 50% 회복, 마나 전부 회복, 경험치 획득, 아이템 획득 등
        # 획득한 보상을 바탕으로 플레이어가 강해 지며 스토리에 따라 게임을 진행할 수 있습니다.
        pass

    def level_exp(self):
        level = 1
        exp = 0
        # 0 경험치에서 시작
        # 사냥할 때 마다 20씩 획득
        # 100경험치 달성시 레벨업!
        # 레벨업  -> 파워 2 증가, 체력 전부 회복
        # 다시 경험치는 0으로 설정
        pass


# 직업별 캐릭터 -> 부모의 부모인 Character 함수 사용 가능!
# 딕셔너리나 리스트로 정리해도 괜찮을 듯..? -> 튜터님께 질문!
class Job(Party):
    # 특수 스킬 공격
    # 영주님
    def skill_attack(self):
        # 파워 어택은 마법 공격보다 2배의 마력을 소모하지만 1.5배의 대미지를 줍니다.
        print(f"{self.character}연결완료")
        pass


# 미영
# 플레이어 생성
def create_party():
    # 이름을 입력
    party_name = input("파티 이름을 정해주세요. \n"
                        "파티 : ")

    return party_name


def select_job(num):
    # 직업 리스트 작성
    job_list = ["Archer", "Warrior", "Wizard", "Healer", "Tanker"]
    choice_job = []
    for i in range(num):
        # 직업 리스트에서 직업을 고르기
        character_jobs = input(f"{i+1}번째 캐릭터의 직업을 선택해주세요. \n"
                            f"1.Archer 2.Warrior 3.Wizard 4.Healer 5.Tanker \n"
                            f"직업(숫자) : ")
        if job_list[int(character_jobs) - 1] in choice_job:
            print("이미 선택한 캐릭터 입니다! \n 처음부터 다시 선택해주세요!")  # 지금은 처음부터 다시 시작이지만 후에 수정예정
            return select_job(num)
        else:
            choice_job.append(job_list[int(character_jobs) - 1])
    choice_job.sort()
    return choice_job


def select_monster():
    monster_style = ['몬스터(물)', '몬스터(불)', '몬스터(바람)', '몬스터(돌)']
    answer = input("상대할 몬스터의 속성을 선택해 주세요. \n"
                   "1.물, 2.불 3.바람 4.돌 \n"
                   "선택 번호 : ")
    return monster_style[int(answer) - 1]


def select_character():
    characters = party.character
    print('전투할 캐릭터를 선택해 주세요.')
    for i in range(len(party.character)):
        print(f"{i+1}.{characters[i]}")
    answer = input("선택한 캐릭터 : ")
    return characters[int(answer)-1]  # 캐릭터 딕셔너리에 키값으로 넣어서 return


def show_attack():
    answer = input("공격을 선택해 주세요. \n"
                   "1.일반공격 \n2.스킬공격 \n3.아이템 사용 \n4.스탯 확인 \n")
    if answer == "1":
        party.normal_attack(monster)
    elif answer == "2":
        # 직업별 스킬 사용 코드
        pass
    elif answer == "3":
        party.item(1)
    elif answer == "4":
        monster.show_status()
        return show_attack()
    else:
        print("잘못된 입력입니다.")
        return show_attack()


def check_answer():
    answer = input("1.예 2.아니오 \n"
                   "선택 : ")
    if answer == "1":
        return "success"
    elif answer == "2":
        print("게임을 종료합니다.")
        return "false"
    else:
        print("잘못된 선택입니다.")
        return check_answer()


character_list = {
    'Warrior': Job(character='Warrior', name="Warrior"),
    'Wizard': Job(character='Wizard', name="Wizard"),
    'Archer': Job(character='Archer', name="Archer"),
    'Tanker': Job(character='Tanker', name="Tanker"),
    'Healer': Job(character='Healer', name="Healer"),
            }


# 파티 이름 정의 -> 미영
party_name = create_party()  # 파티이름
# 플레이 할 캐릭터 수 설정 코드
party_member = input("사용할 캐릭터 수를 적어 주세요.(최대 5명)\n"
                    "answer : ")
character_job = select_job(int(party_member))  # 캐릭터의 job 설정
print(character_job)
party = Party(party_name, character_job, hp=len(character_job))  # part 정의 / 파티명, 선택 캐릭 이름 리스트
party.show_choice_character()  # 선택한 캐릭터를 보여줌
print(party.hp)


# 미영
while True:
    # 몬스터 종류 선택(물, 불, 바람, 돌 중 하나 선택)
    choice_monster = select_monster()
    monster = Monster(choice_monster)
    # 몬스터 스탯 확인
    monster.show_status()
    while True:
        # 플레이어 공격할 캐릭터 선택
        choice_character = select_character()
        attack_choice_character = character_list[choice_character] # choice_character를 key값으로 사용해 직업 정의
        # attack_choice_character.skill_attack()  # 이게 된다고..?
        # 플레이어 공격 선택 (일반 공격, 직업별 스킬, 아이템 사용, 스탯 확인(몬스터,플레이어))
        show_attack()  # 플레이어 공격 포함한 함수
        # 몬스터 공격
        monster.normal_attack(attack_choice_character)  # 유저의 캐릭터들이 모두 피가 0이되면 유저 사망.
        attack_choice_character.check_alive()
        monster.check_alive()
        if not attack_choice_character.alive:
            party.hp -= 1  # 파티의 hp는 캐릭터 수와 같음!
            party.character.remove(attack_choice_character.name)
        if party.hp <= 0:
            print("모든 캐릭터가 사망했습니다.")
            break
        # if party.character == party.die_character :
        #     print("모든 캐릭터가 사망했습니다. 게임을 종료합니다.")
        #     break
        if monster.hp > 0:
            print("다시 공격하시겠습니까?")
            re_attack = check_answer()
            if re_attack == "success":
                continue
            else:
                break

    break