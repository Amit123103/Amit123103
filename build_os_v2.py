import math
import base64
import os
import random

def get_base64_image(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def hex_points(x, y, size):
    pts = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        pts.append(f"{x + size * math.cos(angle)},{y + size * math.sin(angle)}")
    return " ".join(pts)

def isometric_cube(x, y, size):
    # size is the side length
    dx = size * math.cos(math.radians(30))
    dy = size * math.sin(math.radians(30))
    
    # Top face
    top = f"{x},{y} {x+dx},{y-dy} {x},{y-2*dy} {x-dx},{y-dy}"
    # Left face
    left = f"{x},{y} {x-dx},{y-dy} {x-dx},{y+size-dy} {x},{y+size}"
    # Right face
    right = f"{x},{y} {x+dx},{y-dy} {x+dx},{y+size-dy} {x},{y+size}"
    
    return top, left, right

def generate_os_core():
    width = 1600
    height = 900
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#02040A" />
            <stop offset="50%" stop-color="#090B13" />
            <stop offset="100%" stop-color="#000000" />
        </linearGradient>
        <radialGradient id="aurora" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0.15)" />
            <stop offset="50%" stop-color="rgba(79, 70, 229, 0.05)" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        <filter id="neon"><feGaussianBlur stdDeviation="6" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
        <filter id="glass-blur"><feGaussianBlur stdDeviation="3"/></filter>
        
        <clipPath id="panel-clip"><polygon points="30,0 90,0 120,30 120,120 90,150 30,150 0,120 0,30" /></clipPath>
        
        <style>
