import xml.etree.ElementTree as ET

def generate_aurora_languages():
    width = 1200
    height = 360
    
    skills = [
        ("Python &amp; Deep Learning (PyTorch / CUDA / TF)", 95, "#00F5FF", "#0284C7"),
        ("Generative AI &amp; Agentic RAG (LangChain / LLMs)", 92, "#818CF8", "#4F46E5"),
        ("Cloud Infrastructure (AWS EKS / Docker / Kubernetes)", 88, "#C084FC", "#9333EA"),
        ("Backend APIs &amp; Microservices (FastAPI / PostgreSQL)", 90, "#34D399", "#059669"),
        ("Frontend Architecture (TypeScript / React / Next.js)", 85, "#F472B6", "#DB2777")
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes tubeGlow {{
                0%, 100% {{ filter: drop-shadow(0 0 4px rgba(0, 245, 255, 0.4)); }}
                50% {{ filter: drop-shadow(0 0 12px rgba(0, 245, 255, 0.85)); }}
            }}
            @keyframes shimmerBar {{
                0% {{ transform: translateX(-200px); opacity: 0; }}
                50% {{ opacity: 0.7; }}
                100% {{ transform: translateX(960px); opacity: 0; }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .tube-anim {{ animation: tubeGlow 3s ease-in-out infinite alternate; }}
        </style>

        <linearGradient id="lang-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#lang-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">CORE PROFICIENCY &amp; TECHNICAL CAPABILITY BREAKDOWN</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />
'''

    y = 75
    for name, pct, c1, c2 in skills:
        bar_width = int(880 * (pct / 100))
        svg += f'''
        <!-- 3D Skill Gauge: {name} -->
        <g transform="translate(80, {y})">
            <!-- Label & Percentage Chip -->
            <text x="0" y="16" font-size="13" font-weight="700" fill="#F8FAFC">{name}</text>
            <rect x="910" y="0" width="50" height="22" rx="6" fill="rgba(15, 23, 42, 0.8)" stroke="{c1}" stroke-width="1" />
            <text x="935" y="15" font-size="11.5" font-weight="800" fill="{c1}" text-anchor="middle">{pct}%</text>
            
            <!-- 3D Track Base with Inset Shadow -->
            <rect x="0" y="26" width="960" height="14" rx="7" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1" />
            
            <!-- 3D Neon Power Tube Fill -->
            <rect x="1" y="27" width="{bar_width}" height="12" rx="6" fill="{c1}" class="tube-anim" />
            <rect x="1" y="27" width="{bar_width}" height="2" rx="1" fill="#FFFFFF" opacity="0.4" />
            <!-- Glowing Plasma Tip -->
            <circle cx="{bar_width}" cy="33" r="5" fill="#FFFFFF" />
            <circle cx="{bar_width}" cy="33" r="8" fill="{c1}" opacity="0.5" />
        </g>
'''
        y += 54

    svg += '</svg>'
    with open("assets/aurora_languages.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_languages.svg")

def generate_aurora_terminal():
    width = 1200
    height = 360
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes spinReactor {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            @keyframes spinReactorRev {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(-360deg); }}
            }}
            @keyframes scanBeam {{
                0% {{ transform: translateY(0px); opacity: 0.2; }}
                50% {{ transform: translateY(320px); opacity: 0.85; }}
                100% {{ transform: translateY(0px); opacity: 0.2; }}
            }}
            @keyframes pulseGlow {{
                0%, 100% {{ opacity: 0.5; filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.4)); }}
                50% {{ opacity: 0.95; filter: drop-shadow(0 0 16px rgba(0, 245, 255, 0.9)); }}
            }}
            @keyframes cursorBlink {{
                0%, 49% {{ opacity: 1; }}
                50%, 100% {{ opacity: 0; }}
            }}
            @keyframes barPulse {{
                0%, 100% {{ transform: scaleX(0.96); }}
                50% {{ transform: scaleX(1.02); }}
            }}
            @keyframes floatNode {{
                0%, 100% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-8px); }}
            }}

            text {{ font-family: 'Share Tech Mono', 'Courier New', Courier, monospace; fill: #38BDF8; }}
            .prompt {{ fill: #34D399; font-weight: bold; font-size: 13px; }}
            .cmd {{ fill: #F8FAFC; font-size: 13px; }}
            .output {{ fill: #94A3B8; font-size: 12px; }}
            .success {{ fill: #38BDF8; font-size: 12px; }}
            .highlight {{ fill: #C084FC; font-weight: bold; font-size: 12px; }}
            .project {{ fill: #F59E0B; font-weight: bold; font-size: 12px; }}
            
            .reactor-ring {{ transform-origin: 180px 185px; animation: spinReactor 14s linear infinite; }}
            .reactor-ring-rev {{ transform-origin: 180px 185px; animation: spinReactorRev 20s linear infinite; }}
            .reactor-core {{ transform-origin: 180px 185px; animation: pulseGlow 3s ease-in-out infinite; }}
            .scanline {{ animation: scanBeam 6s ease-in-out infinite; }}
            .cursor {{ animation: cursorBlink 0.9s step-start infinite; fill: #00F5FF; }}
            .bar-anim {{ animation: barPulse 2.5s ease-in-out infinite alternate; transform-origin: left; }}
            .node-float {{ animation: floatNode 3.5s ease-in-out infinite alternate; }}
        </style>
        
        <!-- Gradients -->
        <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090d1e" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="panel-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.6)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.85)" />
        </linearGradient>

        <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#38BDF8" />
        </linearGradient>

        <linearGradient id="neon-purple" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#818CF8" />
            <stop offset="100%" stop-color="#C084FC" />
        </linearGradient>

        <linearGradient id="laser-slice" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0)" />
            <stop offset="50%" stop-color="rgba(0, 245, 255, 0.85)" />
            <stop offset="100%" stop-color="rgba(0, 245, 255, 0)" />
        </linearGradient>
        
        <!-- Grid Pattern -->
        <pattern id="grid-3d" width="30" height="30" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="30" y2="0" stroke="rgba(56, 189, 248, 0.05)" stroke-width="1" />
            <line x1="0" y1="0" x2="0" y2="30" stroke="rgba(56, 189, 248, 0.05)" stroke-width="1" />
        </pattern>
    </defs>
    
    <!-- Outer Deck Frame -->
    <rect width="100%" height="100%" fill="url(#term-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.5" />
    <rect width="100%" height="100%" fill="url(#grid-3d)" rx="16" />
    
    <!-- Top Deck Header Bar -->
    <rect width="100%" height="38" fill="rgba(15, 23, 42, 0.9)" rx="16" />
    <rect x="0" y="36" width="100%" height="2" fill="url(#neon-cyan)" opacity="0.6" />
    
    <!-- 3D Window Controls with Inner Shadow -->
    <circle cx="24" cy="19" r="6" fill="#EF4444" opacity="0.9" />
    <circle cx="44" cy="19" r="6" fill="#F59E0B" opacity="0.9" />
    <circle cx="64" cy="19" r="6" fill="#10B981" opacity="0.9" />
    <text x="600" y="24" font-size="12" fill="#64748B" text-anchor="middle" font-family="-apple-system, sans-serif" letter-spacing="1">⚡ QUANTUM NEXUS // 3D HOLOGRAPHIC COMMAND DECK</text>
    <text x="1150" y="24" font-size="11" fill="#34D399" text-anchor="end">[SYS_HEALTH: 100%]</text>

    <!-- LEFT PANEL: 3D Holographic Quantum Reactor & Telemetry (x: 20 to 340) -->
    <g transform="translate(30, 55)">
        <!-- Container -->
        <rect x="0" y="0" width="300" height="285" fill="url(#panel-grad)" rx="12" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />
        <text x="150" y="26" font-size="12" font-weight="700" text-anchor="middle" fill="#00F5FF" letter-spacing="1.5">CORE TELEMETRY</text>
        
        <!-- Rotating 3D Holographic Gyroscope / Reactor Rings (Center at: 150, 105) -->
        <g transform="translate(-30, -55)">
            <!-- Outer Ring -->
            <ellipse cx="180" cy="160" rx="65" ry="35" fill="none" stroke="url(#neon-cyan)" stroke-width="1.5" stroke-dasharray="8 6" class="reactor-ring" />
            <!-- Inner Counter Ring -->
            <ellipse cx="180" cy="160" rx="45" ry="24" fill="none" stroke="url(#neon-purple)" stroke-width="1.2" stroke-dasharray="5 5" class="reactor-ring-rev" />
            <!-- Central Glowing Core -->
            <circle cx="180" cy="160" r="16" fill="rgba(0, 245, 255, 0.2)" stroke="#00F5FF" stroke-width="1.5" class="reactor-core" />
            <circle cx="180" cy="160" r="7" fill="#FFFFFF" class="reactor-core" />
        </g>
        
        <!-- Live System Metric Bars -->
        <g transform="translate(20, 160)">
            <!-- AI Inference Engine -->
            <text x="0" y="0" font-size="11" fill="#94A3B8">AI INFERENCE LOAD</text>
            <text x="260" y="0" font-size="11" font-weight="bold" fill="#00F5FF" text-anchor="end">94% // ACTIVE</text>
            <rect x="0" y="8" width="260" height="7" rx="3.5" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="8" width="244" height="7" rx="3.5" fill="url(#neon-cyan)" class="bar-anim" />

            <!-- GPU Tensor Cluster -->
            <text x="0" y="34" font-size="11" fill="#94A3B8">GPU TENSOR CLUSTER</text>
            <text x="260" y="34" font-size="11" font-weight="bold" fill="#818CF8" text-anchor="end">98% // CUDA 12</text>
            <rect x="0" y="42" width="260" height="7" rx="3.5" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="42" width="254" height="7" rx="3.5" fill="url(#neon-purple)" class="bar-anim" />

            <!-- Vector Database I/O -->
            <text x="0" y="68" font-size="11" fill="#94A3B8">VECTOR DB RETRIEVAL</text>
            <text x="260" y="68" font-size="11" font-weight="bold" fill="#34D399" text-anchor="end">1.4ms LATENCY</text>
            <rect x="0" y="76" width="260" height="7" rx="3.5" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="76" width="230" height="7" rx="3.5" fill="#34D399" class="bar-anim" />

            <!-- Real-time Status Badges -->
            <g transform="translate(0, 102)">
                <rect x="0" y="0" width="80" height="18" rx="4" fill="rgba(0, 245, 255, 0.1)" stroke="rgba(0, 245, 255, 0.3)" />
                <text x="40" y="13" font-size="9" font-weight="bold" fill="#00F5FF" text-anchor="middle">RAG ACTIVE</text>

                <rect x="90" y="0" width="80" height="18" rx="4" fill="rgba(129, 140, 248, 0.1)" stroke="rgba(129, 140, 248, 0.3)" />
                <text x="130" y="13" font-size="9" font-weight="bold" fill="#818CF8" text-anchor="middle">LLM SERVE</text>

                <rect x="180" y="0" width="80" height="18" rx="4" fill="rgba(52, 211, 153, 0.1)" stroke="rgba(52, 211, 153, 0.3)" />
                <text x="220" y="13" font-size="9" font-weight="bold" fill="#34D399" text-anchor="middle">K8S CLOUD</text>
            </g>
        </g>
    </g>

    <!-- RIGHT PANEL: 3D Holographic Terminal & Live CLI (x: 350 to 1170) -->
    <g transform="translate(350, 55)">
        <!-- Container -->
        <rect x="0" y="0" width="820" height="285" fill="url(#panel-grad)" rx="12" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" />
        
        <!-- Terminal Header Info -->
        <g transform="translate(24, 28)">
            <text x="0" y="0"><tspan class="prompt">amit@quantum-nexus</tspan><tspan class="cmd">:~$ </tspan><tspan class="cmd">ai-agent --init --profile=Amit123103</tspan></text>
            
            <text x="0" y="24" class="success">[✔] Neural Weights Loaded: Deep Learning &amp; RAG Architecture (PyTorch / CUDA)</text>
            <text x="0" y="44" class="output">[→] Cloud Infrastructure Connected: AWS EKS Cluster • Docker • Microservices</text>
            <text x="0" y="64" class="output">[→] Vector Databases Synchronized: PostgreSQL • Supabase • Vector Search</text>
            
            <!-- Highlighted Project Modules -->
            <text x="0" y="92" class="highlight">&gt;&gt; PRODUCTION SYSTEMS ONLINE:</text>
            <text x="24" y="112" class="output">├─ <tspan class="project">MyKernel</tspan> : High-performance OS kernel &amp; low-level system modules (C++ / Linux)</text>
            <text x="24" y="132" class="output">├─ <tspan class="project">AI-HUMANIZER-PRO</tspan> : Next-gen generative AI &amp; LLM text synthesis (Python / FastAPI)</text>
            <text x="24" y="152" class="output">└─ <tspan class="project">AI-Interviewer</tspan> : Autonomous agentic AI evaluation &amp; interview simulator (React / Agentic AI)</text>
            
            <!-- Status Line -->
            <text x="0" y="180" class="success">&gt;&gt; IDENTITY: Amit Kumar | Software Developer • AI &amp; ML • MLOps</text>
            
            <!-- Interactive Live Prompt with Blinking Cursor -->
            <text x="0" y="212"><tspan class="prompt">amit@quantum-nexus</tspan><tspan class="cmd">:~$ </tspan><tspan class="cmd">docker ps &amp;&amp; kubectl get pods --all-namespaces </tspan><tspan class="cursor">█</tspan></text>
        </g>
    </g>

    <!-- Animated 3D Holographic Scanning Laser Across Entire Deck -->
    <g class="scanline">
        <rect x="0" y="0" width="1200" height="4" fill="url(#laser-slice)" />
    </g>
</svg>
'''
    with open("assets/aurora_terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_terminal.svg")

def validate_svgs():
    ET.parse("assets/aurora_languages.svg")
    ET.parse("assets/aurora_terminal.svg")
    print("Next-level SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_languages()
    generate_aurora_terminal()
    validate_svgs()
