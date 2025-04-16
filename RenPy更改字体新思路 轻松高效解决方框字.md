# RenPy汉化更改字体新思路
以Tri City Monsters为例，分享一种RenPy汉化更改字体新思路，解决中文翻译无法显示，出现方框的问题。
后文内容按照——所遇问题-->原有方案-->新方案——展开讲解。
## 所遇问题

RenPy汉化完文本后，是不是会遇到中文字体不显示，出现方框的情况。
虽然下面这种全部都是方框的极端情况很少见，但是偶尔出现的方框字还是很影响游戏体验。
严重情况下，方框都不会显示，留下玩家不知所措。

![](https://pic1.imgdb.cn/item/67ffae0688c538a9b5d45d74.jpg)

游戏Tri City Monsters中，UI的设计就非常出色。游戏中使用了多达41种不同的字体，完成了效果的显示。
这个时候，难题就来到我这里了。我该怎样才能保证中文字体的正确显示。我上哪去查这40多种字体用在哪了？

![](https://pic1.imgdb.cn/item/67ffae0c88c538a9b5d45d76.png)
  
# 原有方案
RenPy原生教程中关于[样式的多语言支持](https://doc.renpy.cn/zh-CN/translation.html#style-translations)的内容。

![](https://pic1.imgdb.cn/item/67ffae0688c538a9b5d45d75.png)

原有方案中，需要从以下四处位置，更改游戏中字体。
## 系统配置

```
translate schinese python:
    gui.system_font = "stonecutter.ttf"
    gui.main_font = "stonecutter.ttf"
    gui.text_font = "stonecutter.ttf"
    gui.text_font_bold = "stonecutter.ttf"
    gui.interface_text_font = "stonecutter.ttf"
    gui.name_text_font = "stonecutter.ttf"
    gui.glyph_font = "stonecutter.ttf"
    gui.button_text_font = "stonecutter.ttf"
    gui.choice_button_text_font = "stonecutter.ttf"
    gui.label_text_font = "stonecutter.ttf"  

    style.default.font = "stonecutter.ttf"
```


二、样式
```
translate schinese style default:
    font "stonecutter.ttf"
```


三、通用文本标签

```
"尝试使用字体 {font=mikachan.ttf}mikachan font{/font}。"
```

四、文本样式特性

存在文本样式特性的用户接口语句——input，label，text，textbutton。
```
text "文本样式" font "stonecutter.ttf"
```

修改以上四处位置，以完成全部字体替换。

# 新方案

上面方法太麻烦了，还可能出现遗漏。那有没有轻松高效，一劳永逸的解决方案呢？
有的，兄弟有的。

在游戏Tri City Monsters中，使用了config.font_replacement_map函数来替换字体，提高文字的感官效果。

![](https://pic1.imgdb.cn/item/67ffae0588c538a9b5d45d73.png)

这个函数的本来的作用是将使用A字体斜体的地方，替换成B字体粗体。（例）

换个思路想一想，如果我们将A字体的全部类型组合，都替换成B字体相应的类型组合。是不是就相当于完成了A字体到B字体的替换。那么将游戏文件中所用的全部字体都替换成支持中文的字体，是不是就不会出现方框字了。

现在我们写一个函数，来帮助我们完成字体替换的全部工作。

```
# 需要被替换的字体路径列表  
define game_fonts = [  
# RenPy自带字体  
"DejaVuSans.ttf",  
"DejaVuSans-Bold.ttf",  
"TwemojiCOLRv0.ttf",  
"_OpenDyslexic3-Regular.ttf",  
# 游戏字体  
"fonts/Roboto-Medium.ttf",  
"fonts/Roboto-Regular.ttf"  
]  
  
# 替换后的目标字体路径  
define font_cn = [  
"tl/schinese/font/SourceHanSansCN-Bold.ttf"  
]  
  
  
# 执行替换函数  
translate schinese python:  
# 默认对应替换  
font_replacement(game_fonts,font_cn[0])  
# 指定样式替换  
# font_replacement(game_fonts,font_cn[0],[[False,False],[False,True]],[[False,False],[False,True]])  
  
  
## 批量设置字体替换映射 ##########################################################  
#  
# 参数:  
# source_font: 需要被替换的字体路径列表  
# target_font: 替换后的目标字体路径  
# source_styles: 原字体的样式组合列表 [bold, italic] (可选)  
# target_styles: 目标字体的样式组合列表 [bold, italic] (可选)  
init python:  
def font_replacement(source_font, target_font, source_styles=None, target_styles=None):  
  
# 设置默认样式组合  
if source_styles is None:  
source_styles = [[False, False], [True, False], [False, True], [True, True]]  
if target_styles is None:  
target_styles = [[False, False], [True, False], [False, True], [True, True]]  
  
# 为每种字体和每组对应的样式组合创建替换规则  
for font in source_font:  
for i in range(len(source_styles)):  
src_style = source_styles[i]  
tgt_style = target_styles[i]  
  
# 确保样式组合是 [bold, italic] 格式  
src_bold, src_italic = src_style if len(src_style) == 2 else (False, False)  
tgt_bold, tgt_italic = tgt_style if len(tgt_style) == 2 else (False, False)  
  
# 创建替换映射  
config.font_replacement_map[(font, src_bold, src_italic)] = (target_font, tgt_bold, tgt_italic)
```

font_replacement(source_font, target_font, source_styles=None, target_styles=None)
完成多对一的转换，source_font: 需要被替换的字体路径列表，target_font: 替换后的目标字体路径。
默认情况下，完成粗体，斜体对应的转换，也可以进行设置。

rpy文件使用最简操作：替换game_fonts游戏字体后路径，替换font_cn中路径。