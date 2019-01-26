class Sheet(object):
    def __init__(self):
        self.dice = (
            "d4",
            "d6",
            "d8",
            "d10",
            "d12",
            "d20",)
        self.Classes = (
            "Barbarian",
            "Bard",
            "Cleric",
            "Druid",
            "Fighter",
            "Monk",
            "Paladin",
            "Ranger",
            "Rogue",
            "Sorcerer",
            "Warlock",
            "Wizard",)
        # Initialise everything in the __init__
        # All of these should probably have default values
        self.Race = str
        self.Name = str
        self.alignment = str
        self.background = str
        self.backgroundTrait = str
        self.ClassLevel = {'test': 1}
        self.Trait = int
        self.Ideal = int
        self.Bonds = int
        self.Flaws = int
        self.lvlUpHitDice = dict
        self.ClassLevels = dict
        self.HitDiceSets = dict
        self.SorceryPoints = dict
        self.AbScoreNamelist = list
        self.AbScoreValues = dict
        self.AbScoreMod = dict
        self.ActEffList = list

        self.Race = "Tiefling"

    def general_char_stuff(self):
        self.Name = "Leucis (Kitten)"

        self.alignment = "Chaotic Good"
        self.background = "Acolyte"

        self.backgroundTrait = 8
        self.Trait = 8  # -
        self.Ideal = 5  # - Trust in my deity to guide my actions.
        self.Bonds = 1  # - Recover an ancient relic.
        self.Flaws = 6  # - Obsessing with the goals I set out to accomplish.

        self.lvlUpHitDice = {
            "Barbarian": ["1d12",  7],
            "Bard": ["1d8",  5],
            "Cleric": ["1d8",  5],
            "Druid": ["1d8",  5],
            "Fighter": ["1d10",  6],
            "Monk": ["1d8",  5],
            "Paladin": ["1d10",  6],
            "Ranger": ["1d10",  6],
            "Rogue": ["1d8",  5],
            "Sorcerer": ["1d6",  4],
            "Warlock": ["1d8", 5],
            "Wizard": ["1d6", 4],
        }
        self.ClassLevels = {key: 0 for key in self.Classes}
        # but i'm a sorcerer:
        self.HitDiceSets = {
            key: "{dice} * {lvl} ".format(
                dice=self.lvlUpHitDice[key][0],
                lvl=self.ClassLevel[key])
            for key in self.Classes
        }
        # Set Sorcery Points
        if self.ClassLevels["Sorcerer"] == 1:
            self.SorceryPoints = 0
        else:
            self.SorceryPoints = self.ClassLevels["Sorcerer"]

    def attributes(self):
        self.AbScoreNamelist = ("str",
                                "dex",
                                "const",
                                "int",
                                "wis",
                                "char",)

        self.AbScoreValues = {"str": 7,
                              "dex":  9,
                              "const": 15,
                              "int": 9,
                              "wis": 13,
                              "char": 17}

        self.AbScoreMod = {
            key: int(self.AbScoreValues[key] - 10)
            for key in self.AbScoreNamelist}

    def active_effects(self):
        self.ActEffList = ["Sorcerous Origin", "Font of Magic"]
        # < Wild Magic Surge
        # < Tides of Chaos


"""

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
"""