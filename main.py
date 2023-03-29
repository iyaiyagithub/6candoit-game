from random import randint
# import Job as j

# 플레이어, 몬스터 부모 클래스
# 민경님
class Character:
    def __init__(self, name, hp=100, power=1, normal_attack=50):
        # 이름, hp, power, 일반 공격, 직업
        self.name = name
        self.max_hp = 100
        self.hp = hp
        self.power = power
        self.normal_attack = normal_attack
        self.character = []  # 캐릭터 리스트 -> 유저, 몬스터 둘다 사용 가능??
        self.alive = True

    def show_status(self):
        # 스탯 확인 코드
        print(f"나는 스탯 확인 칸입니다!!!\n")
        pass

    def check_alive(self):
        # 죽었는 지 살았는 지 확인 하는 코드
        pass

    def attack(self, target):
        # 기본 공격 코드
        pass


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
class Player(Character):
    def __init__(self, name, character):
        super().__init__(name)
        self.character = character

    def show_choice_character(self):
        print(self.character)

    def item(self):
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
class Job(Player):
    # 특수 스킬 공격
    # 영주님
    def skill_attack(self):
        # 파워 어택은 마법 공격보다 2배의 마력을 소모하지만 1.5배의 대미지를 줍니다.
        print(f"{self.character}연결완료")
        pass


# 미영
# 플레이어 생성
def create_players():
    # 이름을 입력
    users_name = input("플레이어의 닉네임을 정해주세요. \n"
                        "닉네임 : ")

    return users_name


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
    characters = player.character
    print('전투할 캐릭터를 선택해 주세요.')
    for i in range(len(player.character)):
        print(f"{i+1}.{characters[i]}")
    answer = input("선택한 캐릭터 : ")
    return characters[int(answer)-1]  # 캐릭터 딕셔너리에 키값으로 넣어서 return


def show_attack():
    answer = input("공격을 선택해 주세요."
                   "1.일반공격 \n2.스킬공격 \n3.아이템 사용 \n4.스탯 확인 \n")
    if answer == "1":
        player.attack(monster)
    elif answer == "2":
        # 직업별 스킬 사용 코드
        pass
    elif answer == "3":
        player.item()
    elif answer == "4":
        player.show_status()
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
    'Warrior': Job(character='Warrior', name="전사"),
    'Wizard': Job(character='Wizard', name="마법사"),
    'Archer': Job(character='Archer', name="궁수"),
    'Tanker': Job(character='Tanker', name="탱커"),
    'Healer': Job(character='Healer', name="힐러"),
            }


# 플레이어 정의 -> 미영
player_name = create_players()  # 플레이어 이름
# 플레이 할 캐릭터 수 설정 코드
play_member = input("사용할 캐릭터 수를 적어 주세요.(최대 5명)\n"
                    "answer : ")
character_job = select_job(int(play_member))  # 캐릭터의 job 설정
player = Player(player_name, character_job)  # name
player.show_choice_character()


# 미영
while True:
    # 플레이어의 스탯 확인
    player.show_status()
    # 몬스터 종류 선택(물, 불, 바람, 돌 중 하나 선택)
    choice_monster = select_monster()
    monster = Monster(choice_monster)
    # 몬스터 스탯 확인
    monster.show_status()
    while True:
        # 플레이어 공격할 캐릭터 선택
        choice_character = select_character()
        attack_choice_character = character_list[choice_character] # choice_character를 key갑으로 사용해 직업 정의
        attack_choice_character.skill_attack()  # 이게 된다고..?
        # 플레이어 공격 선택 (일반 공격, 직업별 스킬, 아이템 사용, 스탯 확인(몬스터,플레이어))
        show_attack()  # 플레이어 공격 포함한 함수
        # 몬스터 공격
        monster.attack(player)
        player.check_alive()
        monster.check_alive()
        if monster.hp > 0:
            print("다시 공격하시겠습니까?")
            re_attack = check_answer()
            if re_attack == "success":
                continue
            else:
                break
    break


