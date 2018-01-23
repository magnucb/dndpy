import os


class Sheet(object):

  def __init__(self):
    # rossh-yan pheezeezizt
    self.dice = \
    [
      "d4"  ,
      "d6"  ,
      "d8"  ,
      "d10" ,
      "d12" ,
      "d20" 
    ]
    self.Classes = \
    [
      "Barbarian" ,
      "Bard"      ,
      "Cleric"    ,
      "Druid"     ,
      "Fighter"   ,
      "Monk"      ,
      "Paladin"   ,
      "Ranger"    ,
      "Rogue"     ,
      "Sorcerer"  ,
      "Warlock"   ,
      "Wizard"
    ]

  def generalCharStuff(self):
    self.Race = "Tiefling"
    self.Name = "Leucis (Kitten)"

    self.alignment = "Chaotic Good"
    self.background = "Acolyte"

    self.backgroundTrait = 8
      Trait:   8 - 
      Ideal:   5 - Trust in my deity to guide my actions.
      Bonds:   1 - Recover an ancient relic.
      Flaws:   6 - Obsessing with the goals I set out to accomplish.



    self.lvlUpHitDice = \
    {
      "Barbarian" : [ "1d12" ,  7 ] ,
      "Bard"      : [ "1d8"  ,  5 ] ,
      "Cleric"    : [ "1d8"  ,  5 ] ,
      "Druid"     : [ "1d8"  ,  5 ] ,
      "Fighter"   : [ "1d10" ,  6 ] ,
      "Monk"      : [ "1d8"  ,  5 ] ,
      "Paladin"   : [ "1d10" ,  6 ] ,
      "Ranger"    : [ "1d10" ,  6 ] ,
      "Rogue"     : [ "1d8"  ,  5 ] ,
      "Sorcerer"  : [ "1d6"  ,  4 ] ,
      "Warlock"   : [ "1d8"  ,  5 ] ,
      "Wizard"    : [ "1d6"  ,  4 ] 
    }


    self.ClassLevels = { key : 0 for key in self.Classes }
    # but i'm a sorcerer:

    self.HitDiceSets = \
    {
      key: "{dice} * {lvl} ".format(dice=self.lvlUpHitDice[key][0],
                                    lvl=self.ClassLevel[key]       )
                  for key in self.Classes 
    }

    self.SorceryPoints = \
      0 if self.ClassLevels["Sorcerer"] == 1 else self.ClassLevels["Sorcerer"]


  def attributes(self):

    self.AbScoreNamelist = [ "stren", "dex", "const",
                             "int",   "wis", "char"   ]

    self.AbScoreVals = { "stren":   7, "dex":     9, "const":  15,
                         "int":     9, "wis":    13, "char":   17  }

    self.AbScoreMod = { key: int(self.AbScoreVals[key] - 10) \
                      for key in self.AbScoreNamelist }



  def activeEffects(self):
    self.ActEffList = ["Sorcerous Origin", "Font of Magic"]

      # < Wild Magic Surge
      # < Tides of Chaos
    


  Ability scores (w/ Racial traits):
  =================================
  * Strength:      7   ( -2 )
  * Dexterity:     9   ( -1 )
  * Constitution: 15   ( +2 )
  * Intelligence:  9   ( -1 ) [ R: BaseScore +1 ]
  * Wisdom:       13   ( +1 )
  * Charisma:     17   ( +3 ) [ R: BaseScore +2 ]




  Racial, Class, Physical character attributes:
  ============================================
    * Age:          22 seasons
    * Size:         Medium
    * Speed:        30 feet
    * Languages:
      ---------
        Read and write:
        - Common
        - Infernal
        - Sylvan
        - Elvish
    * Saving throw proficiencies:
      + Charisma
      + Constitution

    * Combat/Defensive proficiencies/traits:
      -------------------------------------
      * Armor  Prof.:  None
      * Weapon Prof.: Daggers, darts, slings, quarterstaves, l. crossbows

      * Hellish resistance:
          =>  Resistance to fire damage
      * Darkvision:
          =>  Thanks to infernal heritage,
              superior vision in dark & dim conditions:
      * Vision Enhancements:
        + Dim:
          =>  See w/in 60 feet as if bright light.
        + Dark: 
          =>  As if in dim lighting, and only in shades of gray.

