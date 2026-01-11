import json
import os
import glob

def check_file(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        all_ids = {}
        duplicates = []
        
        for level in data.get('levels', []):
            for q in level.get('questions', []):
                qid = q.get('id')
                if not qid:
                    continue
                if qid in all_ids:
                    duplicates.append(qid)
                all_ids[qid] = True
                
        if duplicates:
            print(f"FAIL: {os.path.basename(filepath)} has {len(duplicates)} duplicates.")
            print(f"Sample: {duplicates[:5]}")
        else:
            print(f"PASS: {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"ERROR: {os.path.basename(filepath)} - {e}")

assets_dir = 'app/src/main/assets'
files = glob.glob(os.path.join(assets_dir, '*.json'))

print("Checking JSON files for duplicate IDs...")
for f in files:
    check_file(f)
