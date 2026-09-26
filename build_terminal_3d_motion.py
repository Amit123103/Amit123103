import math
import numpy as np
import cv2
from PIL import Image
import os
import base64

def generate_all_3d_assets():
    base_path = "assets/terminal_profile_artwork.jpg"
    if not os.path.exists(base_path):
        print(f"Error: {base_path} not found.")
        return
    
    # Load base image
    base_bgr = cv2.imread(base_path)
    orig_h, orig_w, _ = base_bgr.shape
    
    # Target resolution: 920x514 (ultra-sharp 16:9, optimal 5-6MB GIF size for GitHub)
    target_w = 920
    target_h = int(target_w * (orig_h / orig_w))
    base = cv2.resize(base_bgr, (target_w, target_h), interpolation=cv2.INTER_AREA)
    
    num_frames = 50
    fps = 13  # 76ms per frame -> ~3.85s full cycle (relaxed, cinematic slow motion)
    frame_duration_ms = 76
    frames = []
    
    # Seed 3D particles
    np.random.seed(1337)
    num_particles = 140
    # Particles around portrait and terminal
    px = np.random.uniform(-350, 450, num_particles)
    py = np.random.uniform(-250, 250, num_particles)
    pz = np.random.uniform(40, 380, num_particles)
    p_phase = np.random.uniform(0, 2 * math.pi, num_particles)
    p_speed = np.random.uniform(0.8, 1.8, num_particles)
    
    # Center of ASCII portrait head
    portrait_cx = int(target_w * 0.28) # ~258
    portrait_cy = int(target_h * 0.44) # ~226
    camera_d = 480
    
    print(f"Synthesizing {num_frames} frames of high-fidelity 3D motion graphics...")
    
    for f in range(num_frames):
        t = f / num_frames
        angle = t * 2 * math.pi
        
        frame = base.copy().astype(np.float32)
        glow_layer = np.zeros_like(frame)
        hud_layer = np.zeros_like(frame)
        
        # 1. 3D Holographic Scanning Laser with Volumetric Falloff
        scan_norm = (math.sin(angle - math.pi/2) + 1.0) / 2.0
        scan_y = int(target_h * (0.04 + 0.92 * scan_norm))
        beam_h = 30
        y_min = max(0, scan_y - beam_h)
        y_max = min(target_h, scan_y + beam_h)
        for y in range(y_min, y_max):
            dist = abs(y - scan_y)
            # Core laser beam
            alpha = math.exp(- (dist**2) / 45.0)
            glow_layer[y, :, 0] += alpha * 200 # Cyan B
            glow_layer[y, :, 1] += alpha * 255 # Cyan G
            glow_layer[y, :, 2] += alpha * 90  # Cyan R
            
            # Volumetric aura
            amb = math.exp(- (dist**2) / 380.0) * 0.4
            glow_layer[y, :, 0] += amb * 140
            glow_layer[y, :, 1] += amb * 190
            glow_layer[y, :, 2] += amb * 40
        
        # 2. 3D Rotating Gyroscope & Orbital Ring 1 (Tilted around X, rotating around Z)
        ring1_r = 180
        tilt_x1 = math.radians(68)
        num_pts = 72
        r1_pts = []
        for i in range(num_pts):
            theta = (i / num_pts) * 2 * math.pi + angle
            rx = ring1_r * math.cos(theta)
            ry = ring1_r * math.sin(theta)
            rz = 0
            
            ry_t = ry * math.cos(tilt_x1) - rz * math.sin(tilt_x1)
            rz_t = ry * math.sin(tilt_x1) + rz * math.cos(tilt_x1)
            
            scale = camera_d / (camera_d + rz_t + 100)
            sx = int(portrait_cx + rx * scale)
            sy = int(portrait_cy + ry_t * scale)
            r1_pts.append((sx, sy, rz_t))
        
        for i in range(len(r1_pts)):
            if (i // 3) % 2 == 0:
                p1 = r1_pts[i]
                p2 = r1_pts[(i + 1) % len(r1_pts)]
                if 0 <= p1[0] < target_w and 0 <= p1[1] < target_h and 0 <= p2[0] < target_w and 0 <= p2[1] < target_h:
                    bright = np.clip(1.0 - (p1[2] / 350.0), 0.35, 1.25)
                    color = (int(255 * bright), int(230 * bright), int(60 * bright))
                    cv2.line(hud_layer, (p1[0], p1[1]), (p2[0], p2[1]), color, 1, cv2.LINE_AA)
                    cv2.line(glow_layer, (p1[0], p1[1]), (p2[0], p2[1]), color, 3, cv2.LINE_AA)
        
        # 3. 3D Orbital Ring 2 (Dual tilt: X & Y axes, counter-rotating)
        ring2_r = 235
        tilt_x2 = math.radians(-45)
        tilt_y2 = math.radians(35)
        r2_pts = []
        for i in range(num_pts):
            theta = (i / num_pts) * 2 * math.pi - angle * 0.9
            rx = ring2_r * math.cos(theta)
            ry = ring2_r * math.sin(theta)
            rz = 0
            
            rx_t = rx * math.cos(tilt_y2) + rz * math.sin(tilt_y2)
            rz_temp = -rx * math.sin(tilt_y2) + rz * math.cos(tilt_y2)
            ry_t = ry * math.cos(tilt_x2) - rz_temp * math.sin(tilt_x2)
            rz_t = ry * math.sin(tilt_x2) + rz_temp * math.cos(tilt_x2)
            
            scale = camera_d / (camera_d + rz_t + 100)
            sx = int(portrait_cx + rx_t * scale)
            sy = int(portrait_cy + ry_t * scale)
            r2_pts.append((sx, sy, rz_t))
        
        for i in range(len(r2_pts)):
            if (i // 5) % 2 == 0:
                p1 = r2_pts[i]
                p2 = r2_pts[(i + 1) % len(r2_pts)]
                if 0 <= p1[0] < target_w and 0 <= p1[1] < target_h and 0 <= p2[0] < target_w and 0 <= p2[1] < target_h:
                    bright = np.clip(1.0 - (p1[2] / 450.0), 0.3, 1.15)
                    color = (int(255 * bright), int(170 * bright), int(90 * bright))
                    cv2.line(hud_layer, (p1[0], p1[1]), (p2[0], p2[1]), color, 1, cv2.LINE_AA)
            if i % 18 == 0:
                p = r2_pts[i]
                if 0 <= p[0] < target_w and 0 <= p[1] < target_h:
                    cv2.circle(hud_layer, (p[0], p[1]), 3, (255, 255, 255), -1, cv2.LINE_AA)
                    cv2.circle(glow_layer, (p[0], p[1]), 8, (255, 210, 0), -1, cv2.LINE_AA)
        
        # 4. Floating 3D Depth Particle Field with Constellation Interconnects
        active_coords = []
        for i in range(num_particles):
            cur_z = pz[i] + math.sin(angle + p_phase[i]) * 70
            cur_x = px[i] + math.cos(angle * p_speed[i] + p_phase[i]) * 25
            cur_y = py[i] + math.sin(angle * p_speed[i] + p_phase[i]) * 20
            
            scale = camera_d / (camera_d + cur_z)
            sx = int(portrait_cx + cur_x * scale)
            sy = int(portrait_cy + cur_y * scale)
            
            if 8 <= sx < target_w - 8 and 8 <= sy < target_h - 8:
                active_coords.append((sx, sy, cur_z))
                intensity = np.clip(1.0 - (cur_z / 420.0), 0.15, 1.0)
                p_r = 2 if cur_z < 180 else 1
                p_col = (int(255 * intensity), int(230 * intensity), int(120 * intensity))
                cv2.circle(hud_layer, (sx, sy), p_r, p_col, -1, cv2.LINE_AA)
                if cur_z < 160:
                    cv2.circle(glow_layer, (sx, sy), p_r + 3, (int(220 * intensity), int(160 * intensity), 0), -1, cv2.LINE_AA)
        
        # Connect close neighboring particles in 3D
        for i in range(0, len(active_coords), 3):
            for j in range(i + 1, min(i + 6, len(active_coords))):
                dx = active_coords[i][0] - active_coords[j][0]
                dy = active_coords[i][1] - active_coords[j][1]
                dist_2d = math.hypot(dx, dy)
                if dist_2d < 35:
                    line_alpha = (1.0 - dist_2d / 35.0) * 0.4
                    line_col = (int(255 * line_alpha), int(200 * line_alpha), int(80 * line_alpha))
                    cv2.line(hud_layer, (active_coords[i][0], active_coords[i][1]), (active_coords[j][0], active_coords[j][1]), line_col, 1, cv2.LINE_AA)
        
        # 5. Terminal Window Neon Border Pulse
        # Terminal bounding box: (left: 475, top: 70, right: 890, bottom: 440) in target coords
        t_x1, t_y1, t_x2, t_y2 = int(target_w * 0.515), int(target_h * 0.14), int(target_w * 0.97), int(target_h * 0.855)
        pulse_alpha = 0.5 + 0.5 * math.sin(angle * 2)
        cv2.rectangle(glow_layer, (t_x1, t_y1), (t_x2, t_y2), (int(160 * pulse_alpha), int(220 * pulse_alpha), 0), 2)
        
        # 6. Blinking Terminal Command Cursor
        cur_x = int(target_w * 0.69)
        cur_y = int(target_h * 0.77)
        if math.sin(angle * 4) > 0:
            cv2.rectangle(hud_layer, (cur_x, cur_y - 11), (cur_x + 8, cur_y + 1), (255, 255, 50), -1)
            cv2.rectangle(glow_layer, (cur_x - 1, cur_y - 12), (cur_x + 9, cur_y + 2), (200, 180, 0), -1)
        
        # 7. Sci-Fi HUD Crosshairs, Status & Neural Equalizer
        # Glowing radar status indicator
        cv2.circle(hud_layer, (target_w - 240, 18), 3, (0, 255, 255), -1, cv2.LINE_AA)
        cv2.circle(glow_layer, (target_w - 240, 18), 7, (0, 220, 255), -1, cv2.LINE_AA)
        cv2.putText(hud_layer, "CORE: QUANTUM_NEXUS // ACTIVE", (target_w - 230, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 245, 255), 1, cv2.LINE_AA)
        latency = 12 + int(3 * math.sin(angle * 2))
        cv2.putText(hud_layer, f"TELEMETRY: {latency}ms | 60 FPS // LOCKED", (target_w - 230, 36), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (180, 255, 100), 1, cv2.LINE_AA)
        
        # Neural Waveform Audio Equalizer
        eq_x = int(target_w * 0.54)
        eq_y = int(target_h * 0.94)
        num_bars = 28
        bar_w = 4
        bar_gap = 5
        for b in range(num_bars):
            bar_phase = angle * 3 + b * 0.38
            h_bar = int(3 + 13 * abs(math.sin(bar_phase) * math.cos(angle + b * 0.18)))
            bx = eq_x + b * (bar_w + bar_gap)
            ratio = b / num_bars
            c_b = int(255 * (1.0 - ratio) + 180 * ratio)
            c_g = int(210 * (1.0 - ratio) + 70 * ratio)
            c_r = int(60 * (1.0 - ratio) + 230 * ratio)
            cv2.rectangle(hud_layer, (bx, eq_y - h_bar), (bx + bar_w, eq_y), (c_b, c_g, c_r), -1)
            cv2.rectangle(glow_layer, (bx - 1, eq_y - h_bar - 2), (bx + bar_w + 1, eq_y + 2), (int(c_b*0.5), int(c_g*0.4), int(c_r*0.5)), -1)
        
        # 8. Volumetric Bloom Filtering & Optical Compositing
        glow_soft = cv2.GaussianBlur(glow_layer, (15, 15), 0)
        glow_wide = cv2.GaussianBlur(glow_layer, (35, 35), 0) * 0.45
        composed = frame + glow_soft * 0.85 + glow_wide + hud_layer
        composed = np.clip(composed, 0, 255).astype(np.uint8)
        
        rgb_frame = cv2.cvtColor(composed, cv2.COLOR_BGR2RGB)
        frames.append(Image.fromarray(rgb_frame))
        
        if (f + 1) % 10 == 0 or f == num_frames - 1:
            print(f"Rendered frame {f + 1}/{num_frames}")
    
    # 1. Save WebP (ultra-high fidelity, lightweight)
    output_webp = "assets/terminal_profile_3d.webp"
    print(f"Encoding {output_webp}...")
    frames[0].save(
        output_webp,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration_ms,
        loop=0,
        quality=85
    )
    print(f"Saved {output_webp} ({os.path.getsize(output_webp)/(1024*1024):.2f} MB)")
    
    # 2. Save GIF with optimized palette
    output_gif = "assets/terminal_profile_3d.gif"
    print(f"Quantizing and encoding {output_gif}...")
    palette = frames[0].quantize(colors=128, method=Image.MEDIANCUT)
    quantized_frames = [f.quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG) for f in frames]
    quantized_frames[0].save(
        output_gif,
        save_all=True,
        append_images=quantized_frames[1:],
        duration=frame_duration_ms,
        loop=0,
        optimize=True
    )
    print(f"Saved {output_gif} ({os.path.getsize(output_gif)/(1024*1024):.2f} MB)")
    
    # 3. Generate Interactive SVG with Live 3D CSS Keyframes
    generate_3d_svg(base_path)

def generate_3d_svg(base_path):
    with open(base_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768" width="100%" height="100%">
    <defs>
        <style>
            @keyframes scanline {{
                0% {{ transform: translateY(0px); opacity: 0.8; }}
                50% {{ transform: translateY(720px); opacity: 1; }}
                100% {{ transform: translateY(0px); opacity: 0.8; }}
            }}
            @keyframes rotate3D {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            @keyframes rotate3DRev {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(-360deg); }}
            }}
            @keyframes pulseGlow {{
                0% {{ opacity: 0.4; filter: drop-shadow(0 0 8px rgba(0, 245, 255, 0.4)); }}
                50% {{ opacity: 0.9; filter: drop-shadow(0 0 20px rgba(0, 245, 255, 0.9)); }}
                100% {{ opacity: 0.4; filter: drop-shadow(0 0 8px rgba(0, 245, 255, 0.4)); }}
            }}
            @keyframes cursorBlink {{
                0%, 49% {{ opacity: 1; }}
                50%, 100% {{ opacity: 0; }}
            }}
            @keyframes floatParticle {{
                0% {{ transform: translateY(0px) scale(0.9); opacity: 0.3; }}
                50% {{ transform: translateY(-25px) scale(1.1); opacity: 0.9; }}
                100% {{ transform: translateY(0px) scale(0.9); opacity: 0.3; }}
            }}
            .laser-beam {{
                animation: scanline 7s ease-in-out infinite;
            }}
            .gyro-ring1 {{
                transform-origin: 380px 340px;
                animation: rotate3D 22s linear infinite;
            }}
            .gyro-ring2 {{
                transform-origin: 380px 340px;
                animation: rotate3DRev 32s linear infinite;
            }}
            .terminal-pulse {{
                animation: pulseGlow 5s ease-in-out infinite;
            }}
            .cursor {{
                animation: cursorBlink 1s step-start infinite;
            }}
            .particle {{
                animation: floatParticle 5s ease-in-out infinite alternate;
            }}
        </style>
        
        <linearGradient id="laser-grad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="rgba(0, 245, 255, 0)" />
            <stop offset="50%" stop-color="rgba(0, 245, 255, 0.85)" />
            <stop offset="100%" stop-color="rgba(0, 245, 255, 0)" />
        </linearGradient>

        <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00F5FF" />
            <stop offset="100%" stop-color="#0EA5E9" />
        </linearGradient>
    </defs>
    
    <!-- Base Photorealistic Terminal & ASCII Portrait Artwork -->
    <image href="data:image/jpeg;base64,{img_b64}" width="1376" height="768" />
    
    <!-- 3D Gyroscope Orbital Rings (Centered on Portrait Head: 380, 340) -->
    <g class="gyro-ring1" opacity="0.75">
        <ellipse cx="380" cy="340" rx="260" ry="110" fill="none" stroke="url(#neon-cyan)" stroke-width="1.5" stroke-dasharray="12 18" />
        <circle cx="640" cy="340" r="4" fill="#00F5FF" />
        <circle cx="120" cy="340" r="3" fill="#38BDF8" />
    </g>

    <g class="gyro-ring2" opacity="0.6">
        <ellipse cx="380" cy="340" rx="310" ry="135" fill="none" stroke="#818CF8" stroke-width="1.2" stroke-dasharray="24 16 8 16" />
        <circle cx="690" cy="340" r="5" fill="#818CF8" />
        <circle cx="70" cy="340" r="4" fill="#C084FC" />
    </g>
    
    <!-- Sweeping 3D Holographic Laser Beam -->
    <g class="laser-beam">
        <rect x="0" y="0" width="1376" height="8" fill="url(#laser-grad)" />
        <line x1="0" y1="4" x2="1376" y2="4" stroke="#FFFFFF" stroke-width="1.5" opacity="0.9" />
    </g>
    
    <!-- Terminal Border Neon Pulse -->
    <rect x="715" y="105" width="620" height="545" rx="14" fill="none" stroke="#00F5FF" stroke-width="1.5" class="terminal-pulse" />
    
    <!-- Animated Monospace Cursor -->
    <rect x="948" y="588" width="10" height="18" fill="#00F5FF" class="cursor" />
    
    <!-- Floating 3D Depth Particles -->
    <circle cx="280" cy="180" r="3" fill="#00F5FF" class="particle" style="animation-delay: 0.2s;" />
    <circle cx="450" cy="220" r="2" fill="#38BDF8" class="particle" style="animation-delay: 0.8s;" />
    <circle cx="220" cy="400" r="3" fill="#818CF8" class="particle" style="animation-delay: 1.4s;" />
    <circle cx="490" cy="450" r="2.5" fill="#00F5FF" class="particle" style="animation-delay: 0.5s;" />
    <circle cx="340" cy="550" r="3" fill="#34D399" class="particle" style="animation-delay: 1.1s;" />
    <circle cx="160" cy="280" r="2" fill="#C084FC" class="particle" style="animation-delay: 1.7s;" />
</svg>'''
    
    output_svg = "assets/terminal_profile_3d.svg"
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {output_svg} ({os.path.getsize(output_svg)/(1024*1024):.2f} MB)")

if __name__ == "__main__":
    generate_all_3d_assets()

