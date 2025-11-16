#!/usr/bin/env python3
"""
Museum Guide Generator
Generates a standalone, printable HTML guide from JSON data and a Jinja2 template.
"""

import json
from jinja2 import Template
from pathlib import Path


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
