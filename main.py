from PIL import Image

def convert_pic(filename):
    # filename = r'logo.png'
    img = Image.open(filename)
    # img.save('output/hoge.ico')
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    img.save('output/hoge.ico', sizes=icon_sizes)

if __name__ == '__main__':
    convert_pic('input/hoge.png')