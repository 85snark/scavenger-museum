# Museo del Prado - The Fun Guide

A printable museum scavenger hunt guide generator for the Prado Museum in Madrid, Spain.

## Architecture

This project consists of three main components:

### 1. `artworks.json` - Data File
Contains all details for 10 famous artworks from the Prado Museum, including:
- Basic artwork information (title, artist, dates, location)
- Wikimedia Commons image URLs (no local files needed!)
- Museum source URLs for attribution
- Four interactive sections:
  - **What makes this cool** - Fascinating facts about each artwork
  - **Did you notice?** - Observable details with checkboxes
  - **Mind Blown!** - Surprising insights with checkboxes
  - **Observation Challenge** - Interactive challenges with checkboxes

### 2. `template.html` - Jinja2 Template
A reusable HTML template that creates:
- Beautiful cover page with gradient background
- Consistent layout for each artwork page
- Color-coded sections matching the original PDF design
- Print-friendly CSS with page breaks
- Clickable images linking to museum sources
- Interactive checkboxes for tracking progress

### 3. `generate_guide.py` - Python Generator Script
Reads the JSON data and template to create a standalone, printable HTML file.

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

Generate the museum guide:
```bash
python generate_guide.py
```

This creates `museum_guide.html` - a standalone file ready to print!

### Command-line Options

```bash
# Use custom files
python generate_guide.py --json my_artworks.json --template my_template.html --output my_guide.html

# See all options
python generate_guide.py --help
```

## Printing

1. Open `museum_guide.html` in your web browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac) to open print dialog
3. Each artwork will automatically be on its own page
4. Save as PDF or print directly

## Customization

### Adding New Artworks

Edit `artworks.json` and add new entries following this structure:

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

### Finding Wikimedia Commons Images

1. Search for artwork on [Wikimedia Commons](https://commons.wikimedia.org/)
2. Find high-quality version of the image
3. Right-click image and copy image URL
4. Use this URL in the `image_url` field

### Modifying the Design

Edit `template.html` to customize:
- Colors and styling (in the `<style>` section)
- Layout and structure
- Section headings
- Print formatting

## Files Generated

- `museum_guide.html` - The final printable guide (standalone, includes all styles)

## Technical Details

- **Template Engine**: Jinja2
- **Styling**: Embedded CSS (no external dependencies)
- **Images**: Loaded from Wikimedia Commons URLs
- **Print**: Uses CSS `@page` and `page-break-after` for proper pagination
- **Browser Compatibility**: Works in all modern browsers

## The 10 Artworks Included

1. The Garden of Earthly Delights - Hieronymus Bosch
2. The Triumph of Death - Pieter Bruegel the Elder
3. The Descent from the Cross - Rogier van der Weyden
4. David with the Head of Goliath - Caravaggio
5. The Nobleman with his Hand on his Chest - El Greco
6. Las Meninas (The Ladies-in-Waiting) - Diego Velázquez
7. Charles V at Mühlberg - Titian
8. The Three Graces - Peter Paul Rubens
9. The Third of May 1808 - Francisco Goya
10. Saturn Devouring His Son - Francisco Goya

## License

The artwork images are from Wikimedia Commons and are in the public domain.

The code and template are provided as-is for educational and personal use.
