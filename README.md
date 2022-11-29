<p align="center"><img src = "https://vaul.xyz/vissarion_logo.png" height = "150" width = "150"/>  </p>
<h2 align="center">Vissarion</h2>
<p align="center">the least handicapped open-source discord selfbot</p>
<p align="center">Join us on <a href="https://discord.gg/696CMDNHM2">discord!</a></p>

<p align="center">
  <a href="https://github.com/VissarionSB/Vissarion/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/VissarionSB/Vissarion?color=0088ff" />
  </a>
  <a href="https://github.com/VissarionSB/Vissarion/pulls">
    <img alt="Pull requests" src="https://img.shields.io/github/issues-pr/VissarionSB/Vissarion" />
  </a>
</p>

<br/>

### Features  
* Integrated [embed api](https://embeds.vaul.xyz/api?author=hi&title=so%20thats&description=entirely%20it&image_url=https://media.discordapp.net/attachments/856999073781121044/925056870887084082/fizu.gif&color=ffc219)
* Custom [ANSI syntax](https://www.youtube.com/watch?v=njGefT86RWQ&) that helps you build some awesome codeblocks.
* A fully customizable [session manager](https://www.youtube.com/watch?v=VmW6AnJXXMQ)
* [Spotify spoof](https://www.youtube.com/watch?v=hPe9VMa1R74)
* Customizable gradient ui
* Basic selfbot utility

<br/>

### Compatibility
Should run on Windows as well as on Linux.  
If something doesn't work for you, please [open an issue](https://github.com/VissarionSB/Vissarion/issues/new).

<br/>

### Installation
* `git clone https://github.com/VissarionSB/Vissarion`
* `cd Vissarion`
* `pip install -r requirements.txt`
* `python main.py`

<br/>

### Configuration
#### Default config paths:

Windows:
* `C:/Users/<user>/Documents/Vissarion`

Linux:
* `~/.config/Vissarion`

<br/>

### Preview

<img src = "https://cdn.discordapp.com/attachments/875052335951384627/1047051315961942066/image.png"/>

<h2 align="center">ANSI Parser syntax cheatsheet</h2>

### Components
* `field` <~ consists of `content`  
```
<field>
  title
  <content>
    content
  </content>
</field>
```
<img src = "https://cdn.discordapp.com/attachments/875052335951384627/1047057604590977084/image.png"/>

</br>

* `text` <~ basic component that should be used everytime you need just sum text in your codeblock
```
<text>
  text
</text>
```
<img src = "https://cdn.discordapp.com/attachments/875052335951384627/1047057975774285894/image.png"/>

<br/>

### Syntax
* `col_{color}` <~ Available colors: `gray, red, green, yellow, blue, purple, cyan, white`
```
<text>
  <col_red>
    text
  <reset>
</text>
```
<img src = "https://cdn.discordapp.com/attachments/875052335951384627/1047058877113446420/image.png"/>

<br/>

* `bold`
```
<text>
  <bold>
    text
  <reset>
</text>
```
<img src = "https://cdn.discordapp.com/attachments/875052335951384627/1047059467407200287/image.png"/>

<br/>

* `nl` <~ Places a new line
* `tl` <~ Places a tab
* `quote` <~ Places a quote

<!-- signed -->