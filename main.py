from random import randint


# 플레이어, 몬스터 부모 클래스
# 민경님
class Character:
    def __init__(self, name, hp, power, normal_attack, job):
        # 이름, hp, power, 일반 공격, 직업
        self.name = name
        self.hp = hp
        self.power = power
        self.normal_attack = normal_attack
        self.job = job
        self.alive = True

    def show_status(self):
        # 스탯 확인 코드
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
​
    def monster_group(self):
        pass
​
    # 몬스터 능력치 관리 코드
    def monster_level(self):
        # 다음 층으로 갈수록 몬스터가 강해 지며 수가 많아 집니다.
        pass


# 혜민님
class Player(Character):

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
        pass


# 미영
# 플레이어 생성
def create_players():
    # 직업 리스트 작성
    # [”전사”, “궁수”, "마법사", "탱커"]
    # 이름을 입력
    # 직업 리스트에서 직업을 고르기
    # return 이름, 직업
    pass


# 플레이어 정의 -> 누가 할 것인가!!!

# 미영
while True:
    # 플레이어의 스탯 확인
    # 몬스터 종류 선택(물, 불, 바람, 돌 중 하나 선택)
    # 몬스터 스탯 확인
    while True:
        # 플레이어 공격 선택 (일반 공격, 직업별 스킬, 아이템 사용, 스탯 확인(몬스터,플레이어))
        # 플레이어 공격
        # 몬스터 공격
        break
    break