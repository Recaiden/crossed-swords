STRIKE = 0
LUNGE = 1
ASSAIL = 2

DODGE = 3
BLOCK = 4
RIPOSTE = 5

TAUNT = 6
FOCUS = 7
MEND = 8
HALT = 9

def applyFocus(action, damage, target):
    new_damage = damage
    if action.player.focus_target == target:
        new_damage *= 2
        new_damage += 1
    return new_damage

#==============================================================================#
#                                   Moves                                     #
#==============================================================================#
class Move:
    def __init__(self, player, players, target=None):
        self.player = player
        self.target = target
        self.players = players

    def setup(self):
        pass

    def resolve(self):
        pass

    def name(self):
        return "generic move"

#==============================================================================#
#                                  Attacks                                     #
#==============================================================================#
class Strike(Move):
    """Deal 3 damage to target player."""
    def setup(self):
        self.target.addAttacker(self.player)

    def resolve(self):
        damage_dealt = self.target.damage(applyFocus(self, 3,
                                                      self.target), 
                                          self.player)
        self.player.addVP(damage_dealt)

    def name(self):
        return "Strike"

class Lunge(Move):
    """Deal 5 damage to target player.  
    If that player damages you this turn, he deals 3 additional damage to you,
    plus 6 MORE damage if you were Focused on him."""
    def setup(self):
        """Make the uing player vulnerable to damage by the target."""
        self.target.addAttacker(self.player)
        if self.target == self.player.focus_target:
            self.player.setVulnerable(self.target, 9)
        else:
            self.player.setVulnerable(self.target, 3)

    def resolve(self):
        damage_dealt = self.target.damage(applyFocus(self, 5, 
                                                      self.target), 
                                          self.player)
        self.player.addVP(damage_dealt)

    def name(self):
        return "Lunge"

class Assail(Move):
    """Deal 1 damage to every player.  
    Target player's Defense cards cannot reduce this damage. 
    You cannot gain more than 8 VP from this move on any one turn. """
    def setup(self):
        """Note that all players other than the self are attacked by an Assail"""
        for player in self.players:
            if player == self: continue
            player.addAttacker(self.player)
 
    def resolve(self):
        """Deal 1 damage to each other player.  To the target, it cannot be prevented."""
        vp_count = 0
        vp_count += self.target.damageAP(applyFocus(self, 1, 
                                                     self.target), 
                                         self.player)
        for player in self.players:
            if player == self.player or player == self.target: continue
            vp_count += player.damage(applyFocus(self, 1, player), 
                                      self.player)
        vp_count = min(vp_count, 8)
        self.player.addVP(vp_count)

    def name(self):
        return "Assail"
            

#==============================================================================#
#                                  Defences                                    #
#==============================================================================#

class Dodge(Move):
    """Target player's (Attack) cards deal no damage to you this turn, 
    and 3 less damage to you next turn.  
    All other (Attack) cards deal 3 less damage to you this turn."""
    def setup(self):
        """The immunity call prevents the target from damaging the using player"""
        self.player.setImmunity(self.target)
        self.player.setArmour(3)

    def resolve(self):
        """Set the lingering redduction that will be in effect the next turn."""
        self.player.resistance = self.target
        self.player.resistance_expiring = 2

    def name(self):
        return "Dodge"

class Block(Move):
    """All (Attack) cards deal 2 less damage to you this turn.  
    If target player targets you with an (Attack) card this turn, deal 2 damage to him."""
    def setup(self):
       self.player.setArmour(2)

    def resolve(self):
        """Deal damage to the target if they attacked this player."""
        for player in self.player.attackers:
            if player == self.target:
                damage_dealt = self.target.damageCounter(2, self.player)
                self.player.addVP(damage_dealt)

    def name(self):
        return "Block"

class Riposte(Move):
    """If target player targets you with an (Attack) card this turn, 
    it's damage is reduced to zero, and you deal 3 damage to him."""
    def setup(self):
       self.player.setImmunity(self.target)
 
    def resolve(self):
        if self.target in self.player.attackers:
            damage_dealt = self.target.damageCounter(3, self.player)
            self.player.addVP(damage_dealt)

    def name(self):
        return "Riposte"


#==============================================================================#
#                                  Moves                                     #
#==============================================================================#

class Taunt(Move):
    """Steal 3 counters from target player's Victory Pool.  
    All other player's (Attack) cards deal 1 extra damage to you this turn."""
    def setup(self):
        if self.player.halted == 0:
            self.player.setArmour(-1)

    def resolve(self):
        if self.player.halted == 0:
            self.player.addVP(self.target.drain(3))
        else:
            self.player.damage(3*self.player.halted)
            for halter in self.player.halters:
                halter.addVP(3)

    def name(self):
        return "Taunt"
            

class Focus(Move):
    """If you use an (Attack) card on target player next turn, 
    you deal twice your normal damage, plus one.  
    (Damage-reducing effects apply after Focus is applied.)"""
    def setup(self):
        pass
 
    def resolve(self):
        if self.player.halted == 0:
            self.player.focus_target = self.target
            self.player.focus_expiring = 2
        else:
            self.player.damage(3*self.player.halted)
            for halter in self.player.halters:
                halter.addVP(3)

    def name(self):
        return "Focus"


class Mend(Move):
    """Add 3 counters to target player's Life Pool,
    or 7 counters if you Focused last turn (regardless of the target of your Focus).  
    Gain 1 Victory Point."""
    def setup(self):
        pass
 
    def resolve(self):
        if self.player.halted == 0:
            if self.player.focus_target is not None:
                self.target.heal(7)
            else:
                self.target.heal(3)
            self.player.addVP(1)
        else:
            self.player.damage(3*self.player.halted)
            for halter in self.player.halters:
                halter.addVP(3)

    def name(self):
        return "Mend"
         
class Halt(Move):
    """If target player plays an (Action) card, 
    you deal 3 damage to him or her and negate the effect of the (Move) he played.  
    If two or more players Halt each other in a loop at the same time, nothing happens."""
    def setup(self): 
        pass
    
    def halt(self):
        self.target.halted += 1
        self.target.halters.append(self.player)
 
    def resolve(self):
        if self.player.halted != 0:
            self.player.damage(3*self.player.halted)
            for halter in self.player.halters:
                halter.addVP(3)

    def name(self):
        return "Halt"

# Maintain a list so that Moves can be referred to by the indices of their buttons.
moveList = [Strike, Lunge, Assail,
              Dodge, Block, Riposte, 
              Taunt, Focus, Mend, Halt]
