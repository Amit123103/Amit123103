import xml.etree.ElementTree as ET

def generate_aurora_tech_badges():
    width = 1200
    height = 200
    
    techs = [
        ("Python", "#38BDF8"), ("PyTorch", "#EE4C2C"), ("TensorFlow", "#FF6F00"), 
        ("AWS", "#FF9900"), ("Docker", "#2496ED"), ("Kubernetes", "#326CE5"), 
        ("FastAPI", "#009688"), ("LangChain", "#818CF8"), ("React", "#61DAFB"), 
        ("TypeScript", "#3178C6"), ("PostgreSQL", "#4169E1"), ("Redis", "#DC382D")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .tech-pill {{ fill: rgba(30, 41, 59, 0.7); stroke-width: 1; rx: 12; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.75)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">CORE TECHNOLOGY &amp; INFRASTRUCTURE ECOSYSTEM</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />

    <g transform="translate(60, 80)">
'''
    x = 0
    y = 0
    for name, color in techs:
        w = len(name) * 11 + 36
        if x + w > 1080:
            x = 0
            y += 48
            
        svg += f'''
        <g transform="translate({x}, {y})">
            <rect x="0" y="0" width="{w}" height="36" class="tech-pill" stroke="{color}" opacity="0.9" />
            <circle cx="16" cy="18" r="4" fill="{color}" />
            <text x="{16 + (w-16)/2}" y="23" font-size="13" font-weight="700" fill="#F8FAFC" text-anchor="middle">{name}</text>
        </g>
'''
        x += w + 14

    svg += '''
    </g>
</svg>
'''
    with open("assets/aurora_tech_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_tech_badges.svg")

def validate_svgs():
    ET.parse("assets/aurora_tech_badges.svg")
    print("Tier-5 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_tech_badges()
    validate_svgs()
