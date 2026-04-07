"""
TrendPulse Task 1: Fetch Data from HackerNews API
Fetches trending stories and categorizes them based on keywords in titles.
"""

import requests
import json
import time
import os
from datetime import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Step 1: Define category keywords for classification
CATEGORY_KEYWORDS = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

# API configuration
BASE_URL = "https://hacker-news.firebaseio.com/v0"
HEADERS = {"User-Agent": "TrendPulse/1.0"}
TOP_STORIES_LIMIT = 500
STORIES_PER_CATEGORY = 25

# Create a session with retry strategy for better performance
def create_session():
    """Create a requests session with connection pooling and retry strategy."""
    session = requests.Session()
    retry = Retry(
        total=2,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 503, 504)
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def get_category(title):
    """
    Assign a category to a story based on keywords in its title.
    Returns the category name or None if no match is found.
    """
    title_lower = title.lower()
    
    # Check each category's keywords
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category
    
    return None


def fetch_top_story_ids(session, limit=TOP_STORIES_LIMIT):
    """
    Fetch the list of top story IDs from HackerNews.
    Returns a list of story IDs.
    """
    try:
        url = f"{BASE_URL}/topstories.json"
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        story_ids = response.json()
        return story_ids[:limit]
    except requests.RequestException as e:
        print(f"Error fetching top story IDs: {e}")
        return []


def fetch_story_details(session, story_id):
    """
    Fetch details for a single story by its ID.
    Returns a story object dict or None if the request fails.
    """
    try:
        url = f"{BASE_URL}/item/{story_id}.json"
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching story {story_id}: {e}")
        return None


def extract_story_data(story):
    """
    Extract required fields from a story object.
    Returns a dict with the 7 required fields.
    """
    return {
        "post_id": story.get("id"),
        "title": story.get("title", ""),
        "category": None,  # Will be assigned later
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", ""),
        "collected_at": datetime.now().isoformat()
    }


def collect_stories(session):
    """
    Main function to fetch stories, categorize them, and collect up to 25 per category.
    """
    print("Starting TrendPulse data collection...")
    print(f"Fetching top {TOP_STORIES_LIMIT} story IDs...")
    
    # Fetch top story IDs
    story_ids = fetch_top_story_ids(session)
    if not story_ids:
        print("Failed to fetch story IDs. Exiting.")
        return []
    
    print(f"Retrieved {len(story_ids)} story IDs")
    
    # Initialize category counters
    category_counts = {cat: 0 for cat in CATEGORY_KEYWORDS.keys()}
    collected_stories = []
    
    # Track which stories we've seen to avoid duplicates
    seen_ids = set()
    
    # Process each story ID
    for idx, story_id in enumerate(story_ids):
        # Stop if we have enough stories in all categories
        if all(count >= STORIES_PER_CATEGORY for count in category_counts.values()):
            print(f"Reached target of {STORIES_PER_CATEGORY} stories per category. Stopping.")
            break
        
        # Skip if we've already processed this story
        if story_id in seen_ids:
            continue
        seen_ids.add(story_id)
        
        # Fetch story details
        story = fetch_story_details(session, story_id)
        if story is None or "title" not in story:
            continue
        
        # Extract story data
        story_data = extract_story_data(story)
        
        # Assign category
        category = get_category(story_data["title"])
        if category is None:
            continue  # Skip stories without a matching category
        
        # Only collect if we haven't reached the limit for this category
        if category_counts[category] < STORIES_PER_CATEGORY:
            story_data["category"] = category
            collected_stories.append(story_data)
            category_counts[category] += 1
            
            # Print progress
            print(f"Collected {category}: {story_data['title'][:50]}...")
        
        # Apply 2-second wait once per category (when we finish collecting a category)
        if all(category_counts[cat] >= STORIES_PER_CATEGORY for cat in CATEGORY_KEYWORDS.keys()):
            # All categories are full, we're done
            break
    
    return collected_stories, category_counts


def save_to_json(stories):
    """
    Save collected stories to a JSON file in data/ folder.
    File is named trends_YYYYMMDD.json
    """
    # Create data folder if it doesn't exist
    data_folder = "data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Created {data_folder}/ folder")
    
    # Generate filename with current date
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"{data_folder}/trends_{current_date}.json"
    
    # Save to JSON
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stories, f, indent=2, ensure_ascii=False)
        return filename
    except IOError as e:
        print(f"Error saving to JSON: {e}")
        return None


def main():
    """
    Main entry point for the TrendPulse data collection script.
    """
    # Create a session with connection pooling
    session = create_session()
    
    try:
        # Collect stories
        stories, category_counts = collect_stories(session)
        
        if not stories:
            print("No stories collected. Exiting.")
            return
        
        # Save to JSON
        filename = save_to_json(stories)
        
        # Print summary
        print("\n" + "="*60)
        print(f"Collected {len(stories)} stories. Saved to {filename}")
        print("\nBreakdown by category:")
        for category, count in category_counts.items():
            print(f"  {category}: {count}")
        print("="*60)
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    main()
