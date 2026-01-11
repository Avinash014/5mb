import json
import random

# HYBRID PUZZLE GENERATOR - 200 per level = 600 total
# Strategy: 100 curated riddles/logic + 100 procedural patterns per level

def generate_procedural_patterns(difficulty, count=100):
    """Generate procedural number/letter patterns"""
    patterns = []
    
    for _ in range(count):
        if difficulty == 1:
            # Easy patterns: simple arithmetic, constant series
            pattern_type = random.choice(['add', 'multiply', 'constant', 'subtract'])
            
            if pattern_type == 'add':
                step = random.choice([1, 2, 3, 5, 10])
                start = random.randint(1, 50)
                seq = [start + i*step for i in range(5)]
                ans = start + 5*step
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+step), str(ans-step), str(ans+2*step)]
                expl = f"Add {step} each time."
                
            elif pattern_type == 'multiply':
                mult = random.choice([2, 3, 5, 10])
                start = random.choice([1, 2, 3, 5])
                seq = [start * (mult ** i) for i in range(4)]
                ans = start * (mult ** 4)
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans*2), str(int(ans/mult)), str(ans+10)]
                expl = f"Multiply by {mult} each time."
                
            elif pattern_type == 'constant':
                num = random.randint(1, 20)
                seq = [num] * 5
                ans = num
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+1), str(ans+2), str(ans-1)]
                expl = f"Constant series: all {num}."
                
            else:  # subtract
                step = random.choice([1, 2, 5, 10])
                start = random.randint(50, 100)
                seq = [start - i*step for i in range(5)]
                ans = start - 5*step
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+step), str(ans-step), str(ans+2*step)]
                expl = f"Subtract {step} each time."
                
        elif difficulty == 2:
            # Medium: squares, cubes, fibonacci-like, primes
            pattern_type = random.choice(['square', 'fibonacci', 'double', 'alternating'])
            
            if pattern_type == 'square':
                start = random.randint(1, 10)
                seq = [(start+i)**2 for i in range(4)]
                ans = (start+4)**2
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+10), str(ans-10), str(ans+50)]
                expl = f"Perfect squares starting from {start}²."
                
            elif pattern_type == 'fibonacci':
                a, b = random.randint(1, 5), random.randint(2, 7)
                seq = [a, b]
                for _ in range(3):
                    seq.append(seq[-1] + seq[-2])
                ans = seq[-1] + seq[-2]
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+5), str(ans-5), str(ans+10)]
                expl = f"Each term is sum of previous two."
                
            elif pattern_type == 'double':
                start = random.randint(1, 10)
                seq = [start * (2**i) for i in range(5)]
                ans = start * (2**5)
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+10), str(int(ans/2)), str(ans*2)]
                expl = f"Double each time."
                
            else:  # alternating
                add1 = random.randint(2, 5)
                add2 = random.randint(6, 10)
                start = random.randint(1, 20)
                seq = [start]
                for i in range(4):
                    if i % 2 == 0:
                        seq.append(seq[-1] + add1)
                    else:
                        seq.append(seq[-1] + add2)
                ans = seq[-1] + (add1 if len(seq) % 2 == 0 else add2)
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+5), str(ans-5), str(ans+add1+add2)]
                expl = f"Alternating: +{add1}, +{add2} pattern."
        
        else:  # difficulty 3
            # Hard: cubes, primes, complex Fibonacci, geometric
            pattern_type = random.choice(['cube', 'prime', 'geometric', 'polynomial'])
            
            if pattern_type == 'cube':
                start = random.randint(1, 8)
                seq = [(start+i)**3 for i in range(4)]
                ans = (start+4)**3
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+100), str(ans-100), str(ans+500)]
                expl = f"Perfect cubes: {start}³, {start+1}³, {start+2}³..."
                
            elif pattern_type == 'prime':
                primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
                start_idx = random.randint(0, len(primes)-6)
                seq = primes[start_idx:start_idx+5]
                ans = primes[start_idx+5]
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+2), str(ans+4), str(ans-2)]
                expl = f"Prime number series."
                
            elif pattern_type == 'geometric':
                ratio = random.choice([2, 3, 4])
                start = random.randint(1, 5)
                seq = [start * (ratio**i) for i in range(4)]
                ans = start * (ratio**4)
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans*2), str(int(ans/ratio)), str(ans+100)]
                expl = f"Geometric series: multiply by {ratio}."
                
            else:  # polynomial
                # n² + n pattern
                start = random.randint(1, 10)
                seq = [(start+i)**2 + (start+i) for i in range(4)]
                ans = (start+4)**2 + (start+4)
                q = f"Next number: {', '.join(map(str, seq))}, ?"
                opts = [str(ans), str(ans+20), str(ans-20), str(ans+50)]
                expl = f"Pattern: n² + n where n starts at {start}."
        
        # Shuffle options
        random.shuffle(opts)
        patterns.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(str(ans)),
            "explanation": expl,
            "difficulty": difficulty
        })
    
    return patterns

