以Undercover Hero为例，分享一种Twine类HTML游戏汉化的思路。
# 简述
HTML游戏直接用浏览器就能翻译，所以很少有人专门做汉化。  
这类游戏基本都是文字内容，文本量超大，翻译起来确实挺费劲的。  
不过如果你想自己动手汉化，这份教程可能是目前最详细的指导了！  
希望能帮到你顺利搞定汉化~
# 了解Twine
## 什么是Twine
### 官方简介
Twine 是一个开源工具，用于讲述互动的非线性故事。
您不需要编写任何代码来使用 Twine 创建一个简单的故事，但是当您准备好时，您可以使用变量，条件逻辑，图像，CSS 和 JavaScript 扩展您的故事。
Twine 直接发布到 HTML，所以你可以在几乎任何地方发布你的作品。你用它创建的任何东西都可以完全自由地以任何你喜欢的方式使用，包括用于商业目的。
### 图例
在Twine里，你可以创建数个故事片段，由链接将各个片段联系起来构成完整的故事。
小方格代表故事片段，黑色连线代表链接，绿色圆点表示故事起点。
![](https://pic1.imgdb.cn/item/67ef77650ba3d5a1d7ecc273.png)
### 链接
Twine有桌面版和网页版。
[官网链接](https://twinery.org/)
[Github项目twine-resources](https://github.com/ChapelR/twine-resources)
## 如何判断是否属于Twine类
### 使用Twine工具
直接使用Twine导入功能，识别成功就是Twine类。无法识别会提示网页中没有Twine类故事。
### Twine类HTML游戏网页特点
左边有游戏状态栏，游戏标题，保存按钮。右面显示游戏文本和图片。以文字链接推进游戏。
![](https://pic1.imgdb.cn/item/67ef7b5d0ba3d5a1d7ecc47a.png)
### Twine类HTML游戏文件特点
这类游戏文件夹非常简单，通常由html文件和images文件夹组成。
html为游戏的主体部分。游戏文本，游戏代码都包含在里面。必定存在。
images文件夹存放游戏的图片，视频资源。文件夹名称无固定写法，由作者确定。不一定存在。
以下这两种情况就可能没有images文件夹。
1、纯文本游戏，没有用到图片资源。
2、图片资源储存于网上，游戏中以图片链接形式给出。
![](https://pic1.imgdb.cn/item/67ef77640ba3d5a1d7ecc272.png)

![](https://pic1.imgdb.cn/item/67ef77640ba3d5a1d7ecc271.png)
下面这些游戏就属于这类HTML游戏
- The Family's Curse
- Prison
- Dawn Of Corruption
- Undercover Hero
- ### 其他类型的HTML游戏
以The Cabin为例
![](https://pic1.imgdb.cn/item/67ef85980ba3d5a1d7ecea2e.png)
这里面存在其他.js和.css文件。这属于其他游戏引擎。
虽然汉化方法类似，但不在本文的讨论范围之内，故不做深入展开。
## Twine语法
Twine中有不同的故事格式，但以SugarCube居多。
SugarCube基础语法，具体可参考[SugarCube官方文档](https://www.motoslave.net/sugarcube/2/docs/)
例：链接语法
```
Link
[[Link]]
[[Text|Link]]
[[Link][Setter]]
[[Text|Link][Setter]]
```
# Twine游戏汉化
## 基本游戏汉化流程
- ​获取游戏文件​​
- ​​解包游戏资源​​
- ​​提取待译文本​​
- 机翻+手动润色​​
- 替换翻译文本​​
- ​​重新打包游戏​​
- ​​测试分享成果​​
## 获取游戏文件
HTML游戏有时在网页直接游玩，不提供下载链接。
需要想办法获取到游戏原文件。
itch版的话，使用itch客户端可以下载到html文件。
## 解包游戏资源​​
虽然html文件已经明文存储了游戏文本，但是其可读性很差。
可以通过Twine工具，将html导出为twee格式，方便后续操作。
.twee文件是文本文件，可以直接用文本编辑器打开。(推荐VS Code)
### Twee文件
Twine会按照故事片段标题的名称顺序排列所有故事片段。
以下为一段.twee文本片段
```
:: StoryTitle
Undercover Hero
:: StoryData
{
  "ifid": "4a270d74-48bb-4d1f-8786-ab1f9b91f659",
  "format": "SugarCube",
  "format-version": "2.37.3",
  "start": "タイトル",
  "zoom": 0.6
}
:: 102号トレーニング {"position":"2675,5925","size":"100,100"}
<<if $feel lte 34>>/% 感度低%/<<if $brain lte  69>> /% 洗脳度中以下 %/
正直、彼にこういう頼みをするのはできれば避けたい。
だが、今の私はあまりにも無知だ....助けを求めやすい相手を考えた時、やはりそれは彼しかいない。
```
StoryTitle为游戏标题
StoryData为游戏基础信息
均为Twine添加。真正的故事片段从下面开始。
102号トレーニング为第一个故事片段，position记录位置，size记录大小。
(...后续格式相同)
## 提取待译文本​​
这一步我们需要从.twee文件中提取需要翻译的游戏文本。
我们使用Translator++中custom parser来完成这一步。
### ==重要说明==
Twine类游戏文本写作，非常自由，不同作者之间的写作方式存在一定的差异。
也就是说照搬，在其他游戏上不一定行的通。
但是理解思路后，就能很快的针对游戏进行修改。（毕竟最难的部分我已经写了）
Undercover Hero中使用的custom parser我会在后面贴出来。
### Translator++
Translator++是一款游戏计算机辅助翻译（CAT）或计算机辅助人工翻译（CAHT）软件。它帮助翻译人员高效快速地为各种类型的游戏引擎（如 RPG Makers、Wolf RPG Editor、RenPy、KiriKiri 等）制作高质量的翻译。
[官网链接](https://dreamsavior.net/)
Translator++有赞助版和大众版。免费的大众版已经足够使用。
[下载链接](https://dreamsavior.net/download/)
### Parse any script with custom parser
Translator++除了可以处理以上的游戏引擎，还可以根据自定规则处理其他文本内容。（估计没什么人会用这个功能。）
新建工程中——Parse any script with custom parser
使用自制的文本解析模型 Use existing Parser Model
![](https://pic1.imgdb.cn/item/67ef844b0ba3d5a1d7ece560.png)
![](https://pic1.imgdb.cn/item/67ef84ab0ba3d5a1d7ece6af.png)
### Parser Model Creator
Parser Model Creator 是一个帮助我们创建一组规则来解析文本文件的工具。这个工具的目标是将代码修改的需要减少到最低限度或根本不需要。
1、进入Parser Model Creator工具
右上角图标——工具——Create Custom Parser Model
![](https://pic1.imgdb.cn/item/67ef866c0ba3d5a1d7ececc3.png)
Parser Model Creator工具界面
![](https://pic1.imgdb.cn/item/67ef8bde0ba3d5a1d7ecf82b.png)
2、新建file group
让工具知道要处理那些文件
Add a new file group
![](https://pic1.imgdb.cn/item/67ef8c310ba3d5a1d7ecf970.png)
3、新建文本解析规则
使用正则表达式，JavaScript函数解析文本。
![](https://pic1.imgdb.cn/item/67ef8c330ba3d5a1d7ecf97a.png)
4、保存
写好规则后就可以保存下来。.tpm文件就是写好的Parser Model。就可以在新建工程中使用了。
5、更多
请参考Translator++官方文档[parser model creator部分](https://dreamsavior.net/docs/translator/parser-model-creator/)
### 怎么写基础规则
以下为Undercover Hero开始故事片段中部分文本。
```
<div class = "title">''Undercover Hero''</div>

[img[images/title.png]]	

<div class = "text">※警告！！</div>
このゲームブックは18歳未満の方の閲覧を禁じます。
同性愛表現が含まれるため苦手な方はご注意ください。

[[ゲームを始める|オープニング1]]
<<set $name1 = "ガーディアン">>
<<set $test1 = 0>><<set $test2 = 0>><<set $phase1 = 0>><<set $phase2 = 10>><<set $phase3 = 0>><<set $phase4 = 0>><<set $hugoBad = 0>>
<<set $brain = 0>><<set $mental = 100>><<set $feel = 0>><<set $day = 1>>
<<set $mentalLose1 = 10>><<set $mentalLose2 = 20>><<set $mentalLose3 = 30>>
<<set $brainGain1 = 5>><<set $brainGain2 = 10>><<set $brainGain3 = 15>>
<<set $feelGain1 = 4>><<set $feelGain2 = 7>><<set $feelGain3 = 9>>
<<set $giwaku1 = 0>><<set $giwaku2 = 0>><<set $giwaku3 = 0>><<set $giwaku4 = 0>>
<<set $houshi1 = 2>><<set $houshi2 = 1>><<set $houshi3 = 1>><<set $houshi4 = 2>><<set $houshiCount1 = 0>>
<<set $houshiComp1 = false>><<set $houshiComp2 = false>><<set $houshiComp3 = false>><<set $houshiComp4 = false>><<set $hugoSafty = false>>
<<set $ninmuCount = 0>><<set $phaseCount = 1>><<set $brainLimit = 150>><<set $hiddenStatus = false>><<set $cheat = false>><<set $hint = false>><<set $data17flg = false>><<set $hugoBad = 0>>

<<set $data1 = false>>
```
![](https://pic1.imgdb.cn/item/67ef7b5d0ba3d5a1d7ecc47a.png)
通过与游戏界面对比发现。需要翻译的游戏文本如下。
```
Undercover Hero
※警告！！
このゲームブックは18歳未満の方の閲覧を禁じます。
同性愛表現が含まれるため苦手な方はご注意ください。
ゲームを始める // 链接
```
观察到，几乎所有的<<>><>[[]]中文本都不需要翻译。
那么第一个规则要帮助我们，提取所有不在括号中的内容，排除所有在括号中的内容。
这项规则能为我们提取到绝大多数的所需文本。
Parser Model支持多种规则，其他文本在后续规则中处理。
#### 规则1
普通的正则表达式不能处理这么复杂的规则，所以要用JavaScript函数来解决。
测试用例：
```javascript
// 用例1：基础单标签
const case1 = "<tag>content</tag>";
// 排除：0-4(<tag>), 10-14(</tag>)
// 有效：5-9(content) ✔️

// 用例2：双标签嵌套
const case2 = "<<tag>>text<<tag>>";
// 排除：0-6(<<tag>>), 10-16(<<tag>>)
// 有效：7-9(text) ✔️

// 用例3：带数字标签
const case3 = "<123>value<456></123>";
// 排除：0-4(<123>), 9-13(<456>), 14-19(</123>)
// 有效：5-8(value) ✔️

// 用例4：未闭合标签
const case4 = "<<unclosed>text";
// 排除：0-11(<<unclosed>)
// 有效：12-15(text) ✔️

// 用例5：混合内容
const case5 = "pre<<tag>><inner>mid</inner>post";
// 排除：3-8(<<tag>>), 9-14(<inner>), 19-24(</inner>)
// 有效：0-2(pre), 15-18(mid), 25-28(post) ✔️
```
与deepseek反复掰扯，deepseek给出的解决方案。
```javascript
const result = [];
const lineSplitter = /(\r?\n)/g;
let lineStart = 0;

// 按行分割文本并保留换行符位置
const lines = text.split(lineSplitter);

for (let i = 0; i < lines.length; i += 2) {
    const lineContent = lines[i];
    const lineEnd = lineStart + lineContent.length;
    
    // 当前行的标签匹配
    // const tagRegex = /<<[^>]+>>|<[^>]+?>/g;
    const tagRegex = /<<.+?>>|<[^>]+?>|\[\[.+?\]\]/g;
    let match;
    const excludeInLine = [];
    
    // 逐行匹配标签
    while ((match = tagRegex.exec(lineContent)) !== null) {
        const globalStart = lineStart + match.index;
        const globalEnd = globalStart + match[0].length - 1;
        excludeInLine.push({ start: globalStart, end: globalEnd });
    }
    
    // 计算本行有效区间
    let cursor = lineStart;
    for (const range of excludeInLine) {
        if (range.start > cursor) {
            result.push({
                start: cursor,
                end: range.start
            });
        }
        cursor = Math.max(cursor, range.end + 1);
    }
    
    // 处理行尾内容
    if (cursor <= lineEnd - 1) {
        result.push({
            start: cursor,
            end: lineEnd
        });
    }
    
    // 更新下一行起始位置（包含换行符）
    if (lines[i+1]) {
        lineStart = lineEnd + lines[i+1].length;
    } else {
        lineStart = lineEnd;
    }
}

return result.length ? (result.length > 1 ? result : result[0]) : undefined;
```
步骤：Rules-->JavaScript Function-->贴入代码-->Testing
结果：Original text列确实提取到了需要翻译的文本。
问题：
1、提取到了一些不需要翻译的文本，如:: 102号トレーニング。
2、有些括号中的文本可能需要翻译，如链接。
![](https://pic1.imgdb.cn/item/67ef9a960ba3d5a1d7ed28f4.png)
解决1：提取到不需要的文本
通过改变Action选项（最下面一行）
Action-->Mask vaule
Mask vaule选项，使匹配到的文本不进行提取，而是隐藏起来。后续规则中将无法匹配这些文本。
#### 规则2
排除所有以::开头的行，正则表达式为：
```
/::[^\n]+/gm
```
#### 规则3
排除所有{}，即其中的文本，忽略换行，正则表达式为：
```
/\{[^\}]+?\}/g
```
![](https://pic1.imgdb.cn/item/67ef9cb70ba3d5a1d7ed30e1.png)
解决2：括号中的文本可能需要翻译
#### 规则4
提取所有链接部分文本，正则表达式为：
```
/\[\[(.+?)\|.+\]\]/g
```
Capture Groups中可以选择分组，这里为1。
![](https://pic1.imgdb.cn/item/67ef9f700ba3d5a1d7ed360a.png)
Parser Model会按照Rule的顺序依次执行。所以我们需要重新调整规则的顺序，让其正确发挥作用。
#### 调整后规则
Rule 0 隐藏所有::开头的行
Rule 1 隐藏所有{}包含的内容
Rule 2 提取所有不在括号中的内容
Rule 3 提取链接中的内容
### 特殊情况处理
#### 翻译前处理
例1
链接有可能写成\[\[Link\]\]，这种情况下不能随意更改Link，不然链接就会失效。
这种情况下，我们需要对原文件，即.twee文件进行特殊处理。
\[\[Link\]\]-->\[\[Link\|Link\]\]
手动替换.twee文件中第一种链接形式，至第二种链接形式。
这样我们就能翻译前一个Link文本，并保证链接的正确。
### 扩展规则
如果出现漏翻，说明<<>>中有需要翻译的文本。
这是因为SugarCube中存在[Macros用法](https://www.motoslave.net/sugarcube/2/docs/#macros)
```
/<<di (\S*) "([^"]*)"/g
/<<dio "([^"]*)" "([^"]*)"/g
/<<link "([^"]*)"/g
```
## 机翻+手动润色​​
在上述步骤中我们应该成功使用Translator++提取到了游戏文本。
翻译方式跟其他游戏一致，这里不再赘述。
![](https://pic1.imgdb.cn/item/67efca430ba3d5a1d7ed4791.png)
翻译软件我推荐[LinguaGacha](https://github.com/neavo/LinguaGacha)
![](https://pic1.imgdb.cn/item/67efcb030ba3d5a1d7ed481f.png)

## 替换翻译文本​​
翻译完成后，使用Translator++导出到文件夹，即可得到翻译后的.twee文件。
### BUG
本因如此，但是我处理的时候遇到了一个BUG。
Rule 0 隐藏所有::开头的行
Rule 1 隐藏所有{}包含的内容
Rule 0，Rule 1中被隐藏的文本应该在导出时还原。但实际上，并没有。
### 临时解决方案
新建一个parser model，删除原Rule 0，Rule 1。
Rule 0 提取所有不在括号中的内容
Rule 1 提取链接中的内容
使用新规则创建翻译工程，导入第一版翻译文本。
导出到文件夹，即可得到翻译后的.twee文件。
## 重新打包游戏​​
使用Twine读取.twee，选择发布到文件，得到.html文件。
## 测试分享成果​​
恭喜你得到了翻译后的html文件。
现在你可以分享它了。
# 主要使用工具
## Twine
[官网链接](https://twinery.org/)
[Github项目twine-resources](https://github.com/ChapelR/twine-resources)
## Translator++
[官网链接](https://dreamsavior.net/)
[下载链接](https://dreamsavior.net/download/)
## LinguaGacha
[LinguaGacha](https://github.com/neavo/LinguaGacha)
