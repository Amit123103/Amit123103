import os
import base64
import xml.etree.ElementTree as ET

def generate_aurora_hero():
    width = 1200
    height = 380
    
    # Check if profile image exists to base64 encode or use relative link
    profile_img_src = "assets/profile.jpg"
    if os.path.exists(profile_img_src):
        with open(profile_img_src, "rb") as img_f:
            b64_data = base64.b64encode(img_f.read()).decode("utf-8")
            img_href = f"data:image/jpeg;base64,{b64_data}"
    else:
        img_href = profile_img_src

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .glow-cyan {{ filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.7)); }}
            .glow-avatar {{ filter: drop-shadow(0 0 16px rgba(56, 189, 248, 0.4)); }}
            
            .pulse-ring {{ animation: pulse 4s ease-in-out infinite alternate; transform-origin: center; }}
            @keyframes pulse {{ 0% {{ opacity: 0.4; transform: scale(0.98); }} 100% {{ opacity: 0.8; transform: scale(1.02); }} }}
        </style>
        
        <radialGradient id="aurora-bg" cx="50%" cy="30%" r="85%">
            <stop offset="0%" stop-color="#0f172a" />
            <stop offset="50%" stop-color="#090d16" />
            <stop offset="100%" stop-color="#030712" />
        </radialGradient>
        
        <linearGradient id="aurora-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#38BDF8" />
            <stop offset="50%" stop-color="#818CF8" />
            <stop offset="100%" stop-color="#C084FC" />
        </linearGradient>

        <pattern id="grid-dots" width="30" height="30" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1" fill="rgba(255, 255, 255, 0.05)" />
        </pattern>

        <clipPath id="avatar-clip">
            <circle cx="600" cy="85" r="48" />
        </clipPath>
    </defs>
    
    <!-- Base Background Color & Dots -->
    <rect width="100%" height="100%" fill="url(#aurora-bg)" rx="16" />
    <rect width="100%" height="100%" fill="url(#grid-dots)" rx="16" />

    <!-- Subtle Background Photo Layer -->
    <image href="{img_href}" x="0" y="0" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" opacity="0.18" />
    <rect width="100%" height="100%" fill="url(#aurora-bg)" opacity="0.75" rx="16" />

    <!-- Ambient Glow Rings in Background -->
    <g class="pulse-ring">
        <circle cx="600" cy="190" r="150" fill="none" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1" stroke-dasharray="8 6" />
        <circle cx="600" cy="190" r="200" fill="none" stroke="rgba(129, 140, 248, 0.1)" stroke-width="1" />
    </g>

    <!-- Circular Profile Photo Avatar Header -->
    <g class="glow-avatar">
        <circle cx="600" cy="85" r="52" fill="none" stroke="url(#aurora-grad)" stroke-width="3" />
        <image href="{img_href}" x="552" y="37" width="96" height="96" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />
    </g>

    <!-- Status Pill Badge -->
    <g transform="translate(600, 155)">
        <rect x="-140" y="0" width="280" height="28" rx="14" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1" />
        <circle cx="-115" cy="14" r="4" fill="#38BDF8" class="glow-cyan" />
        <text x="5" y="18" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="1.5" fill="#38BDF8">AI ENGINEER &amp; CLOUD ARCHITECT</text>
    </g>

    <!-- Main Title -->
    <text x="600" y="225" font-size="42" font-weight="900" text-anchor="middle" letter-spacing="4" fill="url(#aurora-grad)">AMIT KUMAR</text>

    <!-- Subtitle -->
    <text x="600" y="262" font-size="15" font-weight="400" text-anchor="middle" fill="#94A3B8" letter-spacing="0.5">Building Intelligent AI Systems, Agentic Workflows &amp; Scalable Cloud Infrastructure</text>

    <!-- Bottom Stat Badges (Centered) -->
    <g transform="translate(600, 320)">
        <!-- Badge 1: Location -->
        <g transform="translate(-230, 0)">
            <rect x="0" y="0" width="140" height="32" rx="16" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1" />
            <text x="70" y="20" font-size="12" font-weight="600" text-anchor="middle" fill="#E2E8F0">📍 India (UTC+5:30)</text>
        </g>
        
        <!-- Badge 2: Status -->
        <g transform="translate(-75, 0)">
            <rect x="0" y="0" width="150" height="32" rx="16" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1" />
            <circle cx="18" cy="16" r="4" fill="#34D399" />
            <text x="82" y="20" font-size="12" font-weight="600" text-anchor="middle" fill="#34D399">Available for Hiring</text>
        </g>

        <!-- Badge 3: Impact -->
        <g transform="translate(90, 0)">
            <rect x="0" y="0" width="140" height="32" rx="16" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(192, 132, 252, 0.35)" stroke-width="1" />
            <text x="70" y="20" font-size="12" font-weight="600" text-anchor="middle" fill="#C084FC">⚡ 2.5k+ Commits</text>
        </g>
    </g>
