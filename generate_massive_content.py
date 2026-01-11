import json
import random

# --- DATASETS FOR TREASURE ---
capitals = [
    ("France", "Paris"), ("Germany", "Berlin"), ("Italy", "Rome"), ("Spain", "Madrid"),
    ("UK", "London"), ("Japan", "Tokyo"), ("China", "Beijing"), ("India", "New Delhi"),
    ("USA", "Washington D.C."), ("Canada", "Ottawa"), ("Brazil", "Brasilia"), ("Russia", "Moscow"),
    ("Australia", "Canberra"), ("Egypt", "Cairo"), ("Kenya", "Nairobi"), ("Mexico", "Mexico City"),
    ("Argentina", "Buenos Aires"), ("Turkey", "Ankara"), ("Thailand", "Bangkok"), ("Vietnam", "Hanoi"),
    ("South Korea", "Seoul"), ("Greece", "Athens"), ("Poland", "Warsaw"), ("Sweden", "Stockholm"),
    ("Norway", "Oslo"), ("Finland", "Helsinki"), ("Denmark", "Copenhagen"), ("Netherlands", "Amsterdam"),
    ("Belgium", "Brussels"), ("Austria", "Vienna"), ("Switzerland", "Bern"), ("Portugal", "Lisbon"),
    ("Ireland", "Dublin"), ("New Zealand", "Wellington"), ("South Africa", "Pretoria"), ("Peru", "Lima"),
    ("Chile", "Santiago"), ("Colombia", "Bogota"), ("Venezuela", "Caracas"), ("Saudi Arabia", "Riyadh"),
    ("Iran", "Tehran"), ("Iraq", "Baghdad"), ("Pakistan", "Islamabad"), ("Bangladesh", "Dhaka"),
    ("Indonesia", "Jakarta"), ("Malaysia", "Kuala Lumpur"), ("Philippines", "Manila"), ("Singapore", "Singapore")
]

elements = [
    ("Hydrogen", "H"), ("Helium", "He"), ("Lithium", "Li"), ("Beryllium", "Be"),
    ("Boron", "B"), ("Carbon", "C"), ("Nitrogen", "N"), ("Oxygen", "O"),
    ("Fluorine", "F"), ("Neon", "Ne"), ("Sodium", "Na"), ("Magnesium", "Mg"),
    ("Aluminum", "Al"), ("Silicon", "Si"), ("Phosphorus", "P"), ("Sulfur", "S"),
    ("Chlorine", "Cl"), ("Argon", "Ar"), ("Potassium", "K"), ("Calcium", "Ca"),
    ("Iron", "Fe"), ("Copper", "Cu"), ("Zinc", "Zn"), ("Silver", "Ag"),
    ("Gold", "Au"), ("Mercury", "Hg"), ("Lead", "Pb"), ("Uranium", "U")
]

# --- TREASURE GENERATOR (Unchanged) ---
def generate_treasure_questions(count=300):
    qs = []
    # Capitals
    for country, cap in capitals:
        wrong = random.sample([c[1] for c in capitals if c[1] != cap], 3)
        options = [cap] + wrong
        random.shuffle(options)
        qs.append({ "text": f"What is the capital of {country}?", "options": options, "correctIndex": options.index(cap), "explanation": f"{cap} is the capital of {country}.", "difficulty": 1 })
    # Elements
    for name, sym in elements:
        wrong = random.sample([e[1] for e in elements if e[1] != sym], 3)
        options = [sym] + wrong
        random.shuffle(options)
        qs.append({ "text": f"What is the chemical symbol for {name}?", "options": options, "correctIndex": options.index(sym), "explanation": f"{sym} is the symbol for {name}.", "difficulty": 1 })
    # Math Trivia
    shapes = [("Triangle", 3), ("Square", 4), ("Pentagon", 5), ("Hexagon", 6), ("Heptagon", 7), ("Octagon", 8)]
    for shape, sides in shapes:
        wrong = [sides + random.randint(1,3), sides - random.randint(1,2), sides + 4]
        options = [str(sides)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"How many sides does a {shape} have?", "options": options, "correctIndex": options.index(str(sides)), "explanation": f"A {shape} has {sides} sides.", "difficulty": 1 })
    
    # Fill remaining
    while len(qs) < 300:
        a, b = random.randint(10, 500), random.randint(10, 500)
        if abs(a - b) < 10: continue
        qs.append({ "text": f"Which number is larger: {a} or {b}?", "options": [str(a), str(b), "Equal", "None"], "correctIndex": 0 if a > b else 1, "explanation": f"{max(a,b)} > {min(a,b)}", "difficulty": 1 })

    random.shuffle(qs)
    # Split strictly into L1 and L2 for Treasure (just distribution)
    # Ideally Treasure difficulty is harder to grade, so we just split.
    l1 = qs[:150]
    l2 = qs[150:300]
    
    def assign_ids(list_qs, prefix):
        final = []
        for i, q in enumerate(list_qs):
            q["id"] = f"{prefix}_{i}"
            final.append(q)
        return final

    return {
        "id": "TREASURE",
        "name": "Treasure",
        "levels": [
            {"id": 1, "questions": assign_ids(l1, "t_l1")},
            {"id": 2, "questions": assign_ids(l2, "t_l2")}
        ]
    }

