init offset = 1

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
#     source_font: 需要被替换的字体路径列表
#     target_font: 替换后的目标字体路径
#     source_styles: 原字体的样式组合列表 [bold, italic] (可选)
#     target_styles: 目标字体的样式组合列表 [bold, italic] (可选)
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