import xml.etree.ElementTree as ET

def generate_aurora_radar():
    width = 1200
    height = 360
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .axis-line {{ stroke: rgba(255, 255, 255, 0.1); stroke-width: 1; }}
            .radar-poly {{ fill: rgba(56, 189, 248, 0.15); stroke: #38BDF8; stroke-width: 2; }}
            .dot {{ fill: #38BDF8; filter: drop-shadow(0 0 6px #38BDF8); }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.75)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">ENGINEERING COMPETENCY RADAR</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />

    <g transform="translate(600, 200)">
        <!-- Concentric Pentagon Web Grid -->
        <polygon points="0,-120 114,-37 70,97 -70,97 -114,-37" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1" />
        <polygon points="0,-90 85,-28 53,73 -53,73 -85,-28" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1" />
        <polygon points="0,-60 57,-18 35,48 -35,48 -57,-18" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1" />

        <!-- Axis Lines -->
        <line x1="0" y1="0" x2="0" y2="-120" class="axis-line" />
        <line x1="0" y1="0" x2="114" y2="-37" class="axis-line" />
        <line x1="0" y1="0" x2="70" y2="97" class="axis-line" />
        <line x1="0" y1="0" x2="-70" y2="97" class="axis-line" />
        <line x1="0" y1="0" x2="-114" y2="-37" class="axis-line" />

        <!-- Engineering Competency Polygon Data -->
        <!-- Top: AI/ML (95%), Top-Right: Cloud (90%), Bottom-Right: System Design (92%), Bottom-Left: DevOps (88%), Top-Left: Full Stack (85%) -->
        <polygon points="0,-114 102,-33 64,89 -61,85 -97,-31" class="radar-poly" />

        <!-- Radar Nodes -->
        <circle cx="0" cy="-114" r="4" class="dot" />
        <circle cx="102" cy="-33" r="4" class="dot" />
        <circle cx="64" cy="89" r="4" class="dot" />
        <circle cx="-61" cy="85" r="4" class="dot" />
        <circle cx="-97" cy="-31" r="4" class="dot" />

        <!-- Axis Labels -->
        <text x="0" y="-132" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">AI &amp; LLM Engineering (95%)</text>
        <text x="130" y="-32" font-size="12" font-weight="700" fill="#818CF8" text-anchor="start">Cloud Infra (90%)</text>
        <text x="80" y="115" font-size="12" font-weight="700" fill="#C084FC" text-anchor="start">System Design (92%)</text>
        <text x="-80" y="115" font-size="12" font-weight="700" fill="#34D399" text-anchor="end">DevOps &amp; MLOps (88%)</text>
        <text x="-130" y="-32" font-size="12" font-weight="700" fill="#F472B6" text-anchor="end">Full Stack APIs (85%)</text>
    </g>
</svg>
'''
    with open("assets/aurora_radar.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_radar.svg")

def generate_aurora_contact():
    width = 1200
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .btn-box {{ fill: rgba(30, 41, 59, 0.7); stroke: rgba(56, 189, 248, 0.3); stroke-width: 1; rx: 10; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.8)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">LET'S CONNECT &amp; COLLABORATE</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />

    <g transform="translate(60, 85)">
        <!-- Link 1: LinkedIn -->
        <g transform="translate(0, 0)">
            <rect x="0" y="0" width="240" height="60" class="btn-box" />
            <text x="120" y="35" font-size="14" font-weight="700" fill="#38BDF8" text-anchor="middle">💼 LinkedIn Profile →</text>
        </g>

        <!-- Link 2: GitHub -->
        <g transform="translate(280, 0)">
            <rect x="0" y="0" width="240" height="60" class="btn-box" />
            <text x="120" y="35" font-size="14" font-weight="700" fill="#818CF8" text-anchor="middle">⚡ GitHub Profile →</text>
        </g>

        <!-- Link 3: Email -->
        <g transform="translate(560, 0)">
            <rect x="0" y="0" width="240" height="60" class="btn-box" />
            <text x="120" y="35" font-size="14" font-weight="700" fill="#34D399" text-anchor="middle">✉️ Direct Email →</text>
        </g>

        <!-- Link 4: Schedule Meeting -->
        <g transform="translate(840, 0)">
            <rect x="0" y="0" width="240" height="60" class="btn-box" fill="rgba(56, 189, 248, 0.15)" stroke="#38BDF8" stroke-width="1.5" />
            <text x="120" y="35" font-size="14" font-weight="800" fill="#38BDF8" text-anchor="middle">📅 Book 1-on-1 Call →</text>
        </g>
    </g>
</svg>
'''
    with open("assets/aurora_contact.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_contact.svg")

def validate_svgs():
    ET.parse("assets/aurora_radar.svg")
    ET.parse("assets/aurora_contact.svg")
    print("Tier-2 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_radar()
    generate_aurora_contact()
    validate_svgs()
