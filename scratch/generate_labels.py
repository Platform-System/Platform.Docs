import os

labels = [
    ("UI", 30),
    ("Identity Service", 120),
    ("Catalog API", 90),
    ("Ordering Service", 120),
    ("Gateway", 70),
    ("Domain", 60),
    ("Application", 85),
    ("Infrastructure", 110),
    ("Contracts", 80),
    ("BuildingBlocks", 110),
    ("SystemContext", 110),
    ("IaC", 40),
    ("CI-CD", 50),
    ("Docs", 50)
]

output_dir = "e:/My_BE/MicroServiceProject/Platform.Docs/assets/labels"
os.makedirs(output_dir, exist_ok=True)

for name, width in labels:
    filename = name.lower().replace(" ", "_").replace("-", "_") + ".svg"
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20">
  <text x="0" y="15" fill="#ffffff" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="bold">{name}</text>
</svg>"""
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(labels)} SVG labels in {output_dir}")
