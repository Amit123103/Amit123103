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
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes podGlow {{
                0%, 100% {{ filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.3)); transform: translateY(0px); }}
                50% {{ filter: drop-shadow(0 0 16px rgba(0, 245, 255, 0.8)); transform: translateY(-4px); }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .pod-anim {{ animation: podGlow 4s ease-in-out infinite alternate; }}
        </style>
        
        <linearGradient id="about-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="pod-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.85)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.95)" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#about-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">CORE FOCUS &amp; STRATEGIC CAPABILITIES</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />
    
    <!-- 3 3D Holographic Pods -->
    <!-- Pod 1: AI & LLM Engineering -->
    <g transform="translate(60, 75)" class="pod-anim">
        <rect x="4" y="6" width="340" height="195" rx="14" fill="rgba(0,0,0,0.6)" />
        <rect x="0" y="0" width="340" height="195" fill="url(#pod-grad)" stroke="#00F5FF" stroke-width="1.5" rx="14" />
        <rect x="0" y="0" width="340" height="4" fill="#00F5FF" rx="2" />
        
        <circle cx="36" cy="40" r="16" fill="rgba(0, 245, 255, 0.15)" stroke="#00F5FF" stroke-width="1" />
        <text x="36" y="47" font-size="18" text-anchor="middle">🤖</text>
        <text x="66" y="45" font-size="15" font-weight="800" fill="#00F5FF">AI &amp; LLM Engineering</text>
        
        <text x="24" y="86" font-size="12.5" fill="#E2E8F0">✦ Agentic Workflows &amp; Multi-Agent Swarms</text>
        <text x="24" y="114" font-size="12.5" fill="#E2E8F0">✦ Production RAG &amp; Vector Search Optimization</text>
        <text x="24" y="142" font-size="12.5" fill="#E2E8F0">✦ Fine-Tuning Open Source LLMs (Llama 3)</text>
        <text x="24" y="170" font-size="12.5" fill="#94A3B8">✦ Deep Neural Networks &amp; PyTorch Inference</text>
    </g>
    
    <!-- Pod 2: Cloud & Infrastructure -->
    <g transform="translate(430, 75)" class="pod-anim" style="animation-delay: 0.5s;">
        <rect x="4" y="6" width="340" height="195" rx="14" fill="rgba(0,0,0,0.6)" />
        <rect x="0" y="0" width="340" height="195" fill="url(#pod-grad)" stroke="#818CF8" stroke-width="1.5" rx="14" />
        <rect x="0" y="0" width="340" height="4" fill="#818CF8" rx="2" />
        
        <circle cx="36" cy="40" r="16" fill="rgba(129, 140, 248, 0.15)" stroke="#818CF8" stroke-width="1" />
        <text x="36" y="47" font-size="18" text-anchor="middle">☁️</text>
        <text x="66" y="45" font-size="15" font-weight="800" fill="#818CF8">Cloud &amp; MLOps Infrastructure</text>
        
        <text x="24" y="86" font-size="12.5" fill="#E2E8F0">✦ High-Scale AWS Cloud Architecture</text>
        <text x="24" y="114" font-size="12.5" fill="#E2E8F0">✦ Docker &amp; Kubernetes (EKS) Orchestration</text>
        <text x="24" y="142" font-size="12.5" fill="#E2E8F0">✦ Resilient Microservices &amp; Linux Environments</text>
        <text x="24" y="170" font-size="12.5" fill="#94A3B8">✦ Continuous CI/CD &amp; Automated Deployments</text>
    </g>

    <!-- Pod 3: Full-Stack & Performance -->
    <g transform="translate(800, 75)" class="pod-anim" style="animation-delay: 1s;">
        <rect x="4" y="6" width="340" height="195" rx="14" fill="rgba(0,0,0,0.6)" />
        <rect x="0" y="0" width="340" height="195" fill="url(#pod-grad)" stroke="#C084FC" stroke-width="1.5" rx="14" />
        <rect x="0" y="0" width="340" height="4" fill="#C084FC" rx="2" />
        
        <circle cx="36" cy="40" r="16" fill="rgba(192, 132, 252, 0.15)" stroke="#C084FC" stroke-width="1" />
        <text x="36" y="47" font-size="18" text-anchor="middle">⚡</text>
        <text x="66" y="45" font-size="15" font-weight="800" fill="#C084FC">Full-Stack &amp; Performance</text>
        
        <text x="24" y="86" font-size="12.5" fill="#E2E8F0">✦ FastAPI &amp; Node.js High-Throughput APIs</text>
        <text x="24" y="114" font-size="12.5" fill="#E2E8F0">✦ React &amp; Next.js Modern Dynamic Interfaces</text>
        <text x="24" y="142" font-size="12.5" fill="#E2E8F0">✦ PostgreSQL &amp; Vector DB High-Speed Queries</text>
        <text x="24" y="170" font-size="12.5" fill="#94A3B8">✦ Low-Latency Caching with Redis &amp; CDN</text>
    </g>
