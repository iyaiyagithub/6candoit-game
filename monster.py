import random
#나중에 합치면서 없애면 될 것 같아요.
# monster_list = [Monster("고블린", 100, 10), Monster("트롤", 200, 20)]
# 기호님 너무 멋져요!! 코드 너무 좋아요ㅜㅜ 밸런스도 신경 쓰신 거 같아서 너무 완벽합니닷^ㅇ^ 조금만 더 화이팅 해봐용! - 묭

class Character:
    def __init__(self, name, hp=100, power=1, normal_attack=50):
        # 이름, hp, power, 일반 공격, 직업
        self.name = name
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
#1. 일단 기본 몬스터 설정.
# def check_mp(mp, mp_required):
#     if mp < mp_required:
#         return -1

class Monster(Character):
    # 몬스터 스킬 사용 코드 -> 랜덤을 사용 하거나, mp나 sp도 좋을 듯!
    # 1차 목표 스킬 구현.
    # 가능하면 여러 가지 스킬 구현.
    def __init__(self, game_difficulty, floor_level): #normal attack 제거 job도 일단 제거
        # 이름, hp, power, 일반 공격, 직업
        # 따로 함수로..고민중!()
        monster_name =''
        named_monster_flag = 0 #네임드 몬스터 결정하는 flag
        name_named_monster_list = ['우두머리', '대장']
        name_first_adjective_list = ['크고','', '작고']
        name_second_adjective_list = ['강인한','평범한', '나약한', '병든']
        name_monster_variation_list = ['멧돼지','돼지','닭']

        name_first_adjective_int = random.randrange(0,3)
        name_second_adjective_int = random.randrange(0,4)
        name_monster_variation_int = random.randrange(0,3)
        
        check_named_monster_int = random.randint(0,9)
        if check_named_monster_int == 0: #1/10 확률로 네임드 몬스터
            named_monster_flag = 1
        name_named_monster_int = random.randrange(0,2) 
        
        monster_name = name_first_adjective_list[name_first_adjective_int]+' '+name_second_adjective_list[name_second_adjective_int]+' '
        if named_monster_flag == 1 :
            monster_name += name_named_monster_list[name_named_monster_int]
        monster_name += name_monster_variation_list[name_monster_variation_int]

        monster_base_hp = random.randrange(80,121) #몬스터 기본체력
        monster_add_hp = ((3-name_first_adjective_int)+(4-name_second_adjective_int)+(3-name_monster_variation_int)+floor_level)*10*game_difficulty #이름에 따른 추가 체력. 레벨상승시 lvl*10*난이도
        monster_total_hp = (monster_base_hp+monster_add_hp)*(named_monster_flag+1) #네임드일 경우 체력 2배

        monster_base_power = random.randrange(8,13) #몬스터 기본파워
        monster_add_power = ((3-name_first_adjective_int)+(4-name_second_adjective_int)+(3-name_monster_variation_int)+floor_level)*game_difficulty #이름에 따른 추가 파워. 레벨상승시 lvl*난이도
        monster_total_power = (monster_base_power+monster_add_power)*(named_monster_flag+1) #네임드일 경우 2배의 파워
        
        self.name = monster_name
        self.hp = monster_total_hp
        self.power = monster_total_power
        # self.normal_attack = normal_attack
        # self.job = job
        self.alive = True

    # Character class에 추가 예정!
    def normal_attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        print(f"{other.name}의 남은 체력은 {other.hp}")
        if other.hp == 0:
            self.alive = False
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other, skill_type):
        # 랜덤 추가 고려중!~~~^ㅇ^
        if skill_type == 1: # 1은 약한 스킬 2는 강한 스킬 3은 회복. 3이 획복이라면 함수 이름 변경 필요할 듯.
            damage = random.randint(self.power, self.power*2+1) #데미지가 power ~ power*2
            if self.mp < 10:
                self.normal_attack(other)
            else:
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                print(f"{other.name}의 남은 체력은 {other.hp}")
                if other.hp == 0:
                    self.alive = False
                    print(f"{other.name}이(가) 쓰러졌습니다.")
        elif skill_type == 2:
            damage = random.randint(self.power*2, self.power*3+1) #데미지가 power*2 ~ power*3
            if self.mp < 20:
                self.normal_attack(other)
            else:
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                print(f"{other.name}의 남은 체력은 {other.hp}")
                if other.hp == 0:
                    self.alive = False
                    print(f"{other.name}이(가) 쓰러졌습니다.")
        elif skill_type == 3:
            heal = random.randint(self.power//2, self.power+1) #1/2~1만큼 회복
            if self.mp < 10:
                self.normal_attack(other)
            else:
                self.hp += heal
                print(f"{self.name}이 {heal}만큼 회복해 hp가 {self.hp}가 되었다!")
#몬스터를 그룹화 해서 묶어주기. 아마 리스트나 딕셔너리로 구현하게 될 것 같음.
#Monster 클래스는 단일 몬스터의 객체로 남겨두려고 함.
#그래서 따로 그룹을 형성하는 함수를 만들려고 함.
#리스트로 생성하려고 함. 처음에는 딕셔너리로 생성하려고 했지만 이미 필요한 정보들이 생성될 몬스터 객체에 들어있어서 리스트로 구성원 체크.
def monster_group(game_difficulty, floor_level):
    number_of_group = random.randint(1,3)+(game_difficulty+floor_level)//2 # 1~3마리 랜덤 생성 + 난이도와 도달한 층에 따라 그룹원 추가
    group_list = []
    for index in range(number_of_group):
        new_monster = Monster(3,3) #Monster()안에 난이도와 계층 변수 필요.
        group_list.append(new_monster)