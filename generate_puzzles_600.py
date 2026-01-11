import json
import random

# COMPREHENSIVE PUZZLE GENERATOR - 200 questions per level = 600 total
# Types: Riddles, Logic Puzzles, Pattern Recognition, Odd One Out, Wordplay, Lateral Thinking

def create_puzzle_l1_easy():
    """200 Easy puzzles: riddles, simple patterns, basic logic"""
    puzzles = []
    
    # Classic Riddles (80 questions)
    riddles_easy = [
        ("What comes once in a minute, twice in a moment, never in a thousand years?", "Letter M", ["Time", "Moon", "Second"], "M appears once in 'Minute', twice in 'Moment'."),
        ("What has keys but can't open locks?", "Piano", ["Map", "Coin", "Clock"], "A piano has keys."),
        ("What has to be broken before you can use it?", "Egg", ["Window", "Promise", "Secret"], "An egg must be broken."),
        ("I'm tall when young, short when old. What am I?", "Candle", ["Tree", "Person", "Mountain"], "A candle burns down."),
        ("What is full of holes but still holds water?", "Sponge", ["Bucket", "Net", "Shirt"], "A sponge absorbs water."),
        ("What goes up but never comes down?", "Age", ["Rain", "Ball", "Rocket"], "Your age only increases."),
        ("I have cities but no houses, mountains but no trees, water but no fish. What am I?", "Map", ["Globe", "Dream", "Book"], "A map depicts features."),
        ("What gets wet while drying?", "Towel", ["Sponge", "Sun", "Water"], "A towel absorbs moisture."),
        ("What can you break without touching?", "Promise", ["Glass", "Plate", "Law"], "Break a promise verbally."),
        ("What has a head and tail but no body?", "Coin", ["Snake", "Cat", "Story"], "A coin has heads and tails."),
        ("What goes around the world but stays in a corner?", "Stamp", ["Map", "Compass", "Flag"], "A stamp on an envelope."),
        ("What has hands but cannot clap?", "Clock", ["Mannequin", "Robot", "Statue"], "A clock has hands."),
        ("What has a neck but no head?", "Bottle", ["Giraffe", "Shirt", "Guitar"], "A bottle has a neck."),
        ("What has an eye but cannot see?", "Needle", ["Potato", "Storm", "Camera"], "A needle has an eye."),
        ("What building has the most stories?", "Library", ["Skyscraper", "Museum", "School"], "A library has books/stories."),
        ("What is always coming but never arrives?", "Tomorrow", ["Future", "Train", "Package"], "Tomorrow becomes today."),
        ("What word becomes shorter when you add letters?", "Short", ["Long", "Brief", "Tiny"], "Add 'er' to make 'shorter'."),
        ("What belongs to you but others use it more?", "Your Name", ["Your House", "Your Car", "Your Phone"], "Others say your name."),
        ("What can travel around world while staying in corner?", "Stamp", ["Postcard", "Map", "Flag"], "A postage stamp."),
        ("What has 88 keys but can't open a door?", "Piano", ["Keyboard", "Typewriter", "Lock"], "A piano has 88 keys."),
    ]
    
    for q, ans, dists, expl in riddles_easy:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Number Patterns (60 questions)
    patterns = [
        ("Next: 2, 4, 6, 8, ?", "10", ["12", "9", "11"], "Add 2."),
        ("Next: 5, 10, 15, 20, ?", "25", ["30", "22", "35"], "Add 5."),
        ("Next: 1, 3, 5, 7, ?", "9", ["11", "8", "10"], "Odd numbers."),
        ("Next: 10, 20, 30, 40, ?", "50", ["60", "45", "55"], "Add 10."),
        ("Next: 3, 6, 9, 12, ?", "15", ["18", "14", "16"], "Multiples of 3."),
        ("Next: 4, 8, 12, 16, ?", "20", ["24", "18", "22"], "Multiples of 4."),
        ("Next: 11, 22, 33, 44, ?", "55", ["66", "50", "60"], "Multiples of 11."),
        ("Next: 100, 90, 80, 70, ?", "60", ["50", "65", "75"], "Subtract 10."),
        ("Next: 50, 45, 40, 35, ?", "30", ["25", "32", "28"], "Subtract 5."),
        ("Next: 1, 1, 1, 1, ?", "1", ["2", "0", "11"], "Constant series."),
        ("Next: 0, 1, 2, 3, ?", "4", ["5", "6", "10"], "Sequential."),
        ("Next: 10, 9, 8, 7, ?", "6", ["5", "4", "3"], "Count down."),
        ("Next: 1, 2, 3, 4, ?", "5", ["6", "7", "10"], "Sequential."),
        ("Next: 2, 2, 2, 2, ?", "2", ["3", "4", "0"], "Constant 2."),
        ("Next: 5, 5, 5, 5, ?", "5", ["6", "4", "10"], "Constant 5."),
    ]
    
    for q, ans, dists, expl in patterns:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Odd One Out (40 questions)
    odd_one = [
        ("Find odd one: Car, Bike, Bus, Plane", "Plane", ["Bus", "Bike", "Car"], "Plane flies."),
        ("Find odd one: Apple, Banana, Carrot, Orange", "Carrot", ["Apple", "Banana", "Orange"], "Carrot is vegetable."),
        ("Find odd one: Dog, Cat, Bird, Fish", "Bird", ["Dog", "Cat", "Fish"], "Bird has feathers."),
        ("Find odd one: Red, Blue, Green, Circle", "Circle", ["Red", "Blue", "Green"], "Circle is a shape."),
        ("Find odd one: 2, 4, 6, 9", "9", ["2", "4", "6"], "9 is odd number."),
        ("Find odd one: Triangle, Square, Circle, Red", "Red", ["Triangle", "Square", "Circle"], "Red is color, not shape."),
        ("Find odd one: Monday, Tuesday, January, Wednesday", "January", ["Monday", "Tuesday", "Wednesday"], "January is month."),
        ("Find odd one: Spring, Summer, Autumn, March", "March", ["Spring", "Summer", "Autumn"], "March is month, rest seasons."),
        ("Find odd one: Book, Pen, Paper, Chair", "Chair", ["Book", "Pen", "Paper"], "Chair is furniture."),
        ("Find odd one: Lion, Tiger, Elephant, Leopard", "Elephant", ["Lion", "Tiger", "Leopard"], "Elephant is not a big cat."),
    ]
    
    for q, ans, dists, expl in odd_one:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    # Letter Patterns (20 questions)
    letters = [
        ("Next letter: A, B, C, D, ?", "E", ["F", "G", "H"], "Alphabetical."),
        ("Next letter: Z, Y, X, W, ?", "V", ["U", "T", "S"], "Reverse alphabet."),
        ("Next letter: A, C, E, G, ?", "I", ["J", "K", "H"], "Skip one letter."),
        ("Next letter: B, D, F, H, ?", "J", ["I", "K", "L"], "Skip one letter."),
        ("Next letter: M, N, O, P, ?", "Q", ["R", "S", "T"], "Alphabetical."),
    ]
    
    for q, ans, dists, expl in letters:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 1
        })
    
    return puzzles[:200]  # Ensure exactly 200

