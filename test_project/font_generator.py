from PIL import Image,ImageDraw,ImageFont

# sample text and font
font_size = 30
unicode_text = u"Hello World!"
font = ImageFont.truetype("/home/embian/Workspace2/test_project/font_dir/fontYouandiModernTR.ttf", font_size , encoding="unic")

# get the line size
#text_width, text_height = font.getsize(unicode_text)
text_width = 50
text_height = 50

label_low = []
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

for i in digits+ascii_lowercase:
    label_low.append(i)

for i in label_low:
        # create a blank canvas with extra space between lines
    canvas = Image.new('RGB', (text_width, text_height), "white")


    # draw the text onto the text canvas, and use black as the text color
    draw = ImageDraw.Draw(canvas)
    draw.text(((text_width-font_size)/2,(text_height-font_size)/2), i, 'black', font)

    # save the blank canvas to a file
    canvas.save('//home/embian/Workspace2/test_project/font_output/generate_font/'+i+".png", "PNG")
    #canvas.show()
    print(i)
    #input()