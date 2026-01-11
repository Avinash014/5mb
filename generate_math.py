import json
import random

def generate_question(level_id, index):
    q_id = f"m_lvl{level_id}_{index}"
    difficulty = level_id

    # --- Level 1: Simple (1-20) ---
    if level_id == 1:
        op = random.choice(['+', '-', '*', '/'])
        a = random.randint(1, 20)
        b = random.randint(1, 10)
        
        if op == '+':
            ans = a + b
            text = f"{a} + {b} = ?"
            expl = f"{a} + {b} = {ans}"
        elif op == '-':
            ans = a - b
            text = f"{a} - {b} = ?"
            expl = f"{a} - {b} = {ans}"
        elif op == '*':
            ans = a * b
            text = f"{a} * {b} = ?"
            expl = f"{a} * {b} = {ans}"
        elif op == '/':
            ans = a 
            a = ans * b
            text = f"{a} / {b} = ?"
            expl = f"{a} / {b} = {ans}"

    # --- Level 2: Moderate (20-100) ---
    elif level_id == 2:
        op = random.choice(['+', '-', '*'])
        a = random.randint(20, 100)
        b = random.randint(10, 50)
        
        if op == '+':
            ans = a + b
            text = f"{a} + {b} = ?"
            expl = f"{a} + {b} = {ans}"
        elif op == '-':
            # Ensure positive for now, or simple negatives
            if b > a: a, b = b, a
            ans = a - b
            text = f"{a} - {b} = ?"
            expl = f"{a} - {b} = {ans}"
        elif op == '*':
            # Smaller numbers for multiply to keep it mental math friendly-ish
            a = random.randint(10, 20)
            b = random.randint(5, 12)
            ans = a * b
            text = f"{a} * {b} = ?"
            expl = f"{a} * {b} = {ans}"

    # --- Level 3: BODMAS (A + B * C) ---
    elif level_id == 3:
        # Template: A op1 B op2 C
        ops = [('+', '*'), ('-', '*'), ('*', '+'), ('*', '-'), ('+', '/'), ('-', '/')]
        op_pair = random.choice(ops)
        op1, op2 = op_pair
        
        a = random.randint(2, 12)
        b = random.randint(2, 10)
        c = random.randint(2, 10)
        
        # Format string
        text = f"{a} {op1} {b} {op2} {c} = ?"
        
        # Calculate Answer carefully considering precedence
        # Python eval handles precedence, but let's be explicit or use eval for simplicity in generation script
        expression = f"{a}{op1}{b}{op2}{c}"
        
        # Ensure division is clean for Level 3 if used
        if '/' in op_pair:
            # Construct specifically to be clean. 
            # E.g. A + (B*C) is safe. A + B / C -> B must be multiple of C.
            if op2 == '/':
                 # A op1 B / C. Make B a multiple of C.
                 res = b * c # Swap
                 b = res
                 # Now B/C = res/c = b_old
                 expression = f"{a}{op1}{b}{op2}{c}"
                 text = f"{a} {op1} {b} {op2} {c} = ?"
            elif op1 == '/':
                 # A / B op2 C. Make A multiple of B.
                 res = a * b
                 a = res
                 expression = f"{a}{op1}{b}{op2}{c}"
                 text = f"{a} {op1} {b} {op2} {c} = ?"

        ans = int(eval(expression))
        expl = f"{text.replace('?', str(ans))}"

    # Generate Options
    options = {ans}
    while len(options) < 4:
        # Variance based on difficulty
        variance = 5 if level_id == 1 else (10 if level_id == 2 else 20)
        fake = ans + random.randint(-variance, variance)
        if fake != ans:
            options.add(fake)
    
    options_list = list(options)
    random.shuffle(options_list)
    
    return {
        "id": q_id,
        "text": text,
        "options": [str(x) for x in options_list],
        "correctIndex": options_list.index(ans),
        "difficulty": difficulty,
        "explanation": expl
    }

def generate_full_math_quiz():
    levels = []
    
    # Generate 200 questions for each of the 3 levels
    for lvl in range(1, 4):
        qs = []
        for i in range(200):
            qs.append(generate_question(lvl, i))
        
        levels.append({
            "id": lvl,
            "questions": qs
        })

    data = {
        "id": "MATH",
        "name": "Math",
        "levels": levels
    }
    return data

if __name__ == "__main__":
    data = generate_full_math_quiz()
    print(json.dumps(data, indent=2))