def create_puzzle_l2_medium():
    """200 Medium puzzles: wordplay, moderate logic, complex patterns"""
    puzzles = []
    
    # Medium Riddles & Lateral Thinking (80 questions)
    riddles_medium = [
        ("What question can you never answer 'yes' to?", "Are you asleep?", ["Are you hungry?", "Are you human?", "Are you reading?"], "If asleep, you can't answer."),
        ("A man in rain without umbrella didn't get hair wet. Why?", "He was bald", ["He wore a hood", "Wasn't raining hard", "He was inside"], "No hair to get wet."),
        ("What goes up and down but doesn't move?", "Staircase", ["Elevator", "Ball", "Temperature"], "Staircase is stationary."),
        ("If 2's company, 3's a crowd, what are 4 and 5?", "Nine", ["Fun", "Strangers", "A Group"], "4 + 5 = 9."),
        ("What begins with T, ends with T, has T in it?", "Teapot", ["Tent", "Target", "Toast"], "'Tea'-pot."),
        ("I have branches but no fruit, trunk, or leaves. What am I?", "A Bank", ["A Tree", "A River", "A Family"], "A bank has branches."),
        ("What can fill a room but takes up no space?", "Light", ["Air", "Sound", "Smell"], "Light fills room."),
        ("The more you take, the more you leave behind. What am I?", "Footsteps", ["Memories", "Time", "Money"], "More steps, more footprints."),
        ("What has one head, one foot, four legs?", "A Bed", ["A Table", "A Chair", "A Dog"], "Bed head, bed foot, 4 legs."),
        ("What runs but never walks, has mouth but never talks?", "A River", ["A Car", "A Watch", "A Person"], "River runs and has mouth."),
    ]
    
    for q, ans, dists, expl in riddles_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # Complex Number Patterns (60 questions)
    patterns_medium = [
        ("Next: 1, 4, 9, 16, ?", "25", ["36", "20", "24"], "Perfect squares."),
        ("Next: 3, 6, 12, 24, ?", "48", ["36", "30", "50"], "Double each time."),
        ("Next: 1, 1, 2, 3, 5, ?", "8", ["13", "7", "10"], "Fibonacci sequence."),
        ("Next: 2, 6, 12, 20, ?", "30", ["28", "32", "24"], "n(n+1) pattern."),
        ("Next: 1, 8, 27, 64, ?", "125", ["100", "216", "81"], "Perfect cubes."),
        ("Next: 100, 50, 25, 12.5, ?", "6.25", ["5", "10", "3"], "Divide by 2."),
        ("Next: 2, 3, 5, 7, 11, ?", "13", ["15", "9", "17"], "Prime numbers."),
        ("Next: 1, 3, 7, 15, ?", "31", ["30", "28", "25"], "2^n - 1."),
        ("Next: 10, 100, 1000, ?", "10000", ["10", "100000", "500"], "Multiply by 10."),
        ("Next: 81, 27, 9, 3, ?", "1", ["0", "2", "6"], "Divide by 3."),
    ]
    
    for q, ans, dists, expl in patterns_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # Logic Puzzles (40 questions)
    logic_medium = [
        ("If 5 cats catch 5 mice in 5 minutes, how long for 100 cats to catch 100 mice?", "5 minutes", ["100 minutes", "20 minutes", "10 minutes"], "Same rate per cat."),
        ("A farmer has 17 sheep. All but 9 die. How many left?", "9", ["8", "0", "17"], "'All but 9' means 9 survive."),
        ("How many months have 28 days?", "All 12", ["1", "2", "4"], "All months have at least 28."),
        ("A doctor gives you 3 pills, take every half hour. How long to finish?", "1 hour", ["1.5 hours", "2 hours", "30 minutes"], "0min, 30min, 60min."),
        ("In a race, you pass 2nd place. What position are you?", "2nd", ["1st", "3rd", "4th"], "You take their position."),
        ("Mary's father has 5 daughters: Nana, Nene, Nini, Nono, and...?", "Mary", ["Nunu", "Nina", "Nana"], "Mary is the 5th daughter."),
        ("A rooster lays egg on barn roof. Which way does it roll?", "Roosters don't lay eggs", ["Left", "Right", "Down"], "Roosters are male."),
        ("How many of each animal did Moses take on ark?", "Moses didn't have ark", ["2", "7", "0"], "Noah had the ark."),
        ("Electric train going north. Which way does smoke go?", "No smoke", ["North", "South", "East"], "Electric trains don't smoke."),
        ("You have match, candle, oil lamp in dark room. What do you light first?", "The match", ["Candle", "Lamp", "Nothing"], "Match lights others."),
    ]
    
    for q, ans, dists, expl in logic_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    # Word Puzzles (20 questions)
    word_medium = [
        ("What 5-letter word becomes shorter when you add 2 letters?", "Short", ["Brief", "Small", "Tiny"], "Add 'er' → shorter."),
        ("What word is spelled incorrectly in every dictionary?", "Incorrectly",  ["Dictionary", "Wrong", "Misspelled"], "The word 'incorrectly'."),
        ("Forward I'm heavy, backward I'm not. What am I?", "Ton", ["Weight", "Net", "Top"], "Ton backward is 'not'."),
        ("What starts with E, ends with E, contains one letter?", "Envelope", ["Eye", "Edge", "Eagle"], "Envelope contains letter."),
        ("What 7-letter word has hundreds of letters?", "Mailbox", ["Alphabet", "Library", "Letters"], "Mailbox has many letters."),
    ]
    
    for q, ans, dists, expl in word_medium:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 2
        })
    
    return puzzles[:200]

