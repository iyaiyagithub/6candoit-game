import character as ch
import random

# import sys
# 출력 색상 변경
R = "\033[91m"
B = "\033[94m"
W = "\033[0m"
G = "\033[92m"


# 타입 체크하는 함수
def check_type(required_type, input_type):
    if required_type != input_type:
        print('잘못된 타입을 입력하셨습니다. 다시 입력해 주세요.')
        # 재입력하는 함수 필요.
        return True
    else:
        # 통과했으니 그냥 그대로 가게 하면 될듯.
        return False


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
        character_jobs = input(f"{i + 1}번째 캐릭터의 직업을 선택해주세요. \n"
                               f"1.Archer 2.Warrior 3.Wizard 4.Healer 5.Tanker \n"
                               f"직업(숫자) : ")
        if job_list[int(character_jobs) - 1] in choice_job:
            print("이미 선택한 캐릭터 입니다! \n 처음부터 다시 선택해주세요!")  # 지금은 처음부터 다시 시작이지만 후에 수정예정
            return select_job(num)
        else:
            choice_job.append(job_list[int(character_jobs) - 1])
    choice_job.sort()
    return choice_job


# def select_monster():
#     ch.
#     monster_style = ['몬스터(물)', '몬스터(불)', '몬스터(바람)', '몬스터(돌)']
#     answer = input("상대할 몬스터의 속성을 선택해 주세요. \n"
#                    "1.물, 2.불 3.바람 4.돌 \n"
#                    "선택 번호 : ")
#     return monster_style[int(answer) - 1]


def select_character():
    characters = party.character
    print('전투할 캐릭터를 선택해 주세요.')
    for i in range(len(party.character)):
        print(f"{i + 1}.{characters[i]}")
    answer = input("선택한 캐릭터 : ")
    return characters[int(answer) - 1]  # 캐릭터 딕셔너리에 키값으로 넣어서 return


def show_attack():
    answer = input("공격을 선택해 주세요. \n"
                   "1.일반공격 \n2.스킬공격 \n3.아이템 사용 \n4.스탯 확인 \n")
    print(monster)
    if answer == "1":
        attack_choice_character.normal_attack(monster_list[0])
    elif answer == "2":
        # 직업별 스킬 사용 코드
        attack_choice_character.magic_attack(monster_list)
    elif answer == "3":
        party.item()
    elif answer == "4":
        monster.show_status()
        return show_attack()
    else:
        print("잘못된 입력입니다.")
        return show_attack()


def check_answer(num=0):
    if num == 1:
        answer = input("파티원 : ")
        if int(answer) > 5 or int(answer) < 1:
            print("범위를 벗어났습니다.")
            return check_answer(1)
        else:
            return int(answer)
    if num == 0:
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
    'Warrior': ch.Warrior(name="Warrior", character="Warrior", hp=3000, mp=500, normal_power=300, magic_power=50),
    # 'Wizard': ch.Wizard(name="Warrior",character="Warrior",hp=300,mp=50,normal_power=30,magic_power=5),
    # 'Archer': ch.Archer(name="Warrior",character="Warrior",hp=300,mp=50,normal_power=30,magic_power=5),
    # 'Tanker': ch.Tanker(name="Warrior",character="Warrior",hp=300,mp=50,normal_power=30,magic_power=5),
    # 'Healer': ch.Healer(name="Warrior",character="Warrior",hp=300,mp=50,normal_power=30,magic_power=5),
}

game_end = 0  # 안쪽 while문이 break되어 게임을 끝내고 싶을 때 +1

monster_list = ch.monster_group()

# 파티 이름 정의 -> 미영
party_name = create_party()  # 파티이름
# 플레이 할 캐릭터 수 설정 코드
print("사용할 캐릭터 수를 적어주세요.(최대 5명)")
party_member = check_answer(1)
character_job = select_job(party_member)  # 캐릭터의 job 설정
party = ch.Party(party_name, character_job, hp=int(party_member))  # part 정의 / 파티명, 선택 캐릭 이름 리스트
party.show_choice_character()  # 선택한 캐릭터를 보여줌

# 미영
while True:
    if game_end == 1:
        break
    # 몬스터 종류 선택(물, 불, 바람, 돌 중 하나 선택)
    # choice_monster = select_monster()
    # monster = ch.Monster(choice_monster)
    monster = ch.monster_generation(3, 3)
    # 몬스터 스탯 확인
    ch.monster_print(monster_list)
    while True:
        # 플레이어 공격할 캐릭터 선택
        choice_character = select_character()
        attack_choice_character = character_list[choice_character]  # choice_character를 key값으로 사용해 직업 정의
        # attack_choice_character.skill_attack()  # 이게 된다고..?
        # 플레이어 공격 선택 (일반 공격, 직업별 스킬, 아이템 사용, 스탯 확인(몬스터,플레이어))
        show_attack()  # 플레이어 공격 포함한 함수
        ch.monster_print(monster_list)
        if len(monster_list) == 0:
            print("모든 몬스터를 사냥하셨습니다.")
            game_end += 1
            break
        # 몬스터 공격
        if monster_list[0].hp > 0:
            attack_type = random.randint(1, 2)
            if attack_type % 2 == 0:  # 일단은 그냥 스킬 쓸 확률 1/2로 해놨습니다.
                monster_list[0].normal_attack(attack_choice_character)  # 유저의 캐릭터들이 모두 피가 0이되면 유저 사망.
            else:
                monster_list[0].skill_attack(attack_choice_character)
        attack_choice_character.check_alive()
        monster.check_alive()
        if monster_list[0].hp <= 0:
            del monster_list[0]
        if not attack_choice_character.alive:
            party.hp -= 1  # 파티의 hp는 캐릭터 수와 같음!
            party.character.remove(attack_choice_character.name)
        if party.hp <= 0:
            print("모든 캐릭터가 사망했습니다.")
            game_end = 1
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
                game_end = 1
                break
        else:
            print("사냥에 성공하셨습니다!")
            print("다음 단계에 도전 하시겠습니까?")
            next_level = check_answer()
            if next_level == "success":
                party.level += 1
                print(party.level)
                break  # 밖의 while문으로 이동
            else:
                game_end = 1
                break

'''
def check_type(required_type, input_type):
    if required_type != input_type:
        print('잘못된 타입을 입력하셨습니다. 다시 입력해 주세요.')
        # 재입력하는 함수 필요. 
        return False
    else:
        #통과했으니 그냥 그대로 가게 하면 될듯.
        return True

do{

    }
while(check_type(변수1, 변수2))

# True or False로 해서 True가 될 때까지 반복문 돌려도 될 것 같음.

'''