</svg>
'''
    with open("assets/aurora_hero_v2.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    # Also overwrite aurora_hero.svg
    with open("assets/aurora_hero.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_hero_v2.svg with photo integration!")

def generate_aurora_about():
    width = 1200
    height = 280
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .card {{ fill: rgba(15, 23, 42, 0.7); stroke: rgba(255, 255, 255, 0.08); stroke-width: 1; rx: 12; }}
        </style>
        
        <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.5)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.8)" />
        </linearGradient>
    </defs>
    
    <!-- Title -->
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">CORE FOCUS &amp; CAPABILITIES</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />
    
    <!-- 3 Clean Cards -->
    <!-- Card 1 -->
    <g transform="translate(60, 80)">
        <rect x="0" y="0" width="340" height="165" fill="url(#card-grad)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" rx="12" />
        <rect x="0" y="0" width="340" height="3" fill="#38BDF8" rx="1.5" />
        <text x="24" y="36" font-size="15" font-weight="700" fill="#38BDF8">🤖 AI &amp; LLM Engineering</text>
        <text x="24" y="68" font-size="13" fill="#94A3B8">• Agentic Workflows &amp; Multi-Agent Systems</text>
        <text x="24" y="94" font-size="13" fill="#94A3B8">• Production RAG &amp; Vector Databases</text>
        <text x="24" y="120" font-size="13" fill="#94A3B8">• Fine-Tuning Open Source Models</text>
    </g>
    
    <!-- Card 2 -->
    <g transform="translate(430, 80)">
        <rect x="0" y="0" width="340" height="165" fill="url(#card-grad)" stroke="rgba(129, 140, 248, 0.25)" stroke-width="1" rx="12" />
        <rect x="0" y="0" width="340" height="3" fill="#818CF8" rx="1.5" />
        <text x="24" y="36" font-size="15" font-weight="700" fill="#818CF8">☁️ Cloud &amp; Infrastructure</text>
        <text x="24" y="68" font-size="13" fill="#94A3B8">• High-Scale AWS / GCP Architecture</text>
        <text x="24" y="94" font-size="13" fill="#94A3B8">• Docker &amp; Kubernetes Orchestration</text>
        <text x="24" y="120" font-size="13" fill="#94A3B8">• Automated CI/CD &amp; MLOps Pipelines</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(800, 80)">
        <rect x="0" y="0" width="340" height="165" fill="url(#card-grad)" stroke="rgba(192, 132, 252, 0.25)" stroke-width="1" rx="12" />
        <rect x="0" y="0" width="340" height="3" fill="#C084FC" rx="1.5" />
        <text x="24" y="36" font-size="15" font-weight="700" fill="#C084FC">⚡ Full-Stack &amp; Performance</text>
        <text x="24" y="68" font-size="13" fill="#94A3B8">• FastAPI &amp; Node.js High-Throughput APIs</text>
        <text x="24" y="94" font-size="13" fill="#94A3B8">• React &amp; Next.js Modern Interfaces</text>
        <text x="24" y="120" font-size="13" fill="#94A3B8">• PostgreSQL &amp; Redis Caching Layers</text>
    </g>
</svg>
'''
    with open("assets/aurora_about.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_about.svg")

