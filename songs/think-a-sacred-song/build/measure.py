from PIL import Image,ImageFont
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for f in sorted((root/'images').glob('*.png')):
    im=Image.open(f)
    print(f.name, im.size)
line='Think the melody, and in that very hour'
for size in range(30,41):
    font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',size*10)
    print(size,font.getlength(line)/10)
