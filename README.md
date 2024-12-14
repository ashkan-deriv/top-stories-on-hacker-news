# Hacker News Top Stories Viewer

A simple and elegant way to view the top stories from Hacker News. This project fetches the latest top stories from Hacker News and displays them in a clean, responsive HTML page.

## Features

- Fetches top 30 stories from Hacker News
- Clean, modern UI with responsive design
- Shows story title, points, author, and timestamp
- Direct links to original stories
- Hover effects for better interaction
- Mobile-friendly layout

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ashkan-deriv/top-stories-on-hacker-news.git
cd top-stories-on-hacker-news
```

2. Install the required package:
```bash
pip install requests
```

## Usage

1. Run the Python script:
```bash
python3 hn_stories.py
```

2. The script will:
   - Fetch the latest top stories from Hacker News
   - Generate an HTML file named `hn_stories.html`
   - Print a confirmation message when done

3. Open `hn_stories.html` in your web browser to view the stories

## How It Works

The project consists of two main components:

1. `hn_stories.py`: Python script that:
   - Fetches data from the Hacker News API
   - Processes the story information
   - Generates a styled HTML page

2. Generated `hn_stories.html`: A responsive webpage that:
   - Displays stories in a clean card layout
   - Shows points, author, and timestamp for each story
   - Provides clickable links to original stories
   - Uses modern CSS styling with hover effects

## Customization

You can modify the following aspects:

- Number of stories: Change the slice index in `story_ids = requests.get(top_stories_url).json()[:30]`
- Styling: Modify the CSS in the `generate_html()` function
- Display format: Adjust the HTML template in the same function

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.