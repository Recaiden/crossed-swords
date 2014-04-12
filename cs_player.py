import random

import cs_moves

RESISTANCE_VALUE = 3
AI_NAMES = ['Humber', 'Celanda', 'Coriolis','Dolores',
            'Waradlis','Venera','Goleanda','Hantelen',
            'Joseph','Kinsworth','Litrian','Queryon',
            'Perrinilt','Eddington', 'Nadriguea', 'Kosso']
current_ai_names = AI_NAMES[:]

def reset_names():
    global current_ai_names
    current_ai_names = AI_NAMES[:]

class Player(object):
    def __init__(self):
        self.hp = 20
        self.vp = 0
        self.focus_target = None
        self.dodge_target = None
        self.halted = 0
        self.resistance = None
        self.immunity = None
        self.vulnerable = (None, 0)
        self.resistance_expiring = 0
        self.focus_expiring = 0
        self.name = "NULL PLAYER"
        self.halters = []
        self.attackers = []
        self.armour = 0

        
    # Damage from Attack moves
    def damage(self, amount, target=None):
        if self.immunity == target and target is not None:
            return 0
        damage = amount - self.armour
        if self.resistance == target and target is not None:
            damage -= RESISTANCE_VALUE
        if self.vulnerable[0] == target:
            damage += self.vulnerable[1]
        damage = max(0, damage)
        self.hp -= damage
        return damage

    # Damage from Defense or Move Moves
    def damageCounter(self, amount, target=None):
        return self.damage(amount, target)

    def damageAP(self, amount, target=None):
        self.hp -= amount
        return amount

    def heal(self, amount):
        self.hp += amount

    def drain(self, amount):
        if amount > self.vp:
            drained = self.vp
            self.vp = 0
            return drained
        else:
            self.vp -= amount
            return amount

    def addVP(self, amount):
        self.vp += amount

    def setVulnerable(self, target, amount):
        self.vulnerable = (target, amount)

    def setImmunity(self, target):
        self.immunity = target

    def addAttacker(self, attacker):
        self.attackers.append(attacker)

    def setArmour(self, amount):
        self.armour += amount

    def newRound(self):
        self.attackers = []
        self.halters = []
        self.resistance_expiring -= 1
        self.focus_expiring -= 1
        self.vulnerable = (None, 0)
        self.halted = 0
        self.dodge_target = None
        self.immunity = None
        self.armour = 0
        if self.resistance_expiring <= 0:
            self.resistance = None
        if self.focus_expiring <=0:
            self.focus_target = None

class PlayerAI(Player):
    def __init__(self, name):
        super(PlayerAI, self).__init__()
        self.name = name


class PlayerHuman(Player):
    def __init__(self, name):
        super(PlayerHuman, self).__init__()
        self.name = name

class AI(object):
    def __init__(self):
        name = random.choice(current_ai_names)
        current_ai_names.remove(name)
        self.player = PlayerAI("AI - %s"%name)

    def act(self):
        def targetAtRandom(move):
            target = self.player
            while target == self.player or target in self.dead_list:
                target = random.choice(self.player_list)
            return move(self.player, self.player_list, target)

        def beAggressive(self):
            if len(self.player_list) - len(self.dead_list) >= 5:
                return targetAtRandom(cs_moves.Assail)
            elif len(self.player_list) - len(self.dead_list) >= 3:
                return targetAtRandom(cs_moves.Lunge)
            else:
                return targetAtRandom(cs_moves.Strike)

        def beDefensive(self):
            if random.randint(0, 10) > 7:
                return targetAtRandom(cs_moves.Taunt)
            if random.randint(0, 10) > 7:
                return cs_moves.Mend(self.player, self.player_list, self.player)
            if len(self.player_list) - len(self.dead_list) >= 5:
                return targetAtRandom(cs_moves.Dodge)
            elif len(self.player_list) - len(self.dead_list) >= 3:
                return targetAtRandom(cs_moves.Block)
            else:
                return targetAtRandom(cs_moves.Riposte)
        def beActive(self):
            target = self.player
            while target == self.player or target in self.dead_list:
                target = random.choice(self.player_list)
            if target.vp >= self.player.vp:
                return cs_moves.Taunt(self.player, self.player_list, target)
            elif False:
                return targetAtRandom(cs_moves.Focus)
            else:
                return targetAtRandom(cs_moves.Halt)
    
        # Make use of the Focus
        if self.player.focus_target is not None:
            return cs_moves.Lunge(self.player, self.player_list, self.player.focus_target)

        # Could be killed by a Lunge, so Mend
        if self.player.hp <= 5:
            return cs_moves.Mend(self.player, self.player_list, self.player)

        # In danger, so choose a Defence Move.
        elif self.player.hp < 10:
            if random.randint(0, 10) > 7:
                return beAggressive(self)
            return beDefensive(self)
        
        # Use an Move Move
        elif random.randint(0, 10) > 7:
            return beActive(self)
        
        # Use an Attack Move
        else:
            if random.randint(0, 10) > 8:
                return beActive(self)
            if random.randint(0, 10) > 8:
                return beDefensive(self)
            return beAggressive(self)
        
        target = self.player
        while target == self.player:
            target = random.choice(self.player_list)
        return cs_moves.Assail(self.player, self.player_list, target)

    def setPlayerListReference(self, player_list, dead_list):
        self.player_list = player_list
        self.dead_list = dead_list
       
     
#==============================================================================#

#==============================================================================#
