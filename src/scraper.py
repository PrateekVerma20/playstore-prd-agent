import sys
import pandas as pd
from datetime import datetime, timedelta
from google_play_scraper import Sort, reviews
from database import get_db_engine
from mapping import APP_MAPPING

def scrape_balanced_reviews(company_name, total_target=1000):
    """
    Fetches a balanced mix of reviews (1-5 stars) from the last 6 months.
    Uses pagination to exceed the default 100-review limit.
    """
    app_id = APP_MAPPING.get(company_name.lower().strip())
    if not app_id:
        print(f"❌ {company_name} not found in mapping.py")
        return

    six_months_ago = datetime.now() - timedelta(days=180)
    all_reviews_list = []
    
    # Target 200 reviews per star rating to reach 1000 total
    per_star_target = total_target // 5 

    print(f"📡 Starting High-Scale Scrape for: {company_name} ({app_id})")

    for star in range(1, 6):
        count_fetched = 0
        token = None
        print(f"⭐ Collecting {star}-star reviews (Target: {per_star_target})...")

        while count_fetched < per_star_target:
            # Fetch batch of 100
            result, token = reviews(
                app_id,
                lang='en',
                country='in',
                sort=Sort.NEWEST,
                count=100,
                filter_score_with=star,
                continuation_token=token
            )

            if not result:
                break
            
            # Convert to DataFrame to process dates
            batch_df = pd.DataFrame(result)
            batch_df['at'] = pd.to_datetime(batch_df['at'])
            
            # Filter for reviews within the last 6 months
            filtered_batch = batch_df[batch_df['at'] >= six_months_ago]
            
            if not filtered_batch.empty:
                all_reviews_list.append(filtered_batch)
            
            count_fetched += len(result)
            print(f"   > Progress: {count_fetched}/{per_star_target}")

            # Optimization: If the whole batch is older than 6 months, stop this star
            if len(filtered_batch) < len(result):
                print(f"   📅 Reached 6-month limit for {star}-star.")
                break
            
            # If no more pages available from Google
            if not token:
                break

    if not all_reviews_list:
        print(f"⚠️ No reviews found for {company_name} in the selected timeframe.")
        return

    # Consolidate all batches
    final_df = pd.concat(all_reviews_list).drop_duplicates(subset=['content', 'userName'])
    
    # Prepare for Database
    df_db = final_df[['content', 'score', 'at', 'userName']].copy()
    df_db['company'] = company_name

    # Upload to Neon
    try:
        engine = get_db_engine()
        df_db.to_sql('raw_reviews', engine, if_exists='append', index=False)
        print(f"✅ SUCCESS: Saved {len(df_db)} balanced reviews for {company_name} to Neon.")
    except Exception as e:
        print(f"❌ Database Error: {e}")

if __name__ == "__main__":
    # Get company names from terminal: python src/scraper.py "Blinkit" "Zomato"
    companies = sys.argv[1:]
    
    if not companies:
        print("💡 Usage: python src/scraper.py 'CompanyName'")
    else:
        for name in companies:
            scrape_balanced_reviews(name, total_target=1000)