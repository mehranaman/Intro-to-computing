#  File: RPG.py
#  Description: Create two RPG characters and have them battle each other
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 9/22/2017
#  Date Last Modified: 9/23/2017



class Weapon():
	
	def __init__(self, weaponType):
		self.weaponType = weaponType
		# weapon types
		if weaponType == "dagger":
			self.damage = 4
		elif weaponType == "axe":
			self.damage = 6
		elif weaponType == "staff":
			self.damage = 6
		elif weaponType == "sword":
			self.damage = 10
		elif weaponType == "none":
			self.damage = 1
		else:
			pass

class Spell():
	
	def __init__(self, spellName):
		self.spellName = spellName
		#Spell types
		if spellName == "Fireball":
			self.cost = 3
			self.effect = 5
		elif spellName == "Lightning Bolt":
			self.cost = 10
			self.effect = 10
		elif spellName == "Heal":
			self.cost = 6
			self.effect = -6
		else:
			self.cost = 0
			self.effect = 0

class Armor():
	
	def __init__(self, armorType):
		self.armorType = armorType
		#Armor type and classes
		if armorType == "plate":
			self.armorClass = 2
		elif armorType == "chain":
			self.armorClass = 5
		elif armorType == "leather":
			self.armorClass = 8
		elif armorType == "none":
			self.armorClass = 10
		else:
			pass


class RPGCharacter():
	def __init__(self, name):
		#creating the character, with max health, spell points and no weapon and armor
		self.name = name
		self.wielding = Weapon("none")
		self.wearing = Armor("none")
		self.currentHealth = self.maxHealth
		self.currentSpellPoints = self.maxSpellPoints

	def wield(self, item):
		#assigning weapon depending on the chaarcter's provisions.
		if item.weaponType in self.wepsAllowed:
			print(self.name, "is now wielding a(n)", item.weaponType)
			self.wielding = item
		else:
			print("Weapon not allowed for this character class.")

	def unwield(self):
		#unwielding is as good as wielding 'none' weapon.
		self.wielding = Weapon("none")
		print(self.name, "is no longer wielding anything.")

	def putOnArmor(self, armor):
		if armor.armorType in self.armorAllowed:
			print(self.name, "is now wearing", armor.armorType)
			self.wearing = armor
		else:
			print("Armor not allowed for this character class.")

	def takeOffArmor(self):		
		self.wearing = Armor("none")
		print(self.name, "is no longer wearing anything.")

	def fight(self, opponent):
		print(self.name, "attacks", opponent.name, "with a(n)", self.wielding.weaponType)
		opponent.currentHealth -= self.wielding.damage
		print(self.name, "does", self.wielding.damage, "damage to", opponent.name)
		print(opponent.name, "is now down to", opponent.currentHealth, "health")
		opponent.checkForDefeat()

	def __str__(self):
		return ("\n" + self.name + "\n   Current Health: " + str(self.currentHealth) + "\n   Current Spell Points: " + str(self.currentSpellPoints) + "\n   Wielding: " + self.wielding.weaponType + "\n   Wearing: " + self.wearing.armorType + "\n   Armor Class: " + str(self.wearing.armorClass) + "\n")

	def checkForDefeat(self):
		if self.currentHealth <= 0:
			print(self.name, "has been defeated!")

class Fighter(RPGCharacter):
	# Provisions for the fighter class
	maxHealth = 40
	maxSpellPoints = 0
	wepsAllowed = ["dagger", "axe", "staff", "sword", "none"]
	armorAllowed = ["plate", "chain", "leather", "none"]



class Wizard(RPGCharacter):
	#Provisions for the wizard class
	maxHealth = 16
	maxSpellPoints = 20
	wepsAllowed = ["staff", "dagger", "none"]
	armorAllowed = ["none"]

	#Since only the wizard can cast spells
	def castSpell(self, spellName, target):
		casting = Spell(spellName)
		
		if casting.effect == 0:
			print("Unknown spell name. Spell failed.")
			return
		
		elif self.currentSpellPoints < casting.cost:
			print("Insufficient spell points")
			return
		else:
			print(self.name, 'casts', spellName, "at", target.name)
			# if the heal spell is used, prevent buffing
			if target.currentHealth - casting.effect > target.maxHealth:
				target.currentHealth = target.maxHealth
			else:
				target.currentHealth -= casting.effect
				self.currentSpellPoints -= casting.cost
			
			if spellName == "Heal":
				print(self.name, "heals", target.name, "for", -1 * casting.effect, "health points")
				print(target.name, "is now at", target.currentHealth, "health")
			else:
				print(self.name, "does", casting.effect, "damage to", target.name)
				print(target.name, "is now down to", target.currentHealth, "health")
				target.checkForDefeat()

def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

main()
