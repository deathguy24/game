
#Basic Setup
import random
dungeon_level = 1
playing = True
enemy_spawned = False
money = 0
heal = 0
debug = False
no_action = False
pcrit = 0
moves = 1
item_bought = False
enemy_attack = True

#Inventory Setup
slot1 = [0,0,0] #Weapon, Strength Upgrades
slot2 = [0,0,0] #Armor
slot3 = [0,0,0] #Weapon, Heal Potion, Greater Healing Potion
slot4 = [0,1,0] #Level, Exp
slot5 = [0,0,0] #Polly Pet, Slime Pet, Gold Pet
slot6 = [0,0,0] #Pet in use, P-Slime, P-Pet
slot7 = [0,0,0] #Evolution Key, Admin
slot8 = [1,0,0] #HP
slot9 = [0,0,0] #Money
slot10 = [0,0,0] #Slime pet evo, Level
slot11 = [0,0,0] #Gold pet evo, Level
slot12 = [0,0,0] #Polly pet evo, Level
slot13 = [0,0,0]
slot14 = [0,0,0]
slot15 = [0,0,0]

#Savefile Interpretation
savecode = []
save = input('Savefile (if you just started, enter 0): ')
if save == 'debug' or save == 'googl':
  save = '999999999999111399919999999899899899'
  debug = True
if save == 'money':
  save = '000000000000000000000100999'
for i in range(len(save)):
  
  slot = i / 3
  slotcode = i % 3
  if slot < 1:
    slot1[slotcode] = int(save[i])
  elif slot < 2:
    slot2[slotcode] = int(save[i])
  elif slot < 3:
    slot3[slotcode] = int(save[i])
  elif slot < 4:
    slot4[slotcode] = int(save[i])
  elif slot < 5:
    slot5[slotcode] = int(save[i])
  elif slot < 6:
    slot6[slotcode] = int(save[i])
  elif slot < 7:
    slot7[slotcode] = int(save[i])
  elif slot < 8:
    slot8[slotcode] = int(save[i])
  elif slot < 9:
    slot9[slotcode] = int(save[i])
  elif slot < 10:
    slot10[slotcode] = int(save[i])
  elif slot < 11:
    slot11[slotcode] = int(save[i])
  elif slot < 12:
    slot12[slotcode] = int(save[i])
  elif slot < 13:
    slot13[slotcode] = int(save[i]) 
  elif slot < 14:
    slot14[slotcode] = int(save[i])
  elif slot < 15:
    slot15[slotcode] = int(save[i]) 

#More Savefile Interpretation
slot4[1] = 1
health = slot8[0]*100 + slot8[1]*10 + slot8[2]
money = slot9[0]*100 + slot9[1]*10 + slot9[2]
level = slot4[0]*10 + slot4[1]
current_xp = int(slot4[2]/10)*level*10
health_max = 10*(level+1)
if health_max < 100:
  health_max = 100
pet = slot6[0]
slime_pet_evo = slot10[0]
gold_pet_evo = slot11[0]
polly_pet_evo = slot12[0]
slime_pet_level = slot10[1]*10 + slot10[2]
gold_pet_level = slot11[1]*10 + slot11[2]
polly_pet_level = slot12[1]*10 + slot12[2]



