import pandas as pd
import os
from src.processor import get_distilled_context  # Matching your function name
from src.agent import generate_prd
from dotenv import load_dotenv

load_dotenv()

def run_reprocess():
    csv_file = "last_raw_fetch.csv"
    
    if not os.path.exists(csv_file):
        print(f"❌ Could not find {csv_file}")
        return

    # 1. Load the CSV into a DataFrame
    print(f"📂 Reading {csv_file}...")
    df = pd.read_csv(csv_file)

    # 2. Get the "Crux" using your processor.py logic
    # Your function expects a DataFrame and returns a string
    crux_context = get_distilled_context(df)
    
    print(f"✅ Distilled context created (Length: {len(crux_context)} chars)")

    # 3. Feed the distilled context into Agent.py
    print("🤖 Agent: Generating PRD...")
    result = generate_prd("YourAppName", crux_context)
    
    print("\n--- FINAL PRD ---\n")
    print(result)

if __name__ == "__main__":
    run_reprocess()