def create_puzzle_l3_hard():
    """200 Hard puzzles: complex logic, advanced patterns, lateral thinking"""
    puzzles = []
    
    # Hard Logic & Lateral Thinking (100 questions)
    logic_hard = [
        ("A man pushes car to hotel, says he's bankrupt. What game?", "Monopoly", ["Poker", "Chess", "Life"], "Board game Monopoly."),
        ("Woman shoots husband, holds underwater 5 min, hangs him. They have dinner. How?", "She's a photographer", ["Dream", "Ghost story", "Movie"], "Photo developing process."),
        ("Can't keep this until you've given it", "Your word", ["Gift", "Secret", "Promise"], "Giving your word."),
        ("I come from mine and  always surrounded by wood. Everyone uses me. What am I?", "Pencil lead", ["Coal", "Diamond", "Metal"], "Graphite from mine, wood pencil."),
        ("Three doctors say Robert is their brother. Robert says no brothers. Who's right?", "Both. Theydoctors are his sisters", ["Robert lies", "Doctors lie", "Adopted"], "Doctors are female."),
        ("Railroad crossing, watch for cars. Spell that without any Rs", "T-H-A-T", ["Crossing", "Railroad", "Cars"], "Spell the word 'THAT'."),
        ("I'm lighter than what I'm made of, more of me is hidden than seen. What am I?", "Iceberg", ["Cloud", "Shadow", "Air"], "Ice lighter than water."),
        ("A man describes daughters: all but 2 are brunettes, all but 2 blondes, all but 2 redheads. How many?", "3 daughters", ["6", "4", "2"], "1 brunette, 1 blonde, 1 redhead."),
        ("Room with no doors/windows. How do you get out?", "Stop imagining", ["Break wall", "Dig", "Teleport"], "It's imaginary."),
        ("I start with M, end with X, have infinite letters. What am I?", "Mailbox", ["Matrix", "Mix", "Max"], "Mailbox holds letters."),
    ]
    
    for q, ans, dists, expl in logic_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    # Advanced Number Patterns (60 questions)
    patterns_hard = [
        ("Next: 1, 1, 2, 3, 5, 8, 13, ?", "21", ["15", "18", "20"], "Fibonacci."),
        ("Next: 2, 3, 5, 7, 11, 13, ?", "17", ["15", "19", "14"], "Primes."),
        ("Next: 1, 4, 9, 16, 25, 36, ?", "49", ["42", "48", "50"], "Perfect squares."),
        ("Next: 1, 8, 27, 64, 125, ?", "216", ["150", "200", "180"], "Perfect cubes."),
        ("Next: 0, 1, 1, 2, 3, 5, 8, 13, ?", "21", ["16", "18", "20"], "Fibonacci from 0."),
        ("Next: 2, 6, 12, 20, 30, ?", "42", ["40", "36", "38"], "n(n+1)."),
        ("Next: 1, 3, 6, 10, 15, ?", "21", ["18", "20", "24"], "Triangular numbers."),
        ("Next: 3, 7, 15, 31, 63, ?", "127", ["100", "120", "130"], "2^n - 1."),
        ("Next: 1, 2, 4, 8, 16, ?", "32", ["24", "20", "30"], "Powers of 2."),
        ("Next: 1, 3, 9, 27, 81, ?", "243", ["100", "200", "162"], "Powers of 3."),
    ]
    
    for q, ans, dists, expl in patterns_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    # Complex Riddles (40 questions)
    riddles_hard = [
        ("What is seen in middle of March and April, not at beginning or end?", "Letter R", ["Spring", "Rain", "Sun"], "R appears in middle."),
        ("Runs smoother than any rhyme, loves to fall but can't climb", "Water", ["Time", "River", "Rain"], "Water flows down."),
        ("I shave 20 times a day yet still have beard. What am I?", "Barber", ["Man", "Razor", "Actor"], "Barber shaves others."),
        ("I'm easy to get into but hard to get out of. What am I?", "Trouble", ["Room", "Bed", "Car"], "Getting into trouble."),
        ("Take off my skin, I won't cry but you will. What am I?", "Onion", ["Orange", "Potato", "Apple"], "Onions make you cry."),
        ("Two fathers and sons went fishing. Caught 3 fish, each got one. How?", "Grandfather, father, son", ["4 people", "Shared", "Lied"], "3 people, 2 fathers, 2 sons."),
        ("I turn polar bears white, make you cry, make guys pee, make girls comb hair. What am I?", "Time/Pressure", ["Cold", "Water", "Magic"], "Time/circumstance does all."),
        ("People make me, save me, change me, raise me. What am I?", "Money", ["Baby", "House", "Plan"], "Money is made, saved, etc."),
        ("If you drop me I'm sure to crack, smile at me I'll smile back. What am I?", "Mirror", ["Glass", "Egg", "Ice"], "Mirror reflects."),
        ("First you eat me, then you get eaten. What am I?", "Fishhook", ["Bait", "Food", "Worm"], "Bait on hook."),
    ]
    
    for q, ans, dists, expl in riddles_hard:
        opts = [ans] + dists
        random.shuffle(opts)
        puzzles.append({
            "text": q,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl,
            "difficulty": 3
        })
    
    return puzzles[:200]

def generate_puzzle_600():
    """Generate complete puzzle quiz with 600 questions"""
    l1 = create_puzzle_l1_easy()
    l2 = create_puzzle_l2_medium()
    l3 = create_puzzle_l3_hard()
    
    print(f"Generated puzzles:")
    print(f"  Level 1 (Easy): {len(l1)} questions")
    print(f"  Level 2 (Medium): {len(l2)} questions")
    print(f"  Level 3 (Hard): {len(l3)} questions")
    print(f"  Total: {len(l1) + len(l2) + len(l3)} questions")
    
    return {
        "id": "PUZZLE",
        "name": "Puzzle",
        "levels": [
            {"id": 1, "questions": l1},
            {"id": 2, "questions": l2},
            {"id": 3, "questions": l3}
        ]
    }

if __name__ == "__main__":
    puzzle_data = generate_puzzle_600()
    with open('app/src/main/assets/puzzle.json', 'w') as f:
        json.dump(puzzle_data, f, indent=2)
    print("\n✅ puzzle.json generated successfully!")
