import json
import random

# --- TREASURE GENERATOR (Procedural - High Volume of Facts) ---
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

def generate_treasure_questions():
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
    
    # Fill to 300
    while len(qs) < 300:
        a, b = random.randint(10, 500), random.randint(10, 500)
        if abs(a - b) < 10: continue
        qs.append({ "text": f"Which number is larger: {a} or {b}?", "options": [str(a), str(b), "Equal", "None"], "correctIndex": 0 if a > b else 1, "explanation": f"{max(a,b)} > {min(a,b)}", "difficulty": 1 })

    random.shuffle(qs)
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

# --- PUZZLE GENERATOR (CURATED - Hand-Picked Variety) ---

def generate_curated_puzzle_quiz():
    # LEVEL 1: Riddles & Simple Logic
    l1_raw = [
        {"text": "What comes once in a minute, twice in a moment, but never in a thousand years?", "options": ["The letter M", "Time", "The Moon", "A Second"], "correct": 0, "expl": "The letter 'M' appears once in 'Minute', twice in 'Moment'."},
        {"text": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "options": ["An Echo", "A Cloud", "A Ghost", "A Tree"], "correct": 0, "expl": "An echo returns sound."},
        {"text": "What has keys but can't open locks?", "options": ["A Piano", "A Map", "A Coin", "A Clock"], "correct": 0, "expl": "A piano has keys."},
        {"text": "What has to be broken before you can use it?", "options": ["An Egg", "A Window", "A Promise", "A Secret"], "correct": 0, "expl": "An egg must be broken to be cooked."},
        {"text": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "options": ["A Candle", "A Tree", "A Person", "A Mountain"], "correct": 0, "expl": "A candle burns down."},
        {"text": "What is full of holes but still holds water?", "options": ["A Sponge", "A Bucket", "A Net", "A Shirt"], "correct": 0, "expl": "A sponge absorbs water."},
        {"text": "Find the odd one out: Car, Bike, Bus, Plane", "options": ["Plane", "Bus", "Bike", "Car"], "correct": 0, "expl": "Plane flies, others are road vehicles."},
        {"text": "What goes up but never comes down?", "options": ["Age", "Rain", "Ball", "Rocket"], "correct": 0, "expl": "Your age only increases."},
        {"text": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", "options": ["A Map", "A Globe", "A Dream", "A Book"], "correct": 0, "expl": "A map depicts these things flat."},
        {"text": "What gets wet while drying?", "options": ["A Towel", "A Sponge", "The Sun", "Water"], "correct": 0, "expl": "A towel absorbs moisture."},
        {"text": "Next number: 2, 4, 6, 8, ?", "options": ["10", "12", "9", "11"], "correct": 0, "expl": "Add 2."},
        {"text": "Next number: 5, 10, 15, 20, ?", "options": ["25", "30", "22", "35"], "correct": 0, "expl": "Add 5."},
        {"text": "Next letter: A, B, C, D, ?", "options": ["E", "F", "G", "H"], "correct": 0, "expl": "Alphabetical order."},
        {"text": "If you have a bowl with six apples and you take away four, how many do you have?", "options": ["4", "2", "6", "0"], "correct": 0, "expl": "You took 4, so you have 4."},
        {"text": "Which month has 28 days?", "options": ["All of them", "February", "January", "December"], "correct": 0, "expl": "All months have at least 28 days."},
        {"text": "What is always in front of you but can’t be seen?", "options": ["The Future", "The Past", "Your Nose", "The Wind"], "correct": 0, "expl": "The future lies ahead."},
        {"text": "I have a head and a tail that will never meet. Having too many of me is always a treat. What am I?", "options": ["A Coin", "A Snake", "A Cat", "A Story"], "correct": 0, "expl": "A coin has a head and tail."},
        {"text": "What can you break, even if you never pick it up or touch it?", "options": ["A Promise", "Glass", "A Plate", "The Law"], "correct": 0, "expl": "You break a promise verbally/mentally."},
        {"text": "Next in series: 1, 1, 1, 1, ?", "options": ["1", "2", "0", "11"], "correct": 0, "expl": "Constant series."},
        {"text": "Mary's father has five daughters: Nana, Nene, Nini, Nono, and...?", "options": ["Mary", "Nunu", "Nina", "Nana"], "correct": 0, "expl": "Mary is the fifth daughter."}
    ]

    # LEVEL 2: Moderate Logic & Wordplay
    l2_raw = [
        {"text": "What question can you never answer 'yes' to?", "options": ["Are you asleep?", "Are you hungry?", "Are you human?", "Are you reading?"], "correct": 0, "expl": "If you are asleep, you cannot answer."},
        {"text": "A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?", "options": ["He was bald", "He wore a hood", "It wasn't raining hard", "He was inside"], "correct": 0, "expl": "He had no hair to get wet."},
        {"text": "What goes up and down but doesn't move?", "options": ["A Staircase", "An Elevator", "A Ball", "Temperature"], "correct": 0, "expl": "A staircase stays in place."},
        {"text": "If two's company, and three's a crowd, what are four and five?", "options": ["Nine", "Fun", "Strangers", "A Group"], "correct": 0, "expl": "4 + 5 = 9."},
        {"text": "What begins with T, ends with T, and has T in it?", "options": ["A Teapot", "A Tent", "Target", "Toast"], "correct": 0, "expl": "'Tea'-pot."},
        {"text": "Next number: 1, 4, 9, 16, ?", "options": ["25", "36", "20", "24"], "correct": 0, "expl": "Squares: 1^2, 2^2, 3^2, 4^2, 5^2."},
        {"text": "Next number: 3, 6, 12, 24, ?", "options": ["48", "36", "30", "50"], "correct": 0, "expl": "Double the previous number."},
        {"text": "Next letter: A, C, E, G, ?", "options": ["I", "H", "J", "K"], "correct": 0, "expl": "Skip 1: B, D, F, H are skipped."},
        {"text": "Identify the pattern: O, T, T, F, F, S, S, ...?", "options": ["E", "N", "T", "O"], "correct": 0, "expl": "One, Two, Three, Four, Five, Six, Seven, Eight."},
        {"text": "What belongs to you, but other people use it more than you?", "options": ["Your Name", "Your Car", "Your Money", "Your House"], "correct": 0, "expl": "People call you by your name."},
        {"text": "I have branches, but no fruit, trunk or leaves. What am I?", "options": ["A Bank", "A River", "A Chair", "A Library"], "correct": 0, "expl": "A bank has branches."},
        {"text": "The more of this there is, the less you see. What is it?", "options": ["Darkness", "Fog", "Light", "Noise"], "correct": 0, "expl": "Darkness obscures vision."},
        {"text": "What has many teeth but cannot bite?", "options": ["A Comb", "A Gear", "A Saw", "A Zipper"], "correct": 0, "expl": "A comb has teeth."},
        {"text": "What is bigger than God, more evil than the devil, the poor have it, the rich need it, and if you eat it you'll die?", "options": ["Nothing", "Everything", "Money", "Power"], "correct": 0, "expl": "Nothing is bigger than God, etc."},
        {"text": "What word is spelled incorrectly in every dictionary?", "options": ["Incorrectly", "Wrongly", "False", "Error"], "correct": 0, "expl": "The word 'Incorrectly' is spelled that way."},
        {"text": "Some months have 30 days, others have 31. How many have 28?", "options": ["12", "1", "6", "11"], "correct": 0, "expl": "All 12 months have at least 28 days."},
        {"text": "Logical sequence: J, F, M, A, M, J, ...?", "options": ["J", "A", "S", "O"], "correct": 0, "expl": "January, February, March... July."},
        {"text": "Tom is taller than Peter, and Peter is shorter than Mark. Mark is shorter than Tom. Who is the tallest?", "options": ["Tom", "Mark", "Peter", "None"], "correct": 0, "expl": "Tom > Mark > Peter."},
        {"text": "If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?", "options": ["A Mirror", "An Egg", "A Glass", "A Phone"], "correct": 0, "expl": "A mirror reflects your smile but breaks easily."},
        {"text": "I exist only when there is light, but direct light kills me. What am I?", "options": ["A Shadow", "A Vampire", "A Photo", "A Film"], "correct": 0, "expl": "A shadow needs light to cast, but light filling it destroys it."}
    ]

    # LEVEL 3: Hard Lateral Thinking & Math Logic
    l3_raw = [
        {"text": "A man is looking at a picture of someone. 'Brothers and sisters I have none, but that man's father is my father's son.' Who is in the picture?", "options": ["His Son", "Himself", "His Father", "His Uncle"], "correct": 0, "expl": "'My father's son' with no siblings is ME. 'That man's father is ME'. So that man is my son."},
        {"text": "If 1=3, 2=3, 3=5, 4=4, 5=4, then 6=?", "options": ["3", "4", "5", "6"], "correct": 0, "expl": "Count the number of letters in the number word: SIX has 3."},
        {"text": "What 5-letter word becomes shorter when you add two letters to it?", "options": ["Short", "Small", "Brief", "Little"], "correct": 0, "expl": "Short + 'er' = Shorter."},
        {"text": "Logic Series: 2, 3, 5, 7, 11, ?", "options": ["13", "15", "17", "12"], "correct": 0, "expl": "Sequence of Prime Numbers."},
        {"text": "Logic Series: 1, 1, 2, 3, 5, 8, ?", "options": ["13", "12", "21", "10"], "correct": 0, "expl": "Fibonacci: 5 + 8 = 13."},
        {"text": "Four people can build a boat in 4 days. How long does it take one person unless they quit?", "options": ["16 Days", "4 Days", "8 Days", "1 Day"], "correct": 0, "expl": "4 people * 4 days = 16 'man-days'. 1 person takes 16 days."},
        {"text": "What can travel around the world while staying in a corner?", "options": ["A Stamp", "A Thought", "A Plane", "The Moon"], "correct": 0, "expl": "A stamp stays on the corner of the envelope."},
        {"text": "Forward I am heavy, but backward I am not. What am I?", "options": ["Ton", "Not", "Pot", "Pan"], "correct": 0, "expl": "TON spelled backward is NOT."},
        {"text": "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?", "options": ["$0.05", "$0.10", "$0.01", "$0.50"], "correct": 0, "expl": "B + b = 1.10. B = b + 1.00. (b+1)+b = 1.10 -> 2b = 0.10 -> b = 0.05."},
        {"text": "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?", "options": ["5 Minutes", "100 Minutes", "20 Minutes", "1 Minute"], "correct": 0, "expl": "Each machine takes 5 minutes to make 1 widget. So 100 machines also take 5 minutes for 100 widgets."},
        {"text": "Next: 31, 28, 31, 30, ...?", "options": ["31", "30", "29", "28"], "correct": 0, "expl": "Days in months: Jan, Feb, Mar, Apr, May (31)."},
        {"text": "You are running in a race and pass the person in second place. What place are you in?", "options": ["Second", "First", "Third", "Last"], "correct": 0, "expl": "You replace the person in second place."},
        {"text": "There are three switches downstairs. Each corresponds to one of three light bulbs in the attic. You can turn the switches on and off and leave them in any position. You can only make one trip upstairs. How do you identify which switch is for which bulb?", "options": ["Heat & Light", "Guess", "Check wires", "Ask a friend"], "correct": 0, "expl": "Turn one on for min, turn off. Turn second on. Go up: Lit=2nd, Warm=1st, Cold=3rd."},
        {"text": "What number is missing: 8, 5, 4, 9, 1, 7, 6, 3, 2, ?", "options": ["0", "10", "11", "12"], "correct": 0, "expl": "Numbers 0-9 in alphabetical order: Eight, Five, Four, Nine, One... Zero."},
        {"text": "Divide 30 by half and add 10. What is the answer?", "options": ["70", "25", "40", "50"], "correct": 0, "expl": "30 / 0.5 = 60. 60 + 10 = 70."},
        {"text": "I am an odd number. Take away a letter and I become even. What number am I?", "options": ["Seven", "Nine", "One", "Three"], "correct": 0, "expl": "SEVEN - S = EVEN."},
        {"text": "You have a match and enter a cold room with a kerosene lamp, a heater, and a candle. What do you light first?", "options": ["The Match", "The Lamp", "The Heater", "The Candle"], "correct": 0, "expl": "You must light the match first."},
        {"text": "How many times can you subtract 10 from 100?", "options": ["Once", "Ten times", "Never", "Twice"], "correct": 0, "expl": "Once. After that, you are subtracting from 90."},
        {"text": "Which is heavier: a ton of bricks or a ton of feathers?", "options": ["Same", "Bricks", "Feathers", "Neither"], "correct": 0, "expl": "Both weigh a ton."},
        {"text": "2 + 2 = Fish. 3 + 3 = Eight. 7 + 7 = ?", "options": ["Triangle", "Fourteen", "Square", "Circle"], "correct": 0, "expl": "Logic: Reverse '3' joined is 8. Reverse '7' joined is Triangle."}
    ]

    def process_raw(raw_list, prefix):
        final = []
        for i, item in enumerate(raw_list):
            # Shuffle options to randomize
            opts = item["options"][:]
            cor_text = opts[item["correct"]]
            random.shuffle(opts)
            new_idx = opts.index(cor_text)
            
            final.append({
                "id": f"{prefix}_{i}",
                "text": item["text"],
                "options": opts,
                "correctIndex": new_idx,
                "explanation": item["expl"],
                "difficulty": 1 # Placeholder, used by list
            })
        return final

    return {
        "id": "PUZZLE",
        "name": "Puzzle",
        "levels": [
            {"id": 1, "questions": process_raw(l1_raw, "p_curated_l1")},
            {"id": 2, "questions": process_raw(l2_raw, "p_curated_l2")},
            {"id": 3, "questions": process_raw(l3_raw, "p_curated_l3")}
        ]
    }

if __name__ == "__main__":
    t_data = generate_treasure_questions()
    p_data = generate_curated_puzzle_quiz()
    
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(t_data, f, indent=2)
        
    with open('app/src/main/assets/puzzle.json', 'w') as f:
        json.dump(p_data, f, indent=2)
    
    print("Curated content generated successfully.")
