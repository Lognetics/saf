# -*- coding: utf-8 -*-
"""Small inline-SVG graphics: the footprint map and the horizontal roadmap."""

from .layout import icon, esc

# Simplified outline of Nigeria as (longitude, latitude). Schematic, not survey-grade:
# it exists to show where the Foundation works, not to draw the border.
_OUTLINE = [
    (3.6, 11.7), (3.9, 12.6), (4.4, 13.3), (5.5, 13.7), (6.9, 13.4), (8.6, 13.7), (10.2, 13.2),
    (11.6, 13.5), (13.0, 13.7), (13.9, 13.1), (14.6, 12.5), (14.0, 11.7), (14.6, 11.0),
    (13.9, 10.4), (13.4, 9.4), (12.8, 8.6), (12.2, 7.9), (11.4, 7.2), (10.6, 6.9), (9.7, 6.6),
    (9.0, 5.9), (8.8, 5.1), (8.5, 4.6), (7.7, 4.4), (6.8, 4.3), (6.0, 4.3), (5.4, 5.5),
    (4.4, 6.2), (3.4, 6.4), (2.7, 6.4), (2.75, 7.4), (3.1, 8.9), (3.7, 9.9), (3.5, 11.0),
]

_SCALE = 34
_X0, _Y0 = 2.5, 14.0


def _xy(lon, lat):
    return round((lon - _X0) * _SCALE + 14, 1), round((_Y0 - lat) * _SCALE + 14, 1)


def nigeria_map():
    pts = " ".join(f"{x},{y}" for x, y in (_xy(*p) for p in _OUTLINE))
    fct = _xy(7.4, 9.1)
    keffi = _xy(7.95, 8.8)
    nnewi = _xy(6.9, 6.0)
    ogun = _xy(3.4, 7.1)
    net = {"Lagos": _xy(3.45, 6.5), "Ibadan": _xy(3.95, 7.55), "Port Harcourt": _xy(7.0, 4.8)}

    def pin(pt, cls):
        x, y = pt
        return (f'<g class="map__pin map__pin--{cls}" transform="translate({x} {y})">'
                f'<circle r="11" class="map__halo"/><circle r="5.5" class="map__dot"/></g>')

    def label(pt, text, dx, dy, anchor="start", cls=""):
        x, y = pt
        return (f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" class="map__label {cls}">'
                f'{esc(text)}</text>')

    w = round((14.9 - _X0) * _SCALE + 28)
    h = round((_Y0 - 4.0) * _SCALE + 28)
    net_pins = "".join(pin(p, "net") for p in net.values())
    net_labels = "".join([
        label(net["Lagos"], "Lagos", -12, 5, "end", "map__label--sm"),
        label(net["Ibadan"], "Ibadan", -12, 4, "end", "map__label--sm"),
        label(net["Port Harcourt"], "Port Harcourt", 12, 5, "start", "map__label--sm"),
    ])
    return f'''
<figure class="map">
  <svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="map-t map-d" class="map__svg">
    <title id="map-t">Where Synia Aid Foundation works in Nigeria</title>
    <desc id="map-d">A simplified map of Nigeria marking the Federal Capital Territory and Nasarawa State
      as the main corridor, Anambra and Ogun as outreach locations, and Lagos, Rivers and Oyo as the
      supporter and volunteer network.</desc>
    <polygon points="{pts}" class="map__land"/>
    <path d="M{fct[0]} {fct[1]} Q{(fct[0] + keffi[0]) / 2} {fct[1] - 16} {keffi[0]} {keffi[1]}" class="map__corridor"/>
    {net_pins}
    {pin(ogun, "out")}{pin(nnewi, "out")}
    {pin(fct, "main")}{pin(keffi, "main")}
    {label(fct, "FCT (Abuja)", -14, 5, "end", "map__label--main")}
    {label(keffi, "Nasarawa (Keffi)", 14, 5, "start", "map__label--main")}
    {label(nnewi, "Anambra (Nnewi)", 14, 5)}
    {label(ogun, "Ogun", 14, 5)}
    {net_labels}
  </svg>
  <figcaption class="map__caption">Schematic map, not to scale.</figcaption>
</figure>'''


def map_legend():
    items = [
        ("main", "Primary corridor", "Federal Capital Territory and Nasarawa (Keffi): head office, principal community base and the FCT resettlement corridor."),
        ("out", "Outreach locations", "Anambra (Nnewi, where the Foundation began) and Ogun."),
        ("net", "Supporter and volunteer network", "Lagos, Rivers (Port Harcourt) and Oyo (Ibadan)."),
    ]
    lis = "".join(
        f'<li><span class="map__key map__key--{k}" aria-hidden="true"></span>'
        f'<span><strong>{esc(t)}</strong><br><span class="small">{esc(b)}</span></span></li>'
        for k, t, b in items)
    return f'<ul class="map__legend">{lis}</ul>'


def roadmap_graphic(phases):
    """Horizontal three-block roadmap. phases: (phase, period, items, test)."""
    icons = ["house", "target", "globe"]
    blocks = []
    for i, (phase, period, items, test) in enumerate(phases):
        lis = "".join(f"<li>{esc(x)}</li>" for x in items)
        blocks.append(f'''
<li class="road__block">
  <span class="road__icon">{icon(icons[i % len(icons)], "", 26)}</span>
  <p class="road__phase">{esc(phase)}</p>
  <h3 class="road__period">{esc(period)}</h3>
  <details class="road__more"><summary>What happens in this phase</summary>
    <ul>{lis}</ul>
    <p class="road__test"><strong>Test of completion.</strong> {esc(test)}</p>
  </details>
</li>''')
    return f'<ol class="road">{"".join(blocks)}</ol>'


def checklist_graphic(steps):
    """Horizontal sequential gate: (title, body) steps with icons."""
    icons = ["doc", "users-check", "chart", "scale", "shield"]
    items = []
    for i, (t, b) in enumerate(steps):
        items.append(f'''
<li class="gate__step">
  <span class="gate__icon">{icon(icons[i % len(icons)], "", 24)}<span class="gate__n">{i + 1}</span></span>
  <h3 class="gate__title">{esc(t)}</h3>
  <details class="gate__more"><summary>Detail</summary><p>{esc(b)}</p></details>
</li>''')
    return f'<ol class="gate">{"".join(items)}</ol>'