def get_curated_riddles():
    """Get all curated riddles organized by difficulty"""
    
    # Level 1 - Easy Riddles (100 items)
    easy = [
        ("What comes once in a minute, twice in a moment, never in thousand years?", "Letter M", ["Time", "Moon", "Second"], "M in 'Minute' once, 'Moment' twice."),
        ("What has keys but can't open locks?", "Piano", ["Map", "Coin", "Clock"], "Piano has keys."),
        ("What has to be broken before you use it?", "Egg", ["Window", "Promise", "Secret"], "Break egg to use."),
        ("I'm tall when young, short when old. What am I?", "Candle", ["Tree", "Person", "Mountain"], "Candle burns down."),
        ("What is full of holes but holds water?", "Sponge", ["Bucket", "Net", "Shirt"], "Sponge absorbs water."),
        ("What goes up but never comes down?", "Age", ["Rain", "Ball", "Rocket"], "Age only increases."),
        ("I have cities, no houses; mountains, no trees; water, no fish. What am I?", "Map", ["Globe", "Dream", "Book"], "Map depicts features."),
        ("What gets wet while drying?", "Towel", ["Sponge", "Sun", "Water"], "Towel absorbs moisture."),
        ("What can you break without touching?", "Promise", ["Glass", "Plate", "Law"], "Break promise verbally."),
        ("What has head and tail but no body?", "Coin", ["Snake", "Cat", "Story"], "Coin has heads/tails."),
        ("What goes around world staying in corner?", "Stamp", ["Map", "Compass", "Flag"], "Stamp on envelope."),
        ("What has hands but can't clap?", "Clock", ["Mannequin", "Robot", "Statue"], "Clock has hands."),
        ("What has neck but no head?", "Bottle", ["Giraffe", "Shirt", "Guitar"], "Bottle has neck."),
        ("What has eye but can't see?", "Needle", ["Potato", "Storm", "Camera"], "Needle has eye."),
        ("What building has most stories?", "Library", ["Skyscraper", "Museum", "School"], "Library has books."),
        ("What is always coming but never arrives?", "Tomorrow", ["Future", "Train", "Package"], "Tomorrow becomes today."),
        ("What word becomes shorter when you add letters?", "Short", ["Long", "Brief", "Tiny"], "Add 'er' = shorter."),
        ("What belongs to you but others use more?", "Your Name", ["Your House", "Your Car", "Your Phone"], "Others say your name."),
        ("What has 88 keys but can't open door?", "Piano", ["Keyboard", "Typewriter", "Lock"], "Piano has 88 keys."),
        ("What runs but never walks, has mouth but never talks?", "River", ["Car", "Watch", "Person"], "River runs, has mouth."),
        ("Find odd one: Car, Bike, Bus, Plane", "Plane", ["Bus", "Bike", "Car"], "Plane flies."),
        ("Find odd one: Apple, Banana, Carrot, Orange", "Carrot", ["Apple", "Banana", "Orange"], "Carrot is vegetable."),
        ("Find odd one: Dog, Cat, Bird, Fish", "Bird", ["Dog", "Cat", "Fish"], "Bird has feathers."),
        ("Find odd one: Red, Blue, Green, Circle", "Circle", ["Red", "Blue", "Green"], "Circle is shape."),
        ("Find odd one: 2, 4, 6, 9", "9", ["2", "4", "6"], "9 is odd number."),
        ("Find odd one: Triangle, Square, Circle, Red", "Red", ["Triangle", "Square", "Circle"], "Red is color, not shape."),
        ("Find odd one: Monday, Tuesday, January, Wednesday", "January", ["Monday", "Tuesday", "Wednesday"], "January is month."),
        ("Find odd one: Spring, Summer, Autumn, March", "March", ["Spring", "Summer", "Autumn"], "March is month."),
        ("Find odd one: Book, Pen, Paper, Chair", "Chair", ["Book", "Pen", "Paper"], "Chair is furniture."),
        ("Find odd one: Lion, Tiger, Elephant, Leopard", "Elephant", ["Lion", "Tiger", "Leopard"], "Elephant not a big cat."),
        ("What is always in front of you but can't be seen?", "The Future", ["The Past", "Your Nose", "The Wind"], "Future lies ahead."),
        ("I have head, tail that never meet. Too many is treat. What am I?", "Coin", ["Snake", "Cat", "Story"], "Coin: head/tail."),
        ("What five-letter word stays the same when you take away first, last, and middle letter?", "Empty", ["Never", "Short", "Music"], "E-M-P-T-Y → M-P-T → M-T → M."),
        ("What can fill a room but takes no space?", "Light", ["Air", "Sound", "Smell"], "Light fills room."),
        ("The more you take, the more you leave behind. What?", "Footsteps", ["Memories", "Time", "Money"], "More steps, more prints."),
        ("What has one head, one foot, four legs?", "Bed", ["Table", "Chair", "Dog"], "Bed head/foot/legs."),
        ("What is black when clean, white when dirty?", "Blackboard", ["Coal", "Snow", "Paper"], "Chalk on blackboard."),
        ("What gets bigger when more is taken away?", "Hole", ["Balloon", "Debt", "Puddle"], "Digging hole."),
        ("Feed me and I live, give me water and I die. What am I?", "Fire", ["Plant", "Cat", "Fish"], "Fire needs fuel."),
        ("What can travel world while staying in corner?", "Stamp", ["Postcard", "Map", "Flag"], "Postage stamp."),
        ("What begins with E, ends with E, has one letter?", "Envelope", ["Eye", "Edge", "Eagle"], "Envelope holds letter."),
        ("David's father has three sons: Snap, Crackle and...?", "David", ["Pop", "Jack", "John"], "David is 3rd son."),
        ("If you have me you want to share me. If you share me you don't have me. What am I?", "Secret", ["Money", "Food", "Toy"], "Sharing secret."),
        ("What has 4 eyes but can't see?", "Mississippi", ["Spider", "Fly", "Potato"], "'ii' appears 4 times."),
        ("Poor have it, rich need it, if you eat it you die. What?", "Nothing", ["Money", "Food", "Water"], "Poor have nothing."),
        ("What tastes better than it smells?", "Tongue", ["Coffee", "Perfume", "Flower"], "Tongue tastes."),
        ("What is easy to get into but hard to get out of?", "Trouble", ["Room", "Bed", "Car"], "Getting into trouble."),
        ("Where does Thursday come before Wednesday?", "Dictionary", ["Calendar", "Week", "Book"], "Alphabetically."),
        ("I'm light as feather yet strongest man can't hold me 5 minutes. What am I?", "Breath", ["Air", "Paper", "Feather"], "Holding breath."),
        ("What month has 28 days?", "All of them", ["February", "January", "December"], "All months have ≥28 days."),
    ]
    
    # Level 2 - Medium (100 items)
    medium = [
        ("What question can you never answer 'yes' to?", "Are you asleep?", ["Are you hungry?", "Are you human?", "Are you reading?"], "Can't answer if asleep."),
        ("Man in rain without umbrella/hat didn't get hair wet. Why?", "He was bald", ["Wore hood", "Wasn't raining hard", "Was inside"], "No hair."),
        ("What goes up and down but doesn't move?", "Staircase", ["Elevator", "Ball", "Temperature"], "Staircase stays still."),
        ("If 2's company, 3's crowd, what are 4 and 5?", "Nine", ["Fun", "Strangers", "Group"], "4 + 5 = 9."),
        ("What begins with T, ends with T, has T in it?", "Teapot", ["Tent", "Target", "Toast"], "Tea-pot."),
        ("I have branches, no fruit/trunk/leaves. What am I?", "Bank", ["Tree", "River", "Family"], "Bank has branches."),
        ("If 5 cats catch 5 mice in 5 minutes, how long for 100 cats to catch 100 mice?", "5 minutes", ["100 minutes", "20 minutes", "10 minutes"], "Same rate."),
        ("Farmer has 17 sheep, all but 9 die. How many left?", "9", ["8", "0", "17"], "'All but 9' = 9 survive."),
        ("Doctor gives 3 pills, one every half hour. How long?", "1 hour", ["1.5 hours", "2 hours", "30 minutes"], "0, 30, 60 min."),
        ("In race, you pass 2nd place. What position?", "2nd", ["1st", "3rd", "4th"], "You take 2nd."),
        ("Mary's father has 5 daughters: Nana, Nene, Nini, Nono, and...?", "Mary", ["Nunu", "Nina", "Nunu"], "Mary is 5th."),
        ("Rooster lays egg on barn roof. Which way rolls?", "Roosters don't lay eggs", ["Left", "Right", "Down"], "Roosters are male."),
        ("How many of each animal did Moses take on ark?", "Moses didn't have ark", ["2", "7", "0"], "Noah had ark."),
        ("Electric train going north. Which way smoke goes?", "No smoke", ["North", "South", "East"], "Electric = no smoke."),
        ("You have match, candle, lamp in dark room. What light first?", "The match", ["Candle", "Lamp", "Nothing"], "Match lights others."),
        ("What 5-letter word becomes shorter when you add 2 letters?", "Short", ["Brief", "Small", "Tiny"], "Add 'er' = shorter."),
        ("What word is spelled incorrectly in every dictionary?", "Incorrectly", ["Dictionary", "Wrong", "Misspelled"], "Word 'incorrectly'."),
        ("Forward I'm heavy, backward I'm not. What am I?", "Ton", ["Weight", "Net", "Top"], "Ton → not."),
        ("What 7-letter word has hundreds of letters?", "Mailbox", ["Alphabet", "Library", "Letters"], "Mailbox has letters."),
        ("A is B's brother. B is C's brother. C is D's sister. How is D related to A?", "Sibling", ["Cousin", "Parent", "Stranger"], "All siblings."),
        ("What comes down but never goes up?", "Rain", ["Age", "Stairs", "Temperature"], "Rain falls down."),
        ("I shave 20 times a day, still have beard. What am I?", "Barber", ["Man", "Razor", "Actor"], "Barber shaves others."),
        ("Take off my skin, I won't cry but you will. What am I?", "Onion", ["Orange", "Potato", "Apple"], "Onions make cry."),
        ("Two fathers and sons went fishing. Caught 3 fish, each got one. How?", "Grandfather, father, son", ["4 people", "Shared", "Lied"], "3 people total."),
        ("People make me, save me, change me, raise me. What am I?", "Money", ["Baby", "House", "Plan"], "Money."),
        ("If you drop me I crack, smile at me I smile back. What am I?", "Mirror", ["Glass", "Egg", "Ice"], "Mirror reflects."),
    ]
    
    # Level 3 - Hard (100 items)
    hard = [
        ("Man pushes car to hotel, says bankrupt. What game?", "Monopoly", ["Poker", "Chess", "Life"], "Board game."),
        ("Woman shoots husband, holds underwater 5 min, hangs him. Dinner together. How?", "She's a photographer", ["Dream", "Ghost story", "Movie"], "Photo developing."),
        ("Can't keep this until you've given it", "Your word", ["Gift", "Secret", "Promise"], "Giving word."),
        ("I come from mine, surrounded by wood. Everyone uses me. What?", "Pencil lead", ["Coal", "Diamond", "Metal"], "Graphite, wood pencil."),
        ("3 doctors say Robert is brother. Robert says no brothers. Who's right?", "Both - doctors are sisters", ["Robert lies", "Doctors lie", "Adopted"], "Doctors are female."),
        ("Railroad crossing, watch for cars. Spell that without Rs", "T-H-A-T", ["Crossing", "Railroad", "Cars"], "Spell 'THAT'."),
        ("I'm lighter than what I'm made of, more hidden than seen. What am I?", "Iceberg", ["Cloud", "Shadow", "Air"], "Ice lighter than water."),
        ("Man describes daughters: all but 2 brunettes, all but 2 blondes, all but 2 redheads. How many?", "3", ["6", "4", "2"], "1 of each color."),
        ("Room with no doors/windows. How get out?", "Stop imagining", ["Break wall", "Dig", "Teleport"], "It's imaginary."),
        ("I start with M, end with X, have infinite letters. What?", "Mailbox", ["Matrix", "Mix", "Max"], "Mailbox holds letters."),
       ("What seen in middle of March/April, not beginning/end?", "Letter R", ["Spring", "Rain", "Sun"], "R in middle."),
        ("Runs smoother than rhyme, loves to fall but can't climb", "Water", ["Time", "River", "Rain"], "Water flows down."),
        ("First you eat me, then you get eaten. What am I?", "Fishhook", ["Bait", "Food", "Worm"], "Bait on hook."),
        ("What is broken every day?", "Promise", ["Glass", "Silence", "Dawn"], "Dawn breaks daily."),
        ("Forward I'm what you do every day, backward I'm somewhere to live. What am I?", "Lived/Devil", ["Room", "Home", "Part"], "Lived reverses to devil."),
    ]
    
    return easy, medium, hard

