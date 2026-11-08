# Museum Scavenger Hunt Guides

Printable, kid-friendly museum guides. Each museum is one JSON file in `data/`; `generate_guide.py` renders it through `template.html` into `output/`. See README.md for the mechanics.

## Curation principles

Priorities, in order:

1. **Cover the most important pieces.** If the museum publishes a highlights/masterpieces trail, copying it directly is fine as long as it meets the other criteria. A "boring" piece belongs if it's important. Repeating artists is fine.
2. **Logical, efficient walking order.** Numbering = route order from where we enter. No unnecessary wandering. Don't order for drama.
3. **Consider crowds and timing.** Keep it simple: if a hotspot is best visited first (e.g. Mona Lisa right after opening), put it first and route from there.

Also:

- **Not just paintings.** Sculpture, antiquities, objects and the building itself count. `artist` / `artist_years` are optional.
- **Engaging for kids.** Plain, lively language. "Did you notice?" items and observation challenges must be doable by looking at the piece in person, not by reading a label.
- **Facts must be accurate.** Check claims against the museum's collection page or another reliable source; skip trivia you can't confirm. Check room/location against the museum's current collection site — galleries move.

## Images

Use openly licensed images, in this order:

1. **Public domain.** Faithful photos of old 2D works (paintings, drawings) on Wikimedia Commons are generally public domain (PD-Art).
2. **Free license (CC0 / CC BY / CC BY-SA)** for 3D works (sculpture, objects, architecture). These are widely available; just pick one with a free license, and credit it if the license requires.
3. Avoid non-free / fair-use files (typically `upload.wikimedia.org/wikipedia/en/...`) and works by artists who died less than ~70 years ago. These are the links that break and can't be freely reproduced.

Prefer `upload.wikimedia.org/wikipedia/commons/...` URLs, and check that each URL loads before generating.
