# =========================================
# Author: Okafor Chidubem Victoria (Vicky)
# Programiz November Challenge: Build a Game
# Title: Neon Arena: Cyber Gladiators
# Description: 
# Fight opponents in a neon cyber arena, 
# use attacks, power moves, and strategy. 
# Beat mini-challenges between fights to test your skills. 
# Opponents react and taunt, making the battle interactive and fun. 
# 🎮⚡💥
# =========================================

import random
import time

# -------------------------
# Helper Functions
# -------------------------
def delay_print(text):
    """Print text with a short delay for dramatic effect."""
    print(text)
    time.sleep(1)

def clear_screen():
    """Clear a few lines to simulate clearing screen without hiding content."""
    print("\n" * 5)

# -------------------------
# Mini-Challenges
# -------------------------
def challenge_zone(opponent_name):
    """
    Mini-challenge zone between fights.
    Combat-themed:
    1. Reflex/Dodge
    2. Hack Weak Point
    3. Combo Memory
    """
    print(f"\n🚀 Mini Challenge Zone! Stay sharp, {player['name']}!")
    print(f"You're facing {opponent_name}'s system. Choose your challenge:")
    print("[1] Dodge Attack ⚡  [2] Hack Weak Point 🔧  [3] Execute Combo 💻")
    choice = input(">> ").strip()
    
    if choice == "1":
        print("⚡ Incoming attack! Press Enter as fast as you can when I say GO!")
        input("Press Enter to start...")
        print("GO!")
        start_time = time.time()
        input("Press Enter NOW!")
        end_time = time.time()
        reaction = end_time - start_time
        if reaction < 1.5:
            print(f"✅ You dodged the attack! Reaction: {reaction:.2f}s")
        else:
            print(f"❌ Too slow! Reaction: {reaction:.2f}s")
    
    elif choice == "2":
        number = random.randint(1,5)
        try:
            guess = int(input("Guess the weak system point (1-5): "))
        except:
            guess = 0
        if guess == number:
            print("✅ Hack successful! You exploited a weakness! 🔥")
        else:
            print(f"❌ Hack failed! The weak point was {number}. Stay focused!")
    
    elif choice == "3":
        sequence = [random.choice(['A','B','X','Y']) for _ in range(4)]
        print("Memorize the attack combo: " + " ".join(sequence))
        time.sleep(2)
        clear_screen()
        user_input = input("Enter the combo sequence separated by spaces: ").strip().upper().split()
        if user_input == sequence:
            print("✅ Combo executed perfectly! 💥")
        else:
            print(f"❌ Combo failed! Correct sequence was: {' '.join(sequence)}")
    
    else:
        print("⚠️ Invalid choice. Challenge skipped.")

    print("✅ Mini-Challenge Complete! Back to the arena...\n")

# -------------------------
# Player Setup
# -------------------------
player = {
    "name": "Cyber Gladiator",
    "hp": 100,
    "power_moves": 2,
    "score": 0,
    "level": 1
}

# -------------------------
# Opponents Setup
# -------------------------
opponents = [
    {"name": "Cyberbot Alpha", "hp": 50, "attack_min": 8, "attack_max": 12},
    {"name": "Neon Sentinel", "hp": 70, "attack_min": 10, "attack_max": 15},
    {"name": "Omega Droid", "hp": 90, "attack_min": 12, "attack_max": 18},
    {"name": "Glitch Phantom", "hp": 110, "attack_min": 15, "attack_max": 22},
    {"name": "Omega Prime", "hp": 150, "attack_min": 18, "attack_max": 25}
]

# -------------------------
# Opponent Reactions & Taunts
# -------------------------
opponent_reactions = {
    "Cyberbot Alpha": [
        "System glitch! 🤖", "You got lucky! ⚡", "Sensors overloaded! 🔥",
        "Processing error!", "Critical hit detected!", "I need repairs! 🛠️",
        "Target locked!", "Malfunction!", "Resistance detected!", "You won't survive long!"
    ],
    "Neon Sentinel": [
        "You'll pay for that! 🔥", "My circuits burn! ⚡", "Shield breached!",
        "Overheating!", "Signal lost!", "Recalculating strategy!", "You think you can win?", 
        "Energy levels critical!", "Not bad... for a human!", "I am unstoppable!"
    ],
    "Omega Droid": [
        "Ugh! Resistance is annoying! 💥", "Impossible! 🤖", "System defenses failing!",
        "You underestimate me!", "Error 404: patience not found!", "Calibrating...", 
        "Your attacks are weak!", "Prepare to be destroyed!", "You cannot win!", "I adapt!"
    ],
    "Glitch Phantom": [
        "You cannot defeat me! 🌀", "My code is flawless! ⚡", "Glitching out!", 
        "Cannot compute!", "Illusions activated!", "Confusion detected!", 
        "You are trapped!", "Systems unstable!", "I phase through!", "You can't hit me!"
    ],
    "Omega Prime": [
        "Argh! You dare! 🔥", "I will crush you! 💥", "Perfection is mine!", 
        "You will fall!", "Resistance is meaningless!", "I dominate!", 
        "Your fate is sealed!", "I am supreme!", "You are insignificant!", "Prepare to perish!"
    ]
}

