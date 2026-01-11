import json
import os
import glob

def check_file(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        filename = os.path.basename(filepath)
        total = 0
        level_counts = []
        unique_texts = set()
        duplicate_texts = 0
        
        print(f"\n--- {filename} ---")
        
        for level in data.get('levels', []):
            count = len(level.get('questions', []))
            level_counts.append(count)
            total += count
            
            for q in level.get('questions', []):
                text = q.get('text', '').strip()
                if text in unique_texts:
                    duplicate_texts += 1
                else:
                    unique_texts.add(text)
        
        print(f"Total Questions: {total}")
        print(f"Counts per Level: {level_counts}")
        print(f"Unique Questions: {len(unique_texts)}")
        print(f"Duplicate Texts: {duplicate_texts}")
        
        if total < 600:
            print(f"WARNING: Total questions < 600")
        if duplicate_texts > 0:
            print(f"WARNING: Contains {duplicate_texts} duplicate questions (same text)")

    except Exception as e:
        print(f"ERROR: {os.path.basename(filepath)} - {e}")

assets_dir = 'app/src/main/assets'
files = glob.glob(os.path.join(assets_dir, '*.json'))

print("Checking JSON files...")
for f in files:
    check_file(f)
