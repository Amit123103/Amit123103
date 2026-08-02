import xml.etree.ElementTree as ET

def generate_aurora_languages():
    width = 1200
    height = 320
    
    skills = [
        ("Python &amp; Deep Learning (PyTorch/TF)", 95, "#38BDF8"),
        ("Generative AI &amp; RAG (LangChain/LLMs)", 92, "#818CF8"),
        ("Cloud Infrastructure (AWS/Docker/K8s)", 88, "#C084FC"),
        ("Backend APIs (FastAPI/Node.js/PostgreSQL)", 90, "#34D399"),
        ("Frontend &amp; UI (TypeScript/React/Next.js)", 85, "#F472B6")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .bar-bg {{ fill: rgba(30, 41, 59, 0.6); rx: 6; }}
            .bar-fill {{ rx: 6; }}
        </style>
    </defs>
    
    <rect width="100%" height="100%" fill="rgba(15, 23, 42, 0.7)" rx="14" stroke="rgba(255, 255, 255, 0.08)" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="2" fill="#38BDF8">CORE PROFICIENCY &amp; SKILL BREAKDOWN</text>
    <rect x="580" y="48" width="40" height="2" fill="#818CF8" />
'''

    y = 85
    for name, pct, color in skills:
        bar_width = int(800 * (pct / 100))
        svg += f'''
        <!-- Skill Row -->
        <g transform="translate(80, {y})">
            <text x="0" y="14" font-size="13" font-weight="600" fill="#E2E8F0">{name}</text>
            <text x="960" y="14" font-size="13" font-weight="700" fill="{color}" text-anchor="end">{pct}%</text>
            
            <rect x="0" y="24" width="960" height="12" class="bar-bg" />
            <rect x="0" y="24" width="{bar_width}" height="12" fill="{color}" class="bar-fill" />
        </g>
'''
        y += 45

    svg += '</svg>'
    with open("assets/aurora_languages.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_languages.svg")

def generate_aurora_terminal():
    width = 1200
    height = 240
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: 'Courier New', Courier, monospace; fill: #38BDF8; font-size: 13px; }}
            .prompt {{ fill: #34D399; font-weight: bold; }}
            .cmd {{ fill: #F8FAFC; }}
            .success {{ fill: #38BDF8; }}
            .highlight {{ fill: #C084FC; font-weight: bold; }}
            .cursor {{ animation: blink 1s step-start infinite; fill: #38BDF8; }}
            @keyframes blink {{ 50% {{ opacity: 0; }} }}
        </style>
    </defs>
    
    <!-- Terminal Window Container -->
    <rect width="100%" height="100%" fill="#090d16" rx="12" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    
    <!-- Title Bar -->
    <rect width="100%" height="32" fill="#0f172a" rx="12" />
    <circle cx="20" cy="16" r="5" fill="#EF4444" />
    <circle cx="36" cy="16" r="5" fill="#F59E0B" />
    <circle cx="52" cy="16" r="5" fill="#10B981" />
    <text x="600" y="20" font-size="12" fill="#64748B" text-anchor="middle" font-family="-apple-system, sans-serif">amit@quantum-nexus: ~ (zsh)</text>
    
    <!-- Console Commands & Telemetry Output -->
    <g transform="translate(24, 60)">
        <text y="0"><tspan class="prompt">amit@quantum-nexus</tspan><tspan class="cmd">:~$ fetch-profile --user=Amit123103</tspan></text>
        <text y="28" class="success">[OK] Initializing Neural Weights &amp; PyTorch Engine...</text>
        <text y="52" class="success">[OK] Connecting to AWS Cloud Cluster (ap-south-1)...</text>
        <text y="76" class="success">[OK] Loading Agentic RAG Workflows &amp; Vector Databases...</text>
        <text y="100" class="highlight">&gt;&gt; STATUS: Senior AI Engineer &amp; Cloud Architect — Ready for High-Impact Roles!</text>
        
        <text y="128"><tspan class="prompt">amit@quantum-nexus</tspan><tspan class="cmd">:~$ </tspan><tspan class="cursor">█</tspan></text>
    </g>
</svg>
'''
    with open("assets/aurora_terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated aurora_terminal.svg")

def validate_svgs():
    ET.parse("assets/aurora_languages.svg")
    ET.parse("assets/aurora_terminal.svg")
    print("Next-level SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_languages()
    generate_aurora_terminal()
    validate_svgs()
