import character as ch
import random
# import sys
# 출력 색상 변경
R = "\033[91m"
B = "\033[94m"
W = "\033[0m"
G = "\033[92m"
M = "\033[95m"

YB = "\033[103m"

# 미영
# 플레이어 생성
def create_party():
    # 이름을 입력
    #이렇게 하면 {B}뒷부분이 파란색이 되구요. {W} 이거는 하얀색이d에요. 그니까 흰색으로 다시 되돌려주려면 {W}를 쓰면돼용
    party_name = input(f"\n{B}파티 이름을 정해주세요. {W}\n"
                        f"파티 : ")

    return party_name

def select_job(num):
    # 직업 리스트 작성
    job_list = ["Warrior", "Wizard", "Archer", "Tanker", "Healer"]
    choice_job = []
    while True: #오류안나게 하는 코드
        try: 
            if int(num) > 5 or int(num) < 1:
                print(f"{R}범위를 벗어났습니다.{W}")
                num = input()
            else:
                break

        except ValueError:
            print(f'{R}숫자를 입력하셔야 합니다.{W}')
            num = input()
    for i in range(num):
        # 직업 리스트에서 직업을 고르기
        character_jobs = input(f"\n{B}{i + 1}번째 캐릭터의 직업을 선택해주세요. {W}\n"
                                f"1.Warrior 2.Wizard 3.Archer 4.Tanker 5.Healer{W} \n"
                                f"직업(숫자) : ")
        if job_list[int(character_jobs) - 1] in choice_job:
            print(f"{R}이미 선택한 캐릭터 입니다! \n 처음부터 다시 선택해주세요!{W}")  # 지금은 처음부터 다시 시작이지만 후에 수정예정
            return select_job(num)
        else:
            choice_job.append(job_list[int(character_jobs) - 1])
    return choice_job

def select_character():
    characters = party.character
    print(characters)
    print(f'\n{B}캐릭터를 선택해 주세요.{W}')
    for i in range(len(party.character)):
        print(f"{i + 1}.{characters[i]}")
    
    answer = input(f"선택한 캐릭터 : ")
    while True: #오류수정 코드
        try:
            if int(answer) > 5 or int(answer) < 1:
                print(f"{R}범위를 벗어났습니다.{W}")
                return select_character()
            else:
                break

        except ValueError:
            print(f'\n{R}숫자를 입력하셔야 합니다.{W}\n')
            answer = input()
    return characters[int(answer) - 1]  # 캐릭터 딕셔너리에 키값으로 넣어서 return

def show_attack():
    test = []
    for i in party.character:  #["Warrior", "Archer"]
        test.append(character_list[i])
    answer = input(f"\n{B}공격을 선택해 주세요. {W}\n"
                    f"1.일반공격 \n2.스킬공격 \n3.아이템 사용 \n4.스탯 확인 \n 선택 번호 :  ")
    if answer == "1":
        attack_choice_character.normal_attack(monster_list[0])
    elif answer == "2":
        # 직업별 스킬 사용 코드
        attack_choice_character.magic_attack(monster_list, test)
    elif answer == "3":
        while(True): #문자 입력해도 안 튕기게.
            select_item = input(
                        f"\n1.steelsword (공격력 증가)\n"
                        f"2.armor (방어력 증가)\n"
                        f"3.hp_portion (HP 회복)\n"
                        f"4.mp_portion (MP 회복)\n\n"
                        f"{B}아이템을 선택해주세요 : {W}")
            try:
                select_item = int(select_item)
                break
            except ValueError:
                print(f'{R}숫자를 입력하셔야 합니다.{W}')         
        if int(select_item) == 1:
            ch.steelsword(attack_choice_character)
        elif int(select_item) == 2:
            ch.armor(attack_choice_character)
        elif int(select_item) == 3:
            ch.hp_portion(attack_choice_character)
        else:
            ch.mp_portion(attack_choice_character)
    elif answer == "4":
        attack_choice_character.show_status()
        monster.show_status()
        return show_attack()
    else:
        print(f"\n{R}잘못된 입력입니다.{W}\n")
        return show_attack()


#이제는 숫자아닌거 입력해도 안 튕겨요.
def check_answer(num=0):
    if num == 1:
        while True:
            answer = input("파티원 : ")
            try:
                if int(answer) > 5 or int(answer) < 1:
                    print(f"\n{R}범위를 벗어났습니다.{W}\n")
                    return check_answer(1)
                else:
                    return int(answer)
            except ValueError:
                print(f'\n{R}숫자를 입력하셔야 합니다.{W}\n')
                
    elif num == 0:
        answer = input("1.예 2.아니오 \n"
                        "선택 : ")
        if answer == "1":
            return "success"
        elif answer == "2":
            print(f"{R}게임을 종료합니다.{W}")
            return "false"
        else:
            print(f"\n{R}잘못된 선택입니다.{W}\n")
            return check_answer()

