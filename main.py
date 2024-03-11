# ORBITAL STRIKE
# By Kacper Kowalewski aka Impulse
# By Łukasz Świderski aka ShadwoWolf
# FINAL 1.5.4 ( Important sage, where all (96%) game features works )

import os, time, random, colorama
from colorama import Fore

# GAME VARIABLES

MENU = True
MAIN_GAME = False

AI_BATTLE = False
HUMAN_BATTLE = False

YELLOW = Fore.YELLOW
RED = Fore.RED
GREEN = Fore.GREEN
PURPLE = Fore.MAGENTA
CYAN = Fore.CYAN

R = Fore.RESET

def OS():
    return os.system('cls')

DEVELOPER_SETTINGS = False

# ASCII ART


PLANET_AI = """"

        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.-'`

"""
graphical_mode = False
graph_mode = f'{RED}OFF{R}'

diffult_ai_name = 'ADAM'

dev_mode = f'{RED}OFF{R}'

audit_logs = f'{RED}OFF{R}'
if_audit_logs = False


first_turn = f'{GREEN}PLAYER {YELLOW}ONE{R}'
turn_change = False

paying_mode = False
paying_option = f'{RED}OFF{R}'

PLAYER_ONE = {
    'health': 100,
    'money': 200,
    'have_shield': False,
    'shield_health': 0,
    'is_turn': True,
    'mines': 1
}

PLAYER_TWO = {
    'health': 100,
    'money': 200,
    'have_shield': False,
    'shield_health': 0,
    'is_turn': False,
    'mines': 1
}

bot_difficulty = f'{GREEN}Easy{R}'

while MENU:
    try:
        OS()
        print('##############################')
        if graphical_mode == False:
            print('1 - VS AI ( SOON )')
            print('2 - VS HUMAN')
            print('3 - Help')
            print('4 - Settings')
        elif graphical_mode == True:
            print('1 - 👤 🆚 🤖 ( 🕒 )')
            print('2 - 👤 🆚 👤')
            print('3 - ❓')
            print('4 - ⚙️')
        battle_type = int(input('> '))

        if battle_type == 1:
            MENU = False
            AI_BATTLE = True
            OS()
        elif battle_type == 2:
            MENU = False
            HUMAN_BATTLE = True
            AI_BATTLE = False
            OS()
        elif battle_type == 4:
            try:
                OS()
                print('--- SETTINGS ---')
                print(f'1 - Graphical Mode : {graph_mode}')
                print(f'2 - BOT Name: {diffult_ai_name}')
                print(f'3 - Developer settings: {dev_mode}')
                print(f'4 - Audit logs: {audit_logs}')
                print(f'5 - First Turn: {first_turn}')
                print(f"6 - {diffult_ai_name}'s Difficulty: {bot_difficulty}")
                print(f'7 - Paying: {paying_option}')

                if_grap = int(input('> '))

                if if_grap == 1:
                    if graphical_mode == False:
                        graphical_mode = True
                        graph_mode = f'{GREEN}ON{R}'
                        OS()
                    elif graphical_mode == True:
                        graphical_mode = False
                        graph_mode = f'{RED}OFF{R}'
                        OS()

                elif if_grap == 2:
                    OS()
                    print('Enter new bot name')
                    diffult_ai_name = input('> ')
                    OS()

                elif if_grap == 3:
                    if DEVELOPER_SETTINGS == False:
                        DEVELOPER_SETTINGS = True
                        dev_mode = f'{GREEN}ON{R}'
                        OS()
                    elif DEVELOPER_SETTINGS == True:
                        DEVELOPER_SETTINGS = False
                        dev_mode = f'{RED}OFF{R}'
                        OS()
                
                elif if_grap == 4:
                    if if_audit_logs == False:
                        if_audit_logs = True
                        audit_logs = f'{GREEN}ON{R}'
                        OS()
                    elif if_audit_logs == True:
                        if_audit_logs == False
                        audit_logs = f'{RED}OFF{R}'
                        OS()

                elif if_grap == 5:
                        if turn_change == False:
                            turn_change = True
                            first_turn = f'{GREEN}PLAYER {YELLOW}TWO{R}'
                            PLAYER_ONE['is_turn'] = False
                            PLAYER_TWO['is_turn'] = True
                            OS()
                        elif turn_change == True:
                            turn_change = False
                            first_turn = f'{GREEN}PLAYER {YELLOW}ONE{R}'
                            PLAYER_ONE['is_turn'] = True
                            PLAYER_TWO['is_turn'] = False
                            OS()
                elif if_grap == 6:
                    try:
                        OS()
                        print(f"-- Select {diffult_ai_name}'s difficulty --")
                        print('1 - Eeasy')
                        print('2 - Medium')
                        print('3 - Hard')
                        what_diffi = int(input('> '))

                        if what_diffi == 1:
                            if bot_difficulty != f'{GREEN}Easy{R}':
                                bot_difficulty = f'{GREEN}Easy{R}'
                            else:
                                OS()
                                print(f"{RED} [!] {R} Bot is already set to {GREEN}easy{R} difficulty!")
                                time.sleep(1.3)

                        elif what_diffi == 2:
                            if bot_difficulty != f'{YELLOW}Medium{R}':
                                bot_difficulty = f'{YELLOW}Medium{R}'
                            else:
                                OS()
                                print(f"{RED} [!] {R} Bot is already set to {YELLOW}medium{R} difficulty!")
                                time.sleep(1.3)
                        elif what_diffi == 3:
                            if bot_difficulty != f'{RED}Hard{R}':
                                bot_difficulty = f'{RED}Hard{R}'
                            else:
                                OS()
                                print(f"{RED} [!] {R} Bot is already set to {RED}hard{R} difficulty!")
                                time.sleep(1.3)
                    except ValueError or KeyError:
                        OS()
                elif if_grap == 7:
                    if paying_mode == False:
                        paying_mode = True
                        paying_option = f'{GREEN}ON{R}'
                    elif paying_mode == True:
                        paying_mode = False
                        paying_option = f'{RED}OFF{R}'



            except ValueError or KeyError:
                OS()
                
            
        elif battle_type == 3:
            OS()
            print('--- HELP FOR NEW PLAYERS ---')
            print('1. Statistics - displayed how much life you have, how many shields and how many mines ')
            print('2. Mines - give money every round and help with the economy. You can buy and sell mining')
            print('3. The shield - protects you from bullets. You can buy and renew shields')
            print('4. Ammunition - you can buy ammunition there and sell bullets which become more expensive and more expensive as they become rarer')
            print('5. Invest is a tab where you invest in the army which gives you increased bullet power, breakthroughs and happines which increase your earnings and the infrastructure of the planet Kotra gives you more life')
            print('6. Attack Player two - you attack the other player with the purchased missiles')
            print('7. First Player Turn - you give the round to your opponent')

            print('')
            exit_help = input(f'{RED}Press enter to exit{R}')


    except ValueError or KeyError:
        OS()

# variables ai

INVEST_MENU = {
    'Trade': 10,
    'Military': 1,
    'Planet_Infrastructure': 1,
    'Happines': 1
}

PLAYER = {
    'health': 100,
    'money': 200,
    'have_shield': False,
    'shield_health': 0,
    'is_turn': True,
    'mines': 1
}

AI = {
    'health': 100,
    'money': 200,
    'have_shield': False,
    'shield_health': 0,
    'mines': 1
}

INVEST_MENU_AI_STATS = {
    'Trade': 10,
    'Military': 1,
    'Planet_Infrastructure': 1,
    'Happines': 1
}

if bot_difficulty == f'{GREEN}Easy{R}':
    AI['health'] = 100
    AI['money'] = 7000000000000000000000000000000
    AI['have_shield'] = False
    AI['shield_health'] = 0
    AI['mines'] = 1
    INVEST_MENU_AI_STATS['Trade'] = 10
    INVEST_MENU_AI_STATS['Military'] = 1
    INVEST_MENU_AI_STATS['Planet_Infrastructure'] = 1
    INVEST_MENU_AI_STATS['Happines'] = 1

elif bot_difficulty == f'{YELLOW}Medium{R}':
    AI['health'] = 80
    AI['money'] = 700000000000000000000000000000
    AI['have_shield'] = False
    AI['shield_health'] = 0
    AI['mines'] = 6
    INVEST_MENU_AI_STATS['Trade'] = 30
    INVEST_MENU_AI_STATS['Military'] = 1.2
    INVEST_MENU_AI_STATS['Planet_Infrastructure'] = 3
    INVEST_MENU_AI_STATS['Happines'] = 3

elif bot_difficulty == f'{RED}Hard{R}':
    AI['health'] = 60
    AI['money'] = 7000000000000000000000000000
    AI['have_shield'] = False
    AI['shield_health'] = 0
    AI['mines'] = 14
    INVEST_MENU_AI_STATS['Trade'] = 50
    INVEST_MENU_AI_STATS['Military'] = 2.4
    INVEST_MENU_AI_STATS['Planet_Infrastructure'] = 5
    INVEST_MENU_AI_STATS['Happines'] = 5


Bullet_ai = {
    'name': 'Iron Bullet',
    'damage': 4,
    'can_shield': False,
    'stock': 0,
    'price': 100,
    'graphical_reference': '🪨'
}

Bullet_ai_2 = {
    'name': 'Zinc Bullet',
    'damage': 7,
    'can_shield': True,
    'stock': 0,
    'price': 400,
    'graphical_reference': '🧲'
}

