import re
import glob
import os
import random

def fix_imports():
    for py_file in glob.glob('*.py'):
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = re.sub(r'^\s*@import\s+url\([^)]+\);\s*\n?', '', content, flags=re.MULTILINE)
        cleaned = cleaned.replace("font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;", "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;")
        if cleaned != content:
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f"Cleaned {py_file}")

def generate_3d_contrib():
    width = 1200
    height = 420
    
    # 3D isometric projection helpers
    # iso: x_screen = (x - y) * cos(30), y_screen = (x + y) * sin(30) - z
    cos30 = 0.866
    sin30 = 0.5
    
    tile_w = 20
    tile_h = 12
    
    cols = 40
    rows = 7
    
    origin_x = 600
    origin_y = 120
    
    colors = ["#0e4429", "#006d32", "#26a641", "#39d353", "#00F5FF"]
    
    bars = []
    
    # Generate random realistic height map for 3D contribution graph
    random.seed(42)
    for r in range(rows):
        for c in range(cols):
            # simulate contribution intensity
            val = random.choices([0, 1, 2, 3, 4], weights=[0.4, 0.25, 0.2, 0.1, 0.05])[0]
            if val > 0:
                h = val * 15 + random.randint(5, 15)
            else:
                h = 4
            bars.append((r, c, val, h))
            
    # Sort bars by depth (r + c) so rendering order is back-to-front
    bars.sort(key=lambda b: (b[0] + b[1], b[0]))
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <style>
            text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #8B949E; font-size: 12px; }}
            .cube {{ transition: all 0.5s ease; }}
            .cube:hover {{ filter: brightness(1.3); }}
            @keyframes pulse-cube {{
                0% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-6px); }}
                100% {{ transform: translateY(0px); }}
            }}
            .anim-pulse {{ animation: pulse-cube 3s ease-in-out infinite alternate; }}
        </style>
        <linearGradient id="grid-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0f1c"/>
            <stop offset="100%" stop-color="#020408"/>
        </linearGradient>
    </defs>

    <rect width="100%" height="100%" fill="url(#grid-bg)" rx="12" />
    
    <text x="600" y="40" font-size="18" font-weight="600" text-anchor="middle" fill="#00F5FF" letter-spacing="2">3D CONTRIBUTION MATRIX</text>
    <rect x="580" y="52" width="40" height="2" fill="#00F5FF" />

    <g transform="translate(0, 40)">
'''

    for r, c, val, bar_h in bars:
        # iso coords
        sx = origin_x + (c - r) * 14
        sy = origin_y + (c + r) * 8
        
        color = colors[val] if val > 0 else "#161b22"
        top_color = "#39d353" if val == 4 else ( "#26a641" if val == 3 else ( "#006d32" if val == 2 else ( "#0e4429" if val == 1 else "#21262d" ) ) )
        side_color1 = "#0e4429" if val > 0 else "#161b22"
        side_color2 = "#006d32" if val > 0 else "#0d1117"
        
        # 3D block isometric vertices
        # Top face polygon
        top_poly = f"{sx},{sy - bar_h} {sx + 12},{sy + 6 - bar_h} {sx},{sy + 12 - bar_h} {sx - 12},{sy + 6 - bar_h}"
        # Left face polygon
        left_poly = f"{sx - 12},{sy + 6 - bar_h} {sx},{sy + 12 - bar_h} {sx},{sy + 12} {sx - 12},{sy + 6}"
        # Right face polygon
        right_poly = f"{sx},{sy + 12 - bar_h} {sx + 12},{sy + 6 - bar_h} {sx + 12},{sy + 6} {sx},{sy + 12}"
        
        anim_class = "anim-pulse" if val >= 3 else ""
        delay = (r + c) * 0.05
        
        svg += f'''
        <g class="cube {anim_class}" style="animation-delay: {delay:.2f}s;">
            <polygon points="{left_poly}" fill="{side_color1}" opacity="0.8" />
            <polygon points="{right_poly}" fill="{side_color2}" opacity="0.9" />
            <polygon points="{top_poly}" fill="{top_color}" stroke="rgba(255,255,255,0.15)" stroke-width="0.5" />
        </g>
'''

    svg += '''
    </g>
</svg>
'''
    os.makedirs("profile-3d-contrib", exist_ok=True)
    with open("profile-3d-contrib/profile-green-animate.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated 3D isometric contribution graph!")

if __name__ == "__main__":
    fix_imports()
    generate_3d_contrib()