text {{ font-family: 'Jura', sans-serif; }}
            .spin-fast {{ animation: spin 8s linear infinite; transform-origin: center; }}
            .spin-slow {{ animation: spin 40s linear infinite reverse; transform-origin: center; }}
            @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
            
            .breathe {{ animation: breathe 3s ease-in-out infinite alternate; }}
            @keyframes breathe {{ 0% {{ opacity: 0.6; transform: scale(0.98); }} 100% {{ opacity: 1; transform: scale(1.02); }} }}
            
            .orbit {{ animation: orbit-anim var(--dur) linear infinite; transform-origin: {width/2}px {height/2}px; }}
            .anti-orbit {{ animation: anti-orbit var(--dur) linear infinite; transform-origin: center; }}
            @keyframes orbit-anim {{ 100% {{ transform: rotate(360deg); }} }}
            @keyframes anti-orbit {{ 100% {{ transform: rotate(-360deg); }} }}
            
            .float {{ animation: floatY 10s ease-in-out infinite alternate; }}
            @keyframes floatY {{ 0% {{ transform: translateY(-10px); }} 100% {{ transform: translateY(10px); }} }}
            
            .radar-sweep {{ animation: sweep 4s linear infinite; transform-origin: {width/2}px {height/2}px; }}
            @keyframes sweep {{ 100% {{ transform: rotate(360deg); }} }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    <circle cx="50%" cy="50%" r="700" fill="url(#aurora)" class="breathe" />
    
    <!-- Radar Sweep -->
    <path d="M{width/2},{height/2} L{width/2},{height/2 - 700} A700,700 0 0,1 {width/2 + 200},{height/2 - 650} Z" fill="rgba(0, 245, 255, 0.05)" class="radar-sweep" />
    <circle cx="50%" cy="50%" r="700" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
    <circle cx="50%" cy="50%" r="500" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="10 20" />
'''

    # Grid
    for x in range(0, width, 100): svg += f'<line x1="{x}" y1="0" x2="{x}" y2="{height}" stroke="rgba(255,255,255,0.02)" />'
    for y in range(0, height, 100): svg += f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="rgba(255,255,255,0.02)" />'

    svg += '''
    <!-- Central AI Core -->
    <g transform="translate(800, 450)" class="float">
        <!-- Energy Rings -->
        <g class="spin-slow">
            <circle cx="0" cy="0" r="180" fill="none" stroke="#00F5FF" stroke-width="1" filter="url(#neon)" opacity="0.5" stroke-dasharray="50 30" />
            <circle cx="0" cy="0" r="190" fill="none" stroke="#4F46E5" stroke-width="2" opacity="0.3" stroke-dasharray="10 20 50 10" />
        </g>
        <g class="spin-fast">
            <polygon points="0,-140 121,-70 121,70 0,140 -121,70 -121,-70" fill="none" stroke="#00F5FF" stroke-width="3" filter="url(#neon)" opacity="0.8"/>
            <circle cx="0" cy="0" r="130" fill="none" stroke="#FFF" stroke-dasharray="5 15" stroke-width="2" />
        </g>
        
        <!-- Glowing Core -->
        <circle cx="0" cy="0" r="80" fill="#000" stroke="#00F5FF" stroke-width="4" filter="url(#neon)" class="breathe" />
        <circle cx="0" cy="0" r="60" fill="rgba(79, 70, 229, 0.4)" filter="url(#neon)" class="breathe" />
        <circle cx="0" cy="0" r="30" fill="#FFF" filter="url(#neon)" />
        
        <text x="0" y="8" fill="#000" text-anchor="middle" font-size="24" font-weight="bold">AI</text>
    </g>
    
    <!-- 3D Distorted Orbit System (The Planets) -->
    <!-- We simulate 3D by wrapping orbits in a squashed transform -->
    <g transform="translate(800, 450) scale(1, 0.6) translate(-800, -450)">
'''

    images = ["iv.jpg", "v2.jpg", "v3.jpg", "v4.jpg", "v5.jpg", "v6.jpg", "v7.jpg", "v8.jpg", "v9.jpg", "v10.jpg"]
    # We map them to orbits
    for i, img in enumerate(images):
        b64 = get_base64_image(img)
        r = 300 + (i * 45)
        dur = 30 + (i * 10)
        angle = (i * 36)
        
        svg += f'''
        <circle cx="800" cy="450" r="{r}" fill="none" stroke="rgba(0, 245, 255, 0.15)" stroke-width="2" />
        <g class="orbit" style="--dur: {dur}s; transform: rotate({angle}deg);">
            <!-- Translate out to radius -->
            <g transform="translate({r}, 0)">
                <!-- Anti-rotate the orbit -->
                <g class="anti-orbit" style="--dur: {dur}s;">
                    <!-- Unsquash to make panels look 3D standing up -->
                    <g transform="scale(1, 1.66)">
                        <g class="float" style="animation-delay: -{i}s;">
                            <!-- Holographic Panel -->
                            <polygon points="30,0 90,0 120,30 120,120 90,150 30,150 0,120 0,30" fill="rgba(0,0,0,0.8)" stroke="#00F5FF" stroke-width="2" filter="url(#neon)" transform="translate(-60, -75)" />
                            <image href="{b64}" x="-60" y="-75" width="120" height="150" clip-path="url(#panel-clip)" preserveAspectRatio="xMidYMid slice" opacity="0.8" />
                            <rect x="-60" y="-75" width="120" height="150" fill="rgba(0, 245, 255, 0.1)" clip-path="url(#panel-clip)" />
                            
                            <!-- Glowing data nodes -->
                            <circle cx="-60" cy="-45" r="3" fill="#FFF" filter="url(#neon)" />
                            <circle cx="60" cy="45" r="3" fill="#FFF" filter="url(#neon)" />
                        </g>
                    </g>
                </g>
            </g>
        </g>
'''

    svg += '''
    </g>
    
    <!-- Top HUD Overlay -->
    <g transform="translate(50, 50)">
        <text x="0" y="0" fill="#00F5FF" font-size="20" letter-spacing="4" filter="url(#neon)">> OS_BOOT_SEQUENCE_COMPLETE</text>
        <text x="0" y="25" fill="#FFF" font-size="14" opacity="0.6">NEURAL LINK ESTABLISHED // WELCOME AMIT</text>
    </g>
</svg>
'''
    with open("assets/os_core.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_os_cmd():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
text {{ font-family: 'Jura', sans-serif; fill: #FFF; }}
            .highlight {{ fill: #00F5FF; font-weight: bold; filter: drop-shadow(0 0 4px #00F5FF); }}
            .panel {{ fill: rgba(5, 10, 25, 0.7); stroke: #4F46E5; stroke-width: 2; }}
            
            .breathe-panel {{ animation: panelBreathe 4s infinite alternate; }}
            @keyframes panelBreathe {{ 0% {{ stroke: #4F46E5; box-shadow: 0 0 10px #4F46E5; }} 100% {{ stroke: #00F5FF; box-shadow: 0 0 20px #00F5FF; }} }}
            
            .typing {{
                overflow: hidden; white-space: nowrap; border-right: 2px solid #00F5FF;
                animation: type 3s steps(40, end) infinite alternate;
            }}
            @keyframes type {{ 0% {{ width: 0; }} 100% {{ width: 100%; }} }}
        </style>
        <filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
    </defs>
    
    <g transform="translate(100, 50)" class="breathe-panel">
        <!-- Futuristic Window Shape -->
        <path d="M0,30 L30,0 L1000,0 L1000,370 L970,400 L0,400 Z" class="panel" filter="url(#glow)" />
        <rect x="0" y="0" width="1000" height="40" fill="rgba(0, 245, 255, 0.1)" />
        <text x="20" y="25" class="highlight" font-size="16">COMMAND CENTER // AI DASHBOARD</text>
        
        <line x1="0" y1="40" x2="1000" y2="40" stroke="#00F5FF" stroke-width="1" />
        
        <!-- Grid pattern inside -->
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="none" stroke="rgba(255,255,255,0.05)" />
        </pattern>
        <path d="M0,40 L1000,40 L1000,370 L970,400 L0,400 Z" fill="url(#grid)" />
        
        <!-- Status Information -->
        <g transform="translate(40, 90)">
            <text x="0" y="0" font-size="18" class="highlight">SYSTEM STATUS:</text>
            <text x="200" y="0" font-size="18">OPTIMAL [■■■■■■■■■□]</text>
            
            <text x="0" y="50" font-size="18" class="highlight">AI CORE:</text>
            <text x="200" y="50" font-size="18">AMIT KUMAR v2.0</text>
            
            <text x="0" y="100" font-size="18" class="highlight">PROFILE ANALYSIS:</text>
            <text x="200" y="100" font-size="18">AI ENGINEER | ML ARCHITECT</text>
            
            <text x="0" y="150" font-size="18" class="highlight">CURRENT MISSION:</text>
            <text x="200" y="150" font-size="18">BUILDING INTELLIGENT REAL-WORLD SYSTEMS</text>
            
            <text x="0" y="200" font-size="18" class="highlight">LEARNING MODE:</text>
            <text x="200" y="200" font-size="18">ENABLED (CONTINUOUS)</text>
            
            <text x="0" y="250" font-size="18" class="highlight">ONLINE STATUS:</text>
            <text x="200" y="250" font-size="18" fill="#10B981">> ACTIVE_SYNC_WITH_GITHUB</text>
        </g>
        
        <!-- decorative tech shapes -->
        <g transform="translate(750, 100)">
            <circle cx="100" cy="100" r="80" fill="none" stroke="#4F46E5" stroke-width="2" stroke-dasharray="20 10" />
            <circle cx="100" cy="100" r="60" fill="none" stroke="#00F5FF" stroke-width="1" />
            <path d="M100,20 L100,180 M20,100 L180,100" stroke="rgba(0, 245, 255, 0.3)" />
            <rect x="95" y="95" width="10" height="10" fill="#FFF" />
        </g>
    </g>
</svg>
'''
    with open("assets/os_cmd.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_os_neural():
    width = 1200
    height = 600
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
text {{ font-family: 'Jura', sans-serif; fill: #FFF; font-weight: bold; font-size: 12px; }}
            .hex {{ fill: rgba(0, 245, 255, 0.05); stroke: #00F5FF; stroke-width: 2; transition: all 0.3s; }}
            
            .breathe {{ animation: coreBreathe 3s ease-in-out infinite alternate; }}
            @keyframes coreBreathe {{
                0% {{ filter: drop-shadow(0 0 2px #00F5FF); transform: translateY(0); }}
                100% {{ filter: drop-shadow(0 0 15px #4F46E5); transform: translateY(-5px); }}
            }}
            .line-pulse {{ stroke: #4F46E5; stroke-width: 1.5; stroke-dasharray: 5 10; animation: dash 20s linear infinite; }}
            @keyframes dash {{ to {{ stroke-dashoffset: 1000; }} }}
        </style>
    </defs>
    
    <text x="600" y="40" font-size="24" fill="#00F5FF" text-anchor="middle" filter="drop-shadow(0 0 5px #00F5FF)">NEURAL NETWORK // CAPABILITY MODULES</text>
    
    <!-- Connective lines -->
    <g id="lines" class="line-pulse">
'''
    # Complex interconnected network mapping
    skills = ["Python", "Machine Learning", "TensorFlow", "PyTorch", "OpenCV", "FastAPI", "React", "Next.js", "Node.js", "Docker", "Kubernetes", "AWS", "Linux", "Git", "GitHub", "SQL", "RAG", "LLMs", "LangChain", "OpenAI"]
    
    cols = 5
    hex_r = 45
    x_offset = hex_r * math.sqrt(3)
    y_offset = hex_r * 1.5
    
    centers = []
    
    for i in range(len(skills)):
        row = i // cols
        col = i % cols
        cx = 250 + col * x_offset + (row % 2) * (x_offset / 2)
        cy = 100 + row * y_offset
        centers.append((cx, cy))
        
    for cx, cy in centers:
        for ox, oy in centers:
            if math.hypot(cx - ox, cy - oy) < (x_offset * 1.2) and (cx, cy) != (ox, oy):
                svg += f'<line x1="{cx}" y1="{cy}" x2="{ox}" y2="{oy}" />\n'
                
    svg += '''
    </g>
    <!-- Hexagons -->
    <g id="hexagons">
'''
    for i, skill in enumerate(skills):
        cx, cy = centers[i]
        points = hex_points(cx, cy, hex_r - 5)
        delay = random.uniform(0, 2)
        svg += f'''
        <g class="breathe" style="animation-delay: {delay}s;">
            <polygon points="{points}" class="hex" />
            <!-- inner tech glow -->
            <circle cx="{cx}" cy="{cy}" r="15" fill="rgba(79, 70, 229, 0.4)" />
            <text x="{cx}" y="{cy + 4}" text-anchor="middle">{skill.upper()}</text>
        </g>
'''
    
    svg += '''
    </g>
</svg>
'''
    with open("assets/os_neural.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_os_matrix():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
text {{ font-family: 'Jura', sans-serif; fill: #FFF; }}
            .cube-face-top {{ fill: rgba(0, 245, 255, 0.2); stroke: #00F5FF; stroke-width: 1.5; }}
            .cube-face-left {{ fill: rgba(79, 70, 229, 0.3); stroke: #00F5FF; stroke-width: 1.5; }}
            .cube-face-right {{ fill: rgba(2, 6, 23, 0.8); stroke: #00F5FF; stroke-width: 1.5; }}
            
            .float {{ animation: floatY 6s ease-in-out infinite alternate; }}
            @keyframes floatY {{ 0% {{ transform: translateY(-10px); }} 100% {{ transform: translateY(10px); }} }}
        </style>
        <filter id="cube-glow"><feGaussianBlur stdDeviation="3" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
    </defs>
    
    <text x="600" y="40" font-size="24" fill="#00F5FF" text-anchor="middle" filter="url(#cube-glow)">3D PROJECT MATRIX</text>
'''
    projects = [
        ("AI VISION SYSTEM", "Python • PyTorch • OpenCV"),
        ("QUANTUM RAG", "LLMs • LangChain • FastAPI"),
        ("CLOUD PIPELINE", "AWS • Docker • Kubernetes"),
    ]
    
    for i, (title, tech) in enumerate(projects):
        cx = 250 + i * 350
        cy = 280
        size = 80
        top, left, right = isometric_cube(0, 0, size)
        
        delay = i * 1.5
        svg += f'''
        <g transform="translate({cx}, {cy})" class="float" style="animation-delay: {delay}s;" filter="url(#cube-glow)">
            <polygon points="{top}" class="cube-face-top" />
            <polygon points="{left}" class="cube-face-left" />
            <polygon points="{right}" class="cube-face-right" />
            
            <!-- Projected Text on the right face -->
            <g transform="translate({size*math.cos(math.radians(30))/2}, {size/2}) skewY(30) scale(0.8)">
                <text x="0" y="0" font-size="14" fill="#00F5FF">{title}</text>
                <text x="0" y="20" font-size="10" fill="#FFF">{tech}</text>
                
                <rect x="0" y="40" width="60" height="15" fill="#4F46E5" />
                <text x="30" y="51" font-size="9" text-anchor="middle">GITHUB</text>
                
                <rect x="70" y="40" width="60" height="15" fill="#00F5FF" />
                <text x="100" y="51" font-size="9" text-anchor="middle" fill="#000">DEMO</text>
            </g>
        </g>
        
        <!-- Fake shadow on the floor -->
        <ellipse cx="{cx}" cy="{cy + 150}" rx="{size}" ry="{size/3}" fill="rgba(0, 245, 255, 0.05)" filter="blur(5px)" />
'''

    svg += '</svg>'
    with open("assets/os_matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_os_social():
    width = 1200
    height = 200
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <radialGradient id="planet-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="30%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        <style>
text {{ font-family: 'Jura', sans-serif; fill: #FFF; font-weight: bold; font-size: 14px; text-anchor: middle; }}
            .float {{ animation: floatP 4s ease-in-out infinite alternate; }}
            @keyframes floatP {{ 0% {{ transform: translateY(-5px); }} 100% {{ transform: translateY(5px); }} }}
        </style>
    </defs>
    <!-- Social Planets -->
'''
    socials = ["LINKEDIN", "PORTFOLIO", "GITHUB", "TWITTER", "DISCORD"]
    spacing = 1200 / (len(socials) + 1)
    
    for i, name in enumerate(socials):
        cx = spacing * (i + 1)
        cy = 100
        delay = i * 0.5
        svg += f'''
        <g class="float" style="animation-delay: {delay}s;">
            <!-- Outer atmosphere -->
            <circle cx="{cx}" cy="{cy-20}" r="40" fill="url(#planet-glow)" opacity="0.3" />
            <!-- Planet Core -->
            <circle cx="{cx}" cy="{cy-20}" r="25" fill="#090B13" stroke="#00F5FF" stroke-width="2" stroke-dasharray="5 5" />
            <!-- Inner Ring -->
            <ellipse cx="{cx}" cy="{cy-20}" rx="35" ry="10" fill="none" stroke="#4F46E5" stroke-width="2" transform="rotate(20 {cx} {cy-20})" />
            <text x="{cx}" y="{cy + 30}">{name}</text>
        </g>
'''
    
    svg += '</svg>'
    with open("assets/os_social.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_os_footer():
    # Same advanced footer as before, fits perfectly.
    width = 1200
    height = 400
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            .drone {{ animation: fly 20s linear infinite; }}
            @keyframes fly {{ 0% {{ transform: translate(-100px, 150px); }} 100% {{ transform: translate(1300px, 150px); }} }}
            .water-glitch {{ animation: wave 5s infinite; }}
            @keyframes wave {{ 0% {{ opacity: 0.8; }} 50% {{ opacity: 0.5; }} 100% {{ opacity: 0.8; }} }}
        </style>
        <linearGradient id="cyber-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#02040A" />
            <stop offset="100%" stop-color="#0F0F23" />
        </linearGradient>
        <filter id="neon-glow"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>
    </defs>
    <rect width="100%" height="300" fill="url(#cyber-sky)" />
    <!-- Huge Cyber Moon -->
    <circle cx="600" cy="150" r="100" fill="rgba(0, 245, 255, 0.1)" filter="url(#neon-glow)" />
    <circle cx="600" cy="150" r="98" fill="none" stroke="#00F5FF" stroke-dasharray="10 20" stroke-width="2" class="drone" style="animation-duration:60s; transform-origin:600px 150px;" />
    <!-- Skyline -->
    <path d="M0,300 L0,220 L30,220 L50,150 L80,220 L150,220 L180,130 L220,220 L300,220 L350,110 L420,220 L500,220 L550,160 L620,220 L750,220 L800,120 L860,220 L1000,220 L1050,150 L1120,220 L1200,220 L1200,300 Z" fill="#04060E" />
    <path d="M50,150 L50,220 M180,130 L180,220 M350,110 L350,220 M550,160 L550,220 M800,120 L800,220" stroke="#00F5FF" stroke-width="2" filter="url(#neon-glow)" opacity="0.5" />
    <!-- Drone -->
    <g class="drone"><circle cx="0" cy="0" r="5" fill="#FFF" filter="url(#neon-glow)" /><rect x="-10" y="-2" width="20" height="4" fill="#4F46E5" /></g>
    <!-- River -->
    <g transform="translate(0, 300)">
        <rect width="1200" height="100" fill="#04060E" />
        <rect width="1200" height="100" fill="rgba(0, 245, 255, 0.05)" class="water-glitch" />
        <!-- Reflection -->
        <rect x="500" y="10" width="200" height="5" fill="rgba(0, 245, 255, 0.5)" filter="url(#neon-glow)" />
        <rect x="520" y="30" width="160" height="5" fill="rgba(0, 245, 255, 0.4)" filter="url(#neon-glow)" />
        <rect x="550" y="50" width="100" height="5" fill="rgba(0, 245, 255, 0.3)" filter="url(#neon-glow)" />
    </g>
</svg>
'''
    with open("assets/os_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    print("Booting AI OS V2 SVG Generator...")
    generate_os_core()
    generate_os_cmd()
    generate_os_neural()
    generate_os_matrix()
    generate_os_social()
    generate_os_footer()
    print("V2 System Online.")