#Gameplay
while playing:
  
  #Turn Begins
  print()
  if not enemy_spawned:
    enemy_pick = random.randint(1,4)
    if moves % 20 == 0:
      enemy_pick = 5
    if level > 0 and level < 11:
      if enemy_pick == 1:
        print("A slime has appeared! It has 4 health.")
        enemy_health = 4
        enemy_damage = 1
        enemy_drop = 3
        enemy_xp = 2
        dodge_chance = 1
        crit_chance = 1
        e_slime = True
        enemy_ability = 0
      if enemy_pick == 2:
        print("A big slime has spawned! It has 6 health.")
        enemy_health = 6
        enemy_damage = 2
        enemy_drop = 4
        enemy_xp = 3
        dodge_chance = 1
        crit_chance = 1
        e_slime = True
        enemy_ability = 0
      if enemy_pick == 3:
        print("An archer slime has appeared! It has 5 health. ")
        enemy_health = 5
        enemy_damage = 2
        enemy_drop = 4
        enemy_xp = 2
        dodge_chance = 3
        crit_chance = 1
        e_slime = True
        enemy_ability = 0
      if enemy_pick == 4:
        print("A slime mage has appeared! It has 3 health.")
        enemy_health = 3
        enemy_damage = 5
        enemy_drop = 4
        enemy_xp = 3
        dodge_chance = 1
        crit_chance = 5
        e_slime = True
        enemy_ability = 0
      if enemy_pick == 5:
        print("A slime king has appeared! It has 11 health.")
        enemy_health = 11
        enemy_damage = 4
        enemy_drop = 7
        enemy_xp = 5
        dodge_chance = 3
        crit_chance = 3
        e_slime = True
        enemy_ability = 1
    elif level > 10 and level < 21:
      if enemy_pick == 1:
        print("A skeleton has appeared! It has 9 health.")
        enemy_health = 9
        enemy_damage = 2
        enemy_drop = 6
        enemy_xp = 5
        dodge_chance = 2
        e_slime = False
        crit_chance = 2
        enemy_ability = 0
      if enemy_pick == 2:
        print("A skeleton brawler has appeared! It has 12 health.")
        enemy_health = 12
        enemy_damage = 4
        enemy_drop = 7
        enemy_xp = 6
        dodge_chance = 2
        crit_chance = 2
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 3:
        print("A skeleton archer has appeared! It has 10 health.")
        enemy_health = 10
        enemy_damage = 4
        enemy_drop = 8
        enemy_xp = 5
        dodge_chance = 6
        crit_chance = 2
        e_slime = False
        enemy_ability = 1
      if enemy_pick == 4:
        print("A skeleton necromancer has appeared! It has 7 health.")
        enemy_health = 7
        enemy_damage = 7
        enemy_drop = 8
        enemy_xp = 6
        dodge_chance = 2
        crit_chance = 6
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 5:
        print("An undead overlord has appeared! It has 21 health.")
        enemy_health = 21
        enemy_damage = 6
        enemy_drop = 19
        enemy_xp = 8
        dodge_chance = 2
        crit_chance = 2
        e_slime = False
        enemy_ability = 1
    elif level > 20 and level < 31:
      if enemy_pick == 1:
        print("An orc has appeared! It has 19 health.")
        enemy_health = 19
        enemy_damage = 11
        enemy_drop = 16
        enemy_xp = 11
        dodge_chance = 3
        crit_chance = 3
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 2:
        print("An orc crossbowman has appeared! It has 21 health.")
        enemy_health = 21
        enemy_damage = 12
        enemy_drop = 18
        enemy_xp = 14
        dodge_chance = 8
        crit_chance = 3
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 3:
        print("An orc hellraiser has appeared! It has 14 health.")
        enemy_health = 14
        enemy_damage = 16
        enemy_drop = 17
        enemy_xp = 13
        dodge_chance = 3
        crit_chance = 8
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 4:
        print("An orc grunt has appeared! It has 20 health.")
        enemy_health = 20
        enemy_damage = 12
        enemy_drop = 16
        enemy_xp = 12
        dodge_chance = 3
        crit_chance = 3
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 5:
        print("An orc guardian has appeared! It has 34 health.")
        enemy_health = 34
        enemy_damage = 17
        enemy_drop = 28
        enemy_xp = 23
        dodge_chance = 3
        crit_chance = 3
        e_slime = False
        enemy_ability = 1
    elif level > 30 and level < 41:
      if enemy_pick == 1:
        print("A wandering spirit has appeared! It has 32 health.")
        enemy_health = 32
        enemy_damage = 18
        enemy_drop = 21
        enemy_xp = 20
        dodge_chance = 4
        crit_chance = 4
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 2:
        print("A poltergeist has appeared! It has 34 health.")
        enemy_health = 34
        enemy_damage = 20
        enemy_drop = 24
        enemy_xp = 23
        dodge_chance = 4
        crit_chance = 4
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 3:
        print("A warrior spirit has appeared! It has 31 health.")
        enemy_health = 31
        enemy_damage = 19
        enemy_drop = 26
        enemy_xp = 24
        dodge_chance = 9
        crit_chance = 4
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 4:
        print("A wise spirit has appeared! It has 24 health.")
        enemy_health = 24
        enemy_damage = 23
        enemy_drop = 26
        enemy_xp = 24
        dodge_chance = 4
        crit_chance = 9
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 5:
        print("An infuriated spirit has appeared! It has 45 health.")
        enemy_health = 45
        enemy_damage = 31
        enemy_drop = 35
        enemy_xp = 34
        dodge_chance = 4
        crit_chance = 4
        e_slime = False
        enemy_ability = 1
    else:
      if enemy_pick == 1:
        print("A demon has appeared! It has 39 health.")
        enemy_health = 39
        enemy_damage = 27
        enemy_drop = 34
        enemy_xp = 31
        dodge_chance = 5
        crit_chance = 5
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 2:
        print("A hellchaser has appeared! It has 41 health.")
        enemy_health = 41
        enemy_damage = 29
        enemy_drop = 39
        enemy_xp = 35
        dodge_chance = 5
        crit_chance = 5
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 3:
        print("A archdemon has appeared! It has 31 health.")
        enemy_health = 31
        enemy_damage = 42
        enemy_drop = 40
        enemy_xp = 38
        dodge_chance = 5
        crit_chance = 10
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 4:
        print("A molten archer has appeared! It has 39 health, and a 100% dodge rate!")
        enemy_health = 39
        enemy_damage = 32
        enemy_drop = 37
        enemy_xp = 32
        dodge_chance = 10
        crit_chance = 5
        e_slime = False
        enemy_ability = 0
      if enemy_pick == 5:
        print("The devil has appeared! It has 50 health.")
        enemy_health = 50
        enemy_damage = 40
        enemy_drop = 50
        enemy_xp = 50
        dodge_chance = 6
        crit_chance = 6
        e_slime = False
        enemy_ability = 1

    enemy_spawned = True
    enemy_damage -= (slot2[0]*100 + slot2[1]*10 + slot2[2])
    if enemy_damage < 1:
      enemy_damage = 1
  if enemy_spawned: 
    print("The enemy has " + str(enemy_health) + " health.")
  print()
  move = input()
  print()

  if move == "livie.hug" and slot7[1] == 1:
    print("Here be easter eggs")
    print("You hugged the enemy")
    print("The enemy gained 1 hp")
    print("The enemy gave you 1 coin")
    print("You were so happy that you gained 1 hp")
    health += 1
    enemy_health += 1
    slot9[2] += 1
    if slot9[2] > 9:
      slot9[2] = slot9[2] % 10
      slot9[1] += 1
    if slot9[1] > 9:
      slot9[1] = slot9[1] % 10
      slot9[0] += 1
    if slot5[0] < 1:
      print("You gained a polly pet uwu.")
      slot5[0] = 1

  elif move == "claireys.gator" and slot7[1] == 1:
    enemy_health -= 1000
    if enemy_health <= 0:
      if pet == 3:
        enemy_drop += 1
      if pet == 1:
        enemy_xp *= 2
      print("The enemy has died! You gained " + str(enemy_drop) + " coins, " + str(enemy_xp) + " experience points and your pet levelled up!")
      if pet == 1 and polly_pet_level < 99:
        polly_pet_level += 1
      if pet == 2 and slime_pet_level < 99:
        slime_pet_level += 1
      if pet == 3 and gold_pet_level < 99:
        gold_pet_level += 1
      enemy_spawned = False
      if slot9[0] < 10 and slot9[1] < 9:
        slot9[2] += enemy_drop
        if slot9[2] > 9:
          slot9[2] = slot9[2] % 10
          slot9[1] += 1
        if slot9[1] > 9:
          slot9[1] = slot9[1] % 10
          slot9[0] += 1
        current_xp += enemy_xp

  elif move == "ooo":
    slot7[1] = 1
    print("Admin activated")
    print("You can use the 'livie.hug' command.")
    print("You can use the 'claireys.gator' command.")

  elif move == "pet" or move == "pets":
    if slot5[0] == 1:
      print("polly - use polly pet (gives double exp and does 1 damage)")
    if slot5[1] == 1:
      print("slime - use slime pet (decreases skeleton dodge chance)")
    if slot5[2] == 1:
      print("gold - use gold pet (increases money earned)")
    print("Using a pet unequips other pets.")
    print()
    use_pet = input()
    print()
    if use_pet == "polly":
      if slot5[0] == 1:
        print("Equipped polly!")
        pet = 1
      else:
        print("You don't have that pet!")
    elif use_pet == "slime":
      if slot5[1] == 1:
        print("Equipped slime!")
        pet = 2
      else:
        print("You don't have that pet!")
    elif use_pet == "gold":
      if slot5[2] == 1:
        print("Equipped gold pet")
        pet = 3
      else:
        print("You don't have that pet!")
    else:
      print("That pet doesn't exist!")
        
  elif move == "help":
    print("Action commands will consume a move")
    print("attack - attack the enemy")
    print("save - get your save code")
    print("quit - exit the game")
    print("shop - opens the shop")
    print("info - get player info")
    print("weapon - change weapon")
    print("use - use an item")
    print("pets - use pets")
    print("evolve - evolve a pet")
  
  elif move == "evolve":
    if pet == 2:
      if slot10[1]*10+slot10[2] > 24 and slot10[0] < 1:
        print("1 - Fire slime")
        print("2 - Ice slime")
        print("Evolutions consume a key")
        print()
        evolution = input()
        print()
        if slot7[0] > 0:
          if evolution == "1":
            print("Evolved!")
            slot10[0] = 1
            slot7[0] -= 1
            evolved = True
          if evolution == "2":
            print("Evolved!")
            slot10[0] = 2
            slot7[0] -= 1
            evolved = True
          else:
            print("That's an invalid evolution")
        else:
          print("You don't have enough evolution keys!")
      elif slot10[1]*10+slot10[2] > 49 and slot10[0] < 3:
        print("1 - Molten slime")
        print("2 - Frozen slime")
        print("Evolutions consume a key")
        print()
        evolution = input()
        print()
        if slot7[0] > 0:
          if evolution == "1":
            slot10[0] = 3
            slot7[0] -= 1
            print("Evolved!")
            evolved = True
          if evolution == "2":
            slot10[0] = 4
            slot7[0] -= 1
            print("Evolved!")
            evolved = True
          else:
            print("That's an invalid evolution")
        else:
          print("You don't have enough evolution keys!")
      elif slot10[1]*10+slot10[2] > 74 and slot10[0] < 5:
        print("1 - Inferno slime")
        print("2 - Frostburn slime")
        print("Evolutions consume a key")
        print()
        evolution = input()
        print()
        if slot7[0] > 0:
          if evolution == "1":
            slot10[0] = 5
            print("Evolved!")
            evolved = True
            slot7[0] -= 1
          if evolution == "2":
            slot10[0] = 6
            print("Evolved!")
            evolved = True
            slot7[0] -= 1
          else:
            print("That's an invalid evolution")
        else:
          print("You don't have enough evolution keys!")    
      elif slot10[1]*10+slot10[2] > 99 and slot10[0] < 7:
        print("1 - Pyro slime")
        print("2 - Cryo slime")
        print("Evolutions consume a key")
        print()
        evolution = input()
        print()
        if slot7[0] > 0:
          if evolution == "1":
            slot10[0] = 7
            slot7[0] -= 1
            print("Evolved!")
            evolved = True
          if evolution == "2":
            slot10[0] = 8
            slot7[0] -= 1
            print("Evolved!")
            evolved = True
          else:
            print("That's an invalid evolution")
        else:
          print("You don't have enough evolution keys!")
    if pet == 1:
      if slot12[1]*10+slot12[2] > 24 and slot12[0] < 1:
        print("This pet will evolve to a shrike or a crow")
        print("Use one evo key? (y/n)")
        print()
        evolution = input()
        print()
        if input == "y":
          if slot7[0] > 0:
            a = random.randint(1,2)
            if a == 1:
              slot12[0] = 1
              print("Your pet evolved to a shrike!")
            elif a == 2:
              slot12[0] = 2
              print("Your pet evolved to a crow!")
            slot7[0] -= 1
            evolved = True
          else:
            print("You don't have enough evolution keys!")
        else:
          print("Okay")
      elif slot12[1]*10+slot12[2] > 49 and slot12[0] < 3:
        print("This pet will evolve to an owl or a raven")
        print("Use one evo key? (y/n)")
        print()
        evolution = input()
        print()
        if input == "y":
          if slot7[0] > 0:
            a = random.randint(1,2)
            if a == 1:
              slot12[0] = 3
              print("Your pet evolved to an owl!")
            elif a == 2:
              slot12[0] = 4
              print("Your pet evolved to a raven!")
            slot7[0] -= 1
            evolved = True
          else:
            print("You don't have enough evolution keys!")
        else:
          print("Okay")
      elif slot12[1]*10+slot12[2] > 74 and slot12[0] < 5:
        print("This pet will evolve to a hawk or a gull")
        print("Use one evo key? (y/n)")
        print()
        evolution = input()
        print()
        if input == "y":
          if slot7[0] > 0:
            a = random.randint(1,2)
            if a == 1:
              slot12[0] = 5
              print("Your pet evolved to a hawk!")
            elif a == 2:
              slot12[0] = 6
              print("Your pet evolved to a gull!")
            slot7[0] -= 1
            evolved = True
          else:
            print("You don't have enough evolution keys!")
        else:
          print("Okay")
      elif slot12[1]*10+slot12[2] > 99 and slot12[0] < 7:
        print("This pet will evolve to an eagle or a vulture")
        print("Use one evo key? (y/n)")
        print()
        evolution = input()
        print()
        if input == "y":
          if slot7[0] > 0:
            a = random.randint(1,2)
            if a == 1:
              slot12[0] = 7
              print("Your pet evolved to an eagle!")
            elif a == 2:
              slot12[0] = 8
              print("Your pet evolved to a vulture!")
            slot7[0] -= 1
            evolved = True
          else:
            print("You don't have enough evolution keys!")
        else:
          print("Okay")

  #Unupdated
  elif move == "monsterindex":
    print("1 - Slime")
    print("2 - Zombie")
    print("3 - Skeleton")
    print("4 - Mage")
    print()
    mon = input()
    print()
    if mon == "1":
      print("4 health, 1 damage, 2 xp, drops 3 coin")
    if mon == "2":
      print("6 health, 2 damage, 3 xp, drops 4 coins")
    if mon == "3":
      print("5 health, 2 damage, 2 xp, drops 4 coins")
    if mon == "4":
      print("3 health, 5 damage, 3 xp, drops 4 coins")
    
  elif move == "weapon":
    print("1 - Wooden Sword")
    if slot3[0] > 0:
      print("2 - Wooden Bow")
    if slot3[0] > 1:
      print("3 - Wooden Wand")
    print()
    wen = input("Enter weapon number: ")
    print()
    if wen == "1":
      slot1[0] = 0
      pcritchance = 1
    if wen == "2":
      if slot3[0] > 0:
        slot1[0] = 2
        pcritchance = 1
    if wen == "3":
      if slot3[0] > 1:
        slot1[0] = 3
        pcritchance = 5

  elif move == "shop":
    print("")
    if slot3[0] == 0:
      print("woodenbow - buy a wooden bow (33% chance to not take damage) for 50 coins!")
    if slot3[0] == 1:
      print("woodenwand - buy a wooden wand (+40% chance for critical damage) for 50 coins!")
    print("w.upgrade - upgrade your weapon.")
    print("a.upgrade - upgrade your armor.")
    print("potion.h - buy a healing potion for 5 coins that heals for 25 health.")
    print("goldpet - buys a gold digging pet for 50 coins!")
    print("potion.s - buy a slime potion for 5 coins!")
    print("potion.p - buy a pet potion for 5 coins that levels up your pet!")
    print()
    shop = input()
    print()
    if shop == "w.upgrade":
      if slot1[1] < 10 and slot1[2] < 9:
        print("It will cost " + str((slot1[1]*10 + slot1[2] +1)*5) + " coins to upgrade your weapon. You currently have " + str(slot1[1]*10 + slot1[2]) + " upgrades. Enter 'confirm' to confirm.")
        confirm = input()
        if confirm == 'confirm':
          if (slot1[1]*10 + slot1[2] +1)*5 > (slot9[0]*100 + slot9[1]*10 + slot9[2]):
            print("You do not have enough money for that!")
          else:
            print("Upgrade purchased!")
            slot1[2] += 1
            money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - (slot1[1]*10 + slot1[2] +1)*5
            slot9[2] = money % 10
            slot9[1] = int(((money % 100) - slot9[2])/10)
            slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
            if slot1[2] == 10:
              slot1[1] += 1
              slot1[2] = 0
            item_bought = True
      else:
        print("You have the maximum amount of weapon upgrades.")
    if shop == "a.upgrade":
      if slot2[0] < 2 and slot2[1] < 10 and slot2[2] < 9:
        print("It will cost " + str((slot2[0]*100 + slot2[1]*10 + slot2[2] +1)*5) + " coins to upgrade your armor. You currently have " + str(slot2[0]*100 + slot2[1]*10 + slot2[2]) + " upgrades. Enter 'confirm' to confirm.")
        confirm = input()
        if confirm == 'confirm':
          if (slot2[0]*100 + slot2[1]*10 + slot2[2] +1)*5 > (slot9[0]*100 + slot9[1]*10 + slot9[2]):
            print("You do not have enough money for that!")
          else:
            print("Upgrade purchased!")
            slot2[2] += 1
            money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - (slot2[0]*100 + slot2[1]*10 + slot2[2] +1)*5
            slot9[2] = money % 10
            slot9[1] = int(((money % 100) - slot9[2])/10)
            slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
            if slot2[2] == 10:
              slot2[1] += 1
              slot2[2] = 0
            if slot2[1] == 10:
              slot2[0] += 1
              slot2[1] = 0
            item_bought = True
      else:
        print("You have the maximum amount of armor upgrades.")
    if shop == "woodenbow":
      if slot3[0] != 0:
        print("You already bought this!")
      elif (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 50:
        print("You do not have enough money to buy this!")
      else:
        slot3[0] = 1
        money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - 50
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        item_bought = True
    if shop == "woodenwand":
      if slot3[0] > 1:
        print("You already bought this!")
      elif (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 50:
        print("You do not have enough money to buy this!")
      else:
        slot3[0] = 1
        money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - 50
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        item_bought = True
    if shop == "potion.h":
      if (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 5:
        print("You do not have enough money for that!")
      elif slot3[1] == 9:
        print("You already have the maximum amount of healing potions!")
      else:
        print("Potion bought!")
        money = ((slot9[0]*100 + slot9[1]*10 + slot9[2]) - 5)
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        slot3[1] += 1
        item_bought = True
    if shop == "potion.s":
      if (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 5:
        print("You do not have enough money for that!")
      elif slot6[1] == 9:
        print("You already have the maximum amount of slime potions!")
      else:
        print("Potion bought!")
        money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - 5
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        slot6[1] += 1
        item_bought = True
    if shop == "goldpet":
      if (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 50:
        print("You do not have enough money for that!")
      elif slot5[2] == 1:
        print("You already have this pet!")
      else:
        print("Pet bought!")
        money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - 50
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        slot5[2] = 1
        item_bought = True
    if shop == "potion.p":
      if (slot9[0]*100 + slot9[1]*10 + slot9[2]) < 5:
        print("You do not have enough money for that!")
      elif slot6[2] == 9:
        print("You already have the maximum amount of pet potions!")
      else:
        print("Potion bought!")
        money = (slot9[0]*100 + slot9[1]*10 + slot9[2]) - 5
        slot9[2] = money % 10
        slot9[1] = int(((money % 100) - slot9[2])/10)
        slot9[0] = int(((money-slot9[2])/10-slot9[1])/10)
        slot6[2] += 1
        item_bought = True

  elif move == "use":
    print("1 - Healing Potions (" + str(slot3[1]) + ")")
    print("2 - Slime Potions (" + str(slot6[1]) + ")")
    print("3 - Pet Potions (" + str(slot6[2]) + ")")
    print()
    use = input()
    print()
    if use == "1":
      if slot3[1] < 1:
        print("You do not have any healing potions!")
      elif health == health_max:
        print("Your health is already full!")
      else:
        print("25 health recovered!")
        used = True
        slot3[1] -= 1
        health += 25
        if health > health_max:
          health = health_max
    if use == "2":
      if slot6[1] < 1:
        print("You do not have any slime potions!")
      elif e_slime:
        if slot5[1] != 1:
          slot5[1] = 1
          print("You gained the slime pet! You consumed a slime potion!")
          slot6[1] -= 1
          used = True
      elif dodge_chance > 1:
        dodge_chance -= 2
        print("Decreased enemy dodge chance! It is now "+ str(dodge_chance*10) + "%!")
        slot6[1] -= 1
        used = True
      else:
        print("You cannot use a slime potion at this time!")
    if use == "3":
      if pet == 1:
        if polly_pet_level == 99:
          print("Your pet is already at the max level!")
        else:
          print("Pet levelled up!")
          polly_pet_level += 1
          used = True
      if pet == 2:
        if slime_pet_level == 99:
          print("Your pet is already at the max level!")
        else:
          print("Levelled up!")
          slime_pet_level += 1
          used = True
      if pet == 3:
        if gold_pet_level == 99:
          print("Your pet is already at the max level!")
        else:
          print("Levelled up!")
          gold_pet_level += 1
          used = True

  elif move == "info":
    print("You have " + str(slot9[0]*100 + slot9[1]*10 + slot9[2]) + " coins.")
    if slot1[0] == 0:
      print("Your weapon is a wooden sword.")
    if slot1[0] == 1:
      print("Your weapon is a wooden bow")
    print("You have " + str(slot1[1]*10 + slot1[2]) + " weapon upgrades.")
    print("You have " + str(slot2[0]*100 + slot2[1]*10 + slot2[2]) + " armor upgrades.")
    if slot4[0] < 9:
      print("You have " + str(slot4[0]) + " levels and are " + str(level*10 - current_xp) + " xp away from the next level.")
    else:
      print("Your level is maxed out.")
    if pet == 1:
      print("You have the polly pet equipped!")
      print("Your current pet level is " + str(polly_pet_level) + ".")
    elif pet == 2:
      print("You have the slime pet equipped!")
      print("Your current pet level is " + str(slime_pet_level) + ".")
    elif pet == 3:
      print("You have the gold pet equipped!")
      print("Your current pet level is " + str(gold_pet_level) + ".")
    print("You have " + str(slot7[0]) + " evolution keys")
        
  elif move == "attack":
    if pet == 2:
      dodge_chance -= 1
    if pet == 2:
      if slot10[0] % 2 == 1:
        if moves % (10 - (slot10[0] + 1)/2) == 0 and moves != 0:
          print("Your slime instakilled the enemy!")
          print("You gained " + str(enemy_drop) + " coins, " + str(enemy_xp) + " experience points, and your pet levelled up!")
          if pet == 2 and slime_pet_level < 99:
            slime_pet_level += 1
          if enemy_ability == 1:
            if slot7[0] < 9:
              print("You gained an evolution key!")
              slot7[0] += 1
            else:
              print("The evolution key was lost!")
          enemy_spawned = False
          if slot9[0] < 10 and slot9[1] < 9:
            slot9[2] += enemy_drop
            if slot9[2] > 9:
              slot9[2] = slot9[2] % 10
              slot9[1] += 1
            if slot9[1] > 9:
              slot9[1] = slot9[1] % 10
              slot9[0] += 1
          current_xp += int(enemy_xp)
    elif random.randint(1,10) > dodge_chance:
      if slot1[0] == 0 or slot1[0] == 1 or slot1[0] == 9:
        if slot1[0] == 2:
          if random.randint(0,9) < pcritchance:
            pcrit = 2
        enemy_health -= 1 + slot1[1]*10 + slot1[2] + pcrit
        print("You did " + str(1+slot1[1]*10 +slot1[2] + pcrit) + " damage!")
        if pet == 1:
          a = 1
          if slot12[0] % 2 == 1:
            a = int(((slot12[0]-1)/2)+2)
          print("Polly saw you attacking and attacked the enemy for " + str(a) + " hp!")
          enemy_health -= 1
        if enemy_health <= 0:
          if pet == 3:
            enemy_drop += 1
          if pet == 1:
            if slot12[0] % 2 == 1:
              enemy_xp *= 2
            elif slot12[0] % 2 == 0:
              enemy_xp *= 2 + (slot12[0] * .5)
          print("The enemy has died! You gained " + str(enemy_drop) + " coins, " + str(enemy_xp) + " experience points and your pet levelled up!")
          if pet == 1 and polly_pet_level < 99:
            polly_pet_level += 1
          if pet == 2 and slime_pet_level < 99:
            slime_pet_level += 1
          if pet == 3 and gold_pet_level < 99:
            gold_pet_level += 1
          if enemy_ability == 1:
            if slot7[0] < 9:
              print("You gained an evolution key!")
              slot7[0] += 1
            else:
              print("The evolution key was lost!")
          enemy_spawned = False
          if slot9[0] < 10 and slot9[1] < 9:
            slot9[2] += enemy_drop
            if slot9[2] > 9:
              slot9[2] = slot9[2] % 10
              slot9[1] += 1
            if slot9[1] > 9:
              slot9[1] = slot9[1] % 10
              slot9[0] += 1
          current_xp += int(enemy_xp)
    else:
      print("The enemy dodged!")
    
  elif move == "save":
    print("Your savefile is: ")
    for i in range(3):
      print(slot1[i], end="")
    for i in range(3):
      print(slot2[i], end="")
    for i in range(3):
      print(slot3[i], end="")
    for i in range(3):
      print(slot4[i], end="")
    for i in range(3):
      print(slot5[i], end="")
    for i in range(3):
      print(slot6[i], end="")
    for i in range(3):
      print(slot7[i], end="")
    for i in range(3):
      print(slot8[i], end="")
    for i in range(3):
      print(slot9[i], end="")
    for i in range(3):
      print(slot10[i], end="")
    for i in range(3):
      print(slot11[i], end="")
    for i in range(3):
      print(slot12[i], end="")
    for i in range(3):
      print(slot13[i], end="")
    for i in range(3):
      print(slot14[i], end="")
    for i in range(3):
      print(slot15[i], end="")
    print()

  elif move == "quit":
    print("You quit the game!")
    playing = False

  else:
    print("Invalid action! (Try entering 'help')")
    no_action = True

  #End of turn actions
  under = True
  if under:

    #Calculate Enemy Crti Damage
    crit = False
    if random.randint(0,9) < crit_chance:
      enemy_damage *= 2
      crit = True

    #Calculate Enemy Damage
    if pet == 2 and slot10[0] % 2 == 0 and slot10[0] != 0:
      if moves % (10 - slot10[0]/2) == 0 and moves != 0:
        enemy_attack = False
        print("The slime stopped an attack!")
    if enemy_attack == True:
      if move == "attack" and enemy_spawned and slot1[0] == 0:
        health -= enemy_damage
        print()
        print("The enemy did " + str(enemy_damage) + " damage to you.")
        print("You have " + str(health) + " health.")
      if move == "attack" and enemy_spawned and slot1[0] == 1:
        if random.randint(1,3) != 1:
          health -= enemy_damage
          print()
          
          print("You have " + str(health) + " health.")
      if move == "weapon":
        health -= enemy_damage
        print()
        print("The enemy did " + str(enemy_damage) + " damage to you.")
        print("You have " + str(health) + " health.")
      if move == "use" and used:
        health -= enemy_damage
        print()
        print("The enemy did " + str(enemy_damage) + " damage to you.")
        print("You have " + str(health) + " health.")
      if move == "shop" and item_bought:
        health -= enemy_damage
        print()
        print("The enemy did " + str(enemy_damage) + " damage to you.")
        print("You have " + str(health) + " health.")
      if move == "evolve" and evolved:
        health -= enemy_damage
        print()
        print("The enemy did " + str(enemy_damage) + " damage to you.")
        print("You have " + str(health) + " health.")  
      
    #Calculate healing and Levelling
    if current_xp > level*10:
      if level == 99:
        current_xp = 0
      else:
        current_xp = 0
        level += 1
        health += 10
        print("You levelled up!")
    if not no_action:
      heal += 1
      
    #Undo Crit Damage
    if crit:
      enemy_damage = int(enemy_damage/2)

    #Reset Variables
    no_action = False
    print()
    used = False
    item_bought = False
    pcrit = 0
    evolved = False
    money = slot9[0]*100 + slot9[1]*10 + slot9[2]
    moves += 1
    enemy_attack = True


    #End Game
    if health <= 0:
      print("You died!")
      playing = False

    #Heal 
    health_max = 10*(level+1)
    if health_max < 100:
      health_max = 100
    if health < health_max:
      if heal % 2 == 1:
        health += 1

    #Set variables
    slot8[2] = health % 10
    slot8[1] = int(((health % 100) - slot8[2])/10)
    slot8[0] = int(((health-slot8[2])/10-slot8[1])/10)

    slot4[1] = level % 10
    slot4[0] = int((level-slot4[1])/10)
    slot4[2] = int(current_xp/(level*10))

    slot10[0] = slime_pet_evo
    slot11[0] = gold_pet_evo
    slot12[0] = polly_pet_evo
    slot10[2] = slime_pet_level % 10
    slot10[1] = int((slime_pet_level-slot10[2])/10)
    slot11[2] = gold_pet_level % 10
    slot11[1] = int((gold_pet_level-slot11[2])/10)
    slot12[2] = polly_pet_level % 10
    slot12[1] = int((polly_pet_level-slot12[2])/10)
    
    slot6[0] = pet
    
    #Debug
    if debug:
      print(slot9)
      print(slot8)

  
  

