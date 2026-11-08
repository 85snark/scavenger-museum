#!/usr/bin/env python3
"""
Museum Guide Generator
Generates a standalone, printable HTML guide from JSON data and a Jinja2 template.
"""

import json
from html import escape
from jinja2 import Template
from pathlib import Path


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Museum Guides</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; margin: 0;
               background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; color: #1f2937; }}
        main {{ max-width: 560px; margin: 0 auto; padding: 2.5rem 1rem; }}
        h1 {{ color: white; font-size: 2.2rem; margin: 0 0 1.5rem; }}
        a {{ display: block; background: white; border-radius: 10px; padding: 1rem 1.25rem; margin-bottom: 0.75rem;
            text-decoration: none; color: inherit; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
        a strong {{ display: block; font-size: 1.2rem; color: #8B0000; }}
        a span {{ font-size: 0.9rem; color: #6b7280; }}
    </style>
</head>
<body>
    <main>
        <h1>Museum Guides</h1>
{links}
    </main>
</body>
</html>
"""


def write_index(output_dir='output', data_dir='data'):
    """Write output/index.html linking every guide that has both a JSON file and generated HTML."""
    links = []
    for json_path in sorted(Path(data_dir).glob('*.json')):
        html_name = f'{json_path.stem}.html'
        if not (Path(output_dir) / html_name).exists():
            continue
        data = load_json(json_path)
        count = len(data['artworks'])
        links.append(
            f'        <a href="{escape(html_name)}"><strong>{escape(data["museum_name"])}</strong>'
            f'<span>{escape(data["guide_title"])} · {count} stops</span></a>'
        )
    index_path = Path(output_dir) / 'index.html'
    index_path.write_text(INDEX_TEMPLATE.format(links='\n'.join(links)), encoding='utf-8')
    return index_path


def load_json(json_path):
    """Load artwork data from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template(template_path):
    """Load HTML template."""
    with open(template_path, 'r', encoding='utf-8') as f:
        return Template(f.read())


def generate_guide(json_path='data/prado_artworks.json', template_path='template.html', output_path=None):
    """
    Generate the museum guide HTML file.

    Args:
        json_path: Path to the JSON data file
        template_path: Path to the Jinja2 template file
        output_path: Path for the generated HTML file
    """
    print("🎨 Museum Guide Generator")
    print("=" * 50)

    # Auto-generate output path if not specified
    if output_path is None:
        json_filename = Path(json_path).stem  # Get filename without extension
        output_path = f'output/{json_filename}.html'

    # Load data
    print(f"📖 Loading artwork data from {json_path}...")
    data = load_json(json_path)

    # Load template
    print(f"📄 Loading template from {template_path}...")
    template = load_template(template_path)

    # Render HTML
    print(f"✨ Rendering HTML...")
    html_output = template.render(
        museum_name=data['museum_name'],
        guide_title=data['guide_title'],
        artworks=data['artworks']
    )

    # Save output
    print(f"💾 Saving to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)

    # Refresh the guide list (only for guides written to the default output/ folder)
    if Path(output_path).parent == Path('output'):
        index_path = write_index()
        print(f"🗂  Updated guide list: {index_path}")

    # Summary
    print("=" * 50)
    print(f"✅ Success! Generated guide with {len(data['artworks'])} artworks")
    print(f"📍 Output file: {Path(output_path).absolute()}")
    print(f"\n💡 Tips:")
    print(f"   • Open {output_path} in your browser")
    print(f"   • Press Ctrl+P (Cmd+P on Mac) to print")
    print(f"   • Each artwork will be on its own page")
    print(f"   • Images link to museum sources on click")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate a printable museum guide from JSON data'
    )
    parser.add_argument(
        '--json',
        default='data/prado_artworks.json',
        help='Path to JSON data file (default: data/prado_artworks.json)'
    )
    parser.add_argument(
        '--template',
        default='template.html',
        help='Path to template file (default: template.html)'
    )
    parser.add_argument(
        '--output',
        default=None,
        help='Output HTML file path (default: output/<json_filename>.html)'
    )

    args = parser.parse_args()

    try:
        generate_guide(
            json_path=args.json,
            template_path=args.template,
            output_path=args.output
        )
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print(f"   Make sure {args.json} and {args.template} exist in the current directory")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {args.json}")
        print(f"   {e}")
        exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        exit(1)


if __name__ == '__main__':
    main()
