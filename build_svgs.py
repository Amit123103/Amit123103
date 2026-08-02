import math

def generate_hero_svg():
    width = 1200
    height = 800
    
    # SVG Header
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <!-- Gradients -->
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#000000" />
            <stop offset="50%" stop-color="#0a0a2a" />
            <stop offset="100%" stop-color="#000000" />
        </linearGradient>
        <linearGradient id="neon-blue" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#4F46E5" />
        </linearGradient>
        <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00D4FF" />
            <stop offset="100%" stop-color="#0EA5E9" />
        </linearGradient>
        <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255,255,255,0.1)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0.02)" />
        </linearGradient>
        
        <!-- Glow Filter -->
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="8" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="glow-heavy" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="20" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="glass-blur">
            <feGaussianBlur in="SourceGraphic" stdDeviation="4" />
        </filter>

        <style>
text {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }}
            
            .star {{
                animation: twinkle 3s infinite alternate;
            }}
            .star:nth-child(even) {{
                animation-duration: 5s;
                animation-delay: 2s;
            }}
            
            @keyframes twinkle {{
                0% {{ opacity: 0.2; transform: scale(0.8); }}
                100% {{ opacity: 1; transform: scale(1.2); }}
            }}
            
            .orbit-outer {{
                transform-origin: {width/2}px {height/2}px;
                animation: spin-outer 60s linear infinite;
            }}
            
            .orbit-outer-reverse {{
                transform-origin: center;
                animation: spin-outer-reverse 60s linear infinite;
            }}
            
            .orbit-inner {{
                transform-origin: {width/2}px {height/2}px;
                animation: spin-inner 40s linear infinite reverse;
            }}
            
            .orbit-inner-reverse {{
                transform-origin: center;
                animation: spin-inner-reverse 40s linear infinite reverse;
            }}
            
            @keyframes spin-outer {{
                100% {{ transform: rotate(360deg); }}
            }}
            
            @keyframes spin-outer-reverse {{
                100% {{ transform: rotate(-360deg); }}
            }}
            
            @keyframes spin-inner {{
                100% {{ transform: rotate(-360deg); }}
            }}
            
            @keyframes spin-inner-reverse {{
                100% {{ transform: rotate(360deg); }}
            }}
            
            .typing-text {{
                font-size: 42px;
                font-weight: 900;
                fill: url(#neon-blue);
                letter-spacing: 2px;
                animation: typing 4s steps(40, end) infinite, blink .75s step-end infinite;
                white-space: nowrap;
                overflow: hidden;
                border-right: 3px solid #00F5FF;
            }}
            
            .subtitle {{
                font-size: 20px;
                fill: #a0a0a0;
                font-weight: 400;
                animation: fade-up 2s ease-out;
            }}
            
            .profile-pulse {{
                animation: pulse 4s infinite alternate;
            }}
            
            @keyframes pulse {{
                0% {{ filter: drop-shadow(0 0 10px #00F5FF); transform: scale(0.98); }}
                100% {{ filter: drop-shadow(0 0 30px #4F46E5); transform: scale(1.02); }}
            }}

            @keyframes fade-up {{
                0% {{ opacity: 0; transform: translateY(20px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </defs>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="url(#bg-grad)" />
    
    <!-- Stars / Particles -->
    <g id="stars">
'''

    # Generate stars
    import random
    random.seed(42)
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.uniform(0.5, 2.5)
        opacity = random.uniform(0.2, 0.8)
        svg += f'        <circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity="{opacity}" class="star" />\n'

    svg += '''
    </g>

    <!-- Glowing Grid / Aurora Simulation -->
    <path d="M0,800 C300,700 600,900 1200,600 L1200,800 L0,800 Z" fill="rgba(79, 70, 229, 0.1)" filter="url(#glow-heavy)" />
    <path d="M0,700 C400,800 800,500 1200,700 L1200,800 L0,800 Z" fill="rgba(0, 245, 255, 0.1)" filter="url(#glow-heavy)" />

    <!-- Center Profile -->
    <g transform="translate(600, 450)" class="profile-pulse">
        <!-- Holographic rings -->
        <circle cx="0" cy="0" r="105" fill="none" stroke="url(#neon-blue)" stroke-width="2" filter="url(#glow)" />
        <circle cx="0" cy="0" r="115" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1" stroke-dasharray="10 5" />
        <circle cx="0" cy="0" r="95" fill="#000" />
        
        <!-- VR/AI Vector Avatar inside center -->
        <circle cx="0" cy="-20" r="30" fill="#0EA5E9" opacity="0.8" filter="url(#glow)"/>
        <path d="M-40,40 Q0,0 40,40 L30,80 L-30,80 Z" fill="#4F46E5" opacity="0.8" filter="url(#glow)"/>
        <text x="0" y="20" fill="#fff" text-anchor="middle" font-size="12" font-weight="bold">AMIT</text>
    </g>

    <!-- Inner Orbit (Tech Stack) -->
    <g class="orbit-inner">
'''

    tech_stack = ["Python", "AI", "ML", "AWS", "Docker", "Linux", "React", "Next.js", "Node", "FastAPI", "SQL", "Git", "K8s", "DevOps"]
    inner_radius = 220
    for i, tech in enumerate(tech_stack):
        angle = (i / len(tech_stack)) * 2 * math.pi
        x = width/2 + inner_radius * math.cos(angle)
        y = 450 + inner_radius * math.sin(angle)
        svg += f'''
        <g transform="translate({x},{y})">
            <g class="orbit-inner-reverse">
                <circle cx="0" cy="0" r="28" fill="url(#glass)" stroke="rgba(255,255,255,0.2)" stroke-width="1" />
                <text x="0" y="4" fill="#00F5FF" font-size="10" font-weight="bold" text-anchor="middle" filter="url(#glow)">{tech}</text>
            </g>
        </g>
'''

    svg += '''
    </g>

    <!-- Outer Orbit (Varanasi Cards) -->
    <g class="orbit-outer" style="transform-style: preserve-3d;">
'''

    varanasi_images = ["Kashi Corridor", "BHU Campus", "Aerial BHU", "Sarnath", "Buddha", "Vishwanath", "Ganga Ghats", "Sunrise Boat", "Evening Ghat", "Skyline"]
    outer_radius = 350
    for i, img in enumerate(varanasi_images):
        angle = (i / len(varanasi_images)) * 2 * math.pi
        x = width/2 + outer_radius * math.cos(angle)
        y = 450 + outer_radius * math.sin(angle)
        
        # We apply an anti-rotation to keep the cards upright
        svg += f'''
        <g transform="translate({x},{y})">
            <g class="orbit-outer-reverse">
                <!-- 3D Glass Card -->
                <rect x="-60" y="-80" width="120" height="160" rx="10" fill="url(#glass)" stroke="url(#neon-cyan)" stroke-width="1.5" filter="url(#glow)" />
                <rect x="-60" y="-80" width="120" height="160" rx="10" fill="rgba(0,0,0,0.5)" />
                <!-- Inner design representing the place -->
                <circle cx="0" cy="-20" r="30" fill="none" stroke="#4F46E5" stroke-width="2" />
                <path d="M-15,-10 L0,-30 L15,-10 Z" fill="#00F5FF" opacity="0.6" />
                <text x="0" y="40" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">{img}</text>
                <text x="0" y="60" fill="#0EA5E9" font-size="8" text-anchor="middle">VARANASI</text>
            </g>
        </g>
'''

    svg += '''
    </g>

    <!-- Top Text Section -->
    <g transform="translate(600, 100)">
        <text x="0" y="0" text-anchor="middle" class="typing-text">Hello World, I'm Amit Kumar</text>
        <text x="0" y="40" text-anchor="middle" class="subtitle">AI Engineer | Machine Learning | Future Builder</text>
    </g>
</svg>
'''
    with open("assets/hero_orbit.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_panels_svg():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255,255,255,0.15)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0.02)" />
        </linearGradient>
        <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#6366F1" />
        </linearGradient>
        <style>
text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
            .float {{ animation: float 6s ease-in-out infinite; }}
            .float-delayed {{ animation: float 6s ease-in-out 3s infinite; }}
            @keyframes float {{
                0% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-10px); }}
                100% {{ transform: translateY(0px); }}
            }}
        </style>
    </defs>
    <!-- Background is transparent to blend with GitHub Dark mode -->
    
    <!-- About Me Panel (Left) -->
    <g transform="translate(50, 50)" class="float">
        <rect x="0" y="0" width="530" height="400" rx="20" fill="url(#glass)" stroke="url(#border-grad)" stroke-width="2" />
        <text x="40" y="60" fill="#00F5FF" font-size="28" font-weight="600">About Me</text>
        <rect x="40" y="80" width="100" height="3" fill="#6366F1" />
        
        <text x="40" y="140" fill="#fff" font-size="16">
            <tspan x="40" dy="0">• Final Year CSE Student bridging theory &amp; production</tspan>
            <tspan x="40" dy="35">• Architecting advanced Machine Learning solutions</tspan>
            <tspan x="40" dy="35">• Cloud-native MLOps and scalable deployments</tspan>
            <tspan x="40" dy="35">• Open Source Contributor &amp; Tech Enthusiast</tspan>
            <tspan x="40" dy="35">• Passionate about the intersection of VR and AI</tspan>
        </text>
    </g>

    <!-- Current Focus (Right) -->
    <g transform="translate(620, 50)" class="float-delayed">
        <rect x="0" y="0" width="530" height="400" rx="20" fill="url(#glass)" stroke="url(#border-grad)" stroke-width="2" />
        <text x="40" y="60" fill="#00D4FF" font-size="28" font-weight="600">Current Focus</text>
        <rect x="40" y="80" width="100" height="3" fill="#0EA5E9" />
        
        <g transform="translate(40, 130)">
            <rect x="0" y="0" width="200" height="60" rx="8" fill="rgba(79, 70, 229, 0.2)" stroke="rgba(79, 70, 229, 0.5)"/>
            <text x="100" y="36" fill="#fff" text-anchor="middle" font-size="16">LLMs &amp; GenAI</text>
            
            <rect x="230" y="0" width="200" height="60" rx="8" fill="rgba(0, 245, 255, 0.2)" stroke="rgba(0, 245, 255, 0.5)"/>
            <text x="330" y="36" fill="#fff" text-anchor="middle" font-size="16">RAG Pipelines</text>

            <rect x="0" y="80" width="200" height="60" rx="8" fill="rgba(14, 165, 233, 0.2)" stroke="rgba(14, 165, 233, 0.5)"/>
            <text x="100" y="116" fill="#fff" text-anchor="middle" font-size="16">Deep Learning</text>

            <rect x="230" y="80" width="200" height="60" rx="8" fill="rgba(99, 102, 241, 0.2)" stroke="rgba(99, 102, 241, 0.5)"/>
            <text x="330" y="116" fill="#fff" text-anchor="middle" font-size="16">Real-World Apps</text>
        </g>
    </g>
</svg>
'''
    with open("assets/about_panels.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_skills_svg():
    width = 1200
    height = 400
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <linearGradient id="bar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#4F46E5" />
            <stop offset="100%" stop-color="#00F5FF" />
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <style>
text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
            .fill-anim {{
                animation: fillBar 2s ease-out forwards;
            }}
            @keyframes fillBar {{
                0% {{ width: 0; }}
            }}
        </style>
    </defs>
'''
    skills = [
        ("Python & Backend", 90),
        ("Machine Learning", 85),
        ("Cloud & DevOps", 75),
        ("React & Frontend", 70)
    ]
    
    for i, (name, val) in enumerate(skills):
        y = 50 + i * 80
        svg += f'''
    <text x="50" y="{y+15}" fill="#fff" font-size="18" font-weight="600">{name}</text>
    <text x="{1000}" y="{y+15}" fill="#00F5FF" font-size="18" font-weight="600" text-anchor="end">{val}%</text>
    <!-- Background Bar -->
    <rect x="50" y="{y+30}" width="950" height="15" rx="7.5" fill="rgba(255,255,255,0.05)" />
    <!-- Filled Bar -->
    <rect x="50" y="{y+30}" width="{9.5 * val}" height="15" rx="7.5" fill="url(#bar-grad)" filter="url(#glow)" class="fill-anim" />
'''

    svg += '</svg>'
    with open("assets/skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_footer_svg():
    width = 1200
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <linearGradient id="sky-grad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#050510" />
            <stop offset="100%" stop-color="#1a1a3a" />
        </linearGradient>
        <linearGradient id="river-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#0a1526" />
            <stop offset="50%" stop-color="#142b4a" />
            <stop offset="100%" stop-color="#0a1526" />
        </linearGradient>
        <filter id="moon-glow">
            <feGaussianBlur stdDeviation="10" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <style>
text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
            .water-flow {{
                animation: flow 10s linear infinite;
            }}
            .boat-move {{
                animation: sail 20s linear infinite;
            }}
            @keyframes flow {{
                0% {{ transform: translateX(0); }}
                100% {{ transform: translateX(-1200px); }}
            }}
            @keyframes sail {{
                0% {{ transform: translateX(-100px); }}
                100% {{ transform: translateX(1300px); }}
            }}
        </style>
    </defs>
    
    <!-- Night Sky -->
    <rect width="100%" height="200" fill="url(#sky-grad)" />
    
    <!-- Moon -->
    <circle cx="200" cy="80" r="40" fill="#fff" filter="url(#moon-glow)" />
    <!-- Moon Texture -->
    <circle cx="210" cy="70" r="10" fill="rgba(0,0,0,0.1)" />
    <circle cx="180" cy="90" r="15" fill="rgba(0,0,0,0.1)" />
    
    <!-- Skyline Silhouette (Varanasi Ghats & Temples) -->
    <path d="M0,200 L0,150 L30,150 L50,110 L70,150 L150,150 L180,100 L210,150 L300,150 L350,80 L400,150 L500,150 L550,120 L600,150 L750,150 L800,90 L850,150 L1000,150 L1050,110 L1100,150 L1200,150 L1200,200 Z" fill="#0a0a1a" />
    
    <!-- River Ganga -->
    <g transform="translate(0, 200)">
        <rect width="2400" height="100" fill="url(#river-grad)" class="water-flow" />
        <rect width="1200" height="100" fill="rgba(0,245,255,0.05)" />
        
        <!-- Moon Reflection in water -->
        <rect x="160" y="0" width="80" height="10" fill="rgba(255,255,255,0.3)" />
        <rect x="170" y="15" width="60" height="8" fill="rgba(255,255,255,0.2)" />
        <rect x="180" y="30" width="40" height="6" fill="rgba(255,255,255,0.1)" />
        
        <!-- Boat -->
        <g class="boat-move" transform="translate(0, 20)">
            <path d="M0,0 L40,0 L50,10 L-10,10 Z" fill="#000" />
            <rect x="15" y="-15" width="2" height="15" fill="#555" />
        </g>
    </g>
    
    <text x="600" y="280" fill="rgba(255,255,255,0.5)" font-size="14" text-anchor="middle">Made with code and magic • Inspired by Varanasi • Amit Kumar</text>
</svg>
'''
    with open("assets/footer_varanasi.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_hero_svg()
    generate_panels_svg()
    generate_skills_svg()
    generate_footer_svg()
    print("SVGs generated successfully!")