# --- PUZZLE GENERATOR (Refactored) ---

def generate_puzzle_level_1():
    # LEVEL 1: Easy Logic (Linear Steps, Simple Letters)
    qs = []
    # 1. Linear Series (+2, +5, -3) (50 qs)
    for _ in range(50):
        start = random.randint(1, 20)
        step = random.choice([2, 3, 4, 5, 10])
        seq = [start + x*step for x in range(5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans+step, ans-1, ans+2]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Next in series: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": f"Add {step} to each number.", "difficulty": 1 })

    # 2. Letter Skip 1 (A, C, E) (50 qs)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(50):
        step = 2 # Fixed skip 1 (step 2)
        start = random.randint(0, 10)
        seq = [alphabet[start + x*step] for x in range(5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [alphabet[start + 4*step + 1], alphabet[start + 4*step - 1], alphabet[start + 4*step + 2]] 
        options = [ans] + wrong
        random.shuffle(options)
        qs.append({ "text": f"Next letter: {', '.join(disp)}, ?", "options": options, "correctIndex": options.index(ans), "explanation": "Skip 1 letter.", "difficulty": 1 })
        
    return qs

def generate_puzzle_level_2():
    # LEVEL 2: Moderate Logic (Squares, Geometric, Letter Step > 2)
    qs = []
    # 1. Squares (50 qs)
    for _ in range(30):
        start = random.randint(1, 6)
        seq = [(start+x)**2 for x in range(5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans+5, ans-5, ans+10]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Complete: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": "Series of squares.", "difficulty": 2 })

    # 2. Geometric (x2, x3) (40 qs)
    for _ in range(40):
        start = random.randint(2, 5)
        mult = random.choice([2, 3])
        seq = [start * (mult**x) for x in range(5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans+mult, ans*2, ans-mult]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Next: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": f"Multiply by {mult}.", "difficulty": 2 })

    # 3. Letter Skip 2 or 3 (30 qs)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(30):
        step = random.randint(3, 4)
        start = random.randint(0, 5)
        seq = [alphabet[start + x*step] for x in range(5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [alphabet[(start+4*step+1)%26], alphabet[(start+4*step-1)%26], "A"]
        options = [ans] + wrong
        random.shuffle(options)
        qs.append({ "text": f"Next letter: {', '.join(disp)}, ?", "options": options, "correctIndex": options.index(ans), "explanation": f"Skip {step-1} letters.", "difficulty": 2 })
        
    return qs
    
def generate_puzzle_level_3():
    # LEVEL 3: Hard Logic (Fibonacci, Primes, Pronic)
    qs = []
    # 1. Fibonacci (30 qs)
    for _ in range(30):
        a, b = random.randint(1, 10), random.randint(1, 10)
        seq = [a, b]
        for _ in range(4): seq.append(seq[-1]+seq[-2])
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans+seq[-2], ans-1, ans+2]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Series: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": "Sum of previous two.", "difficulty": 3 })

    # 2. Pronic n(n+1) (30 qs)
    for _ in range(30):
        start = random.randint(2, 8)
        seq = [x*(x+1) for x in range(start, start+5)]
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans+2, ans+5, ans-2]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Series: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": "n * (n+1) pattern.", "difficulty": 3 })
        
    # 3. Two-Step Ops (x2 + 1) (40 qs)
    for _ in range(40):
        start = random.randint(2, 5)
        curr = start
        seq = [curr]
        for _ in range(4):
            curr = curr * 2 + 1
            seq.append(curr)
        ans = seq[-1]
        disp = seq[:-1]
        wrong = [ans-1, ans+2, ans*2]
        options = [str(ans)] + [str(x) for x in wrong]
        random.shuffle(options)
        qs.append({ "text": f"Next: {', '.join(map(str, disp))}, ?", "options": options, "correctIndex": options.index(str(ans)), "explanation": "Multiply by 2, then add 1.", "difficulty": 3 })

    return qs

def generate_full_puzzle_quiz():
    l1 = generate_puzzle_level_1()
    l2 = generate_puzzle_level_2()
    l3 = generate_puzzle_level_3()
    
    # Pad to ensured counts if needed, but loop counts above ensure ~100 per level
    # We want 3 levels clearly defined.
    
    def assign_ids(list_qs, prefix):
        final = []
        for i, q in enumerate(list_qs):
            q["id"] = f"{prefix}_{i}"
            final.append(q)
        return final

    return {
        "id": "PUZZLE",
        "name": "Puzzle",
        "levels": [
            {"id": 1, "questions": assign_ids(l1, "p_l1")},  # Easy
            {"id": 2, "questions": assign_ids(l2, "p_l2")},  # Medium
            {"id": 3, "questions": assign_ids(l3, "p_l3")}   # Hard
        ]
    }

if __name__ == "__main__":
    t_data = generate_treasure_questions(300)
    p_data = generate_full_puzzle_quiz()
    
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(t_data, f, indent=2)
        
    with open('app/src/main/assets/puzzle.json', 'w') as f:
        json.dump(p_data, f, indent=2)
