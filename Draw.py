import random

'''
덱 클래스의 generate()에서 마지막 shuffle을 삭제하고 작성함
싱글 플레이일 때 게임 클래스나 어디에서 덱을 셔플 해주고 시작해야함. 
덱 안에 스킬 카드가 뒤로 오도록 하기 
'''

class Draw:
    '''
    스토리 모드에서 처음 플레이어들에게 카드를 draw하는 부분
    Parameter: deck -> list, stage -> string
    Return: None
    '''
    def __init__(self, deck, stage):
        self.deck = deck
        self.cards = []

        if stage == '1':
            random.shuffle(self.deck.cards[:66]) # 리스트 앞 쪽 숫자 카드 셔플
            random.shuffle(self.deck.cards[67:]) # 리스트 뒷 쪽 기술카드 셔플 
            for _ in range(5):
                probability = random.uniform(0, 1)
                if probability < 0.6:
                    card = self.deck.cards.pop() # 뒷쪽의 기술카드 pop
                else:
                    self.deck.cards.remove(self.deck.cards[0])
                    card = self.deck.cards.pop(0) # 앞 쪽의 숫자카드 pop
                if card:
                    self.cards.append(card)
        elif stage == '2':
            for _ in range(26): # 총 카드수 108개 중 현재카드 1개를 빼고 플레이어들에게 모두 나눠줌.
                card = self.deck.pop()
                self.cards.append(card)
        elif stage == '3':
            for _ in range(5):
                card = self.deck.pop()
                self.cards.append(card)
        elif stage == '4':
            pass
