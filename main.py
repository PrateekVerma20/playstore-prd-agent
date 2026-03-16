import os
from dotenv import load_dotenv
from src.mapping import APP_MAPPING
from src.harvester import fetch_raw_reviews
from src.processor import get_distilled_context
from src.agent import generate_prd

load_dotenv()

def main():
    target_app = input("Which app from mapping? (e.g., cred, zomato): ").lower()
    app_id = APP_MAPPING.get(target_app)
    
    if not app_id:
        print(f"❌ '{target_app}' not found in src/mapping.py")
        return

    # 1. Harvest (Now supports 10,000)
    raw_df = fetch_raw_reviews(app_id, max_count=10000)
    
    # 2. Process
    clean_context = get_distilled_context(raw_df)
    
    # 3. AI Generation
    if len(clean_context) > 50:
        result = generate_prd(target_app, clean_context)
        
        with open(f"{target_app}_PRD.md", "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"✨ PRD saved to {target_app}_PRD.md")
    else:
        print("❌ Error: Distilled context was too small for AI analysis.")

if __name__ == "__main__":
    main()