character_list = {
    'Warrior': ch.Warrior(name="Warrior", character="Warrior", hp=300, mp=50, normal_power=30, magic_power=20),
    'Wizard': ch.Wizard(name="Wizard",character="Wizard",hp=150,mp=100,normal_power=10,magic_power=40),
    'Archer': ch.Archer(name="Archer",character="Archer",hp=200,mp=80,normal_power=20,magic_power=10),
    'Tanker': ch.Tanker(name="Tanker",character="Tanker",hp=500,mp=30,normal_power=20,magic_power=5),
    'Healer': ch.Healer(name="Healer",character="Healer",hp=150,mp=100,normal_power=5,magic_power=30),
}

game_end = 0  # 안쪽 while문이 break되어 게임을 끝내고 싶을 때 +1

monster_list = ch.monster_group()

# 파티 이름 정의 -> 미영
party_name = create_party()  # 파티이름
# 플레이 할 캐릭터 수 설정 코드
print(f"\n{B}사용할 캐릭터 수를 적어주세요.(최대 5명){W}")
party_member = check_answer(1)
character_job = select_job(party_member)  # 캐릭터의 job 설정
party = ch.Party(party_name, character=character_job, hp=int(party_member),mp=1,normal_power=1,magic_power=1)  # part 정의 / 파티명, 선택 캐릭 이름 리스트
party.show_choice_character()  # 선택한 캐릭터를 보여줌
# 미영
while True:
    if game_end == 1:
        break
    # choice_monster = select_monster()
    # monster = ch.Monster(choice_monster)
    monster = ch.monster_generation(3, 3)
    # 몬스터 스탯 확인
    ch.monster_print(monster_list)
    while True:
        # 플레이어 공격할 캐릭터 선택
        if len(monster_list) == 0:
            print(f"{YB}모든 몬스터를 사냥하셨습니다.{W}")
            print(f"다음 단계에 도전 하시겠습니까?")
            monster_list = ch.monster_group()
            get_exp = check_answer()
            if get_exp == "success":
                test = []
                for i in party.character:  #["Warrior", "Archer"]
                    test.append(character_list[i])
                party.exp += 50
                check_level = party.level_exp(test)
                ch.success_hunt_items(test) 
            else:
                game_end = 1
                break
        choice_character = select_character()
        attack_choice_character = character_list[choice_character]  # choice_character를 key값으로 사용해 직업 정의
        # attack_choice_character.skill_attack()  # 이게 된다고..?
        # 플레이어 공격 선택 (일반 공격, 직업별 스킬, 아이템 사용, 스탯 확인(몬스터,플레이어))
        show_attack()  # 플레이어 공격 포함한 함수
        ch.monster_print(monster_list)
        # 몬스터 공격
        if monster_list[0].hp > 0:
            attack_type = random.randint(1, 2)
            if attack_type % 2 == 0:  # 일단은 그냥 스킬 쓸 확률 1/2로 해놨습니다.
                monster_list[0].normal_attack(attack_choice_character)  # 유저의 캐릭터들이 모두 피가 0이되면 유저 사망.
            else:
                monster_list[0].skill_attack(attack_choice_character)
        attack_choice_character.check_alive()
        monster.check_alive()
        # if monster_list[0].hp <= 0:
        #     del monster_list[0]
        remember_size = len(monster_list)
        remember_index = 0
        try:
            alive_monster =[]
            for index in range(remember_size): # for 로 돌리는게 잘 안돼서 죽은 애들을 표시하고 살아있는 애들을 새 리스트에 추가하고 원래 리스트에 덮어씌움.
                if monster_list[index].hp <= 0:
                        monster_list[index].alive = False
            for index in range(remember_size):
                if monster_list[index].alive == True:
                    alive_monster.append(monster_list[index])
                        # monster_list.remove(monster_list[index])
            monster_list = alive_monster
        except:
            new_remember_index = 0
            for index in range(remember_size-remember_index): # 광역공격 받아서 다 죽으면 다 지워버릴 수 있게 바꿔봄. 될지는 미지수. # 만약에 monster_list에 있는게 삭제가 되면 for는 그 삭제된 이후걸 불러오나 아니면 그 이후이후걸 불러오나? index상으로는 그 이후이후여야 함.
                if monster_list[index].hp <= 0:
                    monster_list.remove(monster_list[index])
                    new_remember_index += 1
            remember_index = new_remember_index
                
        if not attack_choice_character.alive:
            party.hp -= 1  # 파티의 hp는 캐릭터 수와 같음!
            party.character.remove(attack_choice_character.name)
        if party.hp <= 0:
            print(f"{YB}모든 캐릭터가 사망했습니다.{W}")
            game_end = 1
            break
        if len(monster_list) > 0:
            print(f"\n다시 공격하시겠습니까?\n")
            re_attack = check_answer()
            if re_attack == "success":
                continue
            else:
                game_end = 1
                break
