import xml.etree.ElementTree as ET

def generate_aurora_routine():
    width = 1200
    height = 240
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .block {{ fill: rgba(30, 41, 59, 0.6); rx: 6; }}
            .active-ai {{ fill: #38BDF8; rx: 6; }}
            .active-cloud {{ fill: #818CF8; rx: 6; }}
            .active-oss {{ fill: #C084FC; rx: 6; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.75)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">DAILY ENGINEERING ROUTINE &amp; PRODUCTIVITY WINDOWS</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />

    <g transform="translate(60, 90)">
        <!-- 24 Hour Bar -->
        <!-- Hours 09:00 - 13:00 : AI Model Training & RAG -->
        <rect x="0" y="0" width="320" height="40" class="active-ai" />
        <text x="160" y="25" font-size="12" font-weight="700" fill="#030712" text-anchor="middle">🧠 09:00 - 13:00 | AI &amp; RAG Architecture</text>

        <!-- Hours 14:00 - 18:00 : Cloud Infra & DevOps -->
        <rect x="340" y="0" width="340" height="40" class="active-cloud" />
        <text x="510" y="25" font-size="12" font-weight="700" fill="#030712" text-anchor="middle">☁️ 14:00 - 18:00 | AWS &amp; Microservices</text>

        <!-- Hours 19:00 - 22:00 : Open Source R&D -->
        <rect x="700" y="0" width="380" height="40" class="active-oss" />
        <text x="890" y="25" font-size="12" font-weight="700" fill="#030712" text-anchor="middle">⚡ 19:00 - 22:00 | Open Source &amp; Experimentation</text>
    </g>

    <!-- Legend -->
    <g transform="translate(600, 185)">
        <circle cx="-220" cy="0" r="5" fill="#38BDF8" />
        <text x="-210" y="4" font-size="12" fill="#94A3B8">Deep AI Work</text>

        <circle cx="-60" cy="0" r="5" fill="#818CF8" />
        <text x="-50" y="4" font-size="12" fill="#94A3B8">Cloud Systems</text>

        <circle cx="100" cy="0" r="5" fill="#C084FC" />
        <text x="110" y="4" font-size="12" fill="#94A3B8">Open Source R&amp;D</text>
    </g>
</svg>
'''
    with open("assets/aurora_routine.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_routine.svg")

def generate_aurora_badges():
    width = 1200
    height = 180
    
    badges = [
        ("AWS ARCHITECT", "#38BDF8", "☁️"),
        ("PYTORCH SPECIALIST", "#818CF8", "🔥"),
        ("DOCKER &amp; K8S EXPERT", "#C084FC", "🐳"),
        ("TOP 5% CONTRIBUTOR", "#34D399", "🏆")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .badge-box {{ fill: rgba(15, 23, 42, 0.8); stroke-width: 1; rx: 12; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.7)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">ENGINEERING CERTIFICATIONS &amp; HONORS</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />

    <g transform="translate(60, 80)">
'''
    x = 0
    for name, color, icon in badges:
        svg += f'''
        <g transform="translate({x}, 0)">
            <rect x="0" y="0" width="240" height="65" class="badge-box" stroke="{color}" opacity="0.9" />
            <text x="120" y="28" font-size="18" text-anchor="middle">{icon}</text>
            <text x="120" y="48" font-size="12" font-weight="800" fill="{color}" text-anchor="middle" letter-spacing="1">{name}</text>
        </g>
'''
        x += 280

    svg += '''
    </g>
</svg>
'''
    with open("assets/aurora_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_badges.svg")

def validate_svgs():
    ET.parse("assets/aurora_routine.svg")
    ET.parse("assets/aurora_badges.svg")
    print("Tier-3 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_routine()
    generate_aurora_badges()
    validate_svgs()
