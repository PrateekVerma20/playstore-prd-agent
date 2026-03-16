from textblob import TextBlob

def get_distilled_context(df):
    if df.empty:
        return "No review data found."

    # Column name safety check
    if 'text' not in df.columns:
        for col in ['content', 'reviewText', 'body']:
            if col in df.columns:
                df = df.rename(columns={col: 'text'})
                break

    # 1. Immediate Clean-up (Drop columns we don't need to save memory)
    # We only need: text and score
    df = df[['text', 'score']].dropna()
    df['text'] = df['text'].astype(str)

    # 2. Filter for Quality (80+ characters for high-detail feedback)
    df_quality = df[df['text'].str.len() > 80].copy()

    # 3. Sentiment Analysis on the quality set
    print(f"🧠 Processor: Analyzing sentiment for {len(df_quality)} high-quality reviews...")
    df_quality['sentiment'] = df_quality['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # 4. Extract Extremes (Top 50 Negative, Top 50 Positive)
    angry = df_quality[df_quality['score'] <= 2].sort_values('sentiment').head(50)
    happy = df_quality[df_quality['score'] >= 4].sort_values('sentiment', ascending=False).head(50)

    context = "### CRITICAL PAIN POINTS\n" + "\n- ".join(angry['text'].tolist())
    context += "\n\n### POSITIVE HIGHLIGHTS\n" + "\n- ".join(happy['text'].tolist())

    return context