from PIL import ImageFont,Image,ImageDraw
font_size = 50
font = ImageFont.truetype("GenShinGothic-Bold.ttf",font_size)
save = input("請輸入儲存路徑")
n = int(input("你想生成幾張圖片?"))
count = int(int((800/font_size)*1.8))



for i in range(n):
    color = input("請輸入顏色")
    t = input("你要加在圖片上的文字")
    color = color.split(' ')
    image = Image.new('RGB',(800,800),(int(color[0]),(int(color[1])),(int(color[2]))))
    def line_break(line):
        ret = ''
        width = 0
        for c in line:
            if len(c.encode('utf8')) == 3:  # 中文
                if count == width + 1:  # 剩余位置不够一个汉字
                    width = 2
                    ret += '\n' + c
                else: 
                    width += 2
                    ret += c
            else:
                if c == '\n':
                    width = 0
                    ret += c
                else:
                    width += 1
                    ret += c
            if width >= count:
                ret += '\n'
                width = 0
        if ret.endswith('\n'):
            return ret
        return ret + '\n'
    t = line_break(t)
    draw = ImageDraw.Draw(image)
    w,h = draw.textsize(t,font = font)
    draw.text(((800-w)/2,(800-h)/2),t,font = font)
    image.save(save+"\image #{}.png".format(i))

