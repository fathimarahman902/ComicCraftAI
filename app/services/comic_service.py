from .image_generator import generate_image

def generate_comic_panels():
    panels = [
        {
            "title": "Panel 1: The Forest's Edge",
            "desc": "A curious orange fox stands at the edge of a dark forest sunrise",
            "img": generate_image("curious orange fox at edge of dark forest sunrise fog", 11)
        },
        {
            "title": "Panel 2: Into the Woods",
            "desc": "The brave fox ventures into the misty woods",
            "img": generate_image("brave orange fox walking inside misty green forest tall trees", 22)
        },
        {
            "title": "Panel 3: The Glowing Stone",
            "desc": "Fox discovers a glowing magical stone",
            "img": generate_image("orange fox finding glowing blue crystal stone in forest", 33)
        },
        {
            "title": "Panel 4: Brave Faceoff",
            "desc": "Brave fox faces the guardian",
            "img": generate_image("brave orange fox facing big friendly bear in forest", 44)
        },
        {
            "title": "Panel 5: Treasure at Sunset",
            "desc": "Happy fox finds treasure at sunset",
            "img": generate_image("happy orange fox with treasure chest sunset golden light", 55)
        }
    ]
    return panels