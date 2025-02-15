from PIL import Image

# Takes in two rolls, creates an image
def get_image(roll1, roll2):
    if roll1['name'] == "Oinker" or roll2['name'] == "Oinker":
        roll_image = Image.open('images/Oinker.png')
    else:
        first_roll_image = Image.open('images/' + roll1['name'] + '.png')
        second_roll_image = Image.open('images/' + roll2['name'] + '.png')
        roll_image = Image.new('RGBA', (first_roll_image.width + second_roll_image.width, first_roll_image.height))
        roll_image.paste(first_roll_image, (0, 0), first_roll_image)
        roll_image.paste(second_roll_image, (first_roll_image.width, 0), second_roll_image)
    roll_image.save('images/rollimage.png')