def generate_puzzle_quiz():
    """Generate 600 puzzle questions: curated + procedural to reach 200 per level"""
    
    easy_riddles, medium_riddles, hard_riddles = get_curated_riddles()
    
    # Convert tuples to dict format
    def convert(riddles, diff):
        result = []
        for q, ans, dists, expl in riddles:
            opts = [ans] + dists
            random.shuffle(opts)
            result.append({
                "text": q,
                "options": opts,
                "correctIndex": opts.index(ans),
                "explanation": expl,
                "difficulty": diff
            })
        return result
    
    l1_curated = convert(easy_riddles, 1)
    l2_curated = convert(medium_riddles, 2)
    l3_curated = convert(hard_riddles, 3)
    
    # Generate enough procedural to reach 200
    l1_needed = 200 - len(l1_curated)
    l2_needed = 200 - len(l2_curated)
    l3_needed = 200 - len(l3_curated)
    
    l1_procedural = generate_procedural_patterns(1, l1_needed)
    l2_procedural = generate_procedural_patterns(2, l2_needed)
    l3_procedural = generate_procedural_patterns(3, l3_needed)
    
    # Combine and shuffle
    l1_all = l1_curated + l1_procedural
    l2_all = l2_curated + l2_procedural
    l3_all = l3_curated + l3_procedural
    
    random.shuffle(l1_all)
    random.shuffle(l2_all)
    random.shuffle(l3_all)
    
    # Add unique IDs
    for i, q in enumerate(l1_all): q["id"] = f"p_l1_{i}"
    for i, q in enumerate(l2_all): q["id"] = f"p_l2_{i}"
    for i, q in enumerate(l3_all): q["id"] = f"p_l3_{i}"
    
    print(f"✅ Puzzle Generation Complete:")
    print(f"  Level 1: {len(l1_curated)} curated + {len(l1_procedural)} procedural = {len(l1_all)} total")
    print(f"  Level 2: {len(l2_curated)} curated + {len(l2_procedural)} procedural = {len(l2_all)} total")
    print(f"  Level 3: {len(l3_curated)} curated + {len(l3_procedural)} procedural = {len(l3_all)} total")
    print(f"  Grand Total: {len(l1_all) + len(l2_all) + len(l3_all)} questions")
    
    return {
        "id": "PUZZLE",
        "name": "Puzzle",
        "levels": [
            {"id": 1, "questions": l1_all},
            {"id": 2, "questions": l2_all},
            {"id": 3, "questions": l3_all}
        ]
    }

if __name__ == "__main__":
    puzzle_data = generate_puzzle_quiz()
    with open('app/src/main/assets/puzzle.json', 'w') as f:
        json.dump(puzzle_data, f, indent=2)
    print("\n🎉 puzzle.json generated successfully!")
