# Museum Scavenger Hunt Guide Generator

A flexible, printable museum scavenger hunt guide generator that works with any museum or collection. Simply provide your artwork data in JSON format and generate beautiful, interactive HTML guides.

## Architecture

This project consists of three main components:

### 1. JSON Data Files (in `data/` directory)
Contains artwork details in JSON format. Each dataset includes:
- Basic artwork information (title, artist, dates, location)
- Image URLs (supports Wikimedia Commons or any public URL)
- Museum source URLs for attribution
- Four interactive sections:
  - **What makes this cool** - Fascinating facts about each artwork
  - **Did you notice?** - Observable details with checkboxes
  - **Mind Blown!** - Surprising insights with checkboxes
  - **Observation Challenge** - Interactive challenges with checkboxes

**Included datasets:**
- `prado_artworks.json` - Museo del Prado (Madrid, Spain)
- `sofia_reina_artworks.json` - Museo Reina Sofía (Madrid, Spain)

### 2. `template.html` - Jinja2 Template
A reusable HTML template that creates:
- Beautiful cover page with gradient background
- Consistent layout for each artwork page
- Color-coded sections matching the original PDF design
- Print-friendly CSS with page breaks
- Clickable images linking to museum sources
- Interactive checkboxes for tracking progress

### 3. `generate_guide.py` - Python Generator Script
Reads any JSON data file and the template to create standalone, printable HTML files.

**Features:**
- Automatically names output files based on input JSON (e.g., `prado_artworks.json` → `prado_artworks.html`)
- Outputs to `output/` directory for organization
- Command-line options for full customization

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Generate a museum guide using the default dataset (Prado):
```bash
python generate_guide.py
```

This creates `output/prado_artworks.html` - a standalone file ready to print!

Generate a guide from a different dataset:
```bash
python generate_guide.py --json data/sofia_reina_artworks.json
```

This creates `output/sofia_reina_artworks.html`.

### Command-line Options

```bash
# Use custom JSON file (output is auto-named)
python generate_guide.py --json data/my_museum.json

# Override everything
python generate_guide.py --json data/my_museum.json --template my_template.html --output custom_name.html

# See all options
python generate_guide.py --help
```

## Printing

1. Open any generated HTML file from `output/` in your web browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac) to open print dialog
3. Each artwork will automatically be on its own page
4. Save as PDF or print directly

## Creating Your Own Museum Guide

### Option 1: Add to Existing Dataset

Edit any JSON file in `data/` and add new entries following this structure:

```json
{
  "id": 11,
  "title": "Artwork Title",
  "artist": "Artist Name",
  "artist_years": "1400-1500",
  "location": "Room XX - Floor",
  "image_url": "https://upload.wikimedia.org/wikipedia/commons/...",
  "source_url": "https://www.museodelprado.es/...",
  "what_makes_cool": ["Fact 1", "Fact 2"],
  "did_you_notice": ["Detail 1", "Detail 2"],
  "mind_blown": ["Insight 1", "Insight 2"],
  "observation_challenge": ["Challenge 1", "Challenge 2"]
}
```

### Option 2: Create a New Museum Dataset

1. Create a new JSON file in `data/` (e.g., `data/met_artworks.json`)
2. Follow the JSON structure shown above
3. Include your museum name and guide title:
   ```json
   {
     "museum_name": "Your Museum Name",
     "guide_title": "Your Guide Title",
     "artworks": [...]
   }
   ```
4. Generate with: `python generate_guide.py --json data/met_artworks.json`

### Finding Images

**Wikimedia Commons (recommended):**
1. Search for artwork on [Wikimedia Commons](https://commons.wikimedia.org/)
2. Find high-quality version of the image
3. Right-click image and copy image URL
4. Use this URL in the `image_url` field

**Other sources:** Any publicly accessible image URL will work

### Modifying the Design

Edit `template.html` to customize:
- Colors and styling (in the `<style>` section)
- Layout and structure
- Section headings
- Print formatting

## Project Structure

```
scavenger-museum/
├── data/                          # Input JSON datasets
│   ├── prado_artworks.json
│   └── sofia_reina_artworks.json
├── output/                        # Generated HTML guides
│   ├── prado_artworks.html
│   └── sofia_reina_artworks.html
├── template.html                  # HTML template
├── generate_guide.py              # Generator script
└── requirements.txt               # Python dependencies
```

## Technical Details

- **Template Engine**: Jinja2
- **Styling**: Embedded CSS (no external dependencies)
- **Images**: Loaded from Wikimedia Commons URLs
- **Print**: Uses CSS `@page` and `page-break-after` for proper pagination
- **Browser Compatibility**: Works in all modern browsers

## Example Datasets

### Museo del Prado (`prado_artworks.json`)
10 masterpieces including:
- The Garden of Earthly Delights - Hieronymus Bosch
- Las Meninas - Diego Velázquez
- The Third of May 1808 - Francisco Goya
- And 7 more...

### Museo Reina Sofía (`sofia_reina_artworks.json`)
10 modern art masterpieces

## License

The artwork images are from Wikimedia Commons and are in the public domain.

The code and template are provided as-is for educational and personal use.
