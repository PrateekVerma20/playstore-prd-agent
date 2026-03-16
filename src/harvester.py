import os
import pandas as pd
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

def fetch_raw_reviews(app_id, max_count=10000):
    api_token = os.getenv("APIFY_API_TOKEN")
    client = ApifyClient(api_token)
    
    run_input = {
        "appIds": [app_id],
        "maxReviews": max_count,
        "sort": "NEWEST",
        "lang": "en",
        "country": "in"
    }
    
    print(f"📡 Harvester: Starting deep scrape of {max_count} reviews...")
    
    # .start() returns immediately; we then wait for it to finish in the cloud
    actor_run = client.actor("code-node-tools/google-play-reviews-scraper").start(run_input=run_input)
    
    # wait_for_finish is vital for 10k reviews; it keeps the connection alive
    print("⏳ Scraper is running in the cloud. This may take 2-3 minutes...")
    run_details = client.run(actor_run["id"]).wait_for_finish() 

    if run_details["status"] != "SUCCEEDED":
        print(f"❌ Scraper failed with status: {run_details['status']}")
        return pd.DataFrame()

    # Fetching results in one go from the dataset
    results = list(client.dataset(run_details["defaultDatasetId"]).iterate_items())
    df = pd.DataFrame(results)
    
    # Map column names as before
    if 'content' in df.columns:
        df = df.rename(columns={'content': 'text'})
    
    df.to_csv("last_raw_fetch.csv", index=False)
    print(f"✅ Harvested {len(df)} total reviews.")
    return df