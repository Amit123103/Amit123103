#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  ULTIMATE 3D MOTION PROFILE ENGINE v5.0                      ║
║  Complete Redesign: Holographic · Isometric · Cinematic      ║
║  Author: Amit Kumar                                          ║
╚══════════════════════════════════════════════════════════════╝
"""
import math
import base64
import os
import random

# ──────────────────────────────────────────────────────────────
#  COLOR SYSTEM — Ultra-Premium Palette
# ──────────────────────────────────────────────────────────────
COLORS = {
    "bg_deep": "#030711",
    "bg_mid": "#0a0f1e",
    "bg_card": "rgba(8, 14, 32, 0.85)",
    "neon_cyan": "#00F5FF",
    "neon_blue": "#38BDF8",
    "neon_purple": "#818CF8",
    "neon_violet": "#A78BFA",
    "neon_pink": "#F472B6",
    "neon_green": "#34D399",
    "neon_amber": "#FBBF24",
    "neon_rose": "#FB7185",
    "text_primary": "#F1F5F9",
    "text_secondary": "#94A3B8",
    "text_muted": "#64748B",
    "glass_border": "rgba(56, 189, 248, 0.18)",
    "glass_fill": "rgba(15, 23, 42, 0.65)",
}

def get_base64_image(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

# ──────────────────────────────────────────────────────────────
#  SHARED DESIGN TOKENS & ANIMATION LIBRARY
# ──────────────────────────────────────────────────────────────
def shared_defs():
    return '''
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&amp;family=Inter:wght@400;500;600;700;800&amp;display=swap');
            text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
            .mono { font-family: 'JetBrains Mono', 'Share Tech Mono', monospace; }

            /* 3D Orbital Spins */
            @keyframes orbitCW { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes orbitCCW { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }

            /* Holographic Scan */
            @keyframes holoScan {
                0% { transform: translateY(-8px); opacity: 0.15; }
                50% { opacity: 0.85; }
                100% { transform: translateY(var(--scan-h, 500px)); opacity: 0.15; }
            }

            /* Pulse Glow */
            @keyframes pulseNeon {
                0%, 100% { opacity: 0.45; filter: drop-shadow(0 0 6px var(--glow-color, #00F5FF)); }
                50% { opacity: 1; filter: drop-shadow(0 0 22px var(--glow-color, #00F5FF)); }
            }

            /* Float 3D */
            @keyframes float3D {
                0%, 100% { transform: translateY(0px) scale(1); }
                50% { transform: translateY(-12px) scale(1.02); }
            }

            /* Subtle Breathe */
            @keyframes breathe {
                0%, 100% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.04); opacity: 1; }
            }

            /* Cursor Blink */
            @keyframes cursorBlink {
                0%, 49% { opacity: 1; }
                50%, 100% { opacity: 0; }
            }

            /* Bar Fill Animate */
            @keyframes barFill {
                0% { transform: scaleX(0); }
                100% { transform: scaleX(1); }
            }

            /* Particle Drift */
            @keyframes particleDrift {
                0% { transform: translateY(0) translateX(0) scale(0.8); opacity: 0.2; }
                50% { transform: translateY(-18px) translateX(8px) scale(1.2); opacity: 0.9; }
                100% { transform: translateY(0) translateX(0) scale(0.8); opacity: 0.2; }
            }

            /* Gradient Shift */
            @keyframes gradientShift {
                0% { stop-color: #00F5FF; }
                33% { stop-color: #818CF8; }
                66% { stop-color: #F472B6; }
                100% { stop-color: #00F5FF; }
            }

            /* Text Typing */
            @keyframes typeReveal {
                from { width: 0; }
                to { width: 100%; }
            }

            /* Hexagon Rotate */
            @keyframes hexRotate {
                0% { transform: rotate(0deg) scale(0.98); }
                50% { transform: rotate(180deg) scale(1.02); }
                100% { transform: rotate(360deg) scale(0.98); }
            }

            /* Data Stream */
            @keyframes dataStream {
                0% { transform: translateY(-100%); }
                100% { transform: translateY(200%); }
            }
        </style>

        <!-- Premium Gradients -->
        <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#030711" />
            <stop offset="50%" stop-color="#0a0f1e" />
            <stop offset="100%" stop-color="#020409" />
        </linearGradient>

        <linearGradient id="cyan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#38BDF8" />
        </linearGradient>

        <linearGradient id="purple-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#818CF8" />
            <stop offset="100%" stop-color="#C084FC" />
        </linearGradient>

        <linearGradient id="green-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#34D399" />
            <stop offset="100%" stop-color="#10B981" />
        </linearGradient>

        <linearGradient id="rose-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FB7185" />
            <stop offset="100%" stop-color="#F472B6" />
        </linearGradient>

        <linearGradient id="amber-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FBBF24" />
            <stop offset="100%" stop-color="#F59E0B" />
        </linearGradient>

        <linearGradient id="holo-shimmer" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0.08)">
                <animate attributeName="stop-color" values="rgba(0,245,255,0.08);rgba(129,140,248,0.08);rgba(244,114,182,0.08);rgba(0,245,255,0.08)" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="rgba(129, 140, 248, 0.03)">
                <animate attributeName="stop-color" values="rgba(129,140,248,0.03);rgba(244,114,182,0.03);rgba(0,245,255,0.03);rgba(129,140,248,0.03)" dur="8s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="scan-laser" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0)" />
            <stop offset="30%" stop-color="rgba(0, 245, 255, 0.7)" />
            <stop offset="50%" stop-color="rgba(255, 255, 255, 0.95)" />
            <stop offset="70%" stop-color="rgba(0, 245, 255, 0.7)" />
            <stop offset="100%" stop-color="rgba(0, 245, 255, 0)" />
        </linearGradient>

        <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="30%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>

        <!-- Filters -->
        <filter id="neon-blur"><feGaussianBlur stdDeviation="6" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>
        <filter id="soft-glow"><feGaussianBlur stdDeviation="3"/></filter>
        <filter id="heavy-glow"><feGaussianBlur stdDeviation="10" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>

        <!-- Grid Pattern -->
        <pattern id="iso-grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="40" y2="0" stroke="rgba(56, 189, 248, 0.04)" stroke-width="0.5" />
            <line x1="0" y1="0" x2="0" y2="40" stroke="rgba(56, 189, 248, 0.04)" stroke-width="0.5" />
            <line x1="0" y1="0" x2="40" y2="40" stroke="rgba(129, 140, 248, 0.02)" stroke-width="0.3" />
        </pattern>

        <!-- Hex Grid Pattern -->
        <pattern id="hex-grid" width="60" height="52" patternUnits="userSpaceOnUse" patternTransform="scale(0.8)">
            <polygon points="30,2 55,15 55,37 30,50 5,37 5,15" fill="none" stroke="rgba(0,245,255,0.04)" stroke-width="0.5" />
        </pattern>
    </defs>
'''


def gen_particles(count, w, h, colors=None):
    """Generate floating 3D depth particles."""
    if colors is None:
        colors = ["#00F5FF", "#38BDF8", "#818CF8", "#A78BFA", "#34D399", "#F472B6"]
    svg = ""
    rng = random.Random(42)
    for i in range(count):
        x = rng.randint(20, w - 20)
        y = rng.randint(20, h - 20)
        r = rng.uniform(1.0, 3.5)
        c = colors[i % len(colors)]
        delay = round(rng.uniform(0, 6), 1)
        dur = round(rng.uniform(3, 7), 1)
        svg += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="0.6" style="animation: particleDrift {dur}s ease-in-out {delay}s infinite;" />\n'
    return svg


def gen_constellation_lines(count, w, h):
    """Generate subtle constellation connection lines."""
    svg = ""
    rng = random.Random(99)
    points = [(rng.randint(40, w - 40), rng.randint(40, h - 40)) for _ in range(count)]
    for i in range(len(points)):
        for j in range(i + 1, min(i + 3, len(points))):
            d = math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            if d < 200:
                opacity = round(0.08 * (1 - d / 200), 3)
                svg += f'<line x1="{points[i][0]}" y1="{points[i][1]}" x2="{points[j][0]}" y2="{points[j][1]}" stroke="#00F5FF" stroke-width="0.5" opacity="{opacity}" />\n'
    return svg


def glass_card(x, y, w, h, rx=16, accent_color="#00F5FF", accent_width=None):
    """Generate a glassmorphism card with top accent bar."""
    if accent_width is None:
        accent_width = w
    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"
          fill="rgba(8, 14, 32, 0.65)" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1" />
    <rect x="{x}" y="{y}" width="{accent_width}" height="3" rx="{rx}" fill="{accent_color}" opacity="0.7" />
    '''


def section_title(x, y, title, subtitle=None):
    """Generate a section title with decorative elements."""
    svg = f'''
    <text x="{x}" y="{y}" font-size="22" font-weight="800" fill="#F1F5F9" letter-spacing="3" text-anchor="middle">{title}</text>
    <rect x="{x - 30}" y="{y + 8}" width="60" height="2.5" rx="1.25" fill="url(#cyan-grad)" />
    '''
    if subtitle:
        svg += f'<text x="{x}" y="{y + 28}" font-size="12" fill="#64748B" text-anchor="middle" letter-spacing="1">{subtitle}</text>'
    return svg


# ══════════════════════════════════════════════════════════════
#  1. HERO TERMINAL — 3D Holographic Command Deck
# ══════════════════════════════════════════════════════════════
def generate_hero_terminal():
    W, H = 1200, 400
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}

    <!-- Background -->
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />
    <rect width="100%" height="100%" fill="url(#holo-shimmer)" rx="18" />

    <!-- Constellation Network -->
    {gen_constellation_lines(30, W, H)}

    <!-- Outer Frame Glow -->
    <rect width="100%" height="100%" fill="none" rx="18" stroke="rgba(0, 245, 255, 0.2)" stroke-width="1.5" />
    <rect x="0" y="0" width="100%" height="42" fill="rgba(8, 14, 32, 0.95)" rx="18" />
    <rect x="0" y="40" width="100%" height="2" fill="url(#cyan-grad)" opacity="0.5" />

    <!-- Window Controls -->
    <circle cx="26" cy="21" r="6.5" fill="#EF4444" opacity="0.9" />
    <circle cx="48" cy="21" r="6.5" fill="#FBBF24" opacity="0.9" />
    <circle cx="70" cy="21" r="6.5" fill="#34D399" opacity="0.9" />
    <text x="{W//2}" y="26" font-size="11" fill="#64748B" text-anchor="middle" class="mono" letter-spacing="1.5">⚡ QUANTUM NEXUS v5.0 // 3D HOLOGRAPHIC COMMAND INTERFACE</text>
    <text x="{W - 30}" y="26" font-size="10" fill="#34D399" text-anchor="end" class="mono">● ONLINE</text>

    <!-- LEFT: 3D Holographic Reactor Core -->
    <g transform="translate(30, 55)">
        {glass_card(0, 0, 320, 325, accent_color="#00F5FF")}

        <text x="160" y="30" font-size="13" font-weight="700" fill="#00F5FF" text-anchor="middle" letter-spacing="2" class="mono">◆ CORE TELEMETRY</text>

        <!-- Orbital Reactor -->
        <g transform="translate(160, 120)">
            <!-- Outer Ring -->
            <ellipse cx="0" cy="0" rx="75" ry="38" fill="none" stroke="url(#cyan-grad)" stroke-width="1.8"
                     stroke-dasharray="10 8" style="transform-origin: center; animation: orbitCW 16s linear infinite;" />
            <!-- Mid Ring -->
            <ellipse cx="0" cy="0" rx="55" ry="28" fill="none" stroke="url(#purple-grad)" stroke-width="1.3"
                     stroke-dasharray="6 6" style="transform-origin: center; animation: orbitCCW 24s linear infinite;" />
            <!-- Inner Ring -->
            <ellipse cx="0" cy="0" rx="35" ry="18" fill="none" stroke="#A78BFA" stroke-width="1"
                     stroke-dasharray="4 4" style="transform-origin: center; animation: orbitCW 10s linear infinite;" />
            <!-- Core -->
            <circle cx="0" cy="0" r="18" fill="rgba(0, 245, 255, 0.15)" stroke="#00F5FF" stroke-width="2"
                    style="animation: pulseNeon 3s ease-in-out infinite; --glow-color: #00F5FF;" filter="url(#neon-blur)" />
            <circle cx="0" cy="0" r="8" fill="#FFFFFF" style="animation: breathe 2s ease-in-out infinite;" />

            <!-- Orbital Nodes -->
            <circle cx="75" cy="0" r="4" fill="#00F5FF" style="animation: orbitCW 16s linear infinite; transform-origin: 0 0;" />
            <circle cx="-55" cy="0" r="3" fill="#818CF8" style="animation: orbitCCW 24s linear infinite; transform-origin: 55px 0;" />
        </g>

        <!-- System Metrics -->
        <g transform="translate(20, 185)">
            <text x="0" y="0" font-size="10" fill="#94A3B8" class="mono">AI INFERENCE ENGINE</text>
            <text x="280" y="0" font-size="10" font-weight="700" fill="#00F5FF" text-anchor="end" class="mono">97.2%</text>
            <rect x="0" y="8" width="280" height="6" rx="3" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="8" width="272" height="6" rx="3" fill="url(#cyan-grad)" style="animation: barFill 2s ease-out forwards; transform-origin: left;" />

            <text x="0" y="32" font-size="10" fill="#94A3B8" class="mono">GPU TENSOR CLUSTER</text>
            <text x="280" y="32" font-size="10" font-weight="700" fill="#818CF8" text-anchor="end" class="mono">99.1%</text>
            <rect x="0" y="40" width="280" height="6" rx="3" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="40" width="277" height="6" rx="3" fill="url(#purple-grad)" style="animation: barFill 2.5s ease-out forwards; transform-origin: left;" />

            <text x="0" y="64" font-size="10" fill="#94A3B8" class="mono">VECTOR DB RETRIEVAL</text>
            <text x="280" y="64" font-size="10" font-weight="700" fill="#34D399" text-anchor="end" class="mono">0.8ms</text>
            <rect x="0" y="72" width="280" height="6" rx="3" fill="rgba(255,255,255,0.06)" />
            <rect x="0" y="72" width="248" height="6" rx="3" fill="url(#green-grad)" style="animation: barFill 3s ease-out forwards; transform-origin: left;" />

            <!-- Status Badges -->
            <g transform="translate(0, 96)">
                <rect x="0" y="0" width="82" height="20" rx="10" fill="rgba(0,245,255,0.1)" stroke="rgba(0,245,255,0.35)" stroke-width="0.8" />
                <text x="41" y="14" font-size="8" font-weight="700" fill="#00F5FF" text-anchor="middle" class="mono">RAG ACTIVE</text>
                <rect x="92" y="0" width="82" height="20" rx="10" fill="rgba(129,140,248,0.1)" stroke="rgba(129,140,248,0.35)" stroke-width="0.8" />
                <text x="133" y="14" font-size="8" font-weight="700" fill="#818CF8" text-anchor="middle" class="mono">LLM SERVE</text>
                <rect x="184" y="0" width="82" height="20" rx="10" fill="rgba(52,211,153,0.1)" stroke="rgba(52,211,153,0.35)" stroke-width="0.8" />
                <text x="225" y="14" font-size="8" font-weight="700" fill="#34D399" text-anchor="middle" class="mono">K8S CLOUD</text>
            </g>
        </g>
    </g>

    <!-- RIGHT: Live Terminal CLI -->
    <g transform="translate(370, 55)">
        {glass_card(0, 0, 800, 325, accent_color="#818CF8")}

        <g transform="translate(24, 32)">
            <text x="0" y="0" class="mono">
                <tspan font-size="13" fill="#34D399" font-weight="700">amit@quantum-nexus</tspan><tspan font-size="13" fill="#F1F5F9">:~$ </tspan><tspan font-size="13" fill="#F1F5F9">ai-agent --init --profile=Amit123103</tspan>
            </text>

            <text x="0" y="26" font-size="12" fill="#38BDF8" class="mono">[✔] Neural Weights Loaded: Deep Learning &amp; RAG Architecture (PyTorch / CUDA)</text>
            <text x="0" y="48" font-size="12" fill="#94A3B8" class="mono">[→] Cloud Infrastructure: AWS EKS Cluster • Docker • Microservices</text>
            <text x="0" y="70" font-size="12" fill="#94A3B8" class="mono">[→] Vector Databases: PostgreSQL • Supabase • Vector Search Engine</text>

            <text x="0" y="100" font-size="12" fill="#C084FC" font-weight="700" class="mono">&gt;&gt; PRODUCTION SYSTEMS ONLINE:</text>
            <text x="24" y="122" font-size="12" fill="#94A3B8" class="mono">├─ <tspan fill="#FBBF24" font-weight="700">MyKernel</tspan> : High-performance OS kernel &amp; system modules (C++ / Linux)</text>
            <text x="24" y="144" font-size="12" fill="#94A3B8" class="mono">├─ <tspan fill="#FBBF24" font-weight="700">AI-HUMANIZER-PRO</tspan> : Next-gen generative AI &amp; LLM text synthesis</text>
            <text x="24" y="166" font-size="12" fill="#94A3B8" class="mono">└─ <tspan fill="#FBBF24" font-weight="700">AI-Interviewer</tspan> : Autonomous agentic AI evaluation simulator</text>

            <text x="0" y="200" font-size="12" fill="#38BDF8" class="mono">&gt;&gt; IDENTITY: Amit Kumar | Software Developer • AI &amp; ML • MLOps</text>

            <text x="0" y="230" class="mono">
                <tspan font-size="13" fill="#34D399" font-weight="700">amit@quantum-nexus</tspan><tspan font-size="13" fill="#F1F5F9">:~$ </tspan><tspan font-size="13" fill="#F1F5F9">docker ps &amp;&amp; kubectl get pods </tspan><tspan font-size="14" fill="#00F5FF" style="animation: cursorBlink 1s step-start infinite;">█</tspan>
            </text>

            <!-- Neural Waveform -->
            <g transform="translate(0, 260)">'''

    # Neural equalizer bars
    num_bars = 45
    for b in range(num_bars):
        h_bar = 4 + int(14 * abs(math.sin(b * 0.4)))
        delay = round(b * 0.08, 2)
        ratio = b / num_bars
        c1 = f"hsl({180 + ratio * 120}, 85%, 65%)"
        svg += f'''
                <rect x="{b * 16}" y="{-h_bar}" width="10" height="{h_bar}" rx="2" fill="{c1}" opacity="0.7">
                    <animate attributeName="height" values="{h_bar};{h_bar+10};{h_bar-3};{h_bar+7};{h_bar}" dur="2.5s" begin="{delay}s" repeatCount="indefinite" />
                </rect>'''

    svg += '''
            </g>
        </g>
    </g>

    <!-- Scanning Holographic Laser -->
    <g style="animation: holoScan 8s ease-in-out infinite; --scan-h: 370px;">
        <rect x="0" y="0" width="100%" height="3" fill="url(#scan-laser)" />
        <rect x="0" y="1" width="100%" height="1" fill="#FFFFFF" opacity="0.6" />
    </g>

    <!-- Floating Particles -->
    ''' + gen_particles(20, W, H) + '''

</svg>'''

    with open("assets/aurora_terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_terminal.svg ({os.path.getsize('assets/aurora_terminal.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  2. BADGES — 3D Floating Certification Cards
# ══════════════════════════════════════════════════════════════
def generate_badges():
    W, H = 1200, 280
    badges = [
        ("🏆", "AWS Certified", "Cloud Architect", "#FBBF24"),
        ("🎓", "B.Tech CSE", "Final Year", "#00F5FF"),
        ("⚡", "AI/ML Engineer", "Deep Learning", "#818CF8"),
        ("🔧", "Full Stack Dev", "React + FastAPI", "#34D399"),
        ("🐳", "DevOps Expert", "Docker + K8s", "#F472B6"),
        ("🧠", "LLM Specialist", "RAG + Agents", "#A78BFA"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#hex-grid)" rx="18" />
    {gen_constellation_lines(15, W, H)}

    {section_title(W//2, 38, "ENGINEERING CERTIFICATIONS &amp; HONORS")}
'''

    card_w = 170
    gap = 15
    total_w = len(badges) * card_w + (len(badges) - 1) * gap
    start_x = (W - total_w) // 2

    for i, (icon, title, sub, color) in enumerate(badges):
        x = start_x + i * (card_w + gap)
        y = 70
        delay = round(i * 0.3, 1)
        svg += f'''
    <g transform="translate({x}, {y})" style="animation: float3D 5s ease-in-out {delay}s infinite;">
        <rect x="0" y="0" width="{card_w}" height="180" rx="14"
              fill="rgba(8, 14, 32, 0.7)" stroke="{color}" stroke-width="1" stroke-opacity="0.35" />
        <rect x="0" y="0" width="{card_w}" height="3" rx="14" fill="{color}" opacity="0.6" />

        <!-- Glow Circle -->
        <circle cx="{card_w//2}" cy="55" r="28" fill="rgba({",".join(str(int(color.lstrip("#")[i:i+2], 16)) for i in (0, 2, 4))}, 0.08)"
                stroke="{color}" stroke-width="1" stroke-opacity="0.3"
                style="animation: breathe 3s ease-in-out {delay}s infinite;" />
        <text x="{card_w//2}" y="62" font-size="24" text-anchor="middle">{icon}</text>

        <text x="{card_w//2}" y="105" font-size="13" font-weight="700" fill="#F1F5F9" text-anchor="middle">{title}</text>
        <text x="{card_w//2}" y="122" font-size="11" fill="{color}" text-anchor="middle" class="mono">{sub}</text>

        <!-- Status Dot -->
        <circle cx="{card_w//2}" cy="150" r="4" fill="{color}" opacity="0.7"
                style="animation: pulseNeon 2s ease-in-out {delay}s infinite; --glow-color: {color};" filter="url(#soft-glow)" />
        <text x="{card_w//2}" y="170" font-size="8" fill="#64748B" text-anchor="middle" class="mono">VERIFIED</text>
    </g>'''

    svg += f'\n{gen_particles(12, W, H)}\n</svg>'
    with open("assets/aurora_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_badges.svg ({os.path.getsize('assets/aurora_badges.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  3. TECH BADGES — Holographic Technology Ecosystem
# ══════════════════════════════════════════════════════════════
def generate_tech_badges():
    W, H = 1200, 360
    categories = [
        ("AI &amp; Machine Learning", [
            ("Python", "#3776AB"), ("TensorFlow", "#FF6F00"), ("PyTorch", "#EE4C2C"),
            ("OpenCV", "#5C3EE8"), ("LangChain", "#1C3C3C"), ("OpenAI", "#412991"),
            ("HuggingFace", "#FFD21E"), ("scikit-learn", "#F7931E"),
        ], "#00F5FF"),
        ("Backend &amp; Web", [
            ("FastAPI", "#009688"), ("Node.js", "#339933"), ("React", "#61DAFB"),
            ("Next.js", "#FFFFFF"), ("REST API", "#00F5FF"), ("Express", "#000000"),
            ("HTML5", "#E34F26"), ("JavaScript", "#F7DF1E"),
        ], "#818CF8"),
        ("Cloud &amp; Infrastructure", [
            ("AWS", "#FF9900"), ("Docker", "#2496ED"), ("Kubernetes", "#326CE5"),
            ("Linux", "#FCC624"), ("GitHub Actions", "#2088FF"), ("Terraform", "#844FBA"),
            ("MySQL", "#4479A1"), ("PostgreSQL", "#4169E1"),
        ], "#34D399"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />

    {section_title(W//2, 38, "TECHNOLOGY ECOSYSTEM", "Core Infrastructure &amp; Toolchain")}
'''

    y_base = 80
    for ci, (cat_name, techs, accent) in enumerate(categories):
        y = y_base + ci * 95
        svg += f'<text x="80" y="{y}" font-size="12" font-weight="700" fill="{accent}" letter-spacing="1.5" class="mono">{cat_name}</text>'
        svg += f'<line x1="80" y1="{y + 8}" x2="1120" y2="{y + 8}" stroke="rgba(255,255,255,0.06)" stroke-width="1" />'

        for ti, (tech, tc) in enumerate(techs):
            tx = 80 + ti * 130
            ty = y + 22
            delay = round(ci * 0.5 + ti * 0.12, 2)
            tw = max(len(tech) * 8 + 36, 90)
            svg += f'''
    <g transform="translate({tx}, {ty})" style="animation: float3D 6s ease-in-out {delay}s infinite;">
        <rect x="0" y="0" width="{tw}" height="34" rx="17" fill="rgba(255,255,255,0.04)"
              stroke="{accent}" stroke-width="0.8" stroke-opacity="0.3" />
        <circle cx="18" cy="17" r="6" fill="{tc}" opacity="0.8" />
        <text x="{tw//2 + 6}" y="22" font-size="11" font-weight="600" fill="#E2E8F0" text-anchor="middle">{tech}</text>
    </g>'''

    svg += f'\n{gen_particles(10, W, H)}\n</svg>'
    with open("assets/aurora_tech_badges.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_tech_badges.svg ({os.path.getsize('assets/aurora_tech_badges.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  4. ABOUT — 3D Holographic Info Panels
# ══════════════════════════════════════════════════════════════
def generate_about():
    W, H = 1200, 340
    cards = [
        ("🎓", "Education", "Final Year B.Tech", "Computer Science &amp; Engineering", "#00F5FF"),
        ("⚡", "Current Focus", "Generative AI &amp; LLMs", "Scalable Cloud-Native Systems", "#818CF8"),
        ("🎯", "Career Goal", "Building Intelligent", "AI Products for Industry", "#34D399"),
        ("📍", "Location", "India 🇮🇳", "UTC +5:30", "#FBBF24"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#hex-grid)" rx="18" />
    {gen_constellation_lines(20, W, H)}

    {section_title(W//2, 38, "CORE FOCUS &amp; CAPABILITIES", "Engineering Profile Overview")}
'''

    card_w = 255
    gap = 20
    total_w = len(cards) * card_w + (len(cards) - 1) * gap
    start_x = (W - total_w) // 2

    for i, (icon, title, line1, line2, accent) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        y = 80
        delay = round(i * 0.4, 1)

        svg += f'''
    <g transform="translate({x}, {y})" style="animation: float3D 6s ease-in-out {delay}s infinite;">
        <rect x="0" y="0" width="{card_w}" height="230" rx="14"
              fill="rgba(8, 14, 32, 0.7)" stroke="{accent}" stroke-width="1" stroke-opacity="0.25" />
        <rect x="0" y="0" width="{card_w}" height="3" rx="14" fill="{accent}" opacity="0.5" />

        <!-- Icon Circle -->
        <circle cx="{card_w//2}" cy="55" r="30" fill="rgba(255,255,255,0.03)" stroke="{accent}" stroke-width="1.2" stroke-opacity="0.3"
                style="animation: breathe 4s ease-in-out {delay}s infinite;" />
        <text x="{card_w//2}" y="63" font-size="26" text-anchor="middle">{icon}</text>

        <text x="{card_w//2}" y="110" font-size="15" font-weight="700" fill="#F1F5F9" text-anchor="middle">{title}</text>
        <line x1="{card_w//2 - 25}" y1="120" x2="{card_w//2 + 25}" y2="120" stroke="{accent}" stroke-width="1.5" opacity="0.4" />
        <text x="{card_w//2}" y="145" font-size="12" fill="#94A3B8" text-anchor="middle">{line1}</text>
        <text x="{card_w//2}" y="165" font-size="12" fill="#94A3B8" text-anchor="middle">{line2}</text>

        <circle cx="{card_w//2}" cy="200" r="3" fill="{accent}" opacity="0.6"
                style="animation: pulseNeon 3s ease-in-out {delay}s infinite; --glow-color: {accent};" filter="url(#soft-glow)" />
    </g>'''

    svg += f'\n{gen_particles(10, W, H)}\n</svg>'
    with open("assets/aurora_about.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_about.svg ({os.path.getsize('assets/aurora_about.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  5. SKILLS MATRIX — 3D Holographic Skill Orbs
# ══════════════════════════════════════════════════════════════
def generate_skills():
    W, H = 1200, 600
    categories = [
        ("AI &amp; Deep Learning", [
            ("Python", 95), ("TensorFlow", 88), ("PyTorch", 90), ("OpenCV", 82),
            ("Machine Learning", 92), ("Deep Learning", 90), ("LLMs", 88), ("RAG", 85),
            ("LangChain", 87), ("OpenAI API", 84),
        ], "#00F5FF", "cyan-grad"),
        ("Backend &amp; Web Development", [
            ("FastAPI", 90), ("Node.js", 78), ("REST APIs", 88), ("React", 82),
            ("Next.js", 80), ("HTML/CSS", 85), ("JavaScript", 84), ("TypeScript", 76),
        ], "#818CF8", "purple-grad"),
        ("Cloud &amp; Infrastructure", [
            ("AWS", 82), ("Docker", 88), ("Kubernetes", 78), ("Linux", 90),
            ("DevOps", 82), ("GitHub Actions", 85), ("C++", 80), ("Java", 76),
            ("MySQL", 84), ("PostgreSQL", 82),
        ], "#34D399", "green-grad"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />

    {section_title(W//2, 38, "TECHNICAL EXPERTISE MATRIX", "Proficiency Analysis &amp; Skill Breakdown")}
'''

    y_base = 80
    for ci, (cat_name, skills, accent, grad_id) in enumerate(categories):
        y = y_base + ci * 180
        svg += f'''
    <text x="80" y="{y}" font-size="13" font-weight="700" fill="{accent}" letter-spacing="2" class="mono">◆ {cat_name.upper()}</text>
    <line x1="80" y1="{y + 10}" x2="1120" y2="{y + 10}" stroke="rgba(255,255,255,0.06)" stroke-width="1" />'''

        cols = 5
        for si, (skill, level) in enumerate(skills):
            col = si % cols
            row = si // cols
            sx = 80 + col * 210
            sy = y + 28 + row * 58
            bar_w = 120
            fill_w = int(bar_w * level / 100)
            delay = round(ci * 0.3 + si * 0.1, 2)

            svg += f'''
    <g transform="translate({sx}, {sy})" style="animation: float3D 7s ease-in-out {delay}s infinite;">
        <text x="0" y="0" font-size="11" font-weight="600" fill="#E2E8F0">{skill}</text>
        <text x="{bar_w + 35}" y="0" font-size="10" font-weight="700" fill="{accent}" class="mono">{level}%</text>
        <rect x="0" y="8" width="{bar_w + 30}" height="5" rx="2.5" fill="rgba(255,255,255,0.06)" />
        <rect x="0" y="8" width="{fill_w + 15}" height="5" rx="2.5" fill="url(#{grad_id})"
              style="animation: barFill {1 + delay}s ease-out forwards; transform-origin: left;" />
    </g>'''

    svg += f'\n{gen_particles(15, W, H)}\n</svg>'
    with open("assets/aurora_skills.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_skills.svg ({os.path.getsize('assets/aurora_skills.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  6. LANGUAGES — 3D Radial Proficiency Rings
# ══════════════════════════════════════════════════════════════
def generate_languages():
    W, H = 1200, 350
    langs = [
        ("Python", 95, "#3776AB", "#00F5FF"),
        ("C++", 80, "#00599C", "#38BDF8"),
        ("JavaScript", 84, "#F7DF1E", "#FBBF24"),
        ("Java", 76, "#ED8B00", "#F59E0B"),
        ("TypeScript", 76, "#3178C6", "#818CF8"),
        ("C", 72, "#555555", "#94A3B8"),
        ("SQL", 84, "#4479A1", "#34D399"),
        ("HTML/CSS", 85, "#E34F26", "#FB7185"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#hex-grid)" rx="18" />

    {section_title(W//2, 38, "LANGUAGE PROFICIENCY", "Core Programming Languages")}
'''

    cols = 8
    ring_r = 42
    gap = 140
    total_w = cols * gap - (gap - ring_r * 2)
    start_x = (W - total_w) // 2 + ring_r

    for i, (lang, level, base_c, glow_c) in enumerate(langs):
        cx = start_x + i * gap
        cy = 190
        circumference = 2 * math.pi * ring_r
        filled = circumference * level / 100
        delay = round(i * 0.25, 2)

        svg += f'''
    <g transform="translate({cx}, {cy})" style="animation: float3D 6s ease-in-out {delay}s infinite;">
        <!-- Background Ring -->
        <circle cx="0" cy="0" r="{ring_r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="5" />
        <!-- Filled Ring -->
        <circle cx="0" cy="0" r="{ring_r}" fill="none" stroke="{glow_c}" stroke-width="5"
                stroke-dasharray="{filled:.1f} {circumference:.1f}"
                stroke-dashoffset="{circumference * 0.25:.1f}" stroke-linecap="round"
                style="animation: barFill {1.5 + delay}s ease-out forwards; transform-origin: center;"
                filter="url(#soft-glow)" />
        <!-- Inner Glow -->
        <circle cx="0" cy="0" r="{ring_r - 12}" fill="rgba(255,255,255,0.02)" stroke="{glow_c}" stroke-width="0.5" stroke-opacity="0.2" />
        <!-- Center Label -->
        <text x="0" y="-4" font-size="14" font-weight="800" fill="#F1F5F9" text-anchor="middle">{level}%</text>
        <text x="0" y="12" font-size="8" fill="{glow_c}" text-anchor="middle" class="mono">{lang}</text>
        <!-- Color Dot -->
        <circle cx="0" cy="-{ring_r - 2}" r="4" fill="{base_c}" stroke="#FFF" stroke-width="1"
                style="animation: pulseNeon 2s ease-in-out {delay}s infinite; --glow-color: {glow_c};" />
    </g>'''

    svg += f'\n{gen_particles(8, W, H)}\n</svg>'
    with open("assets/aurora_languages.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_languages.svg ({os.path.getsize('assets/aurora_languages.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  7. PROJECTS — 3D Floating Holographic Cards
# ══════════════════════════════════════════════════════════════
def generate_projects():
    W, H = 1200, 440
    projects = [
        ("MyKernel", "High-performance OS kernel &amp; system architecture module.", ["C++", "Linux", "ASM"], "#00F5FF", "🔧"),
        ("AI-HUMANIZER-PRO", "Next-gen LLM generative AI &amp; text humanization engine.", ["Python", "FastAPI", "LLM"], "#818CF8", "🧠"),
        ("AI-Interviewer", "Autonomous agentic AI evaluation &amp; interview simulator.", ["React", "AI", "RAG"], "#34D399", "🤖"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />
    {gen_constellation_lines(25, W, H)}

    {section_title(W//2, 38, "FEATURED PROJECTS", "Production-Grade Systems")}
'''

    card_w = 340
    gap = 30
    total_w = len(projects) * card_w + (len(projects) - 1) * gap
    start_x = (W - total_w) // 2

    for i, (name, desc, tags, accent, icon) in enumerate(projects):
        x = start_x + i * (card_w + gap)
        y = 80
        delay = round(i * 0.5, 1)

        svg += f'''
    <g transform="translate({x}, {y})" style="animation: float3D 6s ease-in-out {delay}s infinite;">
        <!-- Card -->
        <rect x="0" y="0" width="{card_w}" height="340" rx="16"
              fill="rgba(8, 14, 32, 0.75)" stroke="{accent}" stroke-width="1" stroke-opacity="0.25" />
        <rect x="0" y="0" width="{card_w}" height="3.5" rx="16" fill="{accent}" opacity="0.6" />

        <!-- Header Zone -->
        <rect x="16" y="16" width="{card_w - 32}" height="120" rx="10" fill="rgba(255,255,255,0.03)"
              stroke="rgba(255,255,255,0.06)" stroke-width="0.8" />

        <!-- Icon -->
        <circle cx="{card_w//2}" cy="60" r="32" fill="rgba(255,255,255,0.03)" stroke="{accent}" stroke-width="1.5" stroke-opacity="0.3"
                style="animation: breathe 4s ease-in-out {delay}s infinite;" />
        <text x="{card_w//2}" y="68" font-size="28" text-anchor="middle">{icon}</text>
        <text x="{card_w//2}" y="110" font-size="10" fill="{accent}" text-anchor="middle" class="mono">PRODUCTION READY</text>

        <!-- Project Name -->
        <text x="{card_w//2}" y="168" font-size="18" font-weight="800" fill="#F1F5F9" text-anchor="middle">{name}</text>
        <text x="{card_w//2}" y="192" font-size="11" fill="#94A3B8" text-anchor="middle">{desc}</text>'''

        # Tech tags
        tag_x = 24
        for ti, tag in enumerate(tags):
            tw = len(tag) * 8 + 24
            svg += f'''
        <rect x="{tag_x}" y="212" width="{tw}" height="24" rx="12" fill="rgba(255,255,255,0.04)" stroke="{accent}" stroke-width="0.7" stroke-opacity="0.4" />
        <text x="{tag_x + tw//2}" y="228" font-size="10" font-weight="600" fill="{accent}" text-anchor="middle" class="mono">{tag}</text>'''
            tag_x += tw + 10

        svg += f'''
        <!-- Action Buttons -->
        <rect x="24" y="256" width="130" height="32" rx="16" fill="{accent}" />
        <text x="89" y="277" font-size="11" font-weight="700" fill="#000" text-anchor="middle">View Code</text>

        <rect x="164" y="256" width="130" height="32" rx="16" fill="none" stroke="#F1F5F9" stroke-width="1" />
        <text x="229" y="277" font-size="11" font-weight="700" fill="#F1F5F9" text-anchor="middle">Live Demo</text>

        <!-- Status Bar -->
        <g transform="translate(24, 305)">
            <circle cx="4" cy="6" r="4" fill="{accent}" style="animation: pulseNeon 2s ease-in-out infinite; --glow-color: {accent};" />
            <text x="16" y="10" font-size="9" fill="#64748B" class="mono">DEPLOYED • v2.0 • 99.9% UPTIME</text>
        </g>
    </g>'''

    svg += f'\n{gen_particles(12, W, H)}\n</svg>'
    with open("assets/aurora_projects.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_projects.svg ({os.path.getsize('assets/aurora_projects.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  8. ARCHITECTURE — 3D System Blueprint
# ══════════════════════════════════════════════════════════════
def generate_architecture():
    W, H = 1200, 450
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />

    {section_title(W//2, 38, "SYSTEM ARCHITECTURE BLUEPRINT", "Enterprise RAG &amp; Agentic AI Pipeline")}
'''
    layers = [
        ("CLIENT LAYER", ["React UI", "Next.js SSR", "WebSocket", "gRPC"], "#00F5FF", 90),
        ("API GATEWAY", ["FastAPI", "Auth/JWT", "Rate Limiter", "Load Balancer"], "#818CF8", 180),
        ("AI ENGINE", ["LLM Orchestrator", "RAG Pipeline", "Vector Search", "Embeddings"], "#A78BFA", 270),
        ("INFRA LAYER", ["AWS EKS", "Docker Swarm", "PostgreSQL", "Redis Cache"], "#34D399", 360),
    ]

    for li, (layer_name, nodes, accent, y) in enumerate(layers):
        svg += f'''
    <text x="60" y="{y}" font-size="10" font-weight="700" fill="{accent}" class="mono" letter-spacing="1">{layer_name}</text>
    <line x1="180" y1="{y - 3}" x2="1140" y2="{y - 3}" stroke="rgba(255,255,255,0.04)" stroke-width="1" stroke-dasharray="4 4" />'''

        for ni, node in enumerate(nodes):
            nx = 200 + ni * 240
            nw = 200
            delay = round(li * 0.3 + ni * 0.15, 2)

            svg += f'''
    <g transform="translate({nx}, {y - 20})" style="animation: float3D 7s ease-in-out {delay}s infinite;">
        <rect x="0" y="0" width="{nw}" height="38" rx="8"
              fill="rgba(8, 14, 32, 0.7)" stroke="{accent}" stroke-width="0.8" stroke-opacity="0.3" />
        <circle cx="18" cy="19" r="6" fill="{accent}" opacity="0.4" />
        <text x="{nw//2 + 8}" y="24" font-size="11" font-weight="600" fill="#E2E8F0" text-anchor="middle">{node}</text>
    </g>'''

        # Connection arrows between layers
        if li < len(layers) - 1:
            for ni in range(len(nodes)):
                ax = 300 + ni * 240
                svg += f'''
    <line x1="{ax}" y1="{y + 18}" x2="{ax}" y2="{y + 52}" stroke="{accent}" stroke-width="1" stroke-opacity="0.2" stroke-dasharray="3 3">
        <animate attributeName="stroke-opacity" values="0.1;0.5;0.1" dur="3s" begin="{ni * 0.3}s" repeatCount="indefinite" />
    </line>'''

    svg += f'\n{gen_particles(10, W, H)}\n</svg>'
    with open("assets/aurora_architecture.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_architecture.svg ({os.path.getsize('assets/aurora_architecture.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  9. RADAR — 3D Engineering Competency Radar
# ══════════════════════════════════════════════════════════════
def generate_radar():
    W, H = 1200, 450
    cx, cy = W // 2, 250
    max_r = 150
    skills_radar = [
        ("AI/ML", 0.95), ("Backend", 0.88), ("Cloud", 0.82),
        ("DevOps", 0.80), ("Frontend", 0.78), ("System Design", 0.85),
    ]
    n = len(skills_radar)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#hex-grid)" rx="18" />

    {section_title(W//2, 38, "ENGINEERING COMPETENCY RADAR", "Multi-Dimensional Skill Analysis")}
'''

    # Radar grid rings
    for ring in range(5):
        r = max_r * (ring + 1) / 5
        pts = []
        for i in range(n):
            angle = (2 * math.pi * i / n) - math.pi / 2
            pts.append(f"{cx + r * math.cos(angle):.1f},{cy + r * math.sin(angle):.1f}")
        svg += f'<polygon points="{" ".join(pts)}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="0.8" />\n'

    # Radar axes
    for i in range(n):
        angle = (2 * math.pi * i / n) - math.pi / 2
        ex = cx + max_r * math.cos(angle)
        ey = cy + max_r * math.sin(angle)
        svg += f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="rgba(255,255,255,0.08)" stroke-width="0.8" />\n'

    # Data polygon
    data_pts = []
    for i, (_, val) in enumerate(skills_radar):
        angle = (2 * math.pi * i / n) - math.pi / 2
        r = max_r * val
        data_pts.append(f"{cx + r * math.cos(angle):.1f},{cy + r * math.sin(angle):.1f}")

    svg += f'''
    <polygon points="{" ".join(data_pts)}" fill="rgba(0, 245, 255, 0.08)" stroke="#00F5FF" stroke-width="2"
             style="animation: breathe 4s ease-in-out infinite;" filter="url(#soft-glow)" />'''

    # Data points and labels
    for i, (name, val) in enumerate(skills_radar):
        angle = (2 * math.pi * i / n) - math.pi / 2
        r = max_r * val
        px = cx + r * math.cos(angle)
        py = cy + r * math.sin(angle)
        lx = cx + (max_r + 30) * math.cos(angle)
        ly = cy + (max_r + 30) * math.sin(angle)

        svg += f'''
    <circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="#00F5FF" stroke="#FFF" stroke-width="1.5"
            style="animation: pulseNeon 3s ease-in-out {i * 0.3}s infinite; --glow-color: #00F5FF;" />
    <text x="{lx:.1f}" y="{ly:.1f}" font-size="11" font-weight="700" fill="#E2E8F0" text-anchor="middle">{name}</text>
    <text x="{lx:.1f}" y="{ly + 16:.1f}" font-size="9" fill="#00F5FF" text-anchor="middle" class="mono">{int(val*100)}%</text>'''

    # Orbital ring decoration
    svg += f'''
    <ellipse cx="{cx}" cy="{cy}" rx="{max_r + 60}" ry="{max_r // 3 + 10}" fill="none"
             stroke="rgba(129, 140, 248, 0.12)" stroke-width="1" stroke-dasharray="8 12"
             style="transform-origin: {cx}px {cy}px; animation: orbitCW 30s linear infinite;" />
    '''

    svg += f'\n{gen_particles(10, W, H)}\n</svg>'
    with open("assets/aurora_radar.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_radar.svg ({os.path.getsize('assets/aurora_radar.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  10. DAILY ROUTINE — 3D Timeline
# ══════════════════════════════════════════════════════════════
def generate_routine():
    W, H = 1200, 350
    timeline = [
        ("06:00", "🌅", "Wake Up &amp; Exercise", "#FBBF24"),
        ("08:00", "💻", "Deep Work: AI/ML Projects", "#00F5FF"),
        ("12:00", "📚", "Research &amp; Learning", "#818CF8"),
        ("14:00", "🔧", "Backend &amp; System Design", "#34D399"),
        ("18:00", "🚀", "Open Source &amp; Deployment", "#F472B6"),
        ("22:00", "🌙", "Review &amp; Planning", "#A78BFA"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#iso-grid)" rx="18" />

    {section_title(W//2, 38, "DAILY ENGINEERING ROUTINE", "Optimal Workflow Schedule")}
'''

    # Timeline horizontal line
    line_y = 170
    svg += f'<line x1="60" y1="{line_y}" x2="1140" y2="{line_y}" stroke="rgba(255,255,255,0.1)" stroke-width="2" />\n'
    svg += f'<line x1="60" y1="{line_y}" x2="1140" y2="{line_y}" stroke="url(#cyan-grad)" stroke-width="1" opacity="0.4" stroke-dasharray="6 4" />\n'

    gap = (1080) // (len(timeline))
    for i, (time, icon, activity, color) in enumerate(timeline):
        x = 100 + i * gap
        delay = round(i * 0.3, 1)

        svg += f'''
    <g transform="translate({x}, {line_y})" style="animation: float3D 5s ease-in-out {delay}s infinite;">
        <!-- Node -->
        <circle cx="0" cy="0" r="8" fill="{color}" stroke="#FFF" stroke-width="1.5"
                style="animation: pulseNeon 3s ease-in-out {delay}s infinite; --glow-color: {color};" filter="url(#soft-glow)" />

        <!-- Card Above -->
        <rect x="-60" y="-90" width="120" height="70" rx="10"
              fill="rgba(8, 14, 32, 0.7)" stroke="{color}" stroke-width="0.8" stroke-opacity="0.3" />
        <text x="0" y="-60" font-size="20" text-anchor="middle">{icon}</text>
        <text x="0" y="-38" font-size="9" fill="#E2E8F0" text-anchor="middle" font-weight="600">{activity}</text>

        <!-- Time Below -->
        <text x="0" y="30" font-size="11" fill="{color}" text-anchor="middle" class="mono" font-weight="700">{time}</text>
    </g>'''

    svg += f'\n{gen_particles(8, W, H)}\n</svg>'
    with open("assets/aurora_routine.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_routine.svg ({os.path.getsize('assets/aurora_routine.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  11. CONTACT — 3D Holographic Connection Card
# ══════════════════════════════════════════════════════════════
def generate_contact():
    W, H = 1200, 200
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}
    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />
    <rect width="100%" height="100%" fill="url(#hex-grid)" rx="18" />
    {gen_constellation_lines(10, W, H)}

    {section_title(W//2, 38, "LET'S CONNECT &amp; COLLABORATE")}

    <g transform="translate({W//2}, 110)">
        <rect x="-300" y="-30" width="600" height="60" rx="30"
              fill="rgba(0, 245, 255, 0.06)" stroke="#00F5FF" stroke-width="1.2" stroke-opacity="0.4"
              style="animation: breathe 4s ease-in-out infinite;" />
        <text x="0" y="5" font-size="14" font-weight="600" fill="#F1F5F9" text-anchor="middle" letter-spacing="1">
            Open to collaborations, freelance, and full-time opportunities
        </text>
        <text x="0" y="48" font-size="11" fill="#64748B" text-anchor="middle" class="mono">
            amit@quantum-nexus.dev • github.com/Amit123103
        </text>
    </g>

    {gen_particles(6, W, H)}
</svg>'''

    with open("assets/aurora_contact.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_contact.svg ({os.path.getsize('assets/aurora_contact.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  12. FOOTER — Cinematic Cityscape with Infinite Slider
# ══════════════════════════════════════════════════════════════
def generate_footer():
    W, H = 1200, 180
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">
    {shared_defs()}

    <rect width="100%" height="100%" fill="url(#bg-gradient)" rx="18" />

    <!-- Animated gradient line -->
    <rect x="0" y="0" width="100%" height="2" fill="url(#cyan-grad)" opacity="0.4" />

    <!-- Center Quote -->
    <text x="{W//2}" y="60" font-size="16" font-weight="700" fill="#F1F5F9" text-anchor="middle" letter-spacing="2">
        "Building the Future, One Commit at a Time"
    </text>
    <text x="{W//2}" y="85" font-size="11" fill="#64748B" text-anchor="middle" class="mono" letter-spacing="1">
        Amit Kumar • Software Developer • AI &amp; ML • MLOps
    </text>

    <!-- Animated Dots -->
    <g transform="translate({W//2}, 120)">
        <circle cx="-20" cy="0" r="3" fill="#00F5FF" style="animation: pulseNeon 2s ease-in-out 0s infinite; --glow-color: #00F5FF;" />
        <circle cx="0" cy="0" r="3" fill="#818CF8" style="animation: pulseNeon 2s ease-in-out 0.3s infinite; --glow-color: #818CF8;" />
        <circle cx="20" cy="0" r="3" fill="#34D399" style="animation: pulseNeon 2s ease-in-out 0.6s infinite; --glow-color: #34D399;" />
    </g>

    <!-- Bottom line -->
    <text x="{W//2}" y="155" font-size="9" fill="#475569" text-anchor="middle" class="mono">
        © 2025 Amit Kumar • Crafted with ❤️ &amp; Quantum Engineering
    </text>

    {gen_particles(6, W, H)}
</svg>'''

    with open("assets/aurora_footer.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✓ Generated assets/aurora_footer.svg ({os.path.getsize('assets/aurora_footer.svg') / 1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════
#  MAIN — Build All
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("  ULTIMATE 3D MOTION PROFILE ENGINE v5.0")
    print("  Complete Redesign: Holographic · Isometric · Cinematic")
    print("=" * 60)
    print()

    generate_hero_terminal()
    generate_badges()
    generate_tech_badges()
    generate_about()
    generate_skills()
    generate_languages()
    generate_projects()
    generate_architecture()
    generate_radar()
    generate_routine()
    generate_contact()
    generate_footer()

    print()
    print("=" * 60)
    print("  ✓ ALL 12 SECTIONS GENERATED SUCCESSFULLY")
    print("  ✓ 3D Holographic · Glassmorphism · Particle Systems")
    print("  ✓ Orbital Rings · Radial Charts · Animated Bars")
    print("=" * 60)
