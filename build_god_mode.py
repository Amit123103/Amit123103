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

def generate_god_core():
    width = 1400
    height = 900
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <linearGradient id="space-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#020205" />
            <stop offset="30%" stop-color="#050a1f" />
            <stop offset="70%" stop-color="#0a192f" />
            <stop offset="100%" stop-color="#020205" />
        </linearGradient>
        <radialGradient id="nebula-grad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0.15)" />
            <stop offset="50%" stop-color="rgba(79, 70, 229, 0.05)" />
            <stop offset="100%" stop-color="rgba(0, 0, 0, 0)" />
        </radialGradient>
        <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="20%" stop-color="#00F5FF" />
            <stop offset="60%" stop-color="#4F46E5" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        
        <filter id="hyper-glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="arc-reactor" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="5" result="blur1" />
            <feGaussianBlur stdDeviation="20" result="blur2" />
            <feMerge>
                <feMergeNode in="blur2" />
                <feMergeNode in="blur1" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        
        <!-- Clipping for planets -->
        <clipPath id="hex-clip">
            <polygon points="30,0 60,15 60,45 30,60 0,45 0,15" />
        </clipPath>

        <style>
            @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&amp;display=swap');
            text {{ font-family: 'Share Tech Mono', monospace; }}
            
            .spin-fast {{ animation: spin 10s linear infinite; transform-origin: center; }}
            .spin-slow {{ animation: spin 30s linear infinite reverse; transform-origin: center; }}
            @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
            
            .pulse {{ animation: pulse 2s ease-in-out infinite alternate; }}
            @keyframes pulse {{ 0% {{ opacity: 0.7; transform: scale(0.95); }} 100% {{ opacity: 1; transform: scale(1.05); }} }}
            
            .orbit {{ animation: orbit-anim var(--dur) linear infinite; transform-origin: {width/2}px {height/2}px; }}
            .orbit-reverse {{ animation: orbit-rev var(--dur) linear infinite; transform-origin: center; }}
            @keyframes orbit-anim {{ 100% {{ transform: rotate(360deg); }} }}
            @keyframes orbit-rev {{ 100% {{ transform: rotate(-360deg); }} }}
            
            .glitch-text {{
                animation: glitch 3s infinite;
                fill: #00F5FF;
                font-size: 24px;
                letter-spacing: 5px;
            }}
            @keyframes glitch {{
                0% {{ opacity: 1; transform: skew(0deg); }}
                5% {{ opacity: 0.8; transform: skew(5deg); }}
                10% {{ opacity: 1; transform: skew(-5deg); }}
                15% {{ opacity: 1; transform: skew(0deg); }}
                100% {{ opacity: 1; }}
            }}
            
            .floating-particle {{
                animation: floatUp 15s linear infinite;
            }}
            @keyframes floatUp {{
                0% {{ transform: translateY(900px); opacity: 0; }}
                10% {{ opacity: 1; }}
                90% {{ opacity: 1; }}
                100% {{ transform: translateY(-100px); opacity: 0; }}
            }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#space-grad)" />
    <circle cx="50%" cy="50%" r="800" fill="url(#nebula-grad)" class="pulse" />
    
    <!-- Matrix Rain / Particles -->
    <g id="particles">
'''
    random.seed(999)
    for _ in range(80):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.uniform(1, 3)
        dur = random.uniform(10, 25)
        delay = random.uniform(0, 15)
        svg += f'        <circle cx="{x}" cy="{y}" r="{r}" fill="#00F5FF" style="animation: floatUp {dur}s linear {delay}s infinite" opacity="0" class="floating-particle" filter="url(#hyper-glow)" />\n'

    svg += '''
    </g>

    <!-- Top Text HUD -->
    <g transform="translate(700, 80)">
        <text x="0" y="0" text-anchor="middle" class="glitch-text">SYSTEM INITIALIZING...</text>
        <text x="0" y="30" text-anchor="middle" fill="#4F46E5" font-size="16" style="animation: pulse 1s infinite alternate">AUTHENTICATING HUMAN VISITOR // ACCESS GRANTED</text>
        <text x="0" y="70" text-anchor="middle" fill="#FFFFFF" font-size="48" font-weight="bold" filter="url(#hyper-glow)" letter-spacing="10">AMIT'S DIGITAL UNIVERSE</text>
    </g>

    <!-- Central AI Core (The Sun) -->
    <g transform="translate(700, 500)">
        <!-- Outer Energy Ring -->
        <g class="spin-slow">
            <circle cx="0" cy="0" r="160" fill="none" stroke="rgba(0, 245, 255, 0.2)" stroke-width="2" stroke-dasharray="10 30" />
            <circle cx="0" cy="0" r="150" fill="none" stroke="#4F46E5" stroke-width="1" stroke-dasharray="50 15" />
        </g>
        
        <!-- Hexagon Armor -->
        <g class="spin-fast">
            <polygon points="0,-120 104,-60 104,60 0,120 -104,60 -104,-60" fill="none" stroke="#00F5FF" stroke-width="3" filter="url(#arc-reactor)" opacity="0.8"/>
            <polygon points="0,-100 86,-50 86,50 0,100 -86,50 -86,-50" fill="none" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="10 5" />
        </g>
        
        <!-- Reactor Core Glow -->
        <circle cx="0" cy="0" r="70" fill="url(#core-glow)" filter="url(#arc-reactor)" class="pulse" />
        
        <!-- Central Data Hub -->
        <circle cx="0" cy="0" r="40" fill="#000" stroke="#00F5FF" stroke-width="4" filter="url(#hyper-glow)" />
        <text x="0" y="8" fill="#FFF" text-anchor="middle" font-size="24" font-weight="bold">AI</text>
    </g>
    
    <!-- Planetary Orbits (Uploaded Images) -->
    <g id="solar-system">
'''

    images = ["iv.jpg", "v2.jpg", "v3.jpg", "v4.jpg", "v5.jpg", "v6.jpg", "v7.jpg", "v8.jpg", "v9.jpg", "v10.jpg"]
    radii = [240, 280, 320, 360, 400, 440, 480, 520, 560, 600]
    durations = [30, 35, 45, 50, 60, 70, 80, 90, 100, 110]
    
    for i, img in enumerate(images):
        b64 = get_base64_image(img)
        r = radii[i]
        dur = durations[i]
        angle = (i * 36)
        
        # Calculate initial position just to lay it out, but animation handles rotation
        x = width/2 + r * math.cos(math.radians(angle))
        y = 500 + r * math.sin(math.radians(angle))
        
        svg += f'''
        <!-- Orbit Path -->
        <circle cx="700" cy="500" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
        
        <!-- Planet Group -->
        <g class="orbit" style="--dur: {dur}s; transform: rotate({angle}deg);">
            <g transform="translate({r}, 0)">
                <g class="orbit-reverse" style="--dur: {dur}s;">
                    <!-- Hexagonal Image Crystal -->
                    <g transform="translate(-30, -30)">
                        <polygon points="30,0 60,15 60,45 30,60 0,45 0,15" fill="rgba(0, 245, 255, 0.1)" stroke="#00F5FF" stroke-width="2" filter="url(#hyper-glow)" />
                        <image href="{b64}" x="0" y="0" width="60" height="60" clip-path="url(#hex-clip)" preserveAspectRatio="xMidYMid slice" opacity="0.9" />
                    </g>
                    <!-- Small moon orbiting the planet -->
                    <circle cx="45" cy="0" r="3" fill="#4F46E5" filter="url(#hyper-glow)">
                        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="5s" repeatCount="indefinite" />
                    </circle>
                </g>
            </g>
        </g>
'''

    svg += '''
    </g>
</svg>
'''
    with open("assets/god_core.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_god_hud():
    width = 1200
    height = 600
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&amp;display=swap');
            text {{ font-family: 'Share Tech Mono', monospace; }}
            
            .hud-panel {{
                fill: rgba(2, 6, 23, 0.6);
                stroke: #00F5FF;
                stroke-width: 1.5;
            }}
            .scan-line {{
                animation: scan 4s linear infinite;
                fill: rgba(0, 245, 255, 0.2);
            }}
            @keyframes scan {{
                0% {{ transform: translateY(-20px); opacity: 0; }}
                10% {{ opacity: 1; }}
                90% {{ opacity: 1; }}
                100% {{ transform: translateY(400px); opacity: 0; }}
            }}
            
            .glow-text {{ fill: #00F5FF; filter: drop-shadow(0 0 5px #00F5FF); }}
            
            .energy-bar-fill {{
                animation: charge 3s ease-out forwards;
            }}
            @keyframes charge {{ 0% {{ width: 0; }} }}
            
            .hex-module {{
                animation: floatHex 6s ease-in-out infinite;
            }}
            @keyframes floatHex {{
                0% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-10px); }}
                100% {{ transform: translateY(0); }}
            }}
        </style>
        
        <filter id="hud-glow">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <linearGradient id="plasma" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#4F46E5" />
            <stop offset="50%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#FFFFFF" />
        </linearGradient>
    </defs>
    
    <!-- Left Panel: Digital HUD About -->
    <g transform="translate(50, 50)">
        <polygon points="0,20 20,0 500,0 500,400 480,420 0,420" class="hud-panel" filter="url(#hud-glow)" />
        <rect x="5" y="5" width="490" height="410" fill="none" stroke="rgba(255,255,255,0.1)" stroke-dasharray="4 4" />
        
        <rect x="0" y="0" width="500" height="20" class="scan-line" />
        
        <text x="30" y="50" class="glow-text" font-size="24">> TERMINAL_01 // ABOUT</text>
        <text x="30" y="90" fill="#FFF" font-size="16">> IDENT: FINAL YEAR CSE STUDENT</text>
        <text x="30" y="130" fill="#FFF" font-size="16">> ROLE: AI &amp; ML ARCHITECT</text>
        <text x="30" y="170" fill="#FFF" font-size="16">> SECTOR: CLOUD NATIVE MLOPS</text>
        <text x="30" y="210" fill="#FFF" font-size="16">> DIRECTIVE: BUILD THE FUTURE</text>
        <text x="30" y="250" fill="#FFF" font-size="16">> STATUS: ONLINE &amp; READY</text>
        
        <!-- Corner decorations -->
        <path d="M-5,15 L-5,-5 L15,-5" fill="none" stroke="#00F5FF" stroke-width="3" />
        <path d="M485,-5 L505,-5 L505,15" fill="none" stroke="#00F5FF" stroke-width="3" />
        <path d="M-5,405 L-5,425 L15,425" fill="none" stroke="#00F5FF" stroke-width="3" />
        <path d="M485,425 L505,425 L505,405" fill="none" stroke="#00F5FF" stroke-width="3" />
    </g>
    
    <!-- Right Panel: AI Modules (Skills) -->
    <g transform="translate(620, 50)">
        <polygon points="0,0 480,0 500,20 500,420 20,420 0,400" class="hud-panel" filter="url(#hud-glow)" />
        <text x="30" y="50" class="glow-text" font-size="24">> NEURAL_NETWORK // CAPABILITIES</text>
        
        <g transform="translate(30, 90)">
'''
    skills = [("PYTHON", 95), ("MACHINE LEARNING", 90), ("AWS CLOUD", 85), ("DOCKER", 80), ("REACT", 75)]
    for i, (skill, level) in enumerate(skills):
        y = i * 60
        svg += f'''
            <text x="0" y="{y + 15}" fill="#FFF" font-size="14">{skill}</text>
            <text x="440" y="{y + 15}" fill="#00F5FF" font-size="14" text-anchor="end">{level}%</text>
            <rect x="0" y="{y + 25}" width="440" height="8" fill="rgba(255,255,255,0.1)" />
            <rect x="0" y="{y + 25}" width="{4.4 * level}" height="8" fill="url(#plasma)" class="energy-bar-fill" filter="url(#hud-glow)" />
'''
    svg += '''
        </g>
    </g>
</svg>
'''
    with open("assets/god_hud.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_god_footer():
    width = 1200
    height = 400
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            .drone {{ animation: fly 20s linear infinite; }}
            @keyframes fly {{
                0% {{ transform: translate(-100px, 150px); }}
                50% {{ transform: translate(600px, 50px); }}
                100% {{ transform: translate(1300px, 150px); }}
            }}
            .water-glitch {{ animation: wave 5s infinite; }}
            @keyframes wave {{ 0% {{ opacity: 0.8; }} 50% {{ opacity: 0.5; }} 100% {{ opacity: 0.8; }} }}
        </style>
        <linearGradient id="cyber-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#050014" />
            <stop offset="100%" stop-color="#1b0033" />
        </linearGradient>
        <filter id="neon-glow"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>
    </defs>
    
    <rect width="100%" height="300" fill="url(#cyber-sky)" />
    
    <!-- Huge Cyber Moon -->
    <circle cx="600" cy="150" r="100" fill="rgba(0, 245, 255, 0.1)" filter="url(#neon-glow)" />
    <circle cx="600" cy="150" r="98" fill="none" stroke="#00F5FF" stroke-dasharray="10 20" stroke-width="2" class="drone" style="animation-duration:60s; transform-origin:600px 150px;" />
    
    <!-- Cyber Varanasi Skyline -->
    <path d="M0,300 L0,220 L30,220 L50,150 L80,220 L150,220 L180,130 L220,220 L300,220 L350,110 L420,220 L500,220 L550,160 L620,220 L750,220 L800,120 L860,220 L1000,220 L1050,150 L1120,220 L1200,220 L1200,300 Z" fill="#090014" />
    <!-- Neon Highlights on Temples -->
    <path d="M50,150 L50,220 M180,130 L180,220 M350,110 L350,220 M550,160 L550,220 M800,120 L800,220" stroke="#00F5FF" stroke-width="2" filter="url(#neon-glow)" opacity="0.5" />
    
    <!-- AI Drone -->
    <g class="drone">
        <circle cx="0" cy="0" r="5" fill="#FFF" filter="url(#neon-glow)" />
        <rect x="-10" y="-2" width="20" height="4" fill="#4F46E5" />
        <path d="M-10,0 L-30,10 M10,0 L30,10" stroke="#00F5FF" stroke-width="1" />
    </g>
    
    <!-- Digital River -->
    <g transform="translate(0, 300)">
        <rect width="1200" height="100" fill="#050014" />
        <rect width="1200" height="100" fill="rgba(0, 245, 255, 0.1)" class="water-glitch" />
        
        <!-- Digital Moon Reflection -->
        <rect x="500" y="10" width="200" height="5" fill="rgba(0, 245, 255, 0.5)" filter="url(#neon-glow)" />
        <rect x="520" y="30" width="160" height="5" fill="rgba(0, 245, 255, 0.4)" filter="url(#neon-glow)" />
        <rect x="550" y="50" width="100" height="5" fill="rgba(0, 245, 255, 0.3)" filter="url(#neon-glow)" />
        
        <!-- Cyber Boat -->
        <g transform="translate(800, 20)">
            <path d="M0,0 L60,0 L70,15 L-10,15 Z" fill="#1b0033" stroke="#00F5FF" stroke-width="1" filter="url(#neon-glow)" />
            <rect x="25" y="-20" width="2" height="20" fill="#00F5FF" filter="url(#neon-glow)" />
        </g>
    </g>
</svg>
'''
    with open("assets/god_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    print("Initializing God Mode SVGs...")
    generate_god_core()
    generate_god_hud()
    generate_god_footer()
    print("Universe successfully simulated in assets directory.")