def generate_aurora_skills():
    width = 1200
    height = 420
    
    categories = [
        ("AI &amp; DEEP LEARNING", ["Python", "PyTorch", "TensorFlow", "OpenCV", "LangChain", "LLMs", "RAG Systems", "OpenAI", "Vector DBs"]),
        ("CLOUD &amp; DEVOPS", ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Linux", "Nginx", "PostgreSQL", "Redis"]),
        ("FULL-STACK &amp; WEB", ["FastAPI", "Node.js", "React", "TypeScript", "Next.js", "GraphQL", "REST APIs", "TailwindCSS", "Git"])
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .pill {{ fill: rgba(30, 41, 59, 0.6); stroke: rgba(255, 255, 255, 0.1); stroke-width: 1; rx: 16; }}
        </style>
    </defs>
    
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">TECHNICAL EXPERTISE MATRIX</text>
    <rect x="580" y="48" width="40" height="2" fill="#38BDF8" />
'''

    y_offset = 85
    for title, skills in categories:
        svg += f'''
        <text x="80" y="{y_offset}" font-size="14" font-weight="700" fill="#818CF8" letter-spacing="1.5">{title}</text>
        <line x1="80" y1="{y_offset + 10}" x2="1120" y2="{y_offset + 10}" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />
'''
        x = 80
        y = y_offset + 26
        
        for skill in skills:
            w = len(skill) * 9 + 36
            if x + w > 1120:
                x = 80
                y += 42
                
            svg += f'''
            <g transform="translate({x}, {y})">
                <rect x="0" y="0" width="{w}" height="32" class="pill" />
                <circle cx="15" cy="16" r="3" fill="#38BDF8" />
                <text x="{15 + (w-15)/2}" y="20" font-size="12" font-weight="600" text-anchor="middle" fill="#E2E8F0">{skill}</text>
            </g>
'''
            x += w + 12
        y_offset = y + 60

    svg += '</svg>'
    with open("assets/aurora_skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_skills.svg")

def generate_aurora_projects():
    width = 1200
    height = 360
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .proj-card {{ fill: rgba(15, 23, 42, 0.7); stroke: rgba(255, 255, 255, 0.08); stroke-width: 1; rx: 12; }}
            .tag {{ fill: rgba(56, 189, 248, 0.1); stroke: rgba(56, 189, 248, 0.3); stroke-width: 1; rx: 8; }}
        </style>
        
        <linearGradient id="proj-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.5)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.8)" />
        </linearGradient>
    </defs>
    
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">FEATURED PROJECTS</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />
'''

    projects = [
        ("AI Vision System", "Real-time object tracking &amp; computer vision pipeline.", ["PyTorch", "OpenCV"], 60),
        ("Quantum RAG Engine", "High-performance generative retrieval AI framework.", ["LangChain", "FastAPI"], 440),
        ("Cloud MLOps Pipeline", "Automated deployment &amp; monitoring architecture.", ["AWS", "Docker"], 820)
    ]
    
    for title, desc, tags, x in projects:
        svg += f'''
    <g transform="translate({x}, 80)">
        <rect x="0" y="0" width="320" height="240" fill="url(#proj-grad)" class="proj-card" />
        <rect x="0" y="0" width="320" height="3" fill="#38BDF8" rx="1.5" />
        
        <text x="20" y="40" font-size="16" font-weight="700" fill="#F8FAFC">{title}</text>
        <text x="20" y="68" font-size="13" fill="#94A3B8">{desc}</text>
        
        <!-- Tags -->
        <g transform="translate(20, 120)">
            <rect x="0" y="0" width="75" height="24" class="tag" />
            <text x="37" y="16" font-size="11" font-weight="600" fill="#38BDF8" text-anchor="middle">{tags[0]}</text>
            
            <rect x="85" y="0" width="75" height="24" class="tag" />
            <text x="122" y="16" font-size="11" font-weight="600" fill="#38BDF8" text-anchor="middle">{tags[1]}</text>
        </g>
        
        <!-- Action Button -->
        <g transform="translate(20, 175)">
            <rect x="0" y="0" width="280" height="36" rx="8" fill="rgba(56, 189, 248, 0.1)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1" />
            <text x="140" y="22" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">View Repository →</text>
        </g>
    </g>
'''

    svg += '</svg>'
    with open("assets/aurora_projects.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_projects.svg")

def generate_aurora_footer():
    width = 1200
    height = 100
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.6)" rx="12" stroke="rgba(255, 255, 255, 0.08)" />
    
    <text x="600" y="42" font-size="14" font-weight="600" text-anchor="middle" fill="#94A3B8">"Building scalable AI systems and cloud architecture, one commit at a time."</text>
    <text x="600" y="70" font-size="12" fill="#64748B" text-anchor="middle">© 2026 AMIT KUMAR • DESIGNED FOR PERFORMANCE &amp; ELEGANCE</text>
</svg>
'''
    with open("assets/aurora_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_footer.svg")

def validate_all_svgs():
    files = ["assets/aurora_hero_v2.svg", "assets/aurora_about.svg", "assets/aurora_skills.svg", "assets/aurora_projects.svg", "assets/aurora_footer.svg"]
    for file in files:
        ET.parse(file)
    print("ALL AURORA SVGs PASS XML VALIDATION PERFECTLY!")

if __name__ == "__main__":
    generate_aurora_hero()
    generate_aurora_about()
    generate_aurora_skills()
    generate_aurora_projects()
    generate_aurora_footer()
    validate_all_svgs()
