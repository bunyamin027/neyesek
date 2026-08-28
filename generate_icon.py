import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def create_app_icon(output_path="assets/images/app_icon.png", size=1024):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background Gradient (Dark Indigo to Deep Purple)
    for y in range(size):
        ratio = y / size
        # Top: (15, 12, 35), Bottom: (25, 10, 48)
        r = int(12 + 18 * ratio)
        g = int(10 + 8 * (1 - ratio))
        b = int(28 + 32 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # 2. Ambient Glow in the Center
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    center = (size // 2, size // 2)
    glow_radius = int(size * 0.42)
    
    for r in range(glow_radius, 0, -8):
        alpha = int(45 * (1 - (r / glow_radius) ** 1.5))
        glow_draw.ellipse(
            [center[0] - r, center[1] - r, center[0] + r, center[1] + r],
            fill=(255, 107, 53, alpha)  # Coral orange glow
        )
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # 3. Outer Golden Ring with Drop Shadow
    wheel_radius = int(size * 0.36)
    ring_thickness = int(size * 0.028)
    
    # Shadow
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_offset = int(size * 0.02)
    shadow_draw.ellipse(
        [center[0] - wheel_radius - ring_thickness, 
         center[1] - wheel_radius - ring_thickness + shadow_offset, 
         center[0] + wheel_radius + ring_thickness, 
         center[1] + wheel_radius + ring_thickness + shadow_offset],
        fill=(0, 0, 0, 160)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(int(size * 0.03)))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)

    # 4. Wheel Segments
    # 8 Appetizing vibrant colors
    colors = [
        (255, 75, 75),   # Coral Red (Pizza/Meat)
        (255, 165, 0),   # Bright Orange (Tacos/Curry)
        (255, 215, 0),   # Golden Yellow (Cheese/Pasta)
        (76, 209, 55),   # Fresh Green (Salad/Herb)
        (0, 168, 255),   # Azure Blue (Seafood)
        (156, 136, 255), # Lilac Purple (Boba/Exotic)
        (232, 65, 120),  # Berry Pink (Dessert/Sushi)
        (225, 112, 85),  # Teriyaki Brown (BBQ/Grill)
    ]
    num_segments = len(colors)
    angle_step = 360 / num_segments

    # Draw segment pies
    pie_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pie_draw = ImageDraw.Draw(pie_img)
    
    bbox = [center[0] - wheel_radius, center[1] - wheel_radius, 
            center[0] + wheel_radius, center[1] + wheel_radius]
    
    for i, color in enumerate(colors):
        start_angle = i * angle_step - 22.5
        end_angle = (i + 1) * angle_step - 22.5
        pie_draw.pieslice(bbox, start=start_angle, end=end_angle, fill=(*color, 255))
        
        # Subtle segment separator lines
        rad = math.radians(start_angle)
        x_end = center[0] + wheel_radius * math.cos(rad)
        y_end = center[1] + wheel_radius * math.sin(rad)
        pie_draw.line([center, (x_end, y_end)], fill=(255, 255, 255, 140), width=4)

    # Draw crisp vector silhouettes on each segment
    for i in range(num_segments):
        mid_angle = math.radians((i * angle_step) - 22.5 + (angle_step / 2))
        icon_dist = wheel_radius * 0.62
        ix = center[0] + icon_dist * math.cos(mid_angle)
        iy = center[1] + icon_dist * math.sin(mid_angle)
        
        # Draw distinctive stylized symbols
        s = int(size * 0.026)
        if i == 0: # Pizza slice (triangle with crust)
            pie_draw.polygon([(ix, iy - s), (ix - s, iy + s), (ix + s, iy + s)], fill=(255, 255, 255, 230))
            pie_draw.ellipse([ix - s, iy + s - 3, ix + s, iy + s + 3], fill=(255, 220, 100, 240))
        elif i == 1: # Burger (bun, patty, bun)
            pie_draw.rounded_rectangle([ix - s, iy - s, ix + s, iy - s//2], radius=4, fill=(255, 255, 255, 230))
            pie_draw.rectangle([ix - s + 2, iy - s//4, ix + s - 2, iy + s//4], fill=(255, 220, 120, 240))
            pie_draw.rounded_rectangle([ix - s, iy + s//2, ix + s, iy + s], radius=3, fill=(255, 255, 255, 230))
        elif i == 2: # Taco / Crescent
            pie_draw.pieslice([ix - s, iy - s, ix + s, iy + s], start=180, end=360, fill=(255, 255, 255, 230))
            pie_draw.ellipse([ix - s//2, iy - 2, ix + s//2, iy + 4], fill=(255, 215, 0, 240))
        elif i == 3: # Salad / Leaf
            pie_draw.pieslice([ix - s, iy - s, ix + s, iy + s], start=45, end=225, fill=(255, 255, 255, 230))
            pie_draw.line([ix - s//2, iy + s//2, ix + s//2, iy - s//2], fill=(255, 255, 255, 240), width=3)
        elif i == 4: # Sushi roll (circle with center dot)
            pie_draw.ellipse([ix - s, iy - s, ix + s, iy + s], fill=(255, 255, 255, 230), outline=(255, 255, 255, 255), width=2)
            pie_draw.ellipse([ix - s//2, iy - s//2, ix + s//2, iy + s//2], fill=(255, 100, 80, 240))
        elif i == 5: # Noodle Bowl & Chopsticks
            pie_draw.pieslice([ix - s, iy - s//2, ix + s, iy + s], start=0, end=180, fill=(255, 255, 255, 230))
            pie_draw.line([ix - s - 2, iy - s//2, ix + s + 2, iy - s//2], fill=(255, 255, 255, 240), width=4)
            pie_draw.line([ix - s, iy - s, ix + s//2, iy], fill=(255, 255, 255, 220), width=3)
        elif i == 6: # Cupcake / Dessert (dome + base)
            pie_draw.ellipse([ix - s, iy - s, ix + s, iy], fill=(255, 255, 255, 230))
            pie_draw.polygon([(ix - s + 3, iy), (ix + s - 3, iy), (ix + s - 6, iy + s), (ix - s + 6, iy + s)], fill=(255, 230, 150, 240))
        else: # Meat / Drumstick
            pie_draw.ellipse([ix - s, iy - s, ix + s//2, iy + s//2], fill=(255, 255, 255, 230))
            pie_draw.line([ix, iy, ix + s, iy + s], fill=(255, 255, 255, 240), width=5)

    img = Image.alpha_composite(img, pie_img)
    draw = ImageDraw.Draw(img)

    # 5. Golden Outer Rim
    for w in range(ring_thickness):
        r = wheel_radius + w
        # Golden gradient based on angle
        alpha = 255
        draw.ellipse([center[0] - r, center[1] - r, center[0] + r, center[1] + r], outline=(255, 200, 55, alpha), width=2)

    # Outer metallic border highlight
    r_outer = wheel_radius + ring_thickness
    draw.ellipse([center[0] - r_outer, center[1] - r_outer, center[0] + r_outer, center[1] + r_outer], outline=(255, 240, 180, 200), width=3)
    
    # Outer light bulbs / studs along the rim
    num_studs = 16
    for i in range(num_studs):
        angle = math.radians(i * (360 / num_studs))
        stud_r = wheel_radius + ring_thickness // 2
        sx = center[0] + stud_r * math.cos(angle)
        sy = center[1] + stud_r * math.sin(angle)
        stud_size = int(size * 0.012)
        draw.ellipse([sx - stud_size, sy - stud_size, sx + stud_size, sy + stud_size], fill=(255, 255, 240, 255), outline=(218, 165, 32, 255), width=2)

    # 6. Central Golden Hub & Cloche / Fork Icon
    hub_radius = int(size * 0.12)
    # Hub Shadow
    hub_shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hs_draw = ImageDraw.Draw(hub_shadow)
    hs_draw.ellipse(
        [center[0] - hub_radius - 6, center[1] - hub_radius,
         center[0] + hub_radius + 6, center[1] + hub_radius + 12],
        fill=(0, 0, 0, 140)
    )
    hub_shadow = hub_shadow.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img, hub_shadow)
    draw = ImageDraw.Draw(img)

    # Hub circles
    draw.ellipse(
        [center[0] - hub_radius, center[1] - hub_radius, center[0] + hub_radius, center[1] + hub_radius],
        fill=(25, 20, 38, 255), outline=(255, 215, 0, 255), width=6
    )
    inner_hub = int(hub_radius * 0.8)
    draw.ellipse(
        [center[0] - inner_hub, center[1] - inner_hub, center[0] + inner_hub, center[1] + inner_hub],
        fill=(255, 107, 53, 255), outline=(255, 235, 150, 200), width=4
    )

    # 7. Cloche / Fork & Spoon / Cloche silhouette in the center
    # Draw a stylized glowing golden cloche/platter
    cx, cy = center
    dish_w = int(size * 0.05)
    dish_h = int(size * 0.035)
    
    # Platter dome
    draw.pieslice([cx - dish_w, cy - dish_h - 6, cx + dish_w, cy + dish_h], start=180, end=360, fill=(255, 255, 255, 255))
    # Platter base plate
    draw.rounded_rectangle([cx - dish_w - 6, cy + 2, cx + dish_w + 6, cy + 8], radius=3, fill=(255, 215, 0, 255))
    # Handle on dome
    draw.ellipse([cx - 4, cy - dish_h - 12, cx + 4, cy - dish_h - 4], fill=(255, 215, 0, 255))

    # 8. Golden Pointer at Top (pointing down into the wheel)
    pointer_top = center[1] - wheel_radius - int(size * 0.04)
    pointer_bottom = center[1] - wheel_radius + int(size * 0.03)
    pointer_half_w = int(size * 0.035)
    
    pointer_pts = [
        (center[0] - pointer_half_w, pointer_top),
        (center[0] + pointer_half_w, pointer_top),
        (center[0], pointer_bottom)
    ]
    
    # Pointer Shadow
    p_shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ps_draw = ImageDraw.Draw(p_shadow)
    ps_draw.polygon([(p[0], p[1] + 6) for p in pointer_pts], fill=(0, 0, 0, 160))
    p_shadow = p_shadow.filter(ImageFilter.GaussianBlur(6))
    img = Image.alpha_composite(img, p_shadow)
    draw = ImageDraw.Draw(img)

    # Pointer Fill & Outline
    draw.polygon(pointer_pts, fill=(255, 215, 0, 255), outline=(255, 255, 255, 230))
    # Inner pointer accent
    inner_pointer = [
        (center[0] - int(pointer_half_w * 0.5), pointer_top + 4),
        (center[0] + int(pointer_half_w * 0.5), pointer_top + 4),
        (center[0], pointer_bottom - 8)
    ]
    draw.polygon(inner_pointer, fill=(255, 107, 53, 255))

    # 9. Sparkle Stars
    def draw_star(sx, sy, rad, color=(255, 255, 255, 230)):
        star_pts = []
        for a in range(8):
            r = rad if a % 2 == 0 else rad * 0.35
            ang = math.radians(a * 45)
            star_pts.append((sx + r * math.cos(ang), sy + r * math.sin(ang)))
        draw.polygon(star_pts, fill=color)

    draw_star(center[0] - int(size * 0.32), center[1] - int(size * 0.32), int(size * 0.024), (255, 230, 100, 240))
    draw_star(center[0] + int(size * 0.33), center[1] - int(size * 0.28), int(size * 0.03), (255, 255, 255, 255))
    draw_star(center[0] + int(size * 0.31), center[1] + int(size * 0.31), int(size * 0.02), (255, 180, 80, 220))
    draw_star(center[0] - int(size * 0.34), center[1] + int(size * 0.25), int(size * 0.026), (255, 255, 255, 230))

    img.save(output_path, "PNG")
    print(f"App icon created successfully at: {output_path}")

if __name__ == "__main__":
    create_app_icon()
