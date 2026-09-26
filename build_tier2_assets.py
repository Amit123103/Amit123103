import xml.etree.ElementTree as ET

def generate_aurora_radar():
    width = 1200
    height = 380
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes sweepRadar {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            @keyframes radarPulse {{
                0%, 100% {{ opacity: 0.35; filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.3)); }}
                50% {{ opacity: 0.8; filter: drop-shadow(0 0 16px rgba(0, 245, 255, 0.8)); }}
            }}
            @keyframes pingSonar {{
                0% {{ r: 10px; opacity: 0.9; }}
                100% {{ r: 140px; opacity: 0; }}
            }}

            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .radar-sweep {{ transform-origin: 600px 205px; animation: sweepRadar 6s linear infinite; }}
            .poly-glow {{ animation: radarPulse 3.5s ease-in-out infinite alternate; }}
            .axis-line {{ stroke: rgba(56, 189, 248, 0.15); stroke-width: 1; }}
            .sonar-wave {{ transform-origin: 600px 205px; animation: pingSonar 3s ease-out infinite; }}
        </style>

        <linearGradient id="radar-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="sweep-beam" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0)" />
            <stop offset="70%" stop-color="rgba(0, 245, 255, 0.08)" />
            <stop offset="100%" stop-color="rgba(0, 245, 255, 0.45)" />
        </linearGradient>

        <radialGradient id="poly-fill" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0.35)" />
            <stop offset="80%" stop-color="rgba(129, 140, 248, 0.2)" />
            <stop offset="100%" stop-color="rgba(0, 245, 255, 0.05)" />
        </radialGradient>
    </defs>
    
    <!-- Outer Deck Frame -->
    <rect width="100%" height="100%" fill="url(#radar-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title Bar -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">ENGINEERING COMPETENCY RADAR &amp; SKILL TELEMETRY</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />
    <text x="1150" y="38" font-size="11" fill="#34D399" text-anchor="end">[SCANNER: ACTIVE]</text>

    <g transform="translate(600, 205)">
        <!-- Outer Glowing HUD Circles -->
        <circle cx="0" cy="0" r="145" fill="none" stroke="rgba(56, 189, 248, 0.12)" stroke-width="1.5" stroke-dasharray="8 6" />
        <circle cx="0" cy="0" r="115" fill="none" stroke="rgba(56, 189, 248, 0.18)" stroke-width="1" />
        <circle cx="0" cy="0" r="80" fill="none" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1" stroke-dasharray="4 4" />
        <circle cx="0" cy="0" r="45" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />

        <!-- Concentric Pentagon Web Grid -->
        <polygon points="0,-120 114,-37 70,97 -70,97 -114,-37" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1" />
        <polygon points="0,-90 85,-28 53,73 -53,73 -85,-28" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1" />
        <polygon points="0,-60 57,-18 35,48 -35,48 -57,-18" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1" />

        <!-- Axis Lines -->
        <line x1="0" y1="0" x2="0" y2="-130" class="axis-line" />
        <line x1="0" y1="0" x2="125" y2="-40" class="axis-line" />
        <line x1="0" y1="0" x2="78" y2="108" class="axis-line" />
        <line x1="0" y1="0" x2="-78" y2="108" class="axis-line" />
        <line x1="0" y1="0" x2="-125" y2="-40" class="axis-line" />

        <!-- Animated Rotating 3D Sonar Sweep Beam -->
        <path d="M 0 0 L 0 -140 A 140 140 0 0 1 99 -99 Z" fill="url(#sweep-beam)" class="radar-sweep" />

        <!-- Competency Polygon with Neon Gradient Fill -->
        <polygon points="0,-114 102,-33 64,89 -61,85 -97,-31" fill="url(#poly-fill)" stroke="#00F5FF" stroke-width="2.2" class="poly-glow" />

        <!-- Glowing Nodes -->
        <circle cx="0" cy="-114" r="5" fill="#00F5FF" />
        <circle cx="102" cy="-33" r="5" fill="#818CF8" />
        <circle cx="64" cy="89" r="5" fill="#C084FC" />
        <circle cx="-61" cy="85" r="5" fill="#34D399" />
        <circle cx="-97" cy="-31" r="5" fill="#F59E0B" />

        <!-- Center Node -->
        <circle cx="0" cy="0" r="3" fill="#FFFFFF" />

        <!-- Skill Labels with Badges -->
        <text x="0" y="-138" font-size="12" font-weight="800" fill="#00F5FF" text-anchor="middle">AI &amp; LLM Engineering (95%)</text>
        <text x="140" y="-30" font-size="12" font-weight="800" fill="#818CF8" text-anchor="start">Cloud &amp; Distributed Infra (90%)</text>
        <text x="90" y="125" font-size="12" font-weight="800" fill="#C084FC" text-anchor="start">System Design &amp; Architecture (92%)</text>
        <text x="-90" y="125" font-size="12" font-weight="800" fill="#34D399" text-anchor="end">DevOps &amp; MLOps Pipelines (88%)</text>
        <text x="-140" y="-30" font-size="12" font-weight="800" fill="#F59E0B" text-anchor="end">Full Stack &amp; High-Perf APIs (85%)</text>
    </g>
</svg>
'''
    with open("assets/aurora_radar.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_radar.svg")

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
