import math
import base64
import os
import xml.etree.ElementTree as ET

def generate_quantum_hero():
    width = 1200
    height = 500
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; fill: #FFFFFF; }}
            .glow-cyan {{ filter: drop-shadow(0 0 12px rgba(0, 245, 255, 0.8)); }}
            .glow-gold {{ filter: drop-shadow(0 0 12px rgba(255, 215, 0, 0.8)); }}
            
            .spin-cw {{ animation: spin 20s linear infinite; transform-origin: 600px 200px; }}
            .spin-ccw {{ animation: spin 30s linear infinite reverse; transform-origin: 600px 200px; }}
            .pulse-core {{ animation: pulse 3.5s ease-in-out infinite alternate; transform-origin: 600px 200px; }}
            
            @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
            @keyframes pulse {{ 0% {{ transform: scale(0.96); opacity: 0.85; }} 100% {{ transform: scale(1.04); opacity: 1; }} }}
            
            .fade-in {{ animation: fadeIn 1.5s ease-out forwards; }}
            @keyframes fadeIn {{ 0% {{ opacity: 0; transform: translateY(15px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}
        </style>
        
        <radialGradient id="quantum-bg" cx="50%" cy="40%" r="75%">
            <stop offset="0%" stop-color="#0c1021" />
            <stop offset="50%" stop-color="#050814" />
            <stop offset="100%" stop-color="#020308" />
        </radialGradient>
        
        <linearGradient id="cyan-gold" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="50%" stop-color="#7B2CBF" />
            <stop offset="100%" stop-color="#FFD700" />
        </linearGradient>

        <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="50%" stop-color="#FFFFFF" />
            <stop offset="100%" stop-color="#FFD700" />
        </linearGradient>
        
        <pattern id="cyber-grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0, 245, 255, 0.04)" stroke-width="1" />
        </pattern>
    </defs>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="url(#quantum-bg)" rx="16" />
    <rect width="100%" height="100%" fill="url(#cyber-grid)" rx="16" />
    
    <!-- Cyber Ring HUD Core -->
    <g class="pulse-core">
        <circle cx="600" cy="200" r="145" fill="none" stroke="url(#cyan-gold)" stroke-width="1.5" opacity="0.35" />
        <circle cx="600" cy="200" r="125" fill="none" stroke="rgba(0, 245, 255, 0.25)" stroke-width="1" stroke-dasharray="14 8" class="spin-cw" />
        <circle cx="600" cy="200" r="105" fill="none" stroke="rgba(255, 215, 0, 0.35)" stroke-width="2" stroke-dasharray="30 15 5 15" class="spin-ccw" />
        <circle cx="600" cy="200" r="78" fill="rgba(0, 245, 255, 0.04)" stroke="#00F5FF" stroke-width="2" class="glow-cyan" />
        
        <!-- Central Emblem / Name -->
        <text x="600" y="208" font-size="30" font-weight="900" text-anchor="middle" letter-spacing="6" fill="url(#text-grad)">AMIT KUMAR</text>
    </g>
    
    <!-- Typography & Badges -->
    <g class="fade-in" transform="translate(600, 375)">
        <text x="0" y="-10" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="4" fill="#00F5FF">SENIOR AI ENGINEER &amp; CLOUD ARCHITECT</text>
        <text x="0" y="18" font-size="15" font-weight="500" text-anchor="middle" fill="#94A3B8">BUILDING SCALABLE LLM SYSTEMS • RAG PIPELINES • CLOUD INFRASTRUCTURE</text>
        
        <!-- Interactive Status Badges -->
        <g transform="translate(-200, 42)">
            <rect x="0" y="0" width="180" height="34" rx="17" fill="rgba(0, 245, 255, 0.08)" stroke="#00F5FF" stroke-width="1" />
            <circle cx="20" cy="17" r="4" fill="#00FF87" class="glow-cyan" />
            <text x="100" y="22" font-size="12" font-weight="700" text-anchor="middle" fill="#00F5FF">AVAILABLE FOR HIRING</text>
        </g>

        <g transform="translate(20, 42)">
            <rect x="0" y="0" width="180" height="34" rx="17" fill="rgba(255, 215, 0, 0.08)" stroke="#FFD700" stroke-width="1" />
            <circle cx="20" cy="17" r="4" fill="#FFD700" class="glow-gold" />
            <text x="100" y="22" font-size="12" font-weight="700" text-anchor="middle" fill="#FFD700">BASED IN INDIA (UTC+5:30)</text>
        </g>
    </g>
</svg>
'''
    with open("assets/quantum_hero.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated quantum_hero.svg")

def generate_quantum_about():
    width = 1200
    height = 420
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .card {{ fill: rgba(15, 23, 42, 0.7); stroke: rgba(0, 245, 255, 0.25); stroke-width: 1; rx: 14; }}
            .glow-border {{ filter: drop-shadow(0 0 8px rgba(0, 245, 255, 0.2)); }}
        </style>
        
        <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(15, 23, 42, 0.85)" />
            <stop offset="100%" stop-color="rgba(30, 41, 59, 0.55)" />
        </linearGradient>
    </defs>
    
    <!-- Title -->
    <text x="600" y="40" font-size="20" font-weight="700" text-anchor="middle" letter-spacing="3" fill="#00F5FF">ABOUT ME &amp; SYSTEM TELEMETRY</text>
    <rect x="580" y="52" width="40" height="2" fill="#FFD700" />
    
    <!-- Biography Overview Banner -->
    <g transform="translate(60, 80)">
        <rect x="0" y="0" width="1080" height="85" fill="url(#card-grad)" stroke="#00F5FF" stroke-width="1" rx="12" />
        <text x="25" y="32" font-size="15" font-weight="700" fill="#00F5FF">👨‍💻 BIOGRAPHY</text>
        <text x="25" y="58" font-size="13" fill="#CBD5E1">I am a passionate Senior AI Engineer &amp; Cloud Architect focused on building high-performance Agentic AI workflows, vector search systems, and cloud microservices. I bridge the gap between cutting-edge Machine Learning R&amp;D and production-grade software engineering.</text>
    </g>

    <!-- 3 Cards Layout -->
    <!-- Card 1 -->
    <g transform="translate(60, 185)" class="glow-border">
        <rect x="0" y="0" width="340" height="205" fill="url(#card-grad)" stroke="#00F5FF" stroke-width="1" rx="14" />
        <text x="25" y="35" font-size="15" font-weight="700" fill="#00F5FF">🚀 CURRENT FOCUS</text>
        <text x="25" y="68" font-size="13" fill="#CBD5E1">• Generative AI &amp; Agent Workflows</text>
        <text x="25" y="96" font-size="13" fill="#CBD5E1">• Production RAG &amp; Vector DBs</text>
        <text x="25" y="124" font-size="13" fill="#CBD5E1">• High-Scale Distributed Cloud</text>
        <text x="25" y="152" font-size="13" fill="#CBD5E1">• Fine-Tuning LLM Models</text>
        <rect x="25" y="175" width="290" height="4" fill="#00F5FF" rx="2" opacity="0.6" />
    </g>
    
    <!-- Card 2 -->
    <g transform="translate(430, 185)" class="glow-border">
        <rect x="0" y="0" width="340" height="205" fill="url(#card-grad)" stroke="#FFD700" stroke-width="1" rx="14" />
        <text x="25" y="35" font-size="15" font-weight="700" fill="#FFD700">⚡ KEY METRICS</text>
        <text x="25" y="68" font-size="13" fill="#CBD5E1">• Production Systems: <tspan fill="#00FF87" font-weight="700">12+</tspan></text>
        <text x="25" y="96" font-size="13" fill="#CBD5E1">• Total Git Commits: <tspan fill="#00F5FF" font-weight="700">2,500+</tspan></text>
        <text x="25" y="124" font-size="13" fill="#CBD5E1">• Production Uptime: <tspan fill="#00FF87" font-weight="700">99.9%</tspan></text>
        <text x="25" y="152" font-size="13" fill="#CBD5E1">• Open Source Impact: <tspan fill="#FFD700" font-weight="700">Top 5%</tspan></text>
        <rect x="25" y="175" width="290" height="4" fill="#FFD700" rx="2" opacity="0.6" />
    </g>

    <!-- Card 3 -->
    <g transform="translate(800, 185)" class="glow-border">
        <rect x="0" y="0" width="340" height="205" fill="url(#card-grad)" stroke="#FF007F" stroke-width="1" rx="14" />
        <text x="25" y="35" font-size="15" font-weight="700" fill="#FF007F">🌐 CLOUD &amp; INFRASTRUCTURE</text>
        <text x="25" y="68" font-size="13" fill="#CBD5E1">• Cloud: AWS, GCP, Azure</text>
        <text x="25" y="96" font-size="13" fill="#CBD5E1">• Frameworks: PyTorch, FastAPI</text>
        <text x="25" y="124" font-size="13" fill="#CBD5E1">• Containers: Docker, K8s</text>
        <text x="25" y="152" font-size="13" fill="#CBD5E1">• Storage: PostgreSQL, Redis</text>
        <rect x="25" y="175" width="290" height="4" fill="#FF007F" rx="2" opacity="0.6" />
    </g>
</svg>
'''
    with open("assets/quantum_about.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated quantum_about.svg")

def generate_quantum_skills():
    width = 1200
    height = 540
    
    categories = [
        ("AI &amp; DEEP LEARNING MATRIX", ["Python", "PyTorch", "TensorFlow", "OpenCV", "Scikit-Learn", "LLMs", "RAG Systems", "LangChain", "OpenAI", "Vector DBs"]),
        ("CLOUD &amp; DEVOPS INFRASTRUCTURE", ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Linux Admin", "Nginx", "PostgreSQL", "Redis"]),
        ("FULL-STACK &amp; SYSTEM ENGINE", ["FastAPI", "Node.js", "React", "TypeScript", "Next.js", "GraphQL", "REST APIs", "TailwindCSS", "Git"])
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .pill {{ fill: rgba(15, 23, 42, 0.75); stroke: rgba(0, 245, 255, 0.35); stroke-width: 1; rx: 18; transition: all 0.3s; }}
            .pill-anim {{ animation: floatPill 3s ease-in-out infinite alternate; }}
            @keyframes floatPill {{ 0% {{ transform: translateY(0px); stroke: rgba(0, 245, 255, 0.35); }} 100% {{ transform: translateY(-4px); stroke: #FFD700; }} }}
        </style>
    </defs>
    
    <text x="600" y="40" font-size="20" font-weight="700" text-anchor="middle" letter-spacing="3" fill="#00F5FF">TECHNICAL EXPERTISE MATRIX</text>
    <rect x="580" y="52" width="40" height="2" fill="#00F5FF" />
'''

    y_offset = 100
    for title, skills in categories:
        svg += f'''
        <text x="80" y="{y_offset}" font-size="15" font-weight="700" fill="#FFD700" letter-spacing="1.5">{title}</text>
        <line x1="80" y1="{y_offset + 12}" x2="1120" y2="{y_offset + 12}" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1" />
'''
        x = 80
        y = y_offset + 32
        
        for i, skill in enumerate(skills):
            w = len(skill) * 10 + 44
            if x + w > 1120:
                x = 80
                y += 48
                
            delay = (i * 0.15) % 2.5
            svg += f'''
            <g transform="translate({x}, {y})">
                <g class="pill-anim" style="animation-delay: {delay:.2f}s;">
                    <rect x="0" y="0" width="{w}" height="36" class="pill" />
                    <circle cx="18" cy="18" r="4" fill="#00F5FF" />
                    <text x="{18 + (w-18)/2}" y="23" font-size="13" font-weight="600" text-anchor="middle">{skill}</text>
                </g>
            </g>
'''
            x += w + 14
        y_offset = y + 70

    svg += '</svg>'
    with open("assets/quantum_skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated quantum_skills.svg")

def generate_quantum_projects():
    width = 1200
    height = 460
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .proj-card {{ fill: rgba(15, 23, 42, 0.75); stroke: rgba(0, 245, 255, 0.3); stroke-width: 1; rx: 14; }}
            .tag {{ fill: rgba(0, 245, 255, 0.1); stroke: #00F5FF; stroke-width: 1; rx: 10; }}
            .btn {{ fill: #00F5FF; rx: 8; }}
            .hover-card {{ animation: cardFloat 5s ease-in-out infinite alternate; }}
            @keyframes cardFloat {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-8px); }} }}
        </style>
    </defs>
    
    <text x="600" y="40" font-size="20" font-weight="700" text-anchor="middle" letter-spacing="3" fill="#00F5FF">FEATURED QUANTUM PROJECTS</text>
    <rect x="580" y="52" width="40" height="2" fill="#FFD700" />
'''

    projects = [
        ("AI Vision System", "Real-time object tracking &amp; computer vision pipeline.", ["PyTorch", "OpenCV"], 60),
        ("Quantum RAG Engine", "High-performance generative retrieval AI framework.", ["LangChain", "FastAPI"], 440),
        ("Cloud MLOps Pipeline", "Automated deployment &amp; monitoring architecture.", ["AWS", "Docker"], 820)
    ]
    
    for title, desc, tags, x in projects:
        svg += f'''
    <g transform="translate({x}, 100)">
        <g class="hover-card" style="animation-delay: {x/500:.2f}s;">
            <rect x="0" y="0" width="320" height="310" class="proj-card" />
            
            <rect x="15" y="15" width="290" height="130" fill="rgba(0, 245, 255, 0.05)" rx="8" stroke="rgba(255, 215, 0, 0.2)" />
            <text x="160" y="85" font-size="14" font-weight="700" fill="#00F5FF" text-anchor="middle">⚡ HIGH PERFORMANCE</text>
            
            <text x="20" y="175" font-size="17" font-weight="700">{title}</text>
            <text x="20" y="200" font-size="13" fill="#94A3B8">{desc}</text>
            
            <!-- Tags -->
            <rect x="20" y="225" width="80" height="22" class="tag" />
            <text x="60" y="240" font-size="11" font-weight="600" fill="#00F5FF" text-anchor="middle">{tags[0]}</text>
            
            <rect x="110" y="225" width="80" height="22" class="tag" />
            <text x="150" y="240" font-size="11" font-weight="600" fill="#00F5FF" text-anchor="middle">{tags[1]}</text>
            
            <!-- Button -->
            <rect x="20" y="262" width="280" height="32" class="btn" />
            <text x="160" y="283" font-size="13" font-weight="800" fill="#020408" text-anchor="middle">EXPLORE REPOSITORY →</text>
        </g>
    </g>
'''

    svg += '</svg>'
    with open("assets/quantum_projects.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated quantum_projects.svg")

def generate_quantum_footer():
    width = 1200
    height = 180
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
        </style>
        <linearGradient id="footer-bg" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#050811" />
            <stop offset="50%" stop-color="#0f172a" />
            <stop offset="100%" stop-color="#050811" />
        </linearGradient>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#footer-bg)" rx="14" stroke="rgba(0, 245, 255, 0.2)" />
    
    <text x="600" y="60" font-size="18" font-weight="700" text-anchor="middle" fill="#00F5FF" letter-spacing="2">"Building the future of AI &amp; Cloud Infrastructure, one commit at a time."</text>
    
    <circle cx="560" cy="110" r="4" fill="#00FF87" />
    <text x="572" y="114" font-size="13" fill="#94A3B8" font-weight="600">SYSTEM STATUS: ONLINE</text>
    
    <text x="600" y="150" font-size="12" fill="#64748B" text-anchor="middle">© 2026 AMIT KUMAR • DESIGNED WITH QUANTUM NEXUS ARCHITECTURE</text>
</svg>
'''
    with open("assets/quantum_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated quantum_footer.svg")

def validate_all_svgs():
    files = ["assets/quantum_hero.svg", "assets/quantum_about.svg", "assets/quantum_skills.svg", "assets/quantum_projects.svg", "assets/quantum_footer.svg"]
    for file in files:
        ET.parse(file)
    print("ALL SVGs PASS XML VALIDATION PERFECTLY!")

if __name__ == "__main__":
    generate_quantum_hero()
    generate_quantum_about()
    generate_quantum_skills()
    generate_quantum_projects()
    generate_quantum_footer()
    validate_all_svgs()
