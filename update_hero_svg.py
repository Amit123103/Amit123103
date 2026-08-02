import math
import base64
import os

def generate_hero_svg_with_images():
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

        <!-- HD Image Enhancement Filter (Simulated high-quality HDR look) -->
        <filter id="hd-enhance">
            <feComponentTransfer>
                <!-- Increase contrast and brightness -->
                <feFuncR type="linear" slope="1.2" intercept="-0.1"/>
                <feFuncG type="linear" slope="1.2" intercept="-0.1"/>
                <feFuncB type="linear" slope="1.2" intercept="-0.1"/>
            </feComponentTransfer>
            <!-- Add a slight sharpening effect using feConvolveMatrix -->
            <feConvolveMatrix order="3" kernelMatrix="0 -1 0 -1 5 -1 0 -1 0" preserveAlpha="true" opacity="0.5" />
        </filter>

        <!-- Clip path for images to make them rounded -->
        <clipPath id="card-clip">
            <rect x="-60" y="-80" width="120" height="120" rx="10" />
        </clipPath>

        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&amp;display=swap');
            
            text {{ font-family: 'Inter', sans-serif; }}
            
            .star {{ animation: twinkle 3s infinite alternate; }}
            .star:nth-child(even) {{ animation-duration: 5s; animation-delay: 2s; }}
            
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
            
            @keyframes spin-outer {{ 100% {{ transform: rotate(360deg); }} }}
            @keyframes spin-outer-reverse {{ 100% {{ transform: rotate(-360deg); }} }}
            @keyframes spin-inner {{ 100% {{ transform: rotate(-360deg); }} }}
            @keyframes spin-inner-reverse {{ 100% {{ transform: rotate(360deg); }} }}
            
            .typing-text {{
                font-size: 42px; font-weight: 900; fill: url(#neon-blue);
                letter-spacing: 2px;
                animation: typing 4s steps(40, end) infinite, blink .75s step-end infinite;
                white-space: nowrap; overflow: hidden; border-right: 3px solid #00F5FF;
            }}
            
            .subtitle {{
                font-size: 20px; fill: #a0a0a0; font-weight: 400;
                animation: fade-up 2s ease-out;
            }}
            
            .profile-pulse {{ animation: pulse 4s infinite alternate; }}
            
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
    
    <rect width="100%" height="100%" fill="url(#bg-grad)" />
    
    <g id="stars">
'''

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

    <path d="M0,800 C300,700 600,900 1200,600 L1200,800 L0,800 Z" fill="rgba(79, 70, 229, 0.1)" filter="url(#glow-heavy)" />
    <path d="M0,700 C400,800 800,500 1200,700 L1200,800 L0,800 Z" fill="rgba(0, 245, 255, 0.1)" filter="url(#glow-heavy)" />

    <g transform="translate(600, 450)" class="profile-pulse">
        <circle cx="0" cy="0" r="105" fill="none" stroke="url(#neon-blue)" stroke-width="2" filter="url(#glow)" />
        <circle cx="0" cy="0" r="115" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1" stroke-dasharray="10 5" />
        <circle cx="0" cy="0" r="95" fill="#000" />
        
        <circle cx="0" cy="-20" r="30" fill="#0EA5E9" opacity="0.8" filter="url(#glow)"/>
        <path d="M-40,40 Q0,0 40,40 L30,80 L-30,80 Z" fill="#4F46E5" opacity="0.8" filter="url(#glow)"/>
        <text x="0" y="20" fill="#fff" text-anchor="middle" font-size="12" font-weight="bold">AMIT</text>
    </g>

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

    <g class="orbit-outer" style="transform-style: preserve-3d;">
'''

    varanasi_images_titles = ["Kashi Corridor", "BHU Campus", "Aerial BHU", "Sarnath", "Buddha", "Vishwanath", "Ganga Ghats", "Sunrise Boat", "Evening Ghat", "Skyline"]
    image_files = ["iv.jpg", "v2.jpg", "v3.jpg", "v4.jpg", "v5.jpg", "v6.jpg", "v7.jpg", "v8.jpg", "v9.jpg", "v10.jpg"]
    
    outer_radius = 350
    for i, img_title in enumerate(varanasi_images_titles):
        angle = (i / len(varanasi_images_titles)) * 2 * math.pi
        x = width/2 + outer_radius * math.cos(angle)
        y = 450 + outer_radius * math.sin(angle)
        
        # Load and base64 encode image
        img_path = os.path.join("assets", image_files[i % len(image_files)])
        b64_data = ""
        if os.path.exists(img_path):
            with open(img_path, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode('utf-8')
        
        b64_src = f"data:image/jpeg;base64,{b64_data}" if b64_data else ""
        
        svg += f'''
        <g transform="translate({x},{y})">
            <g class="orbit-outer-reverse">
                <!-- 3D Glass Card Background -->
                <rect x="-60" y="-80" width="120" height="150" rx="10" fill="url(#glass)" stroke="url(#neon-cyan)" stroke-width="2" filter="url(#glow)" />
                <rect x="-60" y="-80" width="120" height="150" rx="10" fill="rgba(0,0,0,0.8)" />
                
                <!-- HD Embedded Image -->
                <image href="{b64_src}" x="-60" y="-80" width="120" height="120" clip-path="url(#card-clip)" filter="url(#hd-enhance)" preserveAspectRatio="xMidYMid slice" />
                
                <!-- Gradient overlay to blend image bottom -->
                <rect x="-60" y="20" width="120" height="20" fill="url(#bg-grad)" opacity="0.8" />
                
                <!-- Text -->
                <text x="0" y="55" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">{img_title}</text>
            </g>
        </g>
'''

    svg += '''
    </g>

    <g transform="translate(600, 100)">
        <text x="0" y="0" text-anchor="middle" class="typing-text">Hello World, I'm Amit Kumar</text>
        <text x="0" y="40" text-anchor="middle" class="subtitle">AI Engineer | Machine Learning | Future Builder</text>
    </g>
</svg>
'''
    with open("assets/hero_orbit.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_hero_svg_with_images()
    print("hero_orbit.svg generated successfully with embedded high-quality images!")
