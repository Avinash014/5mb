import json
import random

# --- HELPER: Deduplication Wrapper ---
class UniqueGenerator:
    def __init__(self):
        self.seen_texts = set()

    def add(self, q):
        if q["text"] not in self.seen_texts:
            self.seen_texts.add(q["text"])
            return True
        return False

# Helper for primes
def get_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

# --- 1. SERIES & PATTERNS (Procedural - Infinite Variety) ---
def generate_series(difficulty, count, gen_tracker):
    qs = []
    attempts = 0
    
    # Pre-compute primes for efficiency if needed, or just huge list
    primes_list = get_primes(2000)

    # Increase max attempts
    while len(qs) < count and attempts < count * 500:
        attempts += 1
        
        # Logic Types
        if difficulty == 1:
            # Linear Arith (+n), Sub (-n)
            start = random.randint(1, 100)
            diff = random.randint(2, 15)
            if random.random() > 0.5: op = "add"; seq = [start + i*diff for i in range(5)]
            else: op = "sub"; seq = [start + 100 - i*diff for i in range(5)]
            
            expl = f"Constant difference of {diff}."
            
        elif difficulty == 2:
            # Squares, Mixed (+2, +4, +6)
            mode = random.choice(['square', 'inc_diff', 'alt'])
            if mode == 'square':
                start = random.randint(1, 25)
                seq = [(start+i)**2 for i in range(5)]
                expl = "Perfect squares."
            elif mode == 'inc_diff':
                start = random.randint(5, 50)
                curr = start; seq = [curr]; d = random.randint(2, 5)
                for _ in range(4): curr+=d; seq.append(curr); d+=1 # +2, +3, +4
                expl = "Difference increases by 1."
            else:
                s = random.randint(10, 80)
                jump = random.randint(3, 9)
                seq = [s, s+jump, s, s+jump, s] # Simple alternator
                expl = "Alternating pattern."

        else: # Diff 3
            # Primes, Cube, Fibonacci, Two-Step
            # Bias towards high-entropy (fib, mult_add)
            mode = random.choices(['prime', 'fib', 'cube', 'mult_add'], weights=[1, 5, 2, 5], k=1)[0]

            if mode == 'prime':
                if len(primes_list) > 5:
                    idx = random.randint(0, len(primes_list)-6)
                    seq = primes_list[idx:idx+5]
                    expl = "Prime numbers."
                else:
                    continue
            elif mode == 'fib':
                a, b = random.randint(2, 50), random.randint(2, 50)
                seq = [a, b]; 
                for _ in range(3): seq.append(seq[-1]+seq[-2])
                expl = "Fibonacci sequence."
            elif mode == 'cube':
                s = random.randint(2, 30)
                seq = [i**3 for i in range(s, s+5)]
                expl = "Perfect cubes."
            else: # x2 + k
                 s = random.randint(2, 50)
                 k = random.randint(1, 20)
                 mult = random.choice([2, 3])
                 curr = s; seq = [curr]
                 for _ in range(4): curr=curr*mult+k; seq.append(curr)
                 expl = f"Multiply by {mult} then add {k}."
        
        ans = seq[-1]
        disp = seq[:-1]
        
        # Wrong options
        wrongs = set()
        while len(wrongs) < 3:
            w = ans + random.randint(-10, 10)
            if w != ans: wrongs.add(w)
        
        opts = [str(ans)] + [str(x) for x in list(wrongs)]
        random.shuffle(opts)
        
        q = {
            "text": f"Next in series: {', '.join(map(str, disp))}, ?",
            "options": opts,
            "correctIndex": opts.index(str(ans)),
            "explanation": expl,
            "difficulty": difficulty
        }
        
        if gen_tracker.add(q): qs.append(q)
            
    return qs