opponent_taunts = {
    "Cyberbot Alpha": [
        "You can't hit me! 🤖", "System online, prepare to lose! ⚡",
        "Engaging attack mode!", "Target acquired!", "Feel my circuits!", 
        "You are weak!", "Initializing strike!", "Cannot escape!", "Try harder!", "Weak human!"
    ],
    "Neon Sentinel": [
        "Feel the neon burn! 🔥", "Your circuits are slow! ⚡", "I shine brighter!",
        "Resistance is futile!", "You cannot survive!", "I strike fast!", "Prepare to fry!", 
        "Watch the sparks!", "I am glowing power!", "My lasers are ready!"
    ],
    "Omega Droid": [
        "Resistance is futile! 💥", "You are only level 1, pathetic! 🤖", "I adapt quickly!", 
        "Your tactics fail!", "Prepare for obliteration!", "System upgrade in progress!", 
        "No mercy!", "I am unstoppable!", "You can't stop me!", "Target locked!"
    ],
    "Glitch Phantom": [
        "Can you dodge this glitch? 🌀", "I am everywhere! ⚡", "Phasing attack!", 
        "Illusion strike!", "You see me, you lose!", "Cannot be hit!", "Glitch incoming!", 
        "I confuse you!", "You cannot escape!", "Systems corrupted!"
    ],
    "Omega Prime": [
        "You will fall like all the others! 🔥", "I am perfection incarnate! 💥", 
        "Witness true power!", "Your end is near!", "I am invincible!", "You are doomed!", 
        "Feel my wrath!", "No one can stop me!", "Ultimate strike engaged!", "I dominate all!"
    ]
}

# -------------------------
# Arena Events
# -------------------------
arena_events = [
    "Lightning Surge! Both fighters lose 5 HP! ⚡",
    "Overdrive! Your next attack does double damage! 🔥",
    "Glitch! Opponent loses 10 HP! 🌀",
    "Nano Shield! You block half damage next turn! 🛡️"
]

# -------------------------
# Game Intro
# -------------------------
delay_print("🎮 WELCOME TO NEON ARENA: CYBER GLADIATORS ⚡")
delay_print(f"Prepare for battle, {player['name']}!")
delay_print("Defeat all opponents to become the CHAMPION of the arena!\n")

# -------------------------
# Main Game Loop
# -------------------------
for opp in opponents:
    opponent = opp.copy()
    delay_print(f"\n⚔️ LEVEL {player['level']} — {opponent['name']} enters the arena! ⚡")
    delay_print(f"{opponent['name']} yells: '{random.choice(opponent_taunts[opponent['name']])}'")
    time.sleep(1)
    
    defend_next = False
    overdrive = False
    
    while opponent["hp"] > 0 and player["hp"] > 0:
        # Display status
        print(f"\n💠 {player['name']} HP: {player['hp']} | Power Moves: {player['power_moves']}")
        print(f"🤖 {opponent['name']} HP: {opponent['hp']}")
        
        # Arena Event Trigger (20% chance)
        if random.randint(1,5) == 1:
            event = random.choice(arena_events)
            delay_print(f"\n🎇 ARENA EVENT: {event}")
            if "Both fighters lose 5 HP" in event:
                player["hp"] -= 5
                opponent["hp"] -= 5
            elif "double damage" in event:
                overdrive = True
            elif "Opponent loses 10 HP" in event:
                opponent["hp"] -= 10
            elif "block half damage" in event:
                defend_next = True
        
        # Player Move
        print("\nChoose your move: [1] Attack ⚔️ [2] Defend 🛡️ [3] Power Move 💥")
        move = input(">> ").strip()
        
        if move == "1":
            damage = random.randint(12, 20)
            if overdrive:
                damage *= 2
                overdrive = False
                delay_print("🔥 OVERDRIVE ACTIVATED! Double Damage!")
            opponent["hp"] -= damage
            delay_print(f"⚡ You attack {opponent['name']} for {damage} HP!")
            reaction = random.choice(opponent_reactions[opponent["name"]])
            delay_print(f"{opponent['name']} reacts: '{reaction}'")
        
        elif move == "2":
            delay_print("🛡️ You defend this turn. Incoming damage reduced by 50%")
            defend_next = True
        
        elif move == "3" and player["power_moves"] > 0:
            damage = random.randint(25, 40)
            opponent["hp"] -= damage
            player["power_moves"] -= 1
            delay_print(f"💥 POWER MOVE! {opponent['name']} loses {damage} HP")
            reaction = random.choice(opponent_reactions[opponent["name"]])
            delay_print(f"{opponent['name']} reacts: '{reaction}'")
        
        else:
            delay_print("⚠️ Invalid move or no Power Moves left. Turn skipped.")
        
        # Check opponent defeat
        if opponent["hp"] <= 0:
            delay_print(f"\n🏆 You defeated {opponent['name']}! 🎉")
            player["score"] += player["level"] * 50
            player["level"] += 1
            player["hp"] += 20
            delay_print("✨ 20 HP restored for next fight!")
            challenge_zone(opponent["name"])
            break
        
        # Opponent attack
        ai_damage = random.randint(opponent["attack_min"], opponent["attack_max"])
        if defend_next:
            ai_damage = ai_damage // 2
            defend_next = False
        player["hp"] -= ai_damage
        delay_print(f"🤖 {opponent['name']} attacks! You lose {ai_damage} HP")
        taunt = random.choice(opponent_taunts[opponent["name"]])
        delay_print(f"{opponent['name']} yells: '{taunt}'")
        
        # Player defeat
        if player["hp"] <= 0:
            delay_print("\n💀 You have been defeated! GAME OVER 💀")
            break

# -------------------------
# End Game / Score & Ranking
# -------------------------
if player["hp"] > 0:
    delay_print("\n🌟 CONGRATULATIONS! You are the CHAMPION of NEON ARENA! 🌟")
else:
    delay_print("\n🔥 Better luck next time, Cyber Gladiator! 🔥")

delay_print(f"\n💠 FINAL SCORE: {player['score']} | Level Reached: {player['level']-1}")
delay_print("Thanks for playing NEON ARENA: CYBER GLADIATORS 💫")
delay_print("Created by Vicky 👑")