Bullet_ai_3 = {
    'name': 'Diamond Bullet',
    'damage': 13,
    'can_shield': True,
    'stock': 0,
    'price': 800,
    'graphical_reference': '💎'
}

MINES_MENU_AI = False
SHIELD_MENU_AI = False
BULLETS_MENU_AI = False
INVEST_MENU_AI = False

if PLAYER['have_shield'] == False:
    PLAYER['shield_health'] = f"{RED}None{R}"

def is_shield_broken_ai():
    global PLAYER, AI
    if AI['have_shield'] == True:
        if AI['shield_health'] <= 0:
            AI['shield_health'] = 0
            AI['have_shield'] = False 

def is_shield_broken_ai_player():
    global PLAYER
    if PLAYER['have_shield'] == True:
        if PLAYER['shield_health'] <= 0:
            PLAYER['shield_health'] = 0
            PLAYER['have_shield'] = False


# AI CONTROLLER
    
def ai_invest_military():
    global AI, INVEST_MENU_AI_STATS
    if AI['money'] <= 100:
        AI['money'] -= 1
        INVEST_MENU_AI_STATS['Military'] += 1
    else:
        print(f"{RED} [!] {R} You don't have that much coins!")

def ai_invest_trade():
    global AI, INVEST_MENU_AI_STATS
    if AI['money'] <= 100:
        AI['money'] -= 1
        INVEST_MENU_AI_STATS['Trade'] += 1
    else:
        print(f"{RED} [!] {R} You don't have that much coins!")

def ai_invest_happy():
    global AI, INVEST_MENU_AI_STATS
    if AI['money'] <= 100:
        AI['money'] -= 1
        INVEST_MENU_AI_STATS['Happines'] += 1
    else:
        print(f"{RED} [!] {R} You don't have that much coins!")

def ai_invest_planet():
    global AI, INVEST_MENU_AI_STATS
    if AI['money'] <= 100:
        AI['money'] -= 1
        INVEST_MENU_AI_STATS['Planet_Infrastructure'] += 1
    else:
        print(f"{RED} [!] {R} You don't have that much coins!")

IS_AI_DEATH2 = False

IS_AI_PLATER2 = False

def is_ai_death():
    global AI, AI_BATTLE, IS_AI_DEATH2
    if AI['health'] <= 0:
        AI_BATTLE = False
        IS_AI_DEATH2 = True

def is_ai_death_player():
    global AI, AI_BATTLE, IS_AI_PLATER2
    if PLAYER['health'] <= 0:
        AI_BATTLE = False
        IS_AI_PLATER2 = True

