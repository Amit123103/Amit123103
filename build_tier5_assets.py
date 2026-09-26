import xml.etree.ElementTree as ET

def generate_aurora_tech_badges():
    width = 1200
    height = 220
    
    techs = [
        ("Python", "#00F5FF", "🐍"), ("PyTorch", "#EE4C2C", "🔥"), ("TensorFlow", "#FF6F00", "⚡"), 
        ("AWS", "#FF9900", "☁️"), ("Docker", "#2496ED", "🐳"), ("Kubernetes", "#326CE5", "☸️"), 
        ("FastAPI", "#009688", "🚀"), ("LangChain", "#818CF8", "🦜"), ("React", "#61DAFB", "⚛️"), 
        ("TypeScript", "#3178C6", "🔷"), ("PostgreSQL", "#4169E1", "🐘"), ("Redis", "#DC382D", "⚡")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes chipPulse {{
                0%, 100% {{ filter: drop-shadow(0 0 4px rgba(0, 245, 255, 0.3)); transform: translateY(0px); }}
                50% {{ filter: drop-shadow(0 0 12px rgba(0, 245, 255, 0.7)); transform: translateY(-3px); }}
            }}
            @keyframes scanLineH {{
                0% {{ transform: translateX(-1200px); }}
                100% {{ transform: translateX(1200px); }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .chip-glow {{ animation: chipPulse 3.5s ease-in-out infinite alternate; }}
            .circuit-line {{ stroke: rgba(56, 189, 248, 0.08); stroke-width: 1; }}
        </style>
        
        <linearGradient id="deck-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#0b1226" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="chip-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.85)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.95)" />
        </linearGradient>

        <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#38BDF8" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#deck-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Cyber Circuit Wireframe Background -->
    <g class="circuit-line">
        <line x1="60" y1="40" x2="1140" y2="40" />
        <line x1="60" y1="200" x2="1140" y2="200" />
        <line x1="120" y1="0" x2="120" y2="220" />
        <line x1="600" y1="0" x2="600" y2="220" />
        <line x1="1080" y1="0" x2="1080" y2="220" />
    </g>

    <!-- Header Title -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">CORE TECHNOLOGY &amp; INFRASTRUCTURE ECOSYSTEM</text>
    <rect x="560" y="48" width="80" height="2" fill="url(#neon-cyan)" rx="1" />

    <g transform="translate(60, 75)">
'''
    x = 0
    y = 0
    for name, color, icon in techs:
        w = len(name) * 11 + 52
        if x + w > 1080:
            x = 0
            y += 52
            
        svg += f'''
        <!-- 3D Chip: {name} -->
        <g transform="translate({x}, {y})" class="chip-glow">
            <!-- 3D Pedestal Shadow -->
            <rect x="2" y="4" width="{w}" height="40" rx="10" fill="rgba(0,0,0,0.6)" />
            <!-- Chip Body with 3D Bevel -->
            <rect x="0" y="0" width="{w}" height="40" rx="10" fill="url(#chip-grad)" stroke="{color}" stroke-width="1.2" />
            <!-- Top Neon Accent Line -->
            <rect x="0" y="0" width="{w}" height="2" rx="1" fill="{color}" />
            <!-- Status Node -->
            <circle cx="16" cy="20" r="5" fill="rgba(255,255,255,0.06)" />
            <circle cx="16" cy="20" r="3" fill="{color}" />
            <!-- Label -->
            <text x="{28 + (w-28)/2}" y="25" font-size="13" font-weight="700" fill="#F8FAFC" text-anchor="middle">{name}</text>
        </g>
'''
        x += w + 16

    svg += '''
    </g>
</svg>
'''
    with open("assets/aurora_tech_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_tech_badges.svg")

def validate_svgs():
    ET.parse("assets/aurora_tech_badges.svg")
    print("Tier-5 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_tech_badges()
    validate_svgs()
