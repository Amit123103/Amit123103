import xml.etree.ElementTree as ET

def generate_aurora_architecture():
    width = 1200
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            @keyframes packetFlow {{
                0% {{ stroke-dashoffset: 40; }}
                100% {{ stroke-dashoffset: 0; }}
            }}
            @keyframes pulseNode {{
                0%, 100% {{ filter: drop-shadow(0 0 6px rgba(0, 245, 255, 0.4)); transform: translateY(0px); }}
                50% {{ filter: drop-shadow(0 0 16px rgba(0, 245, 255, 0.85)); transform: translateY(-4px); }}
            }}
            @keyframes beamPulse {{
                0%, 100% {{ opacity: 0.3; }}
                50% {{ opacity: 0.9; }}
            }}
            
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif; fill: #FFFFFF; }}
            .pipeline-node {{ animation: pulseNode 4s ease-in-out infinite alternate; }}
            .flow-cable {{ stroke: #00F5FF; stroke-width: 2.5; stroke-dasharray: 8 6; animation: packetFlow 1.2s linear infinite; }}
            .flow-glow {{ stroke: rgba(0, 245, 255, 0.2); stroke-width: 8; }}
        </style>

        <linearGradient id="arch-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050a18" />
            <stop offset="50%" stop-color="#090e22" />
            <stop offset="100%" stop-color="#030611" />
        </linearGradient>

        <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(30, 41, 59, 0.85)" />
            <stop offset="100%" stop-color="rgba(15, 23, 42, 0.95)" />
        </linearGradient>
    </defs>
    
    <!-- 3D Deck Frame -->
    <rect width="100%" height="100%" fill="url(#arch-bg)" rx="16" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1.2" />
    
    <!-- Title -->
    <text x="600" y="38" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2.5" fill="#38BDF8">ENTERPRISE RAG &amp; AGENTIC SYSTEM ARCHITECTURE</text>
    <rect x="560" y="48" width="80" height="2" fill="#818CF8" rx="1" />

    <!-- 3D Isometric Pipeline Bus Cables -->
    <g transform="translate(0, 15)">
        <line x1="260" y1="145" x2="330" y2="145" class="flow-glow" />
        <line x1="260" y1="145" x2="330" y2="145" class="flow-cable" />

        <line x1="560" y1="145" x2="630" y2="145" class="flow-glow" />
        <line x1="560" y1="145" x2="630" y2="145" class="flow-cable" />

        <line x1="860" y1="145" x2="930" y2="145" class="flow-glow" />
        <line x1="860" y1="145" x2="930" y2="145" class="flow-cable" />
    </g>

    <g transform="translate(45, 80)">
        <!-- Node 1: Client Query (x: 0) -->
        <g transform="translate(0, 0)" class="pipeline-node">
            <rect x="4" y="6" width="220" height="150" rx="14" fill="rgba(0,0,0,0.6)" />
            <rect x="0" y="0" width="220" height="150" rx="14" fill="url(#card-grad)" stroke="#00F5FF" stroke-width="1.5" />
            <rect x="0" y="0" width="220" height="4" rx="2" fill="#00F5FF" />
            
            <circle cx="35" cy="40" r="16" fill="rgba(0, 245, 255, 0.15)" stroke="#00F5FF" stroke-width="1" />
            <text x="35" y="47" font-size="16" text-anchor="middle">🖥️</text>
            <text x="65" y="45" font-size="13" font-weight="800" fill="#00F5FF">CLIENT &amp; UI</text>
            <text x="20" y="80" font-size="12" font-weight="600" fill="#F8FAFC">React • Next.js • WebSockets</text>
            <text x="20" y="104" font-size="11" fill="#94A3B8">• User Prompt Streaming</text>
            <text x="20" y="124" font-size="11" fill="#94A3B8">• Low-Latency Response Render</text>
        </g>

        <!-- Node 2: API Gateway & Agent Orchestrator (x: 290) -->
        <g transform="translate(290, 0)" class="pipeline-node">
            <rect x="4" y="6" width="230" height="150" rx="14" fill="rgba(0,0,0,0.6)" />
            <rect x="0" y="0" width="230" height="150" rx="14" fill="url(#card-grad)" stroke="#818CF8" stroke-width="1.5" />
            <rect x="0" y="0" width="230" height="4" rx="2" fill="#818CF8" />
            
            <circle cx="35" cy="40" r="16" fill="rgba(129, 140, 248, 0.15)" stroke="#818CF8" stroke-width="1" />
            <text x="35" y="47" font-size="16" text-anchor="middle">⚡</text>
            <text x="65" y="45" font-size="13" font-weight="800" fill="#818CF8">AGENT GATEWAY</text>
            <text x="20" y="80" font-size="12" font-weight="600" fill="#F8FAFC">FastAPI • LangGraph Core</text>
            <text x="20" y="104" font-size="11" fill="#94A3B8">• Multi-Agent Task Routing</text>
            <text x="20" y="124" font-size="11" fill="#94A3B8">• JWT Auth &amp; Cluster Rate Limits</text>
        </g>

        <!-- Node 3: Vector DB & Semantic Search (x: 590) -->
        <g transform="translate(590, 0)" class="pipeline-node">
            <rect x="4" y="6" width="230" height="150" rx="14" fill="rgba(0,0,0,0.6)" />
            <rect x="0" y="0" width="230" height="150" rx="14" fill="url(#card-grad)" stroke="#C084FC" stroke-width="1.5" />
            <rect x="0" y="0" width="230" height="4" rx="2" fill="#C084FC" />
            
            <circle cx="35" cy="40" r="16" fill="rgba(192, 132, 252, 0.15)" stroke="#C084FC" stroke-width="1" />
            <text x="35" y="47" font-size="16" text-anchor="middle">📦</text>
            <text x="65" y="45" font-size="13" font-weight="800" fill="#C084FC">VECTOR PIPELINE</text>
            <text x="20" y="80" font-size="12" font-weight="600" fill="#F8FAFC">PostgreSQL • Supabase • FAISS</text>
            <text x="20" y="104" font-size="11" fill="#94A3B8">• HNSW Index Cosine Retrieval</text>
            <text x="20" y="124" font-size="11" fill="#94A3B8">• Context Re-ranking &amp; Filtering</text>
        </g>

        <!-- Node 4: LLM Generative Inference Engine (x: 890) -->
        <g transform="translate(890, 0)" class="pipeline-node">
            <rect x="4" y="6" width="220" height="150" rx="14" fill="rgba(0,0,0,0.6)" />
            <rect x="0" y="0" width="220" height="150" rx="14" fill="url(#card-grad)" stroke="#34D399" stroke-width="1.5" />
            <rect x="0" y="0" width="220" height="4" rx="2" fill="#34D399" />
            
            <circle cx="35" cy="40" r="16" fill="rgba(52, 211, 153, 0.15)" stroke="#34D399" stroke-width="1" />
            <text x="35" y="47" font-size="16" text-anchor="middle">🤖</text>
            <text x="65" y="45" font-size="13" font-weight="800" fill="#34D399">LLM ENGINE</text>
            <text x="20" y="80" font-size="12" font-weight="600" fill="#F8FAFC">PyTorch • Llama 3 / Mistral</text>
            <text x="20" y="104" font-size="11" fill="#94A3B8">• Fine-Tuned Local Weight Docks</text>
            <text x="20" y="124" font-size="11" fill="#94A3B8">• Token Stream &amp; Guardrails</text>
        </g>
    </g>
</svg>
'''
    with open("assets/aurora_architecture.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated redesigned 3D aurora_architecture.svg")

def validate_svgs():
    ET.parse("assets/aurora_architecture.svg")
    print("Tier-4 SVGs pass XML validation!")

if __name__ == "__main__":
    generate_aurora_architecture()
    validate_svgs()