</svg>
'''
    with open("assets/aurora_about.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_about.svg")

def generate_aurora_skills():
    width = 1200
    height = 430
    
    categories = [
        ("AI &amp; DEEP LEARNING MATRIX", ["Python", "PyTorch", "TensorFlow", "OpenCV", "LangChain", "LLMs", "RAG Systems", "OpenAI", "Vector DBs"], "#00F5FF"),
        ("CLOUD, INFRA &amp; MLOPS", ["AWS", "Docker", "Kubernetes", "CI/CD", "Linux", "Terraform", "PostgreSQL", "Supabase", "Redis"], "#818CF8"),
        ("FULL-STACK &amp; SYSTEM SOFTWARE", ["C++", "Java", "JavaScript", "TypeScript", "FastAPI", "React", "Next.js", "REST APIs", "Git"], "#C084FC")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes chipPulse {{
                0%, 100% {{ filter: drop-shadow(0 0 3px rgba(0, 245, 255, 0.3)); transform: translateY(0px); }}
                50% {{ filter: drop-shadow(0 0 8px rgba(0, 245, 255, 0.7)); transform: translateY(-2px); }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .pill-anim {{ animation: chipPulse 3.5s ease-in-out infinite alternate; }}
        </style>

        <linearGradient id="skills-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="pill-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.8)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.95)" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#skills-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">TECHNICAL EXPERTISE &amp; ENGINEERING MATRIX</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />
'''

    y_offset = 80
    for title, skills, cat_color in categories:
        svg += f'''
        <!-- Category Section -->
        <g transform="translate(60, {y_offset})">
            <circle cx="6" cy="7" r="4" fill="{cat_color}" />
            <text x="18" y="11" font-size="13" font-weight="800" fill="{cat_color}" letter-spacing="1.5">{title}</text>
            <line x1="0" y1="20" x2="1080" y2="20" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />
        </g>
'''
        x = 60
        y = y_offset + 32
        
        for skill in skills:
            w = len(skill) * 9 + 42
            if x + w > 1140:
                x = 60
                y += 42
                
            svg += f'''
            <g transform="translate({x}, {y})" class="pill-anim">
                <rect x="2" y="3" width="{w}" height="32" rx="8" fill="rgba(0,0,0,0.5)" />
                <rect x="0" y="0" width="{w}" height="32" rx="8" fill="url(#pill-grad)" stroke="{cat_color}" stroke-width="1" />
                <circle cx="14" cy="16" r="3.5" fill="{cat_color}" />
                <text x="{14 + (w-14)/2}" y="20" font-size="12" font-weight="700" text-anchor="middle" fill="#F8FAFC">{skill}</text>
            </g>
'''
            x += w + 12
        y_offset = y + 54

    svg += '</svg>'
    with open("assets/aurora_skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_skills.svg")

def generate_aurora_projects():
    width = 1200
    height = 380
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes cardHover {{
                0%, 100% {{ filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.3)); transform: translateY(0px); }}
                50% {{ filter: drop-shadow(0 0 18px rgba(0, 245, 255, 0.85)); transform: translateY(-5px); }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .proj-3d {{ animation: cardHover 4s ease-in-out infinite alternate; }}
        </style>
        
        <linearGradient id="proj-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="card-proj-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.85)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.95)" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#proj-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />

    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">FEATURED PRODUCTION PROJECTS &amp; CORE ARCHITECTURE</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />
'''

    projects = [
        ("MyKernel", "High-performance OS kernel &amp; system architecture module.", ["C++", "Linux", "x86_64"], "#00F5FF", 60),
        ("AI-HUMANIZER-PRO", "Next-gen LLM generative AI &amp; text humanization engine.", ["Python", "FastAPI", "LLMs"], "#818CF8", 440),
        ("AI-Interviewer", "Agentic AI automated evaluation &amp; interview simulator.", ["React", "Agentic AI", "Next.js"], "#C084FC", 820)
    ]
    
    for title, desc, tags, color, x in projects:
        svg += f'''
    <g transform="translate({x}, 75)" class="proj-3d">
        <!-- 3D Drop Shadow Pedestal -->
        <rect x="4" y="6" width="320" height="270" rx="14" fill="rgba(0,0,0,0.6)" />
        
        <!-- Card Body -->
        <rect x="0" y="0" width="320" height="270" fill="url(#card-proj-grad)" stroke="{color}" stroke-width="1.5" rx="14" />
        <rect x="0" y="0" width="320" height="4" fill="{color}" rx="2" />
        
        <!-- Status Node -->
        <circle cx="26" cy="40" r="4" fill="{color}" />
        <text x="40" y="45" font-size="18" font-weight="800" fill="#F8FAFC">{title}</text>
        <text x="26" y="78" font-size="13" fill="#94A3B8">{desc}</text>
        
        <!-- Interactive Tech Tags -->
        <g transform="translate(26, 140)">
'''
        tag_x = 0
        for tag in tags:
            tag_w = len(tag) * 8 + 24
            svg += f'''
            <rect x="{tag_x}" y="0" width="{tag_w}" height="26" rx="6" fill="rgba(0, 245, 255, 0.08)" stroke="{color}" stroke-width="1" />
            <text x="{tag_x + tag_w/2}" y="17" font-size="11" font-weight="700" fill="{color}" text-anchor="middle">{tag}</text>
'''
            tag_x += tag_w + 10

        svg += f'''
        </g>
        
        <!-- Action Button with 3D Bevel -->
        <g transform="translate(26, 205)">
            <rect x="2" y="3" width="268" height="42" rx="8" fill="rgba(0,0,0,0.4)" />
            <rect x="0" y="0" width="268" height="42" rx="8" fill="rgba(56, 189, 248, 0.12)" stroke="{color}" stroke-width="1.2" />
            <text x="134" y="26" font-size="13" font-weight="800" fill="{color}" text-anchor="middle">View Repository ⚡ →</text>
        </g>
    </g>
'''

    svg += '</svg>'
    with open("assets/aurora_projects.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_projects.svg")

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
