


class characterBuilding(object):

  def __init__(self):
    # it's storytime!

#    def backgroundCollection(self):

    self.traitdict = \
      {
        "Acolyte" : """
You have spent your life in the service of a temple to a specific god or pantheon of gods.You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices in order to conduct worshipers into the presence of the divine.You are not necessarily a cleric - performing sacred rites is not the same thing as channeling divine power. Choose a god, a pantheon of gods, or some other quasi-divine being from among those listed in appendix B or those specified by your DM, and work with your DM to detail the nature of your religious service. Were you a lesser functionary in a temple, raised from childhood to assist the priests in the sacred rites? Or were you a high priest who suddenly experienced a call to serve your god in a different way? Perhaps you were the leader of a small cult outside of any established temple structure, or even an occult group that served a fiendish master that you now deny.

* Skill Proficiencies: Insight, Religion
* Languages: Two of your choice
* Equipment: A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, and a belt pouch containing 15 GP.
""",
        "Charlatan" : """
You have always had a way with people.You know what makes them tick, you can tease out their hearts' desires after a few minutes of conversation, and with a few leading questions you can read them like they were children's books.It’s a useful talent, and one that you’re perfectly willing to use for your advantage.You know what people want and you deliver, or rather, you promise to deliver.Common sense should steer people away from things that sound too good to be true, but common sense seems to be in short supply when you’re around.The bottle of pink-colored liquid will surely cure that unseemly rash, this ointment—nothing more than a bit of fat with a sprinkle of silver dust—can restore youth and vigor, and there’s a bridge in the city that just happens to be for sale.These marvels sound implausible, but you make them sound like the real deal.

* Skill Proficiencies: Deception, Sleight of Hand
* Tool Proficiencies: Disguise Kit, Forgery Kit
* Equipment: A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), and a belt pouch containing 15 GP.
""",
        "Criminal" : """
You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the criminal underworld. You’re far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society.

* Skill Proficiencies: Deception, Stealth
* Tool Proficiencies: One type of gaming set, thieves’ tools
* Equipment: A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 GP.
""",
        "Entertainer" : """
You thrive in front of an audience. You know how to entrance them, entertain them, and even inspire them. Your poetics can stir the hearts of those who hear you, awakening grief or joy, laughter or anger. Your music raises their spirits or captures their sorrow. Your dance steps captivate, your humor cuts to the quick. Whatever techniques you use, your art is your life.

* Skill Proficiencies: Acrobatics, Performance
* Tool Proficiencies: Disguise kit, one type of musical instrument
* Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 GP.
""",

        "Folk Hero" : """
You come from a humble social rank, but you are destined for so much more. Already the people of your home village regard you as their champion, and your destiny calls you to stand against the tyrants and monsters that threaten the common folk everywhere.

* Skill Proficiencies: Animal Handling, Survival
* Tool Proficiencies: One type of artisan’s tools, vehicles (land)
* Equipment: A set of artisan’s tools (one of your choice), a shovel, an iron pot, a set of common clothes, and a belt pouch containing 10 GP.
""",
        "Guild Artisan" : """
You are a member of an artisan’s guild, skilled in a particular field and closely associated with other artisans.
You are a well-established part of the mercantile world, freed by talent and wealth from the constraints of a feudal social order. You learned your skills as an apprentice to a master artisan, under the sponsorship of your guild, until you became a master in your own right

* Skill Proficiencies: Insight, Persuasion
* Tool Proficiencies: One type of artisan’s tools
* Languages: One of your choice
* Equipment: A set of artisan’s tools (one of your choice), a letter of introduction from your guild, a set of traveler’s clothes, and a belt pouch containing 15 GP.
""",
        "Noble" : """
You understand wealth, power, and privilege. You carry a noble title, and your family owns land, collects taxes, and wields significant political influence. You might be a pampered aristocrat unfamiliar with work or discomfort, a former merchant just elevated to the nobility, or a disinherited scoundrel with a disproportionate sense of entitlement. Or you could be an honest, hard-working landowner who cares deeply about the people who live and work on your land, keenly aware of your responsibility to them. Work with your DM to come up with an appropriate title and determine how much authority that title carries.

A noble title doesn’t stand on its own—it’s connected to an entire family, and whatever title you hold, you will pass it down to your own children. Not only do you need to determine your noble title, but you should also work with the DM to describe your family and their influence on you.

Is your family old and established, or was your title only recently bestowed? How much influence do they wield, and over what area? What kind of reputation does your family have among the other aristocrats of the region? How do the common people regard them? What’s your position in the family? Are you the heir to the head of the family? Have you already inherited the title? How do you feel about that responsibility? Or are you so far down the line of inheritance that no one cares what you do, as long as you don’t embarrass the family? How does the head of your family feel about your adventuring career? Are you in your family’s good graces, or shunned by the rest of your family? Does your family have a coat of arms? An insignia you might wear on a signet ring? Particular colors you wear all the time? An animal you regard as a symbol of your line or even a spiritual member of the family? These details help establish your family and your title as features of the world of the campaign.

* Skill Proficiencies: History, Persuasion
* Tool Proficiencies: One type of gaming set
* Languages: One of your choice
* Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 GP.
""",
        "Outlander" : """
You grew up in the wilds, far from civilization and the comforts of town and technology. You’ve witnessed the migration of herds larger than forests, survived weather more extreme than any city-dweller could comprehend, and enjoyed the solitude of being the only thinking creature for miles in any direction. The wilds are in your blood, whether you were a nomad, an explorer, a recluse, a hunter-gatherer, or even a marauder. Even in places where you don’t know the specific features of the terrain, you know the ways of the wild.

* Skill Proficiencies: Athletics, Survival
* Tool Proficiencies: One type of musical instrument
* Languages: One of your choice
* Equipment: A staff, a hunting trap, a trophy from an animal you killed, a set of traveler’s clothes, and a belt pouch containing 10 GP.
""",
        "Sage" : """
You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you. Your efforts have made you a master in your fields of study.

* Skill Proficiencies: Arcana, History
* Languages: Two of your choice
* Equipment: A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 GP.
""",
        "Sailor" : """
You sailed on a seagoing vessel for years. In that time, you faced down mighty storms, monsters of the deep, and those who wanted to sink your craft to the bottomless depths. Your first love is the distant line of the horizon, but the time has come to try your hand at something new. Discuss the nature of the ship you previously sailed with your Dungeon Master. Was it a merchant ship, a naval vessel, a ship of discovery, or a pirate ship? How famous (or infamous) is it? Is it widely traveled? Is it still sailing, or is it missing and presumed lost with all hands? What were your duties on board—boatswain, captain, navigator, cook, or some other position? Who were the captain and first mate? Did you leave your ship on good terms with your fellows, or on the run?

* Skill Proficiencies: Athletics, Perception
* Tool Proficiencies: Navigator’s tools, vehicles (water)
* Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, and a belt pouch containing 10 GP.
""",
        "Soldier" : """
War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, learned basic survival techniques, including how to stay alive on the battlefield. You might have been part of a standing national army or a mercenary company, or perhaps a member of a local militia who rose to prominence during a recent war. When you choose this background, work with your DM to determine which military organization you were a part of, how far through its ranks you progressed, and what kind of experiences you had during your military career. Was it a standing army, a town guard, or a village militia? Or it might have been a noble’s or merchant’s private army, or a mercenary company.

* Skill Proficiencies: Athletics, Intimidation
* Tool Proficiencies: One type of gaming set, vehicles (land)
* Equipment: An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a set of bone dice or deck of cards, a set of common clothes, and a belt pouch containing 10 GP.
""",
        "Urchin" : """
You grew up on the streets alone, orphaned, and poor. You had no one to watch over you or to provide for you, so you learned to provide for yourself. You fought fiercely over food and kept a constant watch out for other desperate souls who might steal from you. You slept on rooftops and in alleyways, exposed to the elements, and endured sickness without the advantage of medicine or a place to recuperate. You’ve survived despite all odds, and did so through cunning, strength, speed, or some combination of each. You begin your adventuring career with enough money to live modestly but securely for at least ten days. How did you come by that money? What allowed you to break free of your desperate circumstances and embark on a better life?

* Skill Proficiencies: Sleight of Hand, Stealth
* Tool Proficiencies: Disguise kit, thieves’ tools
* Equipment: A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10 GP.
"""
      }
  

  def AcolytePropts(self):

    equipstuff = [
        "A holy symbol (a gift to you when you entered the priesthood)", 
        "a prayer book or prayer wheel", 
        "5 sticks of incense", 
        "vestments", 
        "a set of common clothes", 
        "a belt pouch", 
        "15 GP"
      ]

    self.Equipment  += equipstuff
    self.skillProfs += ["Insight", "Religion"]
    self.addLanguages(2) #Two of your choice

    self.Features["Shelter of the Faithful"] = """
As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.

You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.
"""

    self.AcolyteSuggChars= """
Acolytes are shaped by their experience in temples or other religious communities.
Their study of the history and tenets of their faith and their relationships to temples, shrines, or hierarchies affect their mannerisms and ideals. Their flaws might be some hidden hypocrisy or heretical idea, or an ideal or bond taken to an extreme.
"""
    self.availPersTraits = \
      {
        1: "I idolize a particular hero of my faith, and constantly refer to that person’s deeds and example.",
        2: "I can find common ground between the fiercest enemies, empathizing with them and always working towards peace.",
        3: "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
        4: "Nothing can shake my optimistic attitude.",
        5: "I quote (or misquote) sacred texts and proverbs in almost every situation.",
        6: "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
        7: "I've enjoyed fine food, drink, and high society among my temple’s elite. Rough living grates on me.",
        8: "I’ve spent so long in the temple that I have little practical experience dealing with people in the outside world."
      }

    self.availIdeals = \
      {
        1: "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)",
        2: "Charity. I always try to help those in need, no matter what the personal cost. (Good)",
        3: "Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic)",
        4: "Power. I hope to one day rise to the top of my faith’s religious hierarchy. (Lawful)",
        5: "Faith. I trust that my deity will guide my actions, I have faith that if I work hard, things will go well. (Lawful)",
        6: "Aspiration. I seek to prove myself worthy of my god’s favor by matching my actions against his or her teachings. (Any)"
      }

    self.availBonds = \
      {
        1: "I would die to recover an ancient relic of my faith that was lost long ago.",
        2: "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        3: "I owe my life to the priest who took me in when my parents died.",
        4: "Everything I do is for the common people.",
        5: "I will do anything to protect the temple where I served.",
        6: "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."
      }
    
    self.availFlaws = \
      {
        1: "I judge others harshly, and myself even more severely.",
        2: "I put too much trust in those who wield power within my temple’s hierarchy.",
        3: "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        4: "I am inflexible in my thinking.",
        5: "I am suspicious of strangers and expect the worst of them.",
        6: "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
      }

  def CharlatanPropts(self):

    equipstuff = [
        "Set of fine clothes", 
        "Disguise kit", 
        """Tools of the con of your choice:
    * Ten stoppered bottles filled with colored liquid.
    * A set of weighted dice.
    * A deck of marked cards
    * Or a signet ring of an imaginary duke
  """,
        "a belt pouch",
        "15 gp"
      ]

    self.Equipment  += equipstuff
    self.skillProfs += ["Deception", "Sleight of Hand"]
    self.toolProfs  += ["Disguise Kit", "Forgery Kit"]

    self.Features["False Identity"] = """
You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona.
Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy.
"""

    self.availSchemes = \
      {
        1: "I cheat at games involving chance.",
        2: "I shave coins or forge documents.",
        3: "I insinuate myself into people’s lives to prey on their weakness and secure their fortunes.",
        4: "I put on new identities like clothes.",
        5: "I run sleight-of-hand cons on street corners.",
        6: "I convince people that worthless junk is worth their hard-earned money."
      }

    self.availPersTraits = \
      {
        1: "I fall in and out of love easily, and am always pursuing someone.",
        2: "I have a joke for every occasion, especially occasions where humor is inappropriate.",
        3: "Flattery is my preferred trick for getting what I want.",
        4: "I’m a born gambler who can't resist taking a risk for a potential payoff.",
        5: "I lie about almost everything, even when there’s no good reason to.",
        6: "Sarcasm and insults are my weapons of choice.",
        7: "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        8: "I pocket anything I see that might have some value."
      }

    self.availIdeals = \
      {
        1: "Independence. I am a free spirit— no one tells me what to do. (Chaotic)",
        2: "Fairness. I never target people who can’t afford to lose a few coins. (Lawful)",
        3: "Charity. I distribute the money I acquire to the people who really need it. (Good)",
        4: "Creativity. I never run the same con twice. (Chaotic)",
        5: "Friendship. Material goods come and go. Bonds of friendship last forever. (Good)",
        6: "Aspiration. I’m determined to make something of myself. (Any)"
      }

    self.availBonds = \
      {
        1: "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        2: "I owe everything to my mentor—a horrible person who’s probably rotting in jail somewhere.",
        3: "Somewhere out there, I have a child who doesn’t know me. I’m making the world better for him or her.",
        4: "I come from a noble family, and one day I’ll reclaim my lands and title from those who stole them from me.",
        5: "A powerful person killed someone I love. Some day soon, I’ll have my revenge.",
        6: "I swindled and ruined a person who didn’t deserve it. I seek to atone for my misdeeds but might never be able to forgive myself."
      }

    self.availFlaws = \
      {
        1: "I can’t resist a pretty face.",
        2: "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        3: "I’m convinced that no one could ever fool me the way I fool others.",
        4: "I’m too greedy for my own good. I can’t resist taking a risk if there’s money involved.",
        5: "I can’t resist swindling people who are more powerful than me.",
        6: "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough."
      }


    def CriminalPropts(self):


      equipstuff = [
      "Crowbar",
      "Dark common clothes", 
      "Hood", 
      "Belt pouch", 
      "15 GP"
      ]

      self.Equipment  += equipstuff
      self.skillProfs += ["Deception", "Stealth"]
      self.toolProfs  += ["One type of gaming set", "Thieves’ tools"]

      self.Features["Criminal Contact"] = """
You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you.
"""
      self.variantCriminal = """    Spy:
Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context: as an espionage agent. You might have been an officially sanctioned agent of the crown, or perhaps you sold the secrets you uncovered to the highest bidder.
"""

      self.availPersTraits = \
        {
          1: "I always have a plan for what to do when things go wrong.",
          2: "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
          3: "The first thing I do in a new place is note the locations of everything valuable-or where such things could be hidden.",
          4: "I would rather make a new friend than a new enemy.",
          5: "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
          6: "I don't pay attention to the risks in a situation. Never tell me the odds.",
          7: "The best way to get me to do something is to tell me I can't do it.",
          8: "I blow up at the slightest insult."
        }

      self.availIdeals = \
        {
          1: "Honor. I don’t steal from others in the trade. (Lawful)",
          2: "Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)",
          3: "Charity. I steal from the wealthy so that I can help people in need. (Good)",
          4: "Greed. I will do whatever it takes to become wealthy. (Evil)",
          5: "People. I’m loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)",
          6: "Redemption. There’s a spark of good in everyone. (Good)"
        }

      self.availBonds = \
        {
          1: "I’m trying to pay off an old debt I owe to a generous benefactor.",
          2: "My ill-gotten gains go to support my family.",
          3: "Something important was taken from me, and I aim to steal it back.",
          4: "I will become the greatest thief that ever lived.",
          5: "I’m guilty of a terrible crime. I hope I can redeem myself for it.",
          6: "Someone I loved died because of a mistake I made. That will never happen again."
        }

      self.availFlaws = \
        {
          1: "When I see something valuable, I can’t think about anything but how to steal it.",
          2: "When faced with a choice between money and my friends, I usually choose the money.",
          3: "If there’s a plan, I’ll forget it. If I don’t forget it, I’ll ignore it.",
          4: "I have a “tell” that reveals when I'm lying.",
          5: "I turn tail and run when things look bad.",
          6: "An innocent person is in prison for a crime that I committed. I’m okay with that."
        }

    def EntertainerPropts(self):

      equipstuff = [
          "Musical instrument (one of your choice)",
          "Favor of an admirer (love letter, lock of hair, or trinket)",
          "Costume",
          "Belt pouch",
          "15 GP"
        ]

      self.Equipment  += equipstuff
      self.skillProfs += ["Acrobatics", "Performance"]
      self.toolProfs  += ["Disguise kit", "One type of musical instrument"]

      self.Features["By Popular Demand"] = """
You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble’s court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you.
"""

      self.variantEntertainer = """    Gladiator:
A gladiator is as much an entertainer as any minstrel or circus performer, trained to make the arts of combat into a spectacle the crowd can enjoy. This kind of flashy combat is your entertainer routine, though you might also have some skills as a tumbler or actor. Using your By Popular Demand feature, you can find a place to perform in any place that features combat for entertainment—perhaps a gladiatorial arena or secret pit fighting club. You can replace the musical instrument in your equipment package with an inexpensive but unusual weapon, such as a trident or net.
"""

      self.availPersTraits = \
        {
          1: "I know a story relevant to almost every situation.",
          2: "Whenever I come to a new place, I collect local rumors and spread gossip.",
          3: "I’m a hopeless romantic, always searching for that “special someone.”",
          4: "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
          5: "I love a good insult, even one directed at me.",
          6: "I get bitter if I’m not the center of attention.",
          7: "I’ll settle for nothing less than perfection.",
          8: "I change my mood or my mind as quickly as I change key in a song."
        }

      self.availIdeals = \
        {
          1: "Beauty. When I perform, I make the world better than it was. (Good)",
          2: "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)",
          3: "Creativity. The world is in need of new ideas and bold action. (Chaotic)",
          4: "Greed. I’m only in it for the money and fame. (Evil)",
          5: "People. I like seeing the smiles on people’s faces when I perform. That’s all that matters. (Neutral)",
          6: "Honesty. Art should reflect the soul; it should come from within and reveal who we really are. (Any)"
        }

      self.availBonds = \
        {
          1: "My instrument is my most treasured possession, and it reminds me of someone I love.",
          2: "Someone stole my precious instrument, and someday I’ll get it back.",
          3: "I want to be famous, whatever it takes.",
          4: "I idolize a hero of the old tales and measure my deeds against that person’s.",
          5: "I will do anything to prove myself superior to my hated rival.",
          6: "I would do anything for the other members of my old troupe."
        }

      self.availFlaws = \
        {
          1: "I’ll do anything to win fame and renown.",
          2: "I’m a sucker for a pretty face.",
          3: "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
          4: "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
          5: "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
          6: "Despite my best efforts, I am unreliable to my friends."
        }

    def FolkHeroPropts(self):
      
      equipstuff = [
          "Set of artisan’s tools (one of your choice)",
          "Shovel",
          "Iron pot",
          "Set of common clothes",
          "Belt pouch",
          "10 GP"
        ]

      self.Equipment  += equipstuff
      self.skillProfs += ["Animal Handling", "Survival"]
      self.toolProfs  += ["One type of artisan’s tools", "Vehicles (land)"]

      self.Equipment  += equipstuff

      self.Features["Rustic Hospitality"] = """
Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you.
"""

      self.FolkHeroSuggChars = """
A folk hero is one of the common people, for better or for worse. Most folk heroes look on their humble origins as a virtue, not a shortcoming, and their home communities remain very important to them.
"""
      self.availPersTraits = \
        {
          1: "I judge people by their actions, not their words.",
          2: "If someone is in trouble, I’m always ready to lend help.",
          3: "When I set my mind to something, I follow through no matter what gets in my way.",
          4: "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
          5: "I’m confident in my own abilities and do what I can to instill confidence in others.",
          6: "Thinking is for other people. I prefer action.",
          7: "I misuse long words in an attempt to sound smarter.",
          8: "I get bored easily. When am I going to get on with my destiny?"
        }
      
      self.availIdeals = \
        {
          1: "Respect. People deserve to be treated with dignity and respect. (Good)",
          2: "Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)",
          3: "Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)",
          4: "Might. If I become strong, I can take what I want—what I deserve. (Evil)",
          5: "Sincerity. There’s no good in pretending to be something I’m not. (Neutral)",
          6: "Destiny. Nothing and no one can steer me away from my higher calling. (Any)"
        }

      self.availBonds = \
        {
          1: "I have a family, but I have no idea where they are. One day, I hope to see them again.",
          2: "I worked the land, I love the land, and I will protect the land.",
          3: "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
          4: "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
          5: "I protect those who cannot protect themselves.",
          6: "I wish my childhood sweetheart had come with me to pursue my destiny."
        }

      self.availFlaws = \
        {
          1: "The tyrant who rules my land will stop at nothing to see me killed.",
          2: "I’m convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
          3: "The people who knew me when I was young know my shameful secret, so I can never go home again.",
          4: "I have a weakness for the vices of the city, especially hard drink.",
          5: "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
          6: "I have trouble trusting in my allies."
        }


    def NoblePropts(self):

      equipstuff = [
          "Set of fine clothes",
          "Signet ring",
          "Scroll of pedigree",
          "Purse",
          "25 GP"
        ]

      self.skillProfs += ["History", "Persuasion"]
      self.toolProfs  += ["One type of gaming set"]
      self.addLanguages(1) # One of your choice

      self.Features["Position of Privilege"] = """
Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to.
"""

      self.variantNoble = """    Knight:
A knighthood is among the lowest noble titles in most societies, but it can be a path to higher status. If you wish to be a knight, choose the Retainers feature (see the sidebar) instead of the Position of Privilege feature. One of your commoner retainers is replaced by a noble who serves as your squire, aiding you in exchange for training on his or her own path to knighthood. Your two remaining retainers might include a groom to care for your horse and a servant who polishes your armor (and even helps you put it on). As an emblem of chivalry and the ideals of courtly love, you might include among your equipment a banner or other token from a noble lord or lady to whom you have given your heart—in a chaste sort of devotion (This person could be your bond).
"""

      if self.variantNoble == self.checkchoice():
        self.Features["Retainer"] = """
If your character has a noble background, you may select this background feature instead of Position of Privilege. You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused.
"""
      self.NobleSuggChars = """
Nobles are born and raised to a very different lifestyle than most people ever experience, and their personalities reflect that upbringing. A noble title comes with a plethora of bonds—responsibilities to family, to other nobles (including the sovereign), to the people entrusted to the family’s care, or even to the title itself. But this responsibility is often a good way to undermine a noble.
"""
      self.availPersTraits = \
        {
          1: "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
          2: "The common folk love me for my kindness and generosity.",
          3: "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
          4: "I take great pains to always look my best and follow the latest fashions.",
          5: "I don’t like to get my hands dirty, and I won’t be caught dead in unsuitable accommodations.",
          6: "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
          7: "My favor, once lost, is lost forever.",
          8: "If you do me an injury, I will crush you, ruin your name, and salt your fields."
        }


      self.availIdeals = \
        {
          1: "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity. (Good)",
          2: "Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine. (Lawful)",
          3: "Independence. I must prove that I can handle myself without the coddling of my family. (Chaotic)",
          4: "Power. If I can attain more power, no one will tell me what to do. (Evil)",
          5: "Family. Blood runs thicker than water. (Any)",
          6: "Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)"
        }

      self.availBonds = \
        {
          1: "I will face any challenge to win the approval of my family.",
          2: "My house’s alliance with another noble family must be sustained at all costs.",
          3: "Nothing is more important than the other members of my family.",
          4: "I am in love with the heir of a family that my family despises.",
          5: "My loyalty to my sovereign is unwavering.",
          6: "The common folk must see me as a hero of the people."
        }

      self.availFlaws = \
        {
          1: "I secretly believe that everyone is beneath me.",
          2: "I hide a truly scandalous secret that could ruin my family forever.",
          3: "I too often hear veiled insults and threats in every word addressed to me, and I’m quick to anger.",
          4: "I have an insatiable desire for carnal pleasures.",
          5: "In fact, the world does revolve around me.",
          6: "By my words and actions, I often bring shame to my family."
        }

    def OutlanderPropts(self):

      



###

    {
    1: ,
    2: ,
    3: ,
    4: ,
    5: ,
    6: 
    }

    {
    1: ,
    2: ,
    3: ,
    4: ,
    5: ,
    6: ,
    7: ,
    8: 
    }




