# --- 2. BLOOD RELATIONS (Template Expansion) ---
def generate_blood(difficulty, count, gen_tracker):
    qs = []
    
    # EXPANDED NAME POOL (50+ each)
    m_names = ["John", "Mike", "Alex", "David", "Tom", "Sam", "Chris", "James", "Robert", "Michael", "William", "Richard", "Joseph", "Thomas", "Charles", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "Joshua", "Kevin", "Brian", "George", "Edward", "Ronald"]
    f_names = ["Mary", "Lisa", "Anna", "Sarah", "Emma", "Kate", "Jane", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Karen", "Nancy", "Margaret", "Betty", "Dorothy", "Sandra", "Ashley", "Kimberly", "Donna", "Emily", "Carol", "Michelle", "Amanda", "Melissa", "Deborah"]
    
    templates = [
        # Easy
        ("{0}'s wife is {1}. {2} is {0}'s brother. What is {2} to {1}?", "Brother-in-law", ["Brother", "Uncle", "Husband"], "{2} is husband's brother.", 1),
        ("{0} is the father of {1}. {1} is the brother of {2}. What is {0} to {2}?", "Father", ["Uncle", "Brother", "Grandfather"], "{0} is father of both.", 1),
        ("Who is your father's wife?", "Mother", ["Aunt", "Sister", "Grandmother"], "Father's wife is mother.", 1),
        ("Who is your mother's brother?", "Uncle", ["Nephew", "Father", "Cousin"], "Sibling of parent is Uncle.", 1),
        ("Who is your aunt's daughter?", "Cousin", ["Niece", "Sister", "Mother"], "Child of aunt is cousin.", 1),
        ("{0} is {1}'s brother. {1} is {2}'s sister. How is {0} related to {2} (brother)?", "Brother", ["Cousin", "Father", "Uncle"], "Siblings.", 1),
        
        # Med
        ("{0} introduces {1} saying 'He is the husband of the granddaughter of my father'. How is {1} related to {0}?", "Son-in-law", ["Son", "Brother", "Nephew"], "Granddaughter of father is Daughter. Husband of Daughter is Son-in-law.", 2),
        ("Pointing to a man, a woman said 'His mother is the only daughter of my mother'. Who is the woman?", "Mother", ["Sister", "Aunt", "Grandmother"], "Only daughter of 'my mother' is the speaker herself.", 2),
        ("A and B are brothers. C and D are sisters. A's son is D's brother. How is B related to C?", "Uncle", ["Father", "Brother", "Grandfather"], "Uncle logic.", 2),
        ("{0} says to {1}: 'Your father is the only son of my father'. Who is {0}?", "Father", ["Brother", "Uncle", "Grandfather"], "Speaker is the 'only son'.", 2),
        
        # Hard (Dynamic Puzzles)
        ("If {0} $ {1} means {0} is father of {1}; {0} # {1} means {0} is mother of {1}; {0} * {1} means {0} is sister of {1}. Then how is {1} related to {2} in {2} # {3} $ {0} * {1}?", "Grandchild", ["Child", "Niece", "Sibling"], "{2} is mother of {3}. {3} is father of {0}, {0} is sister of {1}.", 3),
        ("Pointing to a photograph, {0} said 'I have no brother or sister but that man's father is my father's son'.", "His Son", ["Himself", "Father", "Nephew"], "My father's son (no siblings) = Me. 'That man's father is Me'. That man is my son.", 3),
        ("{0} is the brother of {1}. {2} is the brother of {1}. {0} is the brother of {3}. But {1} is not the brother of {3}. How is {1} related to {3}?", "Sister", ["Brother", "Aunt", "Mother"], "If {1} is not brother but sibling, {1} must be Sister.", 3),
        ("Looking at a portrait, {0} said, 'Her mother is the only daughter of my mother'. Who is {0} to the portrait person?", "Mother", ["Sister", "Aunt", "Grandmother"], "Speaker is the only daughter.", 3)
    ]
    
    attempts = 0
    while len(qs) < count and attempts < count * 20:
        attempts += 1
        t = random.choice([x for x in templates if x[4] == difficulty])
        
        nm1 = random.choice(m_names)
        nm2 = random.choice(f_names)
        nm3 = random.choice(m_names)
        nm4 = random.choice(f_names) # Add 4th name
        
        # Determine number of placeholders needed? Just try formatting with 4.
        try:
            txt = t[0].format(nm1, nm2, nm3, nm4)
        except:
             # Fallback if format fails (shouldn't if templates match)
             txt = t[0]
             
        ans = t[1]
        
        opts = [ans] + t[2]
        random.shuffle(opts)
        
        q = {
            "text": txt,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": t[3],
            "difficulty": difficulty
        }
        if gen_tracker.add(q): qs.append(q)
            
    return qs

# --- 3. DIRECTION & RANKING (New for Variety) ---
def generate_positional(difficulty, count, gen_tracker):
    qs = []
    
    # RANKING
    # "A is 5th from left, 6th from right. Total?"
    attempts = 0
    while len(qs) < count // 2 and attempts < count * 20:
        attempts+=1
        l = random.randint(3, 30)
        r = random.randint(3, 30)
        total = l + r - 1
        
        names_p = ["Alex", "Sam", "Jordan", "Taylor", "Casey", "Jamie", "Robin", "Drew", "Morgan"]
        nm = random.choice(names_p)
        
        txt = f"In a row, {nm} is {l}th from the left and {r}th from the right. How many people are in the row?"
        ans = str(total)
        wrongs = [str(total+1), str(total-1), str(total+2)]
        opts = [ans] + wrongs
        random.shuffle(opts)
        
        q = {
            "text": txt,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": f"Total = (Left + Right) - 1 = {l} + {r} - 1 = {total}.",
            "difficulty": 1 if total < 30 else 2
        }
        if gen_tracker.add(q): qs.append(q)

    # DIRECTION
    # "Walks 5km North, turns right, walks 5km. Direction?"
    directions = ["North", "East", "South", "West"]
    right_map = {"North": "East", "East": "South", "South": "West", "West": "North"}
    left_map = {"North": "West", "West": "South", "South": "East", "East": "North"}
    
    attempts = 0
    while len(qs) < count and attempts < count * 20:
        attempts+=1
        start_dir = random.choice(directions)
        turn = random.choice(["right", "left"])
        dist1 = random.randint(5, 50)
        dist2 = random.randint(5, 50)
        
        final_dir = right_map[start_dir] if turn == "right" else left_map[start_dir]
        
        name_d = random.choice(["Sam", "Tom", "Jerry", "Mike", "Steve", "Bill", "Bob"])
        
        txt = f"{name_d} faces {start_dir}. He walks {dist1}m, turns {turn}, and walks {dist2}m. Which direction is he facing now?"
        ans = final_dir
        wrongs = [d for d in directions if d != ans][:3]
        opts = [ans] + wrongs
        random.shuffle(opts)
        
        q = {
            "text": txt,
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": f"Turn {turn} from {start_dir} is {final_dir}.",
            "difficulty": 1
        }
        if gen_tracker.add(q): qs.append(q)
        
    return qs

# --- 4. CODING-DECODING (New) ---
def generate_coding(difficulty, count, gen_tracker):
    qs = []
    # EXPANDED WORD POOL
    words = ["CAT", "DOG", "PEN", "BAT", "SKY", "RED", "MAN", "CUP", "BOX", "FOX", "HAT", "CAR", "BUS", "VAN", "JUG", "MUG", "RUG", "TAG", "BAG", "LEG", "EGG", "ANT", "BEE", "COW", "OWL", "PIG", "RAT", "SUN", "MOON", "STAR", "FISH", "BIRD", "LION", "TIGER", "BEAR", "WOLF", "DUCK", "SWAN", "FROG", "TOAD"]
    
    attempts = 0
    # Type 1: +1/2/-1 Letter
    while len(qs) < count // 2 and attempts < count * 20: 
        attempts += 1
        w1 = random.choice(words)
        w2 = random.choice([x for x in words if x != w1])
        
        shift = random.choice([1, -1, 2])
        
        c1 = "".join([chr(ord(c)+shift) for c in w1])
        ans = "".join([chr(ord(c)+shift) for c in w2])
        
        # Wrong answers
        w_wrong1 = "".join([chr(ord(c)-shift) for c in w2])
        w_wrong2 = "".join([chr(ord(c)) for c in w2])
        w_wrong3 = "".join([chr(ord(c)+shift+1) for c in w2])
        
        opts = [ans, w_wrong1, w_wrong2, w_wrong3]
        random.shuffle(opts)
        
        expl_text = f"Letters shifted by {shift}."
        
        q = {
            "text": f"In a code, {w1} is written as {c1}. How is {w2} written?",
            "options": opts,
            "correctIndex": opts.index(ans),
            "explanation": expl_text,
            "difficulty": 2
        }
        if gen_tracker.add(q): qs.append(q)

    attempts = 0
    # Type 2: Number Coding (A=1)
    while len(qs) < count and attempts < count * 20:
        attempts += 1
        w = random.choice(words)
        # SUM
        val_w = sum([ord(c)-64 for c in w])
        
        # Target
        w2 = random.choice([x for x in words if x != w])
        val_ans = sum([ord(c)-64 for c in w2])
        
        wrongs = set()
        while len(wrongs) < 3:
            r = val_ans + random.randint(-5, 5)
            if r != val_ans and r > 0: wrongs.add(r)
        
        opts = [str(val_ans)] + [str(x) for x in list(wrongs)]
        random.shuffle(opts)
        
        q = {
            "text": f"If {w} = {val_w}, then {w2} = ?",
            "options": opts,
            "correctIndex": opts.index(str(val_ans)),
            "explanation": "Sum of letter positions (A=1, B=2...).",
            "difficulty": 3
        }
        if gen_tracker.add(q): qs.append(q)
            
    return qs

def generate_full_reasoning_quiz():
    gen_tracker = UniqueGenerator()
    final_l1 = []
    final_l2 = []
    final_l3 = []
    
    # L1: Easy Series (100), Easy Blood (40), Easy Direction (30), Easy Ranking (30) -> Total 200
    final_l1.extend(generate_series(1, 100, gen_tracker))
    final_l1.extend(generate_blood(1, 60, gen_tracker)) # Increased attempts
    final_l1.extend(generate_positional(1, 40, gen_tracker))
    
    # L2: Med Series (100), Med Blood (50), Med Coding (50) -> Total 200
    final_l2.extend(generate_series(2, 100, gen_tracker))
    final_l2.extend(generate_blood(2, 60, gen_tracker))
    final_l2.extend(generate_coding(2, 40, gen_tracker))
    
    # L3: Hard Series (100), Hard Blood (50), Hard Coding (50) -> Total 200
    s3 = generate_series(3, 100, gen_tracker); final_l3.extend(s3); print(f"L3 Series: {len(s3)}")
    b3 = generate_blood(3, 60, gen_tracker); final_l3.extend(b3); print(f"L3 Blood: {len(b3)}")
    c3 = generate_coding(3, 40, gen_tracker); final_l3.extend(c3); print(f"L3 Coding: {len(c3)}")
    
    def process(list_qs, prefix):
        random.shuffle(list_qs)
        final = []
        for i, q in enumerate(list_qs):
            if i >= 200: break # STRICT CAP
            q["id"] = f"{prefix}_{i}"
            final.append(q)
        return final

    return {
        "id": "REASONING",
        "name": "Reasoning",
        "levels": [
            {"id": 1, "questions": process(final_l1, "r_full_l1")},
            {"id": 2, "questions": process(final_l2, "r_full_l2")},
            {"id": 3, "questions": process(final_l3, "r_full_l3")}
        ]
    }

if __name__ == "__main__":
    data = generate_full_reasoning_quiz()
    with open('app/src/main/assets/reasoning.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Full 600 Reasoning Questions Generated")
