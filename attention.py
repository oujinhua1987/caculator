# flop/turn/river boardcards handtype HeroPosition holdcards  stack   villanPosition  potBB villanAction betsize potodd
import outs_calculator
class attention:

# street pre/flop/turn/river

    def getStreet(self):
        street=0
        boardcards = []
        if len(boardcards)==0:
            street='pre'
        elif len(boardcards)==3:
            street='flop'
        elif len(boardcards) == 4:
            street = 'turn'
        elif len(boardcards) == 5:
            street = 'river'


        return street

# villan position
    def getVillanPosition(self) :
        villanPosition=0
        return villanPosition
# villan stack
    def getVillanStack(self):
        villanStack=0

        return villanStack

# villan stats
    def getVillanStats(self):
        villanStats=0

        return villanStats

# my position
    def getHeroPosition(self):
        heroPosition=0
        return heroPosition

# my Hands
    def getMyHands(self):
        myHands=0
        return myHands


#handtype
    def getHandType(self):

        oc = outs_calculator.Outs_Calculator()
        my_cards = self.getMyHands()
        # cards_on_table = ['9S', '8H', '6C','TC','KC']
        cards_on_table = ['TH', '8H', 'JD']
        # self.assertEqual(oc.evaluate_hands(my_cards, cards_on_table, oc), 0)
        # oc.hand = my_cards + cards_on_table
        hand_type = oc.hand_type(my_cards, cards_on_table, oc)
        print(hand_type)

        return hand_type

#stack
    def getMyStack(self):
        myHands=0
        return myHands

#3way or 1 on 1
    def getNumberOfPlayerInPool(self):
        number=0
        return number
#potBB
    def getPot(self):
        pot=0
        return pot



#potOdd
    def getPotOdd(self):
        potOdd=0
        return potOdd


#strategy
    def getStrategy(self):
        strategy=0
        return strategy

#frequency
    def getFrequency(self):
        attackFrequency=0
        bluffFrequency=0
        hearCallFrequency=0
        actionFrequency = 0
        return actionFrequency

# betsize
    def getBetSize(self):
        betSize = 0
        return betSize


#action
    def getVillanAction(self):
        villanAction=0
        return villanAction

    def getMyAction(self):
        # what My path represents
        myAction=0
        return myAction

# timingTell
    def getVillanTimingTell(self):
        tankingTime=0
        return tankingTime






