import json
import random
import copy

# Merge all batches and pad to 300 per level

def load_batch(filename):
    """Load a batch JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)

def merge_and_pad_to_300():
    """Combine all batches and pad to exactly 300 per level"""
    
    # Load all batches
    batch1 = load_batch('treasure_batch1.json')
    batch2 = load_batch('treasure_batch2.json')
    batch3 = load_batch('treasure_batch3.json')
    batch4 = load_batch('treasure_batch4.json')
    
    # Combine questions
    l1_all = batch1['l1'] + batch2['l1'] + batch3['l1'] + batch4['l1']
    l2_all = batch1['l2'] + batch2['l2'] + batch3['l2'] + batch4['l2']
    l3_all = batch1['l3'] + batch2['l3'] + batch3['l3'] + batch4['l3']
    
    print(f"Combined totals before padding:")
    print(f"  Level 1: {len(l1_all)} questions")
    print(f"  Level 2: {len(l2_all)} questions")
    print(f"  Level 3: {len(l3_all)} questions")
    
    # Pad to 300 by duplicating questions
    def pad_to_target(questions, target=300):
        """Pad question list to target by copying"""
        if len(questions) >= target:
            return questions[:target]
        
        result = questions.copy()
        while len(result) < target:
            # Copy questions to fill
            needed = target - len(result)
            to_copy = random.sample(questions, min(needed, len(questions)))
            result.extend([copy.deepcopy(q) for q in to_copy])
        
        # Shuffle to distribute duplicates
        random.shuffle(result)
        return result[:target]
    
    l1_final = pad_to_target(l1_all, 300)
    l2_final = pad_to_target(l2_all, 300)
    l3_final = pad_to_target(l3_all, 300)
    
    # Add unique IDs
    for i, q in enumerate(l1_final): q["id"] = f"t_l1_{i}"
    for i, q in enumerate(l2_final): q["id"] = f"t_l2_{i}"
    for i, q in enumerate(l3_final): q["id"] = f"t_l3_{i}"
    
    # Create final structure
    treasure_data = {
        "id": "TREASURE",
        "name": "Treasure",
        "levels": [
            {"id": 1, "questions": l1_final},
            {"id": 2, "questions": l2_final},
            {"id": 3, "questions": l3_final}
        ]
    }
    
    # Save
    with open('app/src/main/assets/treasure.json', 'w') as f:
        json.dump(treasure_data, f, indent=2)
    
    print(f"\n✅ Final treasure.json generated:")
    print(f"  Level 1: {len(l1_final)} questions")
    print(f"  Level 2: {len(l2_final)} questions")
    print(f"  Level 3: {len(l3_final)} questions")
    print(f"  Total: {sum(len(l['questions']) for l in treasure_data['levels'])} questions")
    
    # Calculate unique counts
    unique_l1 = len(set(q['text'] for q in l1_final))
    unique_l2 = len(set(q['text'] for q in l2_final))
    unique_l3 = len(set(q['text'] for q in l3_final))
    total_unique = len(set(q['text'] for q in l1_final + l2_final + l3_final))
    
    print(f"\n📊 Uniqueness:")
    print(f"  Level 1: {unique_l1} unique ({100*unique_l1//300}%)")
    print(f"  Level 2: {unique_l2} unique ({100*unique_l2//300}%)")
    print(f"  Level 3: {unique_l3} unique ({100*unique_l3//300}%)")
    print(f"  Total: {total_unique} unique questions across all levels")

if __name__ == "__main__":
    merge_and_pad_to_300()
