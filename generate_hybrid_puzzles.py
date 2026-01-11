import json
import random

# --- TREASURE GENERATOR (Standard) ---
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

# --- PUZZLE GENERATOR (HYBRID: Curated Lists + Template Logic) ---

def generate_hybrid_puzzles():
    
    # --- TEMPLATE DATA ---
    
    analogies = [
        ("Finger", "Hand", "Toe", "Foot", ["Leg", "Knee", "Shoe"]),
        ("Bird", "Fly", "Fish", "Swim", ["Walk", "Water", "Fins"]),
        ("Hot", "Cold", "Up", "Down", ["Sky", "Left", "High"]),
        ("Doctor", "Hospital", "Teacher", "School", ["Class", "Book", "Student"]),
        ("Car", "Road", "Train", "Track", ["Station", "Rail", "Bus"]),
        ("Book", "Read", "Pen", "Write", ["Draw", "Ink", "Paper"]),
        ("Eye", "See", "Ear", "Hear", ["Listen", "Sound", "Head"]),
        ("Night", "Moon", "Day", "Sun", ["Sky", "Light", "Star"]),
        ("Cow", "Calf", "Cat", "Kitten", ["Puppy", "Dog", "Cub"]),
        ("Man", "Woman", "King", "Queen", ["Prince", "Princess", "Lady"]),
        ("Shoes", "Feet", "Gloves", "Hands", ["Arms", "Warm", "Fingers"]),
        ("Hungry", "Eat", "Thirsty", "Drink", ["Water", "Juice", "Liquid"]),
        ("Happy", "Smile", "Sad", "Frown", ["Cry", "Tears", "Mad"]),
        ("Fire", "Hot", "Ice", "Cold", ["Water", "Freeze", "Snow"]),
        ("Light", "Dark", "Day", "Night", ["Moon", "Black", "Sleep"]),
        ("One", "Single", "Two", "Double", ["Triple", "Pair", "Couple"]),
        ("Circle", "Round", "Square", "Boxy", ["Flat", "Shape", "Cube"]),
        ("Run", "Fast", "Walk", "Slow", ["Stop", "Legs", "Move"]),
        ("Knife", "Cut", "Pen", "Write", ["Ink", "Draw", "Paper"]),
        ("Listen", "Music", "Read", "Book", ["Page", "Story", "Words"]),
        ("Tree", "Leaf", "Flower", "Petal", ["Stem", "Root", "Garden"]),
        ("Ship", "Sea", "Car", "Road", ["Wheel", "Drive", "Street"]),
        ("Baker", "Bread", "Butcher", "Meat", ["Shop", "Food", "Cook"]),
        ("Lion", "Roar", "Dog", "Bark", ["Bite", "Tail", "Pet"]),
        ("Nose", "Smell", "Tongue", "Taste", ["Mouth", "Eat", "Food"])
    ]
    
    odd_one_out = [
        ("Apple", "Banana", "Carrot", "Grape", "Carrot", "It's a vegetable."),
        ("Car", "Bike", "Bus", "Plane", "Plane", "It flies."),
        ("Dog", "Cat", "Cow", "Snake", "Snake", "It has no legs."),
        ("Chair", "Table", "Sofa", "Door", "Door", "It's part of the house structure."),
        ("Red", "Blue", "Green", "Dark", "Dark", "It's a shade, not a hue."),
        ("Square", "Circle", "Triangle", "Cube", "Cube", "It's 3D."),
        ("Inch", "Foot", "Yard", "Pound", "Pound", "It measures weight."),
        ("Second", "Minute", "Hour", "Watch", "Watch", "It measures time."),
        ("Guitar", "Piano", "Violin", "Flute", "Flute", "It's a wind instrument."),
        ("Summer", "Winter", "Spring", "Rain", "Rain", "It's weather, not a season."),
        ("T-Shirt", "Jeans", "Jacket", "Hat", "Hat", "Worn on head."),
        ("Doctor", "Nurse", "Teacher", "Surgeon", "Teacher", "Works in a school."),
        ("London", "Paris", "New York", "Berlin", "New York", "Not a European capital."),
        ("Jupiter", "Mars", "Earth", "Sun", "Sun", "It's a star."),
        ("A", "E", "I", "B", "B", "It's a consonant."),
        ("Tea", "Coffee", "Juice", "Cake", "Cake", "It's food."),
        ("Run", "Walk", "Jump", "Sleep", "Sleep", "Not an active motion."),
        ("Happy", "Sad", "Angry", "Tall", "Tall", "Physical trait, not emotion."),
        ("Penny", "Nickel", "Dime", "Paper", "Paper", "Not a coin."),
        ("Shark", "Whale", "Dolphin", "Goldfish", "Goldfish", "Freshwater/Pet vs Ocean.")
    ]

    # --- HAND-WRITTEN RIDDLES POOL (Expanded) ---
    riddles_easy = [
        ("What has a neck but no head?", "A Bottle", ["A Shirt", "A Giraffe", "A Snake"]),
        ("What can you catch but not throw?", "A Cold", ["A Ball", "A Fish", "A Rope"]),
        ("What has legs but cannot walk?", "A Table", ["A Dog", "A Baby", "A Cat"]),
        ("What has a face and two hands but no arms or legs?", "A Clock", ["A Person", "A Robot", "A Doll"]),
        ("What goes up when rain comes down?", "An Umbrella", ["The Sun", "A Bird", "Smoke"]),
        ("What gets bigger the more you take away?", "A Hole", ["A Pile", "A Box", "A Balloon"]),
        ("What belongs to you but others use it more?", "Your Name", ["Your Pen", "Your Money", "Your Car"]),
        ("What begins with T, ends with T, and has T in it?", "A Teapot", ["A Tent", "Toast", "Target"]),
        ("What has an eye but cannot see?", "A Needle", ["A Cyclone", "A Potato", "A Storm"]),
        ("What has a thumb and four fingers but is not a hand?", "A Glove", ["A Foot", "A Shoe", "A Sock"]),
        ("If you feed me I live, but if you give me a drink I die.", "Fire", ["A Plant", "A Fish", "A Dog"]),
        ("What is full of holes but still holds water?", "A Sponge", ["A Net", "A Bucket", "A Shirt"]),
        ("What comes once in a minute, twice in a moment, but never in a 1000 years?", "The letter M", ["Time", "The Moon", "Second"]),
        ("I have cities but no houses. I have mountains but no trees. I have water but no fish.", "A Map", ["A Globe", "A Book", "A Dream"]),
        ("What gets wet while drying?", "A Towel", ["The Sun", "Water", "A Sponge"]),
        ("What invention lets you look right through a wall?", "A Window", ["X-Ray", "A Door", "Glasses"]),
        ("I’m tall when I’m young, and I’m short when I’m old.", "A Candle", ["A Tree", "A Person", "A Pencil"]),
        ("What question can you never answer 'yes' to?", "Are you asleep?", ["Are you hungry?", "Are you human?", "Are you reading?"]),
        ("What gives you the power to walk through walls?", "A Door", ["Magic", "A Hammer", "A Key"]),
        ("What works only when it is fired?", "A Rocket", ["A Car", "A Computer", "A Phone"]),
        ("I have no life, but I can die. What am I?", "A Battery", ["A Ghost", "A Rock", "A Cloud"]),
        ("What has a head and a tail but no body?", "A Coin", ["A Snake", "A Cat", "A Lizard"]),
        ("What can travel around the world while staying in a corner?", "A Stamp", ["A Plane", "The Moon", "A Thought"]),
        ("I have keys but no locks. I have a space but no room. You can enter, but can’t go outside.", "A Keyboard", ["A House", "A Piano", "A Car"]),
        ("What usually comes in pairs but is often lost one at a time?", "Socks", ["Shoes", "Earrings", "Gloves"]),
        ("What has to be broken before you can use it?", "An Egg", ["Glass", "A Window", "A Promise"]),
        ("I smile when you smile, I frown when you frown.", "A Mirror", ["A Friend", "A Picture", "A Camera"]),
        ("What goes up but never comes down?", "Age", ["Rain", "Rocket", "Ball"]),
        ("What breaks when you say its name?", "Silence", ["Glass", "A Secret", "A Promise"]),
        ("The more you have of it, the less you see.", "Darkness", ["Fog", "Light", "Rain"]),
        ("What has many teeth but cannot bite?", "A Comb", ["A Saw", "A Zipper", "A Gear"]),
        ("What kind of band never plays music?", "A Rubber Band", ["A Rock Band", "A Headband", "A Wristband"]),
        ("What has words, but never speaks?", "A Book", ["A Person", "A Radio", "A Phone"]),
        ("What runs all around a backyard, yet never moves?", "A Fence", ["A Dog", "A Grass", "A Hose"]),
        ("What can fill a room but takes up no space?", "Light", ["Air", "Water", "Furniture"]),
        ("What falls but never breaks?", "Night", ["Glass", "Rain", "Snow"]),
        ("What breaks but never falls?", "Day", ["Night", "Glass", "Egg"]),
        ("What goes through towns and hills but never moves?", "A Road", ["A Car", "A River", "A Train"])
    ]

    riddles_medium = [
        ("A man rode into town on Friday, stayed three days, and rode out on Friday. How?", "Horse is named Friday", ["Time Loop", "He stayed a week", "Magic"]),
        ("Which weighs more: a pound of feathers or a pound of bricks?", "Same", ["Bricks", "Feathers", "Neither"]),
        ("Mary’s father has 5 daughters: Nana, Nene, Nini, Nono. What is the 5th daughter's name?", "Mary", ["Nunu", "Nina", "Nana"]),
        ("How many months have 28 days?", "All 12", ["1", "2", "6"]),
        ("If you drop a yellow hat in the Red Sea, what does it become?", "Wet", ["Red", "Floating", "Salty"]),
        ("A cowboy rode into town on Friday...", "Horse is Friday", ["Magic", "Time Travel", "Fast Horse"]),
        ("What 5-letter word becomes shorter when you add two letters to it?", "Short", ["Small", "Brief", "Tiny"]),
        ("I am an odd number. Take away a letter and I become even. What am I?", "Seven", ["Nine", "One", "Three"]),
        ("You see a boat filled with people, yet there is not a single person on board. How?", "They are married", ["Ghosts", "Invisible", "Underwater"]),
        ("What appears once in a minute, twice in a moment, but never in a thousand years?", "The letter M", ["Time", "A Second", "The Moon"]),
        ("Tom is taller than Peter. Peter is shorter than Mark. Mark is shorter than Tom. Who is tallest?", "Tom", ["Mark", "Peter", "Same"]),
        ("If a rooster lays an egg on top of a barn, which way will it roll?", "Roosters don't lay eggs", ["Left", "Right", "Down"]),
        ("An electric train is moving north at 100mph. The wind is blowing west. Which way does the smoke go?", "No smoke", ["West", "East", "South"]),
        ("How far can a dog run into the woods?", "Halfway", ["All the way", "1 Mile", "Till tired"]),
        ("What has 13 hearts but no other organs?", "Deck of Cards", ["A Monster", "A Love Potion", "A Squid"]),
        ("Forward I am heavy, backward I am not. What am I?", "Ton", ["Not", "Pot", "Pan"]),
        ("Imagine you are in a sinking rowboat surrounded by sharks. How do you survive?", "Stop imagining", ["Swim fast", "Fight", "Call help"]),
        ("A man is looking at a picture. 'Brothers and sisters I have none, but that man's father is my father's son.'", "His son", ["His father", "Himself", "His uncle"]),
        ("The day before yesterday, I was 25. The next year I will be 28. When is my birthday?", "Dec 31", ["Jan 1", "Feb 28", "June 1"]),
        ("What has 4 legs in the morning, 2 in the afternoon, and 3 in the evening?", "Human", ["Dog", "Alien", "Table"]),
        ("What can run but never walks, has a mouth but never talks, has a head but never weeps?", "A River", ["A Mountain", "A Road", "A Car"]),
        ("What is so fragile that saying its name breaks it?", "Silence", ["Glass", "Ice", "Promise"]),
        ("What comes down but never goes up?", "Rain", ["Age", "Rocket", "Balloon"]),
        ("I am always coming, but never arrive. What am I?", "Tomorrow", ["Today", "Yesterday", "The Bus"]),
        ("What can you hold in your right hand, but never in your left?", "Left Hand", ["Right Hand", "A Pen", "A Phone"]),
        ("You can throw me away, but I will always come back. What am I?", "A Boomerang", ["A Ball", "A Dog", "A Frisbee"]),
        ("What goes up and down without moving?", "Stairs", ["Elevator", "Sun", "Ball"]),
        ("Where does success come before work?", "Dictionary", ["School", "Office", "Home"]),
        ("How many letters are in 'The Alphabet'?", "11", ["26", "24", "10"]),
        ("If you have it, you want to share it. If you share it, you don't have it.", "Secret", ["Money", "Love", "Food"])
    ]

    riddles_hard = [
        ("Logic Series: 2, 3, 5, 7, 11, ...", "13", ["15", "17", "9"], "Primes"),
        ("Logic Series: 1, 1, 2, 3, 5, 8, ...", "13", ["21", "10", "12"], "Fibonacci"),
        ("Logic Series: O, T, T, F, F, S, S, ...", "E", ["N", "T", "O"], "One, Two, Three... Eight"),
        ("Logic Series: J, F, M, A, M, J, ...", "J", ["A", "S", "O"], "Months"),
        ("Logic Series: M, T, W, T, F, ...", "S", ["M", "T", "W"], "Days of Week"),
        ("Logic Series: 1, 4, 9, 16, 25, ...", "36", ["30", "49", "32"], "Squares"),
        ("Logic Series: 1, 8, 27, 64, ...", "125", ["100", "216", "36"], "Cubes"),
        ("Divide 30 by 1/2 and add 10.", "70", ["25", "40", "50"], "30 / 0.5 = 60"),
        ("A bat and ball cost $1.10. Bat costs $1 more than ball. Cost of ball?", "$0.05", ["$0.10", "$0.01", "$0.55"], "0.05 + 1.05 = 1.10"),
        ("If 5 machines make 5 widgets in 5 minutes, how long for 100 machines for 100 widgets?", "5 min", ["100 min", "1 min", "20 min"], "Parallel work"),
        ("A doctor gives you 3 pills. Take one every 30 minutes. How long do they last?", "60 min", ["90 min", "30 min", "120 min"], "0, 30, 60"),
        ("You are in a race. Pass the person in 2nd. What place are you?", "2nd", ["1st", "3rd", "Last"], "You replace them"),
        ("You are in a race. Pass the person in Last. What place are you?", "Impossible", ["Last", "2nd Last", "First"], "Can't pass last place"),
        ("How much dirt is in a hole 3ft deep, 6ft long, 4ft wide?", "None", ["72 sq ft", "36 sq ft", "12 sq ft"], "Holes are empty"),
        ("How many times can you subtract 10 from 100?", "Once", ["10 Times", "Infinite", "0"], "Then it is 90"),
        ("Which is correct: 'Yolk of egg is white' or 'are white'?", "Neither", ["Is white", "Are white", "Both"], "Yolks are yellow"),
        ("What goes up a chimney down, but not down a chimney up?", "Umbrella", ["Smoke", "Bird", "Santa"], "Open vs Closed"),
        ("The more you take, the more you leave behind.", "Footsteps", ["Time", "Money", "Memories"], ""),
        ("What has 4 fingers and a thumb but is not living?", "Glove", ["Hand", "Robot", "Statue"], ""),
        ("Only one color, but countless sizes. Stuck at the bottom, yet easily flies. Sun creates, rain destroys.", "Shadow", ["Cloud", "Rainbow", "Wind"], ""),
        ("I have a bed but never sleep. I run but have no legs.", "River", ["Truck", "Ocean", "Clock"], ""),
        ("People make me, save me, change me, raise me.", "Money", ["Time", "Kids", "Plans"], ""),
        ("What breaks on water but not on land?", "Wave", ["Ship", "Ice", "Rock"], "")
    ]

    # --- GENERATION LOGIC ---

    final_L1 = []
    final_L2 = []
    final_L3 = []
    
    # 1. Populate L1 (100 Qs)
    # Source A: Static Riddles (Easy) - ~40
    for r in riddles_easy:
        final_L1.append({"text": r[0], "options": [r[1]] + r[2], "correctIndex": 0, "explanation": "Answer is " + r[1], "difficulty": 1, "shuffle": True})
    
    # Source B: Word Analogies (Easy) - Generate ~30
    for i in range(30):
        t = random.choice(analogies)
        a, b, c, d, wrongs = t
        options = [d] + random.sample(wrongs, 3)
        final_L1.append({"text": f"{a} : {b} :: {c} : ?", "options": options, "correctIndex": 0, "explanation": f"{b} relates to {a} like {d} relates to {c}.", "difficulty": 1, "shuffle": True})

    # Source C: Odd One Out (Simple) - Generate ~30
    for i in range(30):
        t = random.choice(odd_one_out)
        # t = (A, B, C, D, Odd, Reason)
        items = list(t[0:4])
        odd = t[4]
        reason = t[5]
        # We need options to identify the odd one. options = items
        final_L1.append({"text": f"Odd One Out: {', '.join(items)}", "options": items, "correctIndex": items.index(odd), "explanation": reason, "difficulty": 1, "shuffle": False}) # Options already set
        
    # 2. Populate L2 (100 Qs)
    # Source A: Riddles Medium - ~30
    for r in riddles_medium:
        final_L2.append({"text": r[0], "options": [r[1]] + r[2], "correctIndex": 0, "explanation": "Answer is " + r[1], "difficulty": 2, "shuffle": True})

    # Source B: Logic Sequences (Moderate) - Generated from templates in massive gen style but kept strict
    # Square series
    for i in range(20):
        s = random.randint(2, 9)
        seq = [x**2 for x in range(s, s+5)]
        ans = seq[-1]; disp = seq[:-1]
        opts = [str(ans), str(ans+5), str(ans-2), str(ans+10)]
        final_L2.append({"text": f"Next: {', '.join(map(str, disp))}, ?", "options": opts, "correctIndex": 0, "explanation": "Perfect squares.", "difficulty": 2, "shuffle": True})
        
    # Geometric
    for i in range(20):
        s = random.randint(2, 6); m = random.choice([2, 3])
        seq = [s*(m**x) for x in range(5)]
        ans = seq[-1]; disp = seq[:-1]
        opts = [str(ans), str(ans+m), str(ans*2), str(ans-m)]
        final_L2.append({"text": f"Next: {', '.join(map(str, disp))}, ?", "options": opts, "correctIndex": 0, "explanation": f"Multiply by {m}.", "difficulty": 2, "shuffle": True})
        
    # Analogies (Harder/Mixed) - ~30
    for i in range(30):
        t = random.choice(analogies)
        a, b, c, d, wrongs = t
        # Reverse format sometimes
        options = [d] + random.sample(wrongs, 3)
        final_L2.append({"text": f"Analogy: {a} is to {b} as {c} is to ...?", "options": options, "correctIndex": 0, "explanation": f"{d} completes the pair.", "difficulty": 2, "shuffle": True})

    # 3. Populate L3 (100 Qs)
    # Source A: Riddles Hard (Lateral/Math) - ~25
    for r in riddles_hard:
        expl = r[3] if len(r) > 3 else "Logic."
        final_L3.append({"text": r[0], "options": [r[1]] + r[2], "correctIndex": 0, "explanation": expl, "difficulty": 3, "shuffle": True})
        
    # Source B: Harder Sequences (Fibonacci, Primes, Pronic) - 50
    # Fibonacci
    for i in range(25):
        a, b = random.randint(1, 10), random.randint(1, 10)
        seq = [a, b]
        for _ in range(4): seq.append(seq[-1]+seq[-2])
        ans = seq[-1]; disp = seq[:-1]
        opts = [str(ans), str(ans+1), str(ans-2), str(ans+5)]
        final_L3.append({"text": f"Series: {', '.join(map(str, disp))}, ?", "options": opts, "correctIndex": 0, "explanation": "Add previous two.", "difficulty": 3, "shuffle": True})
        
    # Pronic
    for i in range(25):
        s = random.randint(2, 10)
        seq = [x*(x+1) for x in range(s, s+5)]
        ans = seq[-1]; disp = seq[:-1]
        opts = [str(ans), str(ans+4), str(ans-5), str(ans+10)]
        final_L3.append({"text": f"Series: {', '.join(map(str, disp))}, ?", "options": opts, "correctIndex": 0, "explanation": "n * (n+1)", "difficulty": 3, "shuffle": True})

    # Source C: Two Step Math - 25
    for i in range(25):
        s = random.randint(1, 10)
        curr = s; seq = [curr]
        for _ in range(4):
            curr = curr * 2 + 1
            seq.append(curr)
        ans = seq[-1]; disp = seq[:-1]
        opts = [str(ans), str(ans-1), str(ans+2), str(ans*2)]
        final_L3.append({"text": f"Next: {', '.join(map(str, disp))}, ?", "options": opts, "correctIndex": 0, "explanation": "x2 + 1", "difficulty": 3, "shuffle": True})

    # --- FINALIZE ---
    
    def process_list(raw_list, prefix):
        final = []
        for i, item in enumerate(raw_list):
            opts = item["options"][:]
            cor_text = opts[item["correctIndex"]]
            
            if item.get("shuffle", True):
                random.shuffle(opts)
                
            new_idx = opts.index(cor_text)
            
            final.append({
                "id": f"{prefix}_{i}",
                "text": item["text"],
                "options": opts,
                "correctIndex": new_idx,
                "explanation": item["explanation"],
                "difficulty": item["difficulty"]
            })
        return final

    return {
        "id": "PUZZLE",
        "name": "Puzzle",
        "levels": [
            {"id": 1, "questions": process_list(final_L1, "p_hyb_l1")},
            {"id": 2, "questions": process_list(final_L2, "p_hyb_l2")},
            {"id": 3, "questions": process_list(final_L3, "p_hyb_l3")}
        ]
    }

if __name__ == "__main__":
    t_data = generate_treasure_questions()
    p_data = generate_hybrid_puzzles()
    
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(t_data, f, indent=2)
        
    with open('app/src/main/assets/puzzle.json', 'w') as f:
        json.dump(p_data, f, indent=2)
    
    print("Hybrid content generated.")
