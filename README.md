# Matter Edit

edit Jekyll-style YAML front matter with values of passed parameters

## Install 

```shell
pip install matter-edit@git+https://github.com/yknz/matter-edit.git
```

## Usage

sample.txt
```text
---
author: hoge
thumbnail: thumbnail.png
---
Hello, world!
```

### Show front matter value

```shell
> python3 -m matteredit show sample.txt --param thumbnail
thumbnail.png
```

### Update front matter value(s)

```shell
> python3 -m matteredit update sample.txt --params author=fuga
```

sample.txt (value updated)
```text
---
author: fuga
thumbnail: thumbnail.png
---
Hello, world!
```

```shell
> python3 -m matteredit update sample.txt --params author=piyo thumbnail=thumbnail.jpg
```

sample.txt (value updated)
```text
---
author: piyo
thumbnail: thumbnail.jpg
---
Hello, world!
```
