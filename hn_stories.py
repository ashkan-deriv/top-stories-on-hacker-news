import requests
import json
from datetime import datetime

def fetch_top_stories():
    # Fetch top stories IDs
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(top_stories_url).json()[:30]  # Get top 30 stories
    
    stories = []
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()
        if story and 'title' in story:
            stories.append({
                'title': story.get('title'),
                'url': story.get('url', f'https://news.ycombinator.com/item?id={story_id}'),
                'score': story.get('score', 0),
                'by': story.get('by', 'unknown'),
                'time': datetime.fromtimestamp(story.get('time', 0)).strftime('%Y-%m-%d %H:%M:%S')
            })
    return stories

def generate_html(stories):
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Hacker News Top Stories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f6f6ef;
        }
        h1 {
            color: #ff6600;
            text-align: center;
        }
        .story {
            background-color: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .story h2 {
            margin: 0;
            font-size: 18px;
        }
        .story a {
            color: #2e2e2c;
            text-decoration: none;
        }
        .story a:hover {
            text-decoration: underline;
        }
        .meta {
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>Hacker News Top Stories</h1>
    """
    
    for story in stories:
        html += f"""
    <div class="story">
        <h2><a href="{story['url']}">{story['title']}</a></h2>
        <div class="meta">
            {story['score']} points | by {story['by']} | {story['time']}
        </div>
    </div>
        """
    
    html += """
</body>
</html>
    """
    
    with open('hn_stories.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    stories = fetch_top_stories()
    generate_html(stories)
    print("HTML file has been generated as 'hn_stories.html'")