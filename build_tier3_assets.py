import xml.etree.ElementTree as ET

def generate_aurora_routine():
    width = 1200
    height = 240
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes tubeGlow {{
                0%, 100% {{ filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.4)); }}
                50% {{ filter: drop-shadow(0 0 16px rgba(0, 245, 255, 0.85)); }}
            }}
            @keyframes timeSweep {{
                0% {{ transform: translateX(-350px); opacity: 0; }}
                50% {{ opacity: 0.6; }}
                100% {{ transform: translateX(1100px); opacity: 0; }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .tube-pulse {{ animation: tubeGlow 3.5s ease-in-out infinite alternate; }}
            .time-shimmer {{ animation: timeSweep 4s ease-in-out infinite; }}
        </style>

        <linearGradient id="routine-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="ai-tube" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#0284C7" />
        </linearGradient>

        <linearGradient id="cloud-tube" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#818CF8" />
            <stop offset="100%" stop-color="#4F46E5" />
        </linearGradient>

        <linearGradient id="oss-tube" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#C084FC" />
            <stop offset="100%" stop-color="#9333EA" />
        </linearGradient>

        <linearGradient id="sweep-glass" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0)" />
            <stop offset="50%" stop-color="rgba(255, 255, 255, 0.45)" />
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0)" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#routine-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">DAILY ENGINEERING ROUTINE &amp; PRODUCTIVITY WINDOWS</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />

    <g transform="translate(60, 80)">
        <!-- 3D Chrono Timeline Base Track -->
        <rect x="0" y="0" width="1080" height="52" rx="14" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1.5" />
        
        <!-- Slot 1: AI Model Training & RAG (x: 4, width: 340) -->
        <g transform="translate(4, 4)" class="tube-pulse">
            <rect x="0" y="0" width="340" height="44" rx="11" fill="url(#ai-tube)" />
            <rect x="0" y="0" width="340" height="2" rx="1" fill="#FFFFFF" opacity="0.4" />
            <text x="170" y="27" font-size="13" font-weight="800" fill="#030712" text-anchor="middle" letter-spacing="0.5">🧠 09:00 - 13:00 | AI &amp; RAG Architecture</text>
        </g>

        <!-- Slot 2: Cloud Infra & DevOps (x: 352, width: 350) -->
        <g transform="translate(352, 4)" class="tube-pulse">
            <rect x="0" y="0" width="350" height="44" rx="11" fill="url(#cloud-tube)" />
            <rect x="0" y="0" width="350" height="2" rx="1" fill="#FFFFFF" opacity="0.4" />
            <text x="175" y="27" font-size="13" font-weight="800" fill="#030712" text-anchor="middle" letter-spacing="0.5">☁️ 14:00 - 18:00 | AWS &amp; MLOps Pipelines</text>
        </g>

        <!-- Slot 3: Open Source R&D (x: 710, width: 366) -->
        <g transform="translate(710, 4)" class="tube-pulse">
            <rect x="0" y="0" width="366" height="44" rx="11" fill="url(#oss-tube)" />
            <rect x="0" y="0" width="366" height="2" rx="1" fill="#FFFFFF" opacity="0.4" />
            <text x="183" y="27" font-size="13" font-weight="800" fill="#030712" text-anchor="middle" letter-spacing="0.5">⚡ 19:00 - 22:00 | Open Source &amp; Kernel R&amp;D</text>
        </g>
    </g>

    <!-- Holographic Indicator Legend -->
    <g transform="translate(600, 185)">
        <circle cx="-250" cy="0" r="6" fill="#00F5FF" />
        <text x="-238" y="4" font-size="12" font-weight="700" fill="#00F5FF">Deep AI Architecture</text>

        <circle cx="-30" cy="0" r="6" fill="#818CF8" />
        <text x="-18" y="4" font-size="12" font-weight="700" fill="#818CF8">Cloud Systems &amp; MLOps</text>

        <circle cx="190" cy="0" r="6" fill="#C084FC" />
        <text x="202" y="4" font-size="12" font-weight="700" fill="#C084FC">Open Source &amp; Core R&amp;D</text>
    </g>
</svg>
'''
    with open("assets/aurora_routine.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_routine.svg")

def generate_aurora_badges():
    width = 1200
    height = 200
    
    badges = [
        ("AWS CLOUD ARCHITECT", "Serverless &amp; Cloud Infra", "#38BDF8", "#0EA5E9", "☁️", 0),
        ("PYTORCH &amp; LLMs", "Deep Learning &amp; GenAI", "#818CF8", "#6366F1", "🔥", 280),
        ("DOCKER &amp; K8S EXPERT", "Containerized MLOps", "#C084FC", "#A855F7", "🐳", 560),
        ("TOP 5% CONTRIBUTOR", "Open Source Architecture", "#34D399", "#10B981", "🏆", 840)
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes levitate {{
                0%, 100% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-6px); }}
            }}
            @keyframes badgeGlow {{
                0%, 100% {{ opacity: 0.4; filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.3)); }}
                50% {{ opacity: 0.85; filter: drop-shadow(0 0 18px rgba(56, 189, 248, 0.8)); }}
            }}
            @keyframes shimmer {{
                0% {{ transform: translateX(-150px) skewX(-20deg); opacity: 0; }}
                50% {{ opacity: 0.6; }}
                100% {{ transform: translateX(350px) skewX(-20deg); opacity: 0; }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .levitate-icon {{ animation: levitate 3.5s ease-in-out infinite alternate; }}
            .shimmer-bar {{ animation: shimmer 4s ease-in-out infinite; }}
            .badge-glow {{ animation: badgeGlow 4s ease-in-out infinite alternate; }}
        </style>

        <linearGradient id="bg-deck" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#0b1226" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="shimmer-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0)" />
            <stop offset="50%" stop-color="rgba(255, 255, 255, 0.4)" />
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0)" />
        </linearGradient>
    </defs>
    
    <!-- Outer Deck Background -->
    <rect width="100%" height="100%" fill="url(#bg-deck)" rx="16" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />
    
    <!-- Header Title with 3D Cyber Badges -->
    <text x="600" y="36" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">ENGINEERING HONORS &amp; CLOUD CERTIFICATIONS</text>
    <rect x="570" y="46" width="60" height="2" fill="#818CF8" rx="1" />

    <g transform="translate(40, 75)">
'''
    for name, sub, c1, c2, icon, x in badges:
        svg += f'''
        <!-- 3D Holographic Card ({name}) -->
        <g transform="translate({x}, 0)">
            <!-- 3D Drop Shadow Pedestal -->
            <rect x="4" y="6" width="260" height="96" rx="14" fill="rgba(0,0,0,0.6)" />
            
            <!-- Card Body with Glassmorphic Gradient -->
            <rect x="0" y="0" width="260" height="96" rx="14" fill="rgba(15, 23, 42, 0.85)" stroke="{c1}" stroke-width="1.2" opacity="0.95" />
            
            <!-- Top Gradient Accent Strip -->
            <rect x="0" y="0" width="260" height="3" rx="1.5" fill="{c1}" />
            
            <!-- Shimmer Light Sweep Effect (Clipped) -->
            <g clip-path="url(#badge-clip)">
                <rect x="0" y="0" width="40" height="96" fill="url(#shimmer-grad)" class="shimmer-bar" />
            </g>

            <!-- Levitating 3D Emoji Icon & Glow -->
            <g transform="translate(30, 48)" class="levitate-icon">
                <circle cx="0" cy="0" r="22" fill="rgba(255,255,255,0.04)" stroke="{c1}" stroke-width="1" />
                <circle cx="0" cy="0" r="15" fill="{c1}" opacity="0.15" />
                <text x="0" y="7" font-size="20" text-anchor="middle">{icon}</text>
            </g>
            
            <!-- Text Content -->
            <text x="65" y="42" font-size="12" font-weight="800" fill="#F8FAFC" letter-spacing="0.5">{name}</text>
            <text x="65" y="60" font-size="10.5" font-weight="500" fill="#94A3B8">{sub}</text>
            
            <!-- Verified Indicator Dot -->
            <circle cx="242" cy="16" r="3.5" fill="{c1}" class="badge-glow" />
        </g>
'''

    svg += '''
    </g>
</svg>
'''
    with open("assets/aurora_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_badges.svg")

def validate_svgs():
    ET.parse("assets/aurora_routine.svg")
    ET.parse("assets/aurora_badges.svg")
    print("Tier-3 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_routine()
    generate_aurora_badges()
    validate_svgs()