while AI_BATTLE:
    try:
        if PLAYER['is_turn'] == True:
            OS()
            if graphical_mode == False:
                print('Statistics: ')
                print(f"Coins: {PLAYER['money']} [🪙 ] ")
                print(f"Shield Health: {PLAYER['shield_health']} [🛡️ ] ")
                print(f'Health: {PLAYER["health"]} [❤️ ] ')
                print(f'Mines: {PLAYER["mines"]} [⛏️ ] ')
                print("")
                if DEVELOPER_SETTINGS == True:
                    print(f"BOT HEALTH: {AI['health']}")
                    print(f"BOT MONEY: {AI['money']}")
                    print(f"BOT HAVE SHIELD: {AI['have_shield']}")
                    print(f"BOT SHIELD HEALTH: {AI['shield_health']}")
                    print(f"BOT MINES: {AI['mines']}")
                    print(f"BOT TRADE STAT: {INVEST_MENU_AI_STATS['Trade']}")
                    print(f"BOT MILITARY STAT: {INVEST_MENU_AI_STATS['Military']}")
                    print(f"BOT PLANET STAT: {INVEST_MENU_AI_STATS['Planet_Infrastructure']}")
                    print(f"BOT HAPPINES STAT: {INVEST_MENU_AI_STATS['Happines']}")
                    print()
                print('1 - Statistics')
                print('2 - Mines')
                print('3 - Shield')
                print('4 - Ammunition')
                print('5 - Invest')
                print('6 - Attack AI')
                print('7 - AI Turn')
            elif graphical_mode == True:
                print('-- 📊 --')
                print(f"🪙 : {PLAYER['money']}$")
                print(f"🛡️ : {PLAYER['shield_health']}%")
                print(f'❤️ : {PLAYER["health"]}%')
                print(f'⛏️ : {PLAYER["mines"]}')
                print("")
                if DEVELOPER_SETTINGS == True:
                    print(f"BOT HEALTH: {AI['health']}")
                    print(f"BOT MONEY: {AI['money']}")
                    print(f"BOT HAVE SHIELD: {AI['have_shield']}")
                    print(f"BOT SHIELD HEALTH: {AI['shield_health']}")
                    print(f"BOT MINES: {AI['mines']}")
                    print(f"BOT TRADE STAT: {INVEST_MENU_AI_STATS['Trade']}")
                    print(f"BOT MILITARY STAT: {INVEST_MENU_AI_STATS['Military']}")
                    print(f"BOT PLANET STAT: {INVEST_MENU_AI_STATS['Planet_Infrastructure']}")
                    print(f"BOT HAPPINES STAT: {INVEST_MENU_AI_STATS['Happines']}")
                    print()
                print('1 - 📊')
                print('2 - ⛏️')
                print('3 - 🛡️')
                print('4 - 🔫')
                print('5 - 📈')
                print('6 - ⚔️')
                print('7 - -> 🤖')

            players_turn = int(input('> '))

            if players_turn == 1:
                OS()
                print('Stats: ')
            elif players_turn == 2:
                if MINES_MENU_AI == False:
                    MINES_MENU_AI = True
                    AI_BATTLE = False
                    OS()
                    
                    while MINES_MENU_AI:
                        try:
                            if graphical_mode == False:
                                print('----- MINES MENU -----')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- ⛏️  ☰ -----')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            mines_player_ai_pick = int(input('> '))

                            if mines_player_ai_pick == 1:
                                OS()
                                print('--- CREATE MINE ---')
                                print('Mine x1 - Price : 150 - press 1 to buy')

                                mine_picker = int(input('> '))

                                if mine_picker == 1:
                                    if PLAYER['money'] >= 150:
                                        PLAYER['mines'] += 1
                                        PLAYER['money'] -= 150
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought 1 mine!")
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")

                            elif mines_player_ai_pick == 2:
                                if PLAYER['mines'] > 0:
                                    PLAYER['mines'] -= 1
                                    PLAYER['money'] += 150
                                    OS()
                                    print(f"{YELLOW} [?] {R} You sold 1 mine!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have any mine to sell!")

                            elif mines_player_ai_pick == 3:
                                MINES_MENU_AI = False
                                AI_BATTLE = True
                                OS()
                        
                        except ValueError or KeyError:
                            OS()

            elif players_turn == 3:
                AI_BATTLE = False
                SHIELD_MENU_AI = True
                OS()

                while SHIELD_MENU_AI:
                    try:
                        if graphical_mode == False:
                            print('----- SHIELD MENU -----')
                            print('1 - Buy - 100 🪙')
                            print('2 - Upgrade - 70 🪙')
                            print('3 - Refill - 50 🪙')
                            print('4 - Leave')
                        elif graphical_mode == True:
                            print('----- 🛡️  ☰ -----')
                            print('1 - 🛒 : 100 🪙')
                            print('2 - ⬆️ : 70 🪙')
                            print('3 - ♻ : 50 🪙')
                            print('4 - 🚪')

                        shield_player_ai_pick = int(input('> '))

                        if shield_player_ai_pick == 1:
                            if PLAYER['have_shield'] == False:
                                if PLAYER['money'] >= 100:
                                    PLAYER['money'] -= 100
                                    PLAYER['have_shield'] = True
                                    PLAYER['shield_health'] = 100
                                    OS()
                                    print(f"{YELLOW} [?] {R} You bought shield!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have that much coins!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You already have shield!")
                                    
                        elif shield_player_ai_pick == 2:
                            if PLAYER['have_shield'] == True:
                                if PLAYER['shield_health'] == 100:
                                        if PLAYER['money'] >= 70:
                                            PLAYER['shield_health'] = 200
                                            OS()
                                            print(f"{YELLOW} [?] {R} You upgraded your shield!")
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} Your shield don't have max health!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")

                        elif shield_player_ai_pick == 3:
                            if PLAYER['have_shield'] == True:
                                if PLAYER['shield_health'] < 50:
                                    if PLAYER['money'] >= 50:
                                        PLAYER['shield_health'] = 100
                                        PLAYER['money'] -= 50
                                        OS()
                                        print(f"{YELLOW} [?] {R} You refilled your shield!")
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                                else:
                                    OS()
                                    print(f"{RED} [?] {R} Your shield has more than 50 health!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")


                        elif shield_player_ai_pick == 4:
                            AI_BATTLE = True
                            SHIELD_MENU_AI = False
                            OS()


                    except ValueError or KeyError:
                        OS()
                
            elif players_turn == 4:
                try:
                    BULLETS_MENU_AI = True
                    AI_BATTLE = False
                    OS()

                    while BULLETS_MENU_AI:
                        try:
                            if graphical_mode == False:
                                print('----- AMMUNITION -----')
                                print('--- STOCK ---')
                                print(f'{Bullet_ai["name"]} : {Bullet_ai["stock"]}')
                                print(f'{Bullet_ai_2["name"]} : {Bullet_ai_2["stock"]}')
                                print(f'{Bullet_ai_3["name"]} : {Bullet_ai_3["stock"]}')
                                print('')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- 🔫 -----')
                                print('--- 📈 ---')
                                print(f'{Bullet_ai["graphical_reference"]} : {Bullet_ai["stock"]}')
                                print(f'{Bullet_ai_2["graphical_reference"]}: {Bullet_ai_2["stock"]}')
                                print(f'{Bullet_ai_3["graphical_reference"]} : {Bullet_ai_3["stock"]}')
                                print('')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            bullets_player_ai_pick = int(input('> '))

                            if bullets_player_ai_pick == 1:
                                OS()
                                print('--- SELECT AMMO ---')
                                print(f'1 - {Bullet_ai["name"]} - {Bullet_ai["price"]} 🪙')
                                print(f'2 - {Bullet_ai_2["name"]} - {Bullet_ai_2["price"]} 🪙')
                                print(f'3 - {Bullet_ai_3["name"]} - {Bullet_ai_3["price"]} 🪙')

                                what_ammo = int(input('> '))

                                if what_ammo == 1:
                                    if PLAYER['money'] >= Bullet_ai['price']:
                                        PLAYER['money'] -= Bullet_ai['price']
                                        Bullet_ai['stock'] += 1
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought {Bullet_ai['name']} x1")
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                                
                                elif what_ammo == 2:
                                        if PLAYER['money'] >= Bullet_ai_2['price']:
                                            PLAYER['money'] -= Bullet_ai_2['price']
                                            Bullet_ai_2['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_ai_2['name']} x1")
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                
                                elif what_ammo == 3:
                                        if PLAYER['money'] >= Bullet_ai_3['price']:
                                            PLAYER['money'] -= Bullet_ai_3['price']
                                            Bullet_ai_3['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_ai_3['name']} x1")
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")

                            
                            elif bullets_player_ai_pick == 3:
                                AI_BATTLE = True
                                BULLETS_MENU_AI = False
                                OS()


                        except ValueError or KeyError:
                            OS()

                except ValueError or KeyError:
                    OS()

            elif players_turn == 5:
                INVEST_MENU_AI = True
                AI_BATTLE = False
                OS()

                while INVEST_MENU_AI:
                    try:
                        if graphical_mode == False:
                            print('----- INVEST -----')
                            print('')
                            print('1 - Millitary - 100🪙')
                            print('2 - Trade - 100🪙')
                            print('3 - Planet Infrascructure - 100🪙')
                            print('4 - Happines - 100🪙')
                            print('5 - Leave')
                        elif graphical_mode == True:
                            print('----- 📊 -----')
                            print('')
                            print('1 - 🪖 : 100 🪙')
                            print('2 - 💱 : 100 🪙')
                            print('3 - 🏗️ : 100 🪙')
                            print('4 - 🍀 : 100 🪙')
                            print('5 - 🚪')

                        invest_picker = int(input('> '))

                        if invest_picker == 1:
                            if PLAYER['money'] >= 100:
                                PLAYER['money'] -= 100
                                INVEST_MENU['Military'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in millitary")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")

                        elif invest_picker == 2:
                            if PLAYER['money'] >= 100:
                                PLAYER['money'] -= 100
                                INVEST_MENU['Trade'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in trade")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        
                        elif invest_picker == 3:
                            if PLAYER['money'] >= 100:
                                PLAYER['money'] -= 100
                                INVEST_MENU['Planet_Infrastructure'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in planet")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")

                        elif invest_picker == 4:
                            if PLAYER['money'] >= 100:
                                PLAYER['money'] -= 100
                                INVEST_MENU['Happines'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in happines")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")

                        elif invest_picker == 5:
                            AI_BATTLE = True
                            INVEST_MENU_AI = False
                            OS()

                        else:
                            OS()

                    except ValueError or KeyError:
                        OS()

            elif players_turn == 6:
                OS()
                print('What bullet you want to shoot')
                print(f"1 - {Bullet_ai['name']}")
                print(f"2 - {Bullet_ai_2['name']}")
                print(f"3 - {Bullet_ai_3['name']}")
                
                what_bullet = int(input('> '))

                if what_bullet == 1: 
                    if Bullet_ai['stock'] >= 1:
                        if AI['have_shield'] == False:
                            Bullet_ai['stock'] -= 1
                            AI['health'] -= Bullet_ai['damage'] * INVEST_MENU['Military']
                            is_ai_death()
                        else:
                            OS()
                            print(f"{YELLOW} [?] {R} {Bullet_ai['name']} can't break shield")
                            time.sleep(1)
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_ai['name']}")
                        time.sleep(1)

                elif what_bullet == 2:
                    if Bullet_ai_2['stock'] >= 1:
                        if AI['have_shield'] == True:
                            Bullet_ai_2['stock'] -= 1
                            AI['shield_health'] -= Bullet_ai_2['damage'] * INVEST_MENU['Military']
                            is_shield_broken_ai()
                        elif AI['have_shield'] == False:
                            AI['health'] -= Bullet_ai_2['damage'] * INVEST_MENU['Military']
                            Bullet_ai_2['stock'] -= 1
                            is_ai_death()
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_ai_2['name']}")
                        time.sleep(1)

                elif what_bullet == 3:
                    if Bullet_ai_3['stock'] >= 1:
                        if AI['have_shield'] == True:
                            Bullet_ai_3['stock'] -= 1
                            AI['shield_health'] -= Bullet_ai_3['damage'] * INVEST_MENU['Military']
                            is_shield_broken_ai()
                        elif AI['have_shield'] == False:
                            AI['health'] -= Bullet_ai_3['damage'] * INVEST_MENU['Military']
                            Bullet_ai_3['stock'] -= 1
                            is_ai_death()
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_ai_3['name']}")
                        time.sleep(1)
        

            elif players_turn == 7:
                PLAYER['is_turn'] = False

        # AI CONTROLLER / HANDLE
        elif PLAYER['is_turn'] == False:
            PLAYER['money'] += PLAYER['mines'] * INVEST_MENU['Trade'] + INVEST_MENU['Happines']
            if PLAYER['health'] == 100:
                bullet_picker = random.randint(1, 3)
                if bullet_picker == 1:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 2: 
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 3:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True

            elif PLAYER['health'] <= 99:
                bullet_picker = random.randint(1, 3)
                if bullet_picker == 1:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 2: 
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 3:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True

            if PLAYER['health'] <= 0:
                OS()
                is_ai_death_player()

            if AI['health'] < 60 and AI['health'] >= 40:
                AI['have_shield'] = True
                AI['shield_health'] = 100
                bullet_picker = random.randint(1, 3)
                if bullet_picker == 1:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 2: 
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                elif bullet_picker == 3:
                    if PLAYER['have_shield'] == True:
                        PLAYER['shield_health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        is_shield_broken_ai_player()
                        PLAYER['is_turn'] = True
                    else:
                        PLAYER['health'] -= INVEST_MENU_AI_STATS['Military'] * Bullet_ai_2['damage'] / INVEST_MENU['Planet_Infrastructure']
                        PLAYER['is_turn'] = True
                







    except ValueError or KeyError:
        OS()





# VERSUSUS HUMAAAAAAAAAAAAN-------------------------------------^^--------------------------------------------------------------------------------------------------------------------------------------------------
# VERSUSUS HUMAAAAAAAAAAAAN-----------------------------------^^&----------------------------------------------------------------------------------------------------------------------------------------------------
# VERSUSUS HUMAAAAAAAAAAAAN---------------------------------&&------------------------------------------------------------------------------------------------------------------------------------------------------


PLANET_P1 = f""""
==============================================================
=         _____                                              =
=     ,-:` \;',`'-,     HEALTH: {PLAYER_ONE['health']}       =
=   .'-;_,;  ':-;_,'.                                        =
=  /;   '/    ,  _`.-\  SHIELD: {PLAYER_ONE['have_shield']}  =
= | '`. (`     /` ` \`|                                      =
= |:.  `\`-.   \_   / |                                      =
= |     (   `,  .`\ ;'|                                      =
=  \     | .'     `-'/                                       =
=   `.   ;/        .'                                        =
=     `'-._____.-'`            PLAYER ONE                    =
==============================================================
"""

PLANET_P2 = f""""
==============================================================
=         _____                                              =
=     ,-:` \;',`'-,     HEALTH: {PLAYER_TWO['health']}       =
=   .'-;_,;  ':-;_,'.                                        =
=  /;   '/    ,  _`.-\  SHIELD: {PLAYER_TWO['have_shield']}  =
= | '`. (`     /` ` \`|                                      =
= |:.  `\`-.   \_   / |                                      =
= |     (   `,  .`\ ;'|                                      =
=  \     | .'     `-'/                                       =
=   `.   ;/        .'                                        =
=     `'-._____.-'`            PLAYER TWO                    =
==============================================================
"""


# variable human

GAME_OVER_P1 = False

GAME_OVER_P2 = False

def is_shield_broken_p1():
    global PLAYER_ONE
    if PLAYER_ONE['have_shield'] == True:
        if PLAYER_ONE['shield_health'] <= 0:
            PLAYER_ONE['shield_health'] = 0
            PLAYER_ONE['have_shield'] = False 

def is_shield_broken_p2():
    global PLAYER_TWO
    if PLAYER_TWO['have_shield'] == True:
        if PLAYER_TWO['shield_health'] <= 0:
            PLAYER_TWO['shield_health'] = 0
            PLAYER_TWO['have_shield'] = False 


def is_health_over_p1():
    global PLAYER_ONE, PLAYER_TWO, HUMAN_BATTLE, MINES_MENU_HR, SHIELD_MENU_HR, BULLETS_MENU_HR, INVEST_MENU_HR, GAME_OVER_P1
    if PLAYER_ONE['health'] <= 0:
        PLAYER_ONE['health'] = 0
        PLAYER_ONE['is_turn'] = False
        PLAYER_TWO['is_turn'] = False
        HUMAN_BATTLE = False
        MINES_MENU_HR = False
        SHIELD_MENU_HR = False
        BULLETS_MENU_HR = False
        INVEST_MENU_HR = False
        GAME_OVER_P1 = True


def is_health_over_p2():
    global PLAYER_ONE, PLAYER_TWO, HUMAN_BATTLE, MINES_MENU_HR_TWO, SHIELD_MENU_HR_TWO, BULLETS_MENU_HR_TWO, INVEST_MENU_HR_TWO, GAME_OVER_P2
    if PLAYER_TWO['health'] <= 0:
        PLAYER_TWO['health'] = 0
        PLAYER_TWO['is_turn'] = False
        PLAYER_ONE['is_turn'] = False
        HUMAN_BATTLE = False
        MINES_MENU_HR_TWO = False
        SHIELD_MENU_HR_TWO = False
        BULLETS_MENU_HR_TWO = False
        INVEST_MENU_HR_TWO = False
        GAME_OVER_P2 = True


audit_log_p1 = []
audit_log_p2 = []

def show_logs_p1():
    global audit_log_p1
    for key in audit_log_p1:
        print(f'{key}\n')

def show_logs_p2():
    global audit_log_p2
    for key in audit_log_p2:
        print(f'{key}\n')

INVEST_MENU_P1 = {
    'Trade': 10,
    'Military': 1,
    'Planet_Infrastructure': 1,
    'Happines': 0
}

INVEST_MENU_P2 = {
    'Trade': 10,
    'Military': 1,
    'Planet_Infrastructure': 1,
    'Happines': 0
}


Bullet_hr_1 = {
    'name': 'Iron Bullet',
    'damage': 4,
    'can_shield': False,
    'stock': 0,
    'price': 100,
    'graphical_reference': '🪨'
}

Bullet_hr_2 = {
    'name': 'Gold Bullet',
    'damage': 7,
    'can_shield': False,
    'stock': 0,
    'price': 300,
    'graphical_reference': '🧈'
}

Bullet_hr_3 = {
    'name': 'Diamond Bulet',
    'damage': 13,
    'can_shield': True,
    'stock': 0,
    'price': 700,
    'graphical_reference': '💎'
}

Bullet_hr_4 = {
    'name': 'Obsidian Bullet',
    'damage': 30,
    'can_shield': True,
    'stock': 0,
    'price': 1100,
    'graphical_reference': '⚫'
}

# ############################################################# #

Bullet_hr_1_two = {
    'name': 'Iron Bullet',
    'damage': 4,
    'can_shield': False,
    'stock': 0,
    'price': 100,
    'graphical_reference': '🪨'
}

Bullet_hr_2_two = {
    'name': 'Gold Bullet',
    'damage': 7,
    'can_shield': False,
    'stock': 0,
    'price': 300,
    'graphical_reference': '🧈'
}

Bullet_hr_3_two = {
    'name': 'Diamond Bullet',
    'damage': 13,
    'can_shield': True,
    'stock': 0,
    'price': 700,
    'graphical_reference': '💎'
}

Bullet_hr_4_two = {
    'name': 'Obsidian Bullet',
    'damage': 30,
    'can_shield': True,
    'stock': 0,
    'price': 1100,
    'graphical_reference': '⚫'
}

MINES_MENU_HR = False
SHIELD_MENU_HR = False
BULLETS_MENU_HR = False
INVEST_MENU_HR = False

MINES_MENU_HR_TWO = False
SHIELD_MENU_HR_TWO = False
BULLETS_MENU_HR_TWO = False
INVEST_MENU_HR_TWO = False

while HUMAN_BATTLE:
    try:
        if PLAYER_ONE['is_turn'] == True:
            OS()
            #print(ocean_list)
            if graphical_mode == False:
                print('--- Statistics: --- ')
                print('--- PLAYER`S ONE TURN --- ')
                print(f"Coins: {PLAYER_ONE['money']} [🪙 ] ")
                print(f"Shield Health: {PLAYER_ONE['shield_health']} [🛡️ ] ")
                print(f'Health: {PLAYER_ONE["health"]} [❤️ ] ')
                print(f'Mines: {PLAYER_ONE["mines"]} [⛏️ ] ')
                if DEVELOPER_SETTINGS == True:
                    print(f"player two health: {PLAYER_TWO['health']}")
                    print(f"player two shield health: {PLAYER_TWO['shield_health']}")
                    print(f"player two shield active: {PLAYER_TWO['have_shield']}")
                    print(PLANET_P2)
                print("")
                print('1 - Statistics')
                print('2 - Mines')
                print('3 - Shield')
                print('4 - Ammunition')
                print('5 - Invest')
                print('6 - Attack Player Two')
                print('7 - Second Player Turn')
                if if_audit_logs == True:
                    print('8 - Show Audit Logs')
                if paying_mode == True:
                    print('9 - Pay')
            elif graphical_mode == True:
                print('-- 📊 --')
                print('--- 1️⃣👤 ---')
                print(f"🪙 : {PLAYER_ONE['money']}$")
                print(f"🛡️ : {PLAYER_ONE['shield_health']}%")
                print(f'❤️ : {PLAYER_ONE["health"]}%')
                print(f'⛏️ : {PLAYER_ONE["mines"]}')
                if DEVELOPER_SETTINGS == True:
                    print(f"player two health: {PLAYER_TWO['health']}")
                    print(f"player two shield health: {PLAYER_TWO['shield_health']}")
                    print(f"player two shield active: {PLAYER_TWO['have_shield']}")
                    print(PLANET_P2)
                print("")
                print('1 - 📊')
                print('2 - ⛏️')
                print('3 - 🛡️')
                print('4 - 🔫')
                print('5 - 📈')
                print('6 - ⚔️')
                print('7 --> 2️⃣👤 ')
                if if_audit_logs == True:
                    print('8 - 📁')
                if paying_mode == True:
                    print('9 - 💳')
            players_one_turn = int(input('> '))
            if players_one_turn == 1:
                OS()
                print('Stats: ')
            elif players_one_turn == 2:
                if MINES_MENU_HR == False:
                    MINES_MENU_HR = True
                    HUMAN_BATTLE = False
                    OS()
                    while MINES_MENU_HR:
                        try:
                            if graphical_mode == False:
                                print('----- MINES MENU -----')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- ⛏️  ☰ -----')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            mines_player_one_pick = int(input('> '))
                            if mines_player_one_pick == 1:
                                OS()
                                print('--- CREATE MINE ---')
                                print('Mine x1 - Price : 150 - press 1 to buy')
                                player_mine_picker = int(input('> '))
                                if player_mine_picker == 1:
                                    if PLAYER_ONE['money'] >= 150:
                                        PLAYER_ONE['mines'] += 1
                                        PLAYER_ONE['money'] -= 150
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought 1 mine!")
                                        audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}x1 mine{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                            elif mines_player_one_pick == 2:
                                if PLAYER_ONE['mines'] > 0:
                                    PLAYER_ONE['mines'] -= 1
                                    PLAYER_ONE['money'] += 150
                                    OS()
                                    print(f"{YELLOW} [?] {R} You sold 1 mine!")
                                    audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {RED}sold{R} {YELLOW}x1 mine{R}')
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have any mine to sell!")
                            elif mines_player_one_pick == 3:
                                MINES_MENU_HR = False
                                HUMAN_BATTLE = True
                                OS()
                        except ValueError or KeyError:
                            OS()
            elif players_one_turn == 3:
                HUMAN_BATTLE = False
                SHIELD_MENU_HR = True
                OS()
                while SHIELD_MENU_HR:
                    try:
                        if graphical_mode == False:
                            print('----- SHIELD MENU -----')
                            print('1 - Buy - 100 🪙')
                            print('2 - Upgrade - 70 🪙')
                            print('3 - Refill - 50 🪙')
                            print('4 - Leave')
                        elif graphical_mode == True:
                            print('----- 🛡️  ☰ -----')
                            print('1 - 🛒 : 100 🪙')
                            print('2 - ⬆️ : 70 🪙')
                            print('3 - ♻ : 50 🪙')
                            print('4 - 🚪')
                        shield_player_one_pick = int(input('> '))
                        if shield_player_one_pick == 1:
                            if PLAYER_ONE['have_shield'] == False:
                                if PLAYER_ONE['money'] >= 100:
                                    PLAYER_ONE['money'] -= 100
                                    PLAYER_ONE['have_shield'] = True
                                    PLAYER_ONE['shield_health'] = 100
                                    OS()
                                    print(f"{YELLOW} [?] {R} You bought shield!")
                                    audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}shield{R}')
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have that much coins!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You already have shield!")                                  
                        elif shield_player_one_pick == 2:
                            if PLAYER_ONE['have_shield'] == True:
                                if PLAYER_ONE['shield_health'] == 100:
                                        if PLAYER_ONE['money'] >= 70:
                                            PLAYER_ONE['shield_health'] = 200
                                            OS()
                                            print(f"{YELLOW} [?] {R} You upgraded your shield!")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}upgraded{R} {YELLOW}shield{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} Your shield don't have max health!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")
                        elif shield_player_one_pick == 3:
                            if PLAYER_ONE['have_shield'] == True:
                                if PLAYER_ONE['money'] >= 50:
                                    if PLAYER_ONE['shield_health'] < 50:
                                        PLAYER_ONE['shield_health'] = 100
                                        PLAYER_ONE['money'] -= 50
                                        OS()
                                        print(f"{YELLOW} [?] {R} You refilled your shield!")
                                        audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}refilled{R} {YELLOW}shield{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [?] {R} Your shield has more than 50 health!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have that much coins!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")
                        elif shield_player_one_pick == 4:
                            HUMAN_BATTLE = True
                            SHIELD_MENU_HR = False
                            OS()
                    except ValueError or KeyError:
                        OS()
            elif players_one_turn == 4:
                try:
                    BULLETS_MENU_HR = True
                    HUMAN_BATTLE = False
                    OS()
                    while BULLETS_MENU_HR:
                        try:
                            if graphical_mode == False:
                                OS()
                                print('----- AMMUNITION -----')
                                print('--- STOCK ---')
                                print(f'{Bullet_hr_1["name"]} : {Bullet_hr_1["stock"]}')
                                print(f'{Bullet_hr_2["name"]} : {Bullet_hr_2["stock"]}')
                                print(f'{Bullet_hr_3["name"]} : {Bullet_hr_3["stock"]}')
                                print(f'{Bullet_hr_4["name"]} : {Bullet_hr_4["stock"]}')
                                print('')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- 🔫 -----')
                                print('--- 📈 ---')
                                print(f'{Bullet_hr_1["graphical_reference"]} : {Bullet_hr_1["stock"]}')
                                print(f'{Bullet_hr_2["graphical_reference"]}: {Bullet_hr_2["stock"]}')
                                print(f'{Bullet_hr_3["graphical_reference"]} : {Bullet_hr_3["stock"]}')
                                print(f'{Bullet_hr_4["graphical_reference"]} : {Bullet_hr_4["stock"]}')
                                print('')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            bullets_player_one_pick = int(input('> '))
                            if bullets_player_one_pick == 1:
                                OS()
                                print('--- SELECT AMMO ---')
                                print(f'1 - {Bullet_hr_1["name"]} - {Bullet_hr_1["price"]} 🪙')
                                print(f'2 - {Bullet_hr_2["name"]} - {Bullet_hr_2["price"]} 🪙')
                                print(f'3 - {Bullet_hr_3["name"]} - {Bullet_hr_3["price"]} 🪙')
                                print(f'4 - {Bullet_hr_4["name"]} - {Bullet_hr_4["price"]} 🪙')
                                player_one_what_ammo = int(input('> '))
                                if player_one_what_ammo == 1:
                                    if PLAYER_ONE['money'] >= Bullet_hr_1['price']:
                                        PLAYER_ONE['money'] -= Bullet_hr_1['price']
                                        Bullet_hr_1['stock'] += 1
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought {Bullet_hr_1['name']} x1")
                                        audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_1["name"]}{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_one_what_ammo == 2:
                                        if PLAYER_ONE['money'] >= Bullet_hr_2['price']:
                                            PLAYER_ONE['money'] -= Bullet_hr_2['price']
                                            Bullet_hr_2['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_2['name']} x1")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_2["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_one_what_ammo == 3:
                                        if PLAYER_ONE['money'] >= Bullet_hr_3['price']:
                                            PLAYER_ONE['money'] -= Bullet_hr_3['price']
                                            Bullet_hr_3['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_3['name']} x1")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_3["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_one_what_ammo == 4:
                                        if PLAYER_ONE['money'] >= Bullet_hr_4['price']:
                                            PLAYER_ONE['money'] -= Bullet_hr_4['price']
                                            Bullet_hr_4['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_4['name']} x1")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_4["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                            elif bullets_player_one_pick == 2:
                                OS()
                                print('--- SELECT AMMO ---')
                                print(f'1 - {Bullet_hr_1["name"]} - {Bullet_hr_1["price"]} 🪙')
                                print(f'2 - {Bullet_hr_2["name"]} - {Bullet_hr_2["price"]} 🪙')
                                print(f'3 - {Bullet_hr_3["name"]} - {Bullet_hr_3["price"]} 🪙')
                                print(f'4 - {Bullet_hr_4["name"]} - {Bullet_hr_4["price"]} 🪙')
                                print('')
                                player_one_what_ammo_sell = int(input('> '))
                                if player_one_what_ammo_sell == 1:
                                    if Bullet_hr_1['stock'] >= 1:
                                        Bullet_hr_1['stock'] -= 1
                                        PLAYER_ONE['money'] += Bullet_hr_1['price'] / 2
                                        OS()
                                        print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_1['name']} for {Bullet_hr_1['price'] / 2}$")
                                        audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {RED}sold{R} {YELLOW}x1 {Bullet_hr_1["name"]}{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have any {Bullet_hr_1['name']}!")
                                elif player_one_what_ammo_sell == 2:
                                        if Bullet_hr_2['stock'] >= 1:
                                            Bullet_hr_2['stock'] -= 1
                                            PLAYER_ONE['money'] += Bullet_hr_2['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_2['name']} for {Bullet_hr_2['price'] / 2}$")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {RED}sold{R} {YELLOW}x1 {Bullet_hr_2["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_2['name']}!")
                                elif player_one_what_ammo_sell == 3:
                                        if Bullet_hr_3['stock'] >= 1:
                                            Bullet_hr_3['stock'] -= 1
                                            PLAYER_ONE['money'] += Bullet_hr_3['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold 1x {Bullet_hr_3['name']} for {Bullet_hr_3['price'] / 2}$")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {RED}sold{R} {YELLOW}x1 {Bullet_hr_3["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_3['name']}!")
                                elif player_one_what_ammo_sell == 4:
                                        if Bullet_hr_4['stock'] >= 1:
                                            Bullet_hr_4['stock'] -= 1
                                            PLAYER_ONE['money'] += Bullet_hr_4['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold 1x {Bullet_hr_4['name']} for {Bullet_hr_1['price'] / 2}$")
                                            audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {RED}sold{R} {YELLOW}x1 {Bullet_hr_4["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_4['name']}!")
                            elif bullets_player_one_pick == 3:
                                HUMAN_BATTLE = True
                                BULLETS_MENU_HR = False
                                OS()
                        except ValueError or KeyError:
                            OS()
                except ValueError or KeyError:
                    OS()
            elif players_one_turn == 5:
                INVEST_MENU_HR = True
                HUMAN_BATTLE = False
                OS()
                while INVEST_MENU_HR:
                    try:
                        if graphical_mode == False:
                            print('----- INVEST -----')
                            print('')
                            print('1 - Millitary - 100🪙')
                            print('2 - Trade - 100🪙')
                            print('3 - Planet Infrascructure - 100🪙')
                            print('4 - Happines - 100🪙')
                            print('5 - Leave')
                        elif graphical_mode == True:
                            print('----- 📊 -----')
                            print('')
                            print('1 - 🪖 : 100 🪙')
                            print('2 - 💱 : 100 🪙')
                            print('3 - 🏗️ : 100 🪙')
                            print('4 - 🍀 : 100 🪙')
                            print('5 - 🚪 : 100 🪙')
                        invest_one_picker = int(input('> '))
                        if invest_one_picker == 1:
                            if PLAYER_ONE['money'] >= 100:
                                PLAYER_ONE['money'] -= 100
                                INVEST_MENU_P1['Military'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in millitary")
                                audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {PURPLE}invested{R} {YELLOW}in millitary{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_one_picker == 2:
                            if PLAYER_ONE['money'] >= 100:
                                PLAYER_ONE['money'] -= 100
                                INVEST_MENU_P1['Trade'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in trade")
                                audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {PURPLE}invested{R} {YELLOW}in trade{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_one_picker == 3:
                            if PLAYER_ONE['money'] >= 100:
                                PLAYER_ONE['money'] -= 100
                                INVEST_MENU_P1['Planet_Infrastructure'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in your planet")
                                audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {PURPLE}invested{R} {YELLOW}in planet{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_one_picker == 4:
                            if PLAYER_ONE['money'] >= 100:
                                PLAYER_ONE['money'] -= 100
                                INVEST_MENU_P1['Happines'] += 2
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in happines")
                                audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {PURPLE}invested{R} {YELLOW}in happines{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_one_picker == 5:
                            HUMAN_BATTLE = True
                            INVEST_MENU_HR = False
                            OS()
                        else:
                            OS()
                    except ValueError or KeyError:
                        OS()
            elif players_one_turn == 6:
                OS()
                print('What bullet you want to shoot')
                print(f"1 - {Bullet_hr_1['name']}")
                print(f"2 - {Bullet_hr_2['name']}")
                print(f"3 - {Bullet_hr_3['name']}")
                print(f"4 - {Bullet_hr_4['name']}")
                what_bullet = int(input('> '))
                if what_bullet == 1: 
                    if Bullet_hr_1['stock'] >= 1:
                        if PLAYER_TWO['have_shield'] == False:
                            Bullet_hr_1['stock'] -= 1
                            PLAYER_TWO['health'] -= Bullet_hr_1['damage'] * INVEST_MENU_P1['Military'] / INVEST_MENU_P2['Planet_Infrastructure']
                            is_health_over_p2()
                        else:
                            OS()
                            print(f"{YELLOW} [?] {R} {Bullet_hr_1['name']} can't break shield")
                            time.sleep(1)
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_1['name']}")
                        time.sleep(1)
                elif what_bullet == 2:
                    if Bullet_hr_2['stock'] >= 1:
                        if PLAYER_TWO['have_shield'] == True:
                            Bullet_hr_2['stock'] -= 1
                            PLAYER_TWO['shield_health'] -= Bullet_hr_2['damage'] * INVEST_MENU_P1['Military']
                            is_shield_broken_p2()
                        elif PLAYER_TWO['have_shield'] == False:
                            PLAYER_TWO['health'] -= Bullet_hr_2['damage'] * INVEST_MENU_P2['Military'] / INVEST_MENU_P2['Planet_Infrastructure']
                            is_health_over_p2()  
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_2['name']}")
                        time.sleep(1)
                elif what_bullet == 3:
                    if Bullet_hr_3['stock'] >= 1:
                        if PLAYER_TWO['have_shield'] == True:
                            Bullet_hr_3['stock'] -= 1
                            PLAYER_TWO['shield_health'] -= Bullet_hr_3['damage'] * INVEST_MENU_P1['Military']
                            is_shield_broken_p2()
                        elif PLAYER_TWO['have_shield'] == False:
                            PLAYER_TWO['health'] -= Bullet_hr_3['damage'] * INVEST_MENU_P2['Military'] / INVEST_MENU_P2['Planet_Infrastructure']
                            is_health_over_p2()
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_3['name']}")
                        time.sleep(1) 
                elif what_bullet == 4:
                    if Bullet_hr_4['stock'] >= 1:
                        if PLAYER_TWO['have_shield'] == True:
                            Bullet_hr_4['stock'] -= 1
                            PLAYER_TWO['shield_health'] -= Bullet_hr_4['damage'] * INVEST_MENU_P1['Military']
                            is_shield_broken_p2()
                        elif PLAYER_TWO['have_shield'] == False:
                            PLAYER_TWO['health'] -= Bullet_hr_4['damage'] * INVEST_MENU_P2['Military'] / INVEST_MENU_P2['Planet_Infrastructure']
                            is_health_over_p2()
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_4['name']}")
                        time.sleep(1)            
            elif players_one_turn == 7:
                PLAYER_ONE['is_turn'] = False
                PLAYER_TWO['is_turn'] = True
                PLAYER_ONE['money'] += PLAYER_ONE['mines'] * INVEST_MENU_P1['Trade'] + INVEST_MENU_P1['Happines']
                audit_log_p1.append(f'    {CYAN}^^^ - PREVIOUS ROUND - ^^^{R}')
                OS()
            elif players_one_turn == 8 and if_audit_logs == True:
                OS()
                if graphical_mode == False:
                    print('--- Audit Log ---')
                    show_logs_p2()
                    two_exit = input(f'{RED}Press Enter To Exit{R}')
                elif graphical_mode == True:
                    print('--- 📁 ---')
                    show_logs_p2()
                    two_exit = input(f'{RED}Press Enter To Exit{R}')
            elif players_one_turn == 9 and paying_mode == True:
                OS()
                print('-- PAY SOME CASH TO PLAYER TWO --')
                print('How many cash u want to pay?')
                how_many_p1 = int(input('> '))
                if PLAYER_ONE['money'] >= how_many_p1:
                    PLAYER_ONE['money'] -= how_many_p1
                    PLAYER_TWO['money'] += how_many_p1
                    audit_log_p1.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player one {PURPLE}paid{R} {YELLOW}you {how_many_p1}${R}')
                    OS()
                else:
                    OS()
                    print(f"{RED} [!] {R} You don't have that much coins!")
                    time.sleep(1.3)
        elif PLAYER_TWO['is_turn'] == True: 
            OS()
            if graphical_mode == False:
                print('--- Statistics: --- ')
                print("--- PLAYER'S TWO TURN ---")
                print(f"Coins: {PLAYER_TWO['money']} [🪙 ] ")
                print(f"Shield Health: {PLAYER_TWO['shield_health']} [🛡️ ] ")
                print(f'Health: {PLAYER_TWO["health"]} [❤️ ] ')
                print(f'Mines: {PLAYER_TWO["mines"]} [⛏️ ] ')
                if DEVELOPER_SETTINGS == True:
                    print(f"player one health: {PLAYER_ONE['health']}")
                    print(f"player one shield health: {PLAYER_ONE['shield_health']}")
                    print(f"player one shield active: {PLAYER_ONE['have_shield']}")
                    print(PLANET_P1)
                print("")
                print('1 - Statistics')
                print('2 - Mines')
                print('3 - Shield')
                print('4 - Ammunition')
                print('5 - Invest')
                print('6 - Attack Player One')
                print('7 - First Player Turn')
                if if_audit_logs == True:
                    print('8 - Show Audit Logs')
                if paying_mode == True:
                    print('9 - Pay')
            elif graphical_mode == True:
                print('-- 📊 --')
                print("--- 2️⃣👤 ---")
                print(f"🪙 : {PLAYER_TWO['money']}$")
                print(f"🛡️ : {PLAYER_TWO['shield_health']}%")
                print(f'❤️ : {PLAYER_TWO["health"]}%')
                print(f'⛏️ : {PLAYER_TWO["mines"]}')
                if DEVELOPER_SETTINGS == True:
                    print(f"player one health: {PLAYER_ONE['health']}")
                    print(f"player one shield health: {PLAYER_ONE['shield_health']}")
                    print(f"player one shield active: {PLAYER_ONE['have_shield']}")
                    print(PLANET_P1)
                print("")
                print('1 - 📊')
                print('2 - ⛏️')
                print('3 - 🛡️')
                print('4 - 🔫')
                print('5 - 📈')
                print('6 - ⚔️')
                print('7 --> 1️⃣👤 ')
                if if_audit_logs == True:
                    print('8 - 📁')
                if paying_mode == True:
                    print('9 - 💳')
            players_two_turn = int(input('> '))
            if players_two_turn == 1:
                OS()
                print('Stats: ')
            elif players_two_turn == 2:
                if MINES_MENU_HR_TWO == False:
                    MINES_MENU_HR_TWO = True
                    HUMAN_BATTLE = False
                    OS()
                    while MINES_MENU_HR_TWO:
                        try:
                            if graphical_mode == False:
                                print('----- MINES MENU -----')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- ⛏️  ☰ -----')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            mines_player_two_pick = int(input('> '))
                            if mines_player_two_pick == 1:
                                OS()
                                print('--- CREATE MINE ---')
                                print('Mine x1 - Price : 150 - press 1 to buy')
                                player2_mine_picker = int(input('> '))
                                if player2_mine_picker == 1:
                                    if PLAYER_TWO['money'] >= 150:
                                        PLAYER_TWO['mines'] += 1
                                        PLAYER_TWO['money'] -= 150
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought 1 mine!")
                                        audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}x1 mine{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                            elif mines_player_two_pick == 2:
                                if PLAYER_TWO['mines'] > 0:
                                    PLAYER_TWO['mines'] -= 1
                                    PLAYER_TWO['money'] += 150
                                    OS()
                                    print(f"{YELLOW} [?] {R} You sold 1 mine!")
                                    audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {RED}sold{R} {YELLOW}x1 mine{R}')
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have any mine to sell!")
                            elif mines_player_two_pick == 3:
                                MINES_MENU_HR_TWO = False
                                HUMAN_BATTLE = True
                                OS()
                        except ValueError or KeyError:
                            OS()
            elif players_two_turn == 3:
                HUMAN_BATTLE = False
                SHIELD_MENU_HR_TWO = True
                OS()
                while SHIELD_MENU_HR_TWO:
                    try:
                        if graphical_mode == False:
                            print('----- SHIELD MENU -----')
                            print('1 - Buy - 100 🪙')
                            print('2 - Upgrade - 70 🪙')
                            print('3 - Refill - 50 🪙')
                            print('4 - Leave')
                        elif graphical_mode == True:
                            print('----- 🛡️  ☰ -----')
                            print('1 - 🛒 : 100 🪙')
                            print('2 - ⬆️ : 70 🪙')
                            print('3 - ♻ : 50 🪙')
                            print('4 - 🚪')
                        shield_player_two_pick = int(input('> '))
                        if shield_player_two_pick == 1:
                            if PLAYER_TWO['have_shield'] == False:
                                if PLAYER_TWO['money'] >= 100:
                                    PLAYER_TWO['money'] -= 100
                                    PLAYER_TWO['have_shield'] = True
                                    PLAYER_TWO['shield_health'] = 100
                                    OS()
                                    print(f"{YELLOW} [?] {R} You bought shield!")
                                    audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}shield{R}')
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have that much coins!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You already have shield!")   
                        elif shield_player_two_pick == 2:
                            if PLAYER_TWO['have_shield'] == True:
                                if PLAYER_TWO['shield_health'] == 100:
                                        if PLAYER_TWO['money'] >= 70:
                                            PLAYER_TWO['shield_health'] = 200
                                            OS()
                                            print(f"{YELLOW} [?] {R} You upgraded your shield!")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}upgraded{R} {YELLOW}shield{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} Your shield don't have max health!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")
                        elif shield_player_two_pick == 3:
                            if PLAYER_TWO['have_shield'] == True:
                                if PLAYER_TWO['money'] >= 50:
                                    if PLAYER_TWO['shield_health'] < 50:
                                        PLAYER_TWO['shield_health'] = 100
                                        PLAYER_TWO['money'] -= 50
                                        OS()
                                        print(f"{YELLOW} [?] {R} You refilled your shield!")
                                        audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}refilled{R} {YELLOW}shield{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [?] {R} Your shield has more than 50 health!")
                                else:
                                    OS()
                                    print(f"{RED} [!] {R} You don't have that much coins!")
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have shield!")
                        elif shield_player_two_pick == 4:
                            HUMAN_BATTLE = True
                            SHIELD_MENU_HR_TWO = False
                            OS()
                    except ValueError or KeyError:
                        OS()
            elif players_two_turn == 4:
                try:
                    BULLETS_MENU_HR_TWO = True
                    HUMAN_BATTLE = False
                    OS()
                    while BULLETS_MENU_HR_TWO:
                        try:
                            if graphical_mode == False:
                                OS()
                                print('----- AMMUNITION -----')
                                print('--- STOCK ---')
                                print(f'{Bullet_hr_1_two["name"]} : {Bullet_hr_1_two["stock"]}')
                                print(f'{Bullet_hr_2_two["name"]} : {Bullet_hr_2_two["stock"]}')
                                print(f'{Bullet_hr_3_two["name"]} : {Bullet_hr_3_two["stock"]}')
                                print(f'{Bullet_hr_4_two["name"]} : {Bullet_hr_4_two["stock"]}')
                                print('')
                                print('1 - Buy')
                                print('2 - Sell')
                                print('3 - Leave')
                            elif graphical_mode == True:
                                print('----- 🔫 -----')
                                print('--- 📈 ---')
                                print(f'{Bullet_hr_1_two["graphical_reference"]} : {Bullet_hr_1_two["stock"]}')
                                print(f'{Bullet_hr_2_two["graphical_reference"]}: {Bullet_hr_2_two["stock"]}')
                                print(f'{Bullet_hr_3_two["graphical_reference"]} : {Bullet_hr_3_two["stock"]}')
                                print(f'{Bullet_hr_4_two["graphical_reference"]} : {Bullet_hr_4_two["stock"]}')
                                print('')
                                print('1 - 🛒')
                                print('2 - 🏷️')
                                print('3 - 🚪')
                            bullets_player_two_pick = int(input('> '))
                            if bullets_player_two_pick == 1:
                                OS()
                                print('--- SELECT AMMO ---')
                                print(f'1 - {Bullet_hr_1_two["name"]} - {Bullet_hr_1_two["price"]} 🪙')
                                print(f'2 - {Bullet_hr_2_two["name"]} - {Bullet_hr_2_two["price"]} 🪙')
                                print(f'3 - {Bullet_hr_3_two["name"]} - {Bullet_hr_3_two["price"]} 🪙')
                                print(f'4 - {Bullet_hr_4_two["name"]} - {Bullet_hr_4_two["price"]} 🪙')
                                player_two_what_ammo = int(input('> '))
                                if player_two_what_ammo == 1:
                                    if PLAYER_TWO['money'] >= Bullet_hr_1_two['price']:
                                        PLAYER_TWO['money'] -= Bullet_hr_1_two['price']
                                        Bullet_hr_1_two['stock'] += 1
                                        OS()
                                        print(f"{YELLOW} [?] {R} You bought {Bullet_hr_1_two['name']} x1")
                                        audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_1_two["name"]}{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_two_what_ammo == 2:
                                        if PLAYER_TWO['money'] >= Bullet_hr_2_two['price']:
                                            PLAYER_TWO['money'] -= Bullet_hr_2_two['price']
                                            Bullet_hr_2_two['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_2_two['name']} x1")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_2_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_two_what_ammo == 3:
                                        if PLAYER_TWO['money'] >= Bullet_hr_3_two['price']:
                                            PLAYER_TWO['money'] -= Bullet_hr_3_two['price']
                                            Bullet_hr_3_two['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_3_two['name']} x1")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_3_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                                elif player_two_what_ammo == 4:
                                        if PLAYER_TWO['money'] >= Bullet_hr_4_two['price']:
                                            PLAYER_TWO['money'] -= Bullet_hr_4_two['price']
                                            Bullet_hr_4_two['stock'] += 1
                                            OS()
                                            print(f"{YELLOW} [?] {R} You bought {Bullet_hr_4_two['name']} x1")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {GREEN}bought{R} {YELLOW}x1 {Bullet_hr_4_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have that much coins!")
                            elif bullets_player_two_pick == 2:
                                OS()
                                print('--- SELECT AMMO ---')
                                print(f'1 - {Bullet_hr_1_two["name"]} - {Bullet_hr_1_two["price"]} 🪙')
                                print(f'2 - {Bullet_hr_2_two["name"]} - {Bullet_hr_2_two["price"]} 🪙')
                                print(f'3 - {Bullet_hr_3_two["name"]} - {Bullet_hr_3_two["price"]} 🪙')
                                print(f'4 - {Bullet_hr_4_two["name"]} - {Bullet_hr_4_two["price"]} 🪙')
                                print('')
                                player_two_what_ammo_sell = int(input('> '))
                                if player_two_what_ammo_sell == 1:
                                    if Bullet_hr_1_two['stock'] >= 1:
                                        Bullet_hr_1_two['stock'] -= 1
                                        PLAYER_TWO['money'] += Bullet_hr_1_two['price'] / 2
                                        OS()
                                        print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_1_two['name']} for {Bullet_hr_1_two['price'] / 2}$")
                                        audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {RED}sold{R} {YELLOW}x1 {Bullet_hr_1_two["name"]}{R}')
                                    else:
                                        OS()
                                        print(f"{RED} [!] {R} You don't have any {Bullet_hr_1_two['name']}!")
                                elif player_two_what_ammo_sell == 2:
                                        if Bullet_hr_2_two['stock'] >= 1:
                                            Bullet_hr_2_two['stock'] -= 1
                                            PLAYER_TWO['money'] += Bullet_hr_2_two['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_2_two['name']} for {Bullet_hr_2_two['price'] / 2}$")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {RED}sold{R} {YELLOW}x1 {Bullet_hr_2_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_2_two['name']}!")
                                elif player_two_what_ammo_sell == 3:
                                        if Bullet_hr_3_two['stock'] >= 1:
                                            Bullet_hr_3_two['stock'] -= 1
                                            PLAYER_TWO['money'] += Bullet_hr_3_two['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_3_two['name']} for {Bullet_hr_3_two['price'] / 2}$")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {RED}sold{R} {YELLOW}x1 {Bullet_hr_3_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_3_two['name']}!")
                                elif player_two_what_ammo_sell == 4:
                                        if Bullet_hr_4_two['stock'] >= 1:
                                            Bullet_hr_4_two['stock'] -= 1
                                            PLAYER_TWO['money'] += Bullet_hr_4_two['price'] / 2
                                            OS()
                                            print(f"{YELLOW} [?] {R} You sold x1 {Bullet_hr_4_two['name']} for {Bullet_hr_4_two['price'] / 2}$")
                                            audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {RED}sold{R} {YELLOW}x1 {Bullet_hr_4_two["name"]}{R}')
                                        else:
                                            OS()
                                            print(f"{RED} [!] {R} You don't have any {Bullet_hr_4_two['name']}!")
                            elif bullets_player_two_pick == 3:
                                HUMAN_BATTLE = True
                                BULLETS_MENU_HR_TWO = False
                                OS()
                        except ValueError or KeyError:
                            OS()
                except ValueError or KeyError:
                    OS()
            elif players_two_turn == 5:
                INVEST_MENU_HR_TWO = True
                HUMAN_BATTLE = False
                OS()
                while INVEST_MENU_HR_TWO:
                    try:
                        if graphical_mode == False:
                            print('----- INVEST -----')
                            print('')
                            print('1 - Millitary - 100🪙')
                            print('2 - Trade - 100🪙')
                            print('3 - Planet Infrascructure - 100🪙')
                            print('4 - Happines - 100🪙')
                            print('5 - Leave')
                        elif graphical_mode == True:
                            print('----- 📊 -----')
                            print('')
                            print('1 - 🪖 : 100 🪙')
                            print('2 - 💱 : 100 🪙')
                            print('3 - 🏗️ : 100 🪙')
                            print('4 - 🍀 : 100 🪙')
                            print('5 - 🚪 : 100 🪙')
                        invest_two_picker = int(input('> '))
                        if invest_two_picker == 1:
                            if PLAYER_TWO['money'] >= 100:
                                PLAYER_TWO['money'] -= 100
                                INVEST_MENU_P2['Military'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in millitary")
                                audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {PURPLE}invested{R} {YELLOW}in millitary{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_two_picker == 2:
                            if PLAYER_TWO['money'] >= 100:
                                PLAYER_TWO['money'] -= 100
                                INVEST_MENU_P2['Trade'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in trade")
                                audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {PURPLE}invested{R} {YELLOW}in trade{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_two_picker == 3:
                            if PLAYER_TWO['money'] >= 100:
                                PLAYER_TWO['money'] -= 100
                                INVEST_MENU_P2['Planet_Infrastructure'] += 1
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in your planet")
                                audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {PURPLE}invested{R} {YELLOW}in planet{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                        elif invest_two_picker == 4:
                            if PLAYER_TWO['money'] >= 100:
                                PLAYER_TWO['money'] -= 100
                                INVEST_MENU_P2['Happines'] += 2
                                OS()
                                print(f"{YELLOW} [?] {R} You invested in happines")
                                audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {PURPLE}invested{R} {YELLOW}in happines{R}')
                            else:
                                OS()
                                print(f"{RED} [!] {R} You don't have that much coins!")
                            
                        elif invest_two_picker == 5:
                            HUMAN_BATTLE = True
                            INVEST_MENU_HR_TWO = False
                            #OS()
                        else:
                            OS()
                    except ValueError or KeyError:
                        OS()
            elif players_two_turn == 6:
                OS()
                print('What bullet you want to shoot')
                print(f"1 - {Bullet_hr_1_two['name']}")
                print(f"2 - {Bullet_hr_2_two['name']}")
                print(f"3 - {Bullet_hr_3_two['name']}")
                print(f"4 - {Bullet_hr_4_two['name']}")
                what_bullet = int(input('> '))
                if what_bullet == 1: 
                    if Bullet_hr_1_two['stock'] >= 1:
                        if PLAYER_ONE['have_shield'] == False:
                            Bullet_hr_1['stock'] -= 1
                            PLAYER_ONE['health'] -= Bullet_hr_1_two['damage'] * INVEST_MENU_P1['Military'] / INVEST_MENU_P1['Planet_Infrastructure']
                        else:
                            OS()
                            print(f"{YELLOW} [?] {R} {Bullet_hr_1_two['name']} can't break shield")
                            time.sleep(1)
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_1_two['name']}")
                        time.sleep(1)
                elif what_bullet == 2:
                    if Bullet_hr_2_two['stock'] >= 1:
                        if PLAYER_ONE['have_shield'] == True:
                            Bullet_hr_2_two['stock'] -= 1
                            PLAYER_ONE['shield_health'] -= Bullet_hr_2_two['damage'] * INVEST_MENU_P2['Military']
                            is_shield_broken_p1()
                        elif PLAYER_ONE['have_shield'] == False:
                            PLAYER_ONE['health'] -= Bullet_hr_2_two['damage'] * INVEST_MENU_P1['Military'] / INVEST_MENU_P1['Planet_Infrastructure']
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_2_two['name']}")
                        time.sleep(1)
                elif what_bullet == 3:
                    if Bullet_hr_3_two['stock'] >= 1:
                        if PLAYER_ONE['have_shield'] == True:
                            Bullet_hr_3_two['stock'] -= 1
                            PLAYER_ONE['shield_health'] -= Bullet_hr_3_two['damage'] * INVEST_MENU_P2['Military']
                            is_shield_broken_p1()
                        elif PLAYER_ONE['have_shield'] == False:
                            PLAYER_ONE['health'] -= Bullet_hr_3_two['damage'] * INVEST_MENU_P1['Military'] / INVEST_MENU_P1['Planet_Infrastructure']
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_3_two['name']}")
                        time.sleep(1) 
                elif what_bullet == 4:
                    if Bullet_hr_4_two['stock'] >= 1:
                        if PLAYER_ONE['have_shield'] == True:
                            Bullet_hr_4_two['stock'] -= 1
                            PLAYER_ONE['shield_health'] -= Bullet_hr_4_two['damage'] * INVEST_MENU_P2['Military']
                            is_shield_broken_p1()
                        elif PLAYER_ONE['have_shield'] == False:
                            PLAYER_ONE['health'] -= Bullet_hr_4_two['damage'] * INVEST_MENU_P1['Military'] / INVEST_MENU_P1['Planet_Infrastructure']
                    else:
                        OS()
                        print(f"{YELLOW} [?] {R} You don't have any {Bullet_hr_4_two['name']}")
                        time.sleep(1)            
            elif players_two_turn == 7:
                PLAYER_ONE['is_turn'] = True
                PLAYER_TWO['is_turn'] = False
                PLAYER_TWO['money'] += PLAYER_TWO['mines'] * INVEST_MENU_P2['Trade'] + INVEST_MENU_P2['Happines']
                audit_log_p2.append(f'    {CYAN}^^^ - PREVIOUS ROUND - ^^^{R}')
                OS()
            elif players_two_turn == 8 and if_audit_logs == True:
                OS()
                if graphical_mode == False:
                    print('--- Audit Log ---')
                    show_logs_p1()
                    two_exit = input(f'{RED}Press Enter To Exit{R}')
                elif graphical_mode == True:
                    print('--- 📁 ---')
                    show_logs_p1()
                    two_exit = input(f'{RED}Press Enter To Exit{R}')
            elif players_two_turn == 9 and paying_mode == True:
                OS()
                print('-- PAY SOME CASH TO PLAYER TWO --')
                print('How many cash u want to pay?')
                how_many_p2 = int(input('> '))
                if PLAYER_TWO['money'] >= how_many_p2:
                    PLAYER_TWO['money'] -= how_many_p2
                    PLAYER_ONE['money'] += how_many_p2
                    OS()
                    audit_log_p2.append(f'{GREEN}[LOGS] / [?] {YELLOW}Player two {PURPLE}paid{R} {YELLOW}you {how_many_p2}${R}')
                    OS()
                else:
                    OS()
                    print(f"{RED} [!] {R} You don't have that much coins!")
                    time.sleep(1.3)
    except ValueError or KeyError:
        OS()
if GAME_OVER_P1 == True:
    OS()
    if graphical_mode == False:
        print('--- PLAYER TWO WON! ---')
        print('')
        print('<-- DEVELOPERS -->')
        print('DEV - Kacper Kowalewski')
        print('DEV - Łukasz Świderski')
        print('')
        print('<-- MAIN GAME DESIGNER -->')
        print('DES - Kacper Kowalewski')
        print('')
        print('<-- BETA TESTERS -->')
        print('BETA - Michał K')
        print('')
    elif graphical_mode == True:
        print('--- 👤2️⃣🏆 ---')
        print('')
        print('<-- </> -->')
        print('</> - Kacper Kowalewski')
        print('</> - Łukasz Świderski')
        print('')
        print('<-- 🖌️ -->')
        print('🖌️ - Kacper Kowalewski')
        print('')
        print('<-- 🕵 -->')
        print('🕵 - Michał K')
        print('')
elif GAME_OVER_P2 == True:
    OS()
    if graphical_mode == False:
        print('<-- PLAYER ONE WON! -->')
        print('')
        print('<-- DEVELOPERS -->')
        print('DEV - Kacper Kowalewski')
        print('DEV - Łukasz Świderski')
        print('')
        print('<-- MAIN GAME DESIGNER -->')
        print('DES - Kacper Kowalewski')
        print('')
        print('<-- BETA TESTERS -->')
        print('BETA - Michał K')
        print('')
    elif graphical_mode == True:
        print('--- 👤1️⃣🏆 ---')
        print('')
        print('<-- </> -->')
        print('</> - Kacper Kowalewski')
        print('</> - Łukasz Świderski')
        print('')
        print('<-- 🖌️ -->')
        print('🖌️ - Kacper Kowalewski')
        print('')
        print('<-- 🕵 -->')
        print('🕵 - Michał K')
        print('')


if IS_AI_DEATH2 == True:
    if graphical_mode == False:
        print('--- PLAYER WON! ---')
        print('')
        print('<-- DEVELOPERS -->')
        print('DEV - Kacper Kowalewski')
        print('DEV - Łukasz Świderski')
        print('')
        print('<-- MAIN GAME DESIGNER -->')
        print('DES - Kacper Kowalewski')
        print('')
        print('<-- BETA TESTERS -->')
        print('BETA - Michał K')
        print('')
    elif graphical_mode == True:
        print('--- 👤🏆 ---')
        print('')
        print('<-- </> -->')
        print('</> - Kacper Kowalewski')
        print('</> - Łukasz Świderski')
        print('')
        print('<-- 🖌️ -->')
        print('🖌️ - Kacper Kowalewski')
        print('')
        print('<-- 🕵 -->')
        print('🕵 - Michał K')
        print('')
elif IS_AI_PLATER2 == True:
    if graphical_mode == False:
        print('--- AI WON! ---')
        print('')
        print('<-- DEVELOPERS -->')
        print('DEV - Kacper Kowalewski')
        print('DEV - Łukasz Świderski')
        print('')
        print('<-- MAIN GAME DESIGNER -->')
        print('DES - Kacper Kowalewski')
        print('')
        print('<-- BETA TESTERS -->')
        print('BETA - Michał K')
        print('')
    elif graphical_mode == True:
        print('--- 🤖🏆 ---')
        print('')
        print('<-- </> -->')
        print('</> - Kacper Kowalewski')
        print('</> - Łukasz Świderski')
        print('')
        print('<-- 🖌️ -->')
        print('🖌️ - Kacper Kowalewski')
        print('')
        print('<-- 🕵 -->')
        print('🕵 - Michał K')
        print('')
