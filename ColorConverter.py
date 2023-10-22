fair = {
    "Baby Blue": (173, 216, 230),
    "Light Pink": (255, 182, 193),
    "Lavender": (230, 230, 250),
    "Mint Green": (152, 255, 152),
    "Ivory": (255, 255, 240),
    "Beige": (245, 245, 220),
    "Sky Blue": (135, 206, 235),
    "Pale Yellow": (255, 255, 153),
    "Dusty Rose": (209, 109, 123),
    "Buttercup": (252, 209, 22),
    "Lilac": (200, 162, 200),
    "Peach": (255, 229, 180),
    "Soft Coral": (255, 153, 153),
    "Periwinkle": (204, 204, 255),
    "Soft Brown": (188, 143, 143),
    "Light Gray": (211, 211, 211),
    "Pale Green": (152, 251, 152),
    "Powder Blue": (176, 224, 230),
    "Light Lavender": (230, 230, 250),
    "Soft Purple": (180, 131, 149)
}

medium = {
    "Pale Pink": (255, 228, 225),
    "Soft Blue": (173, 216, 230),
    "Light Lavender": (230, 230, 250),
    "Mint Green": (152, 255, 152),
    "Ivory": (255, 255, 240),
    "Beige": (245, 245, 220),
    "Lilac": (200, 162, 200),
    "Peach": (255, 229, 180),
    "Buttercream": (255, 253, 208),
    "Soft Coral": (255, 153, 153),
    "Powder Blue": (176, 224, 230),
    "Soft Gray": (211, 211, 211),
    "Pale Green": (152, 251, 152),
    "Pale Yellow": (255, 255, 153),
    "Cotton Candy": (255, 188, 217),
    "Lavender Gray": (196, 195, 208),
    "Seafoam Green": (120, 222, 130),
    "Champagne": (247, 231, 206),
    "Dusty Rose": (209, 109, 123),
    "Pearl White": (255, 239, 219)
}

tan = {
    "Terracotta": (204, 78, 92),
    "Deep Brown": (139, 69, 19),
    "Olive Green": (85, 107, 47),
    "Burnt Orange": (204, 85, 0),
    "Deep Red": (139, 0, 0),
    "Rich Purple": (102, 51, 153),
    "Rust": (183, 65, 14),
    "Bronze": (205, 127, 50),
    "Copper": (184, 115, 51),
    "Olive Drab": (107, 142, 35),
    "Sienna": (160, 82, 45),
    "Aubergine": (51, 0, 51),
    "Cinnamon": (210, 105, 30),
    "Terra Cotta": (204, 78, 92),
    "Amber": (255, 191, 0),
    "Burgundy": (128, 0, 32),
    "Sage Green": (134, 161, 125),
    "Marsala": (123, 63, 59),
    "Chocolate Brown": (139, 69, 19),
}

dark = {
    "Navy Blue": (0, 0, 128),
    "Emerald Green": (0, 128, 0),
    "Sapphire Blue": (0, 0, 255),
    "Royal Purple": (102, 51, 153),
    "Bright White": (255, 255, 255),
    "Pastel Pink": (255, 182, 193),
    "Light Lavender": (230, 230, 250),
    "Pale Yellow": (255, 255, 153),
    "Mint Green": (152, 255, 152),
    "Powder Blue": (176, 224, 230),
    "Cocoa Brown": (139, 69, 19),
    "Charcoal Gray": (54, 69, 79),
    "Jet Black": (0, 0, 0),
    "Crimson": (220, 20, 60),
    "Ivory": (255, 255, 240),
    "Silver Gray": (192, 192, 192),
    "Lilac": (200, 162, 200),
    "Cobalt Blue": (0, 71, 171),
    "Amethyst": (153, 102, 204),
    "Soft Pink": (255, 182, 193),
    "Turquoise": (64, 224, 208),
}

import numpy as np
import random


def euclidean_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))

def categorize_skin_color(rgb_value):
    # Define RGB values for the center of each skin color category
    fair_center = (255, 240, 210)
    medium_center = (215, 180, 130)
    tan_center = (165, 130, 80)
    dark_center = (115, 75, 30)

    # Calculate the Euclidean distance from the input color to each center
    distances = {
        "fair": euclidean_distance(rgb_value, fair_center),
        "medium": euclidean_distance(rgb_value, medium_center),
        "tan": euclidean_distance(rgb_value, tan_center),
        "dark": euclidean_distance(rgb_value, dark_center),
    }

    # Find the category with the smallest distance
    closest_category = min(distances, key=distances.get)
    return closest_category



def get_clothing_color(skin_color):
    category = globals()[categorize_skin_color(skin_color)]
    random_key = random.choice(list(category.keys()))
    random_value = category[random_key]
    return random_key, random_value

# Example usage:
# random_key, random_value = get_clothing_color((255,219,172))
# print(f"Random Color Name: {random_key}")
# print(f"Random Color RGB: {random_value}")