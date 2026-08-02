import math
import base64
import os

def get_base64_image(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def generate_zenith_hero():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&amp;display=swap');
            text {{ font-family: 'Inter', sans-serif; fill: #FFF; }}
            .glow {{ filter: drop-shadow(0 0 10px rgba(0,245,255,0.6)); }}
            .pulse {{ animation: pulse 4s infinite alternate ease-in-out; transform-origin: center; }}
            @keyframes pulse {{ 0% {{ transform: scale(0.98); opacity: 0.8; }} 100% {{ transform: scale(1.02); opacity: 1; }} }}
            
            .typing-container {{ animation: fadeUp 2s ease-out forwards; }}
            @keyframes fadeUp {{ 0% {{ opacity: 0; transform: translateY(20px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}
            
            .ring {{ transform-origin: center; animation: spin var(--speed) linear infinite var(--dir); }}
            @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
        </style>
        <radialGradient id="bg" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#0a0f1c" />
            <stop offset="100%" stop-color="#020408" />
        </radialGradient>
        <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="20%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        <filter id="neon"><feGaussianBlur stdDeviation="4" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Central Axis Alignment -->
    <g transform="translate(600, 200)">
        <g class="pulse">
            <!-- Rings -->
            <circle cx="0" cy="0" r="100" fill="none" stroke="rgba(0,245,255,0.1)" stroke-width="1" class="ring" style="--speed:20s; --dir:normal;" stroke-dasharray="10 5" />
            <circle cx="0" cy="0" r="115" fill="none" stroke="rgba(79,70,229,0.3)" stroke-width="2" class="ring" style="--speed:30s; --dir:reverse;" stroke-dasharray="30 20 10 5" />
            <circle cx="0" cy="0" r="130" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" class="ring" style="--speed:40s; --dir:normal;" />
            
            <!-- Core -->
            <circle cx="0" cy="0" r="80" fill="#000" stroke="#00F5FF" stroke-width="2" filter="url(#neon)" />
            <circle cx="0" cy="0" r="60" fill="url(#core-glow)" opacity="0.8" />
            <text x="0" y="8" font-size="24" font-weight="700" text-anchor="middle" fill="#000">AMIT</text>
        </g>
    </g>
    
    <!-- Typography perfectly aligned -->
    <g transform="translate(600, 360)">
        <g class="typing-container">
            <text x="0" y="0" font-size="32" font-weight="700" text-anchor="middle" letter-spacing="4">AMIT KUMAR</text>
            <text x="0" y="30" font-size="16" font-weight="400" fill="#00F5FF" text-anchor="middle" letter-spacing="2">AI ENGINEER | CLOUD ARCHITECT | FULL STACK DEVELOPER</text>
            
            <!-- Buttons / Badges -->
            <g transform="translate(-150, 60)">
                <rect x="0" y="0" width="140" height="30" rx="15" fill="rgba(0,245,255,0.1)" stroke="#00F5FF" stroke-width="1" />
                <text x="70" y="19" font-size="12" font-weight="600" text-anchor="middle" fill="#00F5FF">AVAILABLE FOR WORK</text>
            </g>
            <g transform="translate(10, 60)">
                <rect x="0" y="0" width="140" height="30" rx="15" fill="rgba(79,70,229,0.1)" stroke="#4F46E5" stroke-width="1" />
                <text x="70" y="19" font-size="12" font-weight="600" text-anchor="middle" fill="#818CF8">BASED IN INDIA</text>
            </g>
        </g>
    </g>
</svg>
'''
    with open("assets/zenith_hero.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_zenith_about():
    width = 1200
    height = 400
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&amp;display=swap');
            text {{ font-family: 'Inter', sans-serif; fill: #FFF; }}
            .card {{ fill: rgba(255,255,255,0.03); stroke: rgba(255,255,255,0.1); stroke-width: 1; transition: all 0.3s; }}
            .card-glow {{ fill: rgba(0, 245, 255, 0.02); stroke: #00F5FF; stroke-width: 1.5; filter: drop-shadow(0 0 10px rgba(0,245,255,0.2)); }}
        </style>
    </defs>
    
    <!-- Title -->
    <text x="600" y="40" font-size="20" font-weight="600" text-anchor="middle" letter-spacing="2">PERSONAL DETAILS</text>
    <rect x="580" y="55" width="40" height="2" fill="#00F5FF" />
    
    <!-- 3x1 Grid -->
    <!-- Card 1: Education -->
    <g transform="translate(100, 100)">
        <rect x="0" y="0" width="300" height="200" rx="16" class="card" />
        <rect x="0" y="0" width="300" height="4" fill="#00F5FF" opacity="0.8" clip-path="inset(0 0 0 0 round 16px 16px 0 0)" />
        <circle cx="150" cy="50" r="20" fill="rgba(0,245,255,0.1)" />
        <text x="150" y="55" font-size="20" text-anchor="middle">🎓</text>
        <text x="150" y="100" font-size="16" font-weight="600" text-anchor="middle">Education</text>
        <text x="150" y="130" font-size="14" fill="#A0A0A0" text-anchor="middle">Final Year B.Tech</text>
        <text x="150" y="155" font-size="14" fill="#A0A0A0" text-anchor="middle">Computer Science</text>
    </g>

    <!-- Card 2: Focus (Highlighted) -->
    <g transform="translate(450, 100)">
        <rect x="0" y="0" width="300" height="200" rx="16" class="card card-glow" />
        <rect x="0" y="0" width="300" height="4" fill="#00F5FF" clip-path="inset(0 0 0 0 round 16px 16px 0 0)" />
        <circle cx="150" cy="50" r="20" fill="rgba(0,245,255,0.2)" />
        <text x="150" y="55" font-size="20" text-anchor="middle">⚡</text>
        <text x="150" y="100" font-size="16" font-weight="600" text-anchor="middle" fill="#00F5FF">Current Focus</text>
        <text x="150" y="130" font-size="14" fill="#A0A0A0" text-anchor="middle">Generative AI &amp; LLMs</text>
        <text x="150" y="155" font-size="14" fill="#A0A0A0" text-anchor="middle">Scalable Cloud Systems</text>
    </g>

    <!-- Card 3: Goals -->
    <g transform="translate(800, 100)">
        <rect x="0" y="0" width="300" height="200" rx="16" class="card" />
        <rect x="0" y="0" width="300" height="4" fill="#4F46E5" opacity="0.8" clip-path="inset(0 0 0 0 round 16px 16px 0 0)" />
        <circle cx="150" cy="50" r="20" fill="rgba(79,70,229,0.1)" />
        <text x="150" y="55" font-size="20" text-anchor="middle">🎯</text>
        <text x="150" y="100" font-size="16" font-weight="600" text-anchor="middle">Career Goal</text>
        <text x="150" y="130" font-size="14" fill="#A0A0A0" text-anchor="middle">Building Intelligent</text>
        <text x="150" y="155" font-size="14" fill="#A0A0A0" text-anchor="middle">AI Products for Industry</text>
    </g>
</svg>
'''
    with open("assets/zenith_about.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_zenith_skills():
    width = 1200
    height = 550
    
    categories = [
        ("AI &amp; ML", ["Python", "TensorFlow", "PyTorch", "OpenCV", "Machine Learning", "Deep Learning", "LLMs", "RAG", "LangChain", "OpenAI"]),
        ("Backend & Web", ["FastAPI", "Node.js", "REST APIs", "React", "Next.js", "HTML", "CSS", "JavaScript"]),
        ("Cloud & Core", ["AWS", "Docker", "Linux", "DevOps", "GitHub Actions", "C++", "Java", "C", "MySQL", "SQLite"])
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap');
            text {{ font-family: 'Inter', sans-serif; fill: #FFF; }}
            .capsule {{ fill: rgba(255,255,255,0.05); stroke: rgba(255,255,255,0.15); stroke-width: 1; rx: 18; }}
            .capsule-anim {{ animation: float-capsule 4s ease-in-out infinite alternate; }}
            @keyframes float-capsule {{ 0% {{ transform: translateY(0px); filter: drop-shadow(0 0 0 rgba(0,0,0,0)); stroke: rgba(255,255,255,0.15); }} 100% {{ transform: translateY(-4px); filter: drop-shadow(0 4px 8px rgba(0,245,255,0.2)); stroke: rgba(0,245,255,0.5); }} }}
        </style>
    </defs>
    
    <text x="600" y="40" font-size="20" font-weight="600" text-anchor="middle" letter-spacing="2">TECHNICAL EXPERTISE</text>
    <rect x="580" y="55" width="40" height="2" fill="#00F5FF" />
'''

    y_offset = 100
    for title, skills in categories:
        svg += f'<text x="100" y="{y_offset}" font-size="16" font-weight="600" fill="#00F5FF">{title}</text>'
        svg += f'<line x1="100" y1="{y_offset + 10}" x2="1100" y2="{y_offset + 10}" stroke="rgba(255,255,255,0.1)" stroke-width="1" />'
        
        x = 100
        y = y_offset + 30
        
        for i, skill in enumerate(skills):
            # Calculate text width approximation
            w = len(skill) * 9 + 40
            if x + w > 1100:
                x = 100
                y += 50
            
            delay = (i * 0.1) % 2
            svg += f'''
            <g transform="translate({x}, {y})">
                <g class="capsule-anim" style="animation-delay: {delay}s;">
                    <rect x="0" y="0" width="{w}" height="36" class="capsule" />
                    <text x="{w/2}" y="23" font-size="14" font-weight="500" text-anchor="middle">{skill}</text>
                </g>
            </g>
'''
            x += w + 15
        y_offset = y + 80

    svg += '</svg>'
    with open("assets/zenith_skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_zenith_projects():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;display=swap');
            text {{ font-family: 'Inter', sans-serif; fill: #FFF; }}
            .card {{ fill: rgba(20,20,30,0.4); stroke: rgba(255,255,255,0.1); stroke-width: 1; rx: 12; }}
            .tag {{ fill: rgba(0,245,255,0.1); stroke: #00F5FF; stroke-width: 1; rx: 10; }}
            .btn {{ fill: #00F5FF; rx: 6; }}
            .float {{ animation: hoverLift 6s ease-in-out infinite alternate; }}
            @keyframes hoverLift {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-10px); }} }}
        </style>
        <filter id="shadow"><feGaussianBlur stdDeviation="10" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
    </defs>
    
    <text x="600" y="40" font-size="20" font-weight="600" text-anchor="middle" letter-spacing="2">FEATURED PROJECTS</text>
    <rect x="580" y="55" width="40" height="2" fill="#00F5FF" />
'''

    projects = [
        ("AI Vision System", "Advanced real-time object detection and tracking built on PyTorch.", ["PyTorch", "OpenCV"], 100),
        ("Quantum RAG Pipeline", "A production-grade GenAI retrieval system with LLMs.", ["LangChain", "FastAPI"], 480),
        ("Cloud Native MLOps", "Automated deployment pipeline for machine learning models.", ["AWS", "Docker"], 860)
    ]
    
    for title, desc, tags, x in projects:
        svg += f'''
    <g transform="translate({x}, 120)">
        <g class="float" style="animation-delay: {x/400}s;">
            <!-- Card background with fake shadow -->
            <rect x="10" y="20" width="320" height="300" fill="rgba(0,0,0,0.5)" filter="url(#shadow)" rx="12" />
            <rect x="0" y="0" width="340" height="320" class="card" />
            
            <!-- Image placeholder -->
            <rect x="15" y="15" width="310" height="140" fill="rgba(255,255,255,0.05)" rx="8" />
            <path d="M15,155 L325,155" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
            
            <text x="20" y="185" font-size="18" font-weight="700">{title}</text>
            <text x="20" y="210" font-size="14" fill="#A0A0A0">{desc}</text>
            
            <!-- Tech Stack Tags -->
            <rect x="20" y="240" width="{len(tags[0])*8 + 20}" height="24" class="tag" />
            <text x="{20 + (len(tags[0])*8 + 20)/2}" y="256" font-size="11" font-weight="600" fill="#00F5FF" text-anchor="middle">{tags[0]}</text>
            
            <rect x="{20 + len(tags[0])*8 + 30}" y="240" width="{len(tags[1])*8 + 20}" height="24" class="tag" />
            <text x="{20 + len(tags[0])*8 + 30 + (len(tags[1])*8 + 20)/2}" y="256" font-size="11" font-weight="600" fill="#00F5FF" text-anchor="middle">{tags[1]}</text>
            
            <!-- Action Buttons -->
            <rect x="20" y="280" width="100" height="28" class="btn" />
            <text x="70" y="299" font-size="12" font-weight="700" fill="#000" text-anchor="middle">View Code</text>
            
            <rect x="130" y="280" width="100" height="28" fill="rgba(255,255,255,0.1)" stroke="#FFF" stroke-width="1" rx="6" />
            <text x="180" y="299" font-size="12" font-weight="700" fill="#FFF" text-anchor="middle">Live Demo</text>
        </g>
    </g>
'''

    svg += '</svg>'
    with open("assets/zenith_projects.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_zenith_footer():
    width = 1200
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            .slide {{ animation: slide 40s linear infinite; }}
            @keyframes slide {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-1200px); }} }}
            .glass-img {{ opacity: 0.7; rx: 8; transition: all 0.3s; }}
        </style>
        <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#020408" stop-opacity="1" />
            <stop offset="20%" stop-color="#020408" stop-opacity="0" />
            <stop offset="80%" stop-color="#020408" stop-opacity="0" />
            <stop offset="100%" stop-color="#020408" stop-opacity="1" />
        </linearGradient>
    </defs>
    
    <!-- We simulate an infinite slider by doubling the images -->
'''
    images = ["iv.jpg", "v2.jpg", "v3.jpg", "v4.jpg", "v5.jpg"]
    
    svg += '<g class="slide">'
    for iteration in range(3): # repeat 3 times to ensure no gap during 40s slide
        offset = iteration * (len(images) * 240)
        for i, img in enumerate(images):
            b64 = get_base64_image(img)
            x = offset + i * 240
            svg += f'''
            <g transform="translate({x + 20}, 50)">
                <rect x="0" y="0" width="200" height="200" fill="rgba(255,255,255,0.05)" rx="10" />
                <image href="{b64}" x="5" y="5" width="190" height="190" preserveAspectRatio="xMidYMid slice" class="glass-img" />
                <rect x="5" y="5" width="190" height="190" fill="rgba(0, 245, 255, 0.2)" rx="8" style="mix-blend-mode: overlay;" />
            </g>
'''
    
    svg += '''
    </g>
    <!-- Top and bottom fade masks to make it look cinematic -->
    <rect width="100%" height="100%" fill="url(#fade)" pointer-events="none" />
</svg>
'''
    with open("assets/zenith_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_zenith_hero()
    generate_zenith_about()
    generate_zenith_skills()
    generate_zenith_projects()
    generate_zenith_footer()
    print("V3 Zenith Mathematical Engine execution complete.")
