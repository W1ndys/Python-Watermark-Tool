# Python-Watermark-Tool

这是一个用于为图片批量添加水印的 Python 脚本。你可以自定义水印的文本、字体大小、旋转角度、间隔和颜色。

## 功能

- 支持批量处理图片
- 自定义水印文本、字体大小、旋转角度、间隔和颜色
- 支持 PNG、JPG 和 JPEG 格式的图片

## 依赖

在运行此脚本之前，请确保你已经安装了以下 Python 库：

- Pillow

你可以通过以下命令安装这些库：

```bash
pip install pillow
```

## 使用方法

### 1. 准备工作

- 下载或克隆此项目到你的本地机器。
- 在项目根目录中创建两个文件夹：`input` 和 `output`。
  - `input` 文件夹用于存放你要添加水印的图片。
  - `output` 文件夹用于存放添加了水印后的图片。

### 2. 配置参数

在脚本中，你可以根据需要调整以下参数：

- `input_dir`：输入图片的文件夹路径（默认为 `input`）。
- `output_dir`：输出图片的文件夹路径（默认为 `output`）。
- `watermark_text`：水印文本内容。
- `font_size`：水印文本的字体大小。
- `angle`：水印文本的旋转角度。
- `spacing`：水印文本之间的间隔。
- `color_hex`：水印文本的颜色（十六进制颜色代码）。

### 3. 运行脚本

在终端中导航到项目根目录，并运行以下命令：

```bash
python main.py
```

脚本将会处理 `input` 文件夹中的所有图片，并将处理后的图片保存到 `output` 文件夹中。处理完成后，输出文件夹将自动打开。

### 示例

假设你有如下文件结构：

```
Python-Watermark-Tool/
├── main.py
├── input/
│   ├── image1.jpg
│   ├── image2.png
│   └── image3.jpeg
└── output/
```

你可以在 `main.py` 中设置参数，例如：

```python
input_dir = "input"
output_dir = "output"
watermark_text = "https://github.com/W1ndys/Python-Watermark-Tool"
font_size = 40
angle = 30
spacing = 50
color_hex = "#6e6e6e "
```

运行脚本后，`output` 文件夹中将包含添加了水印的图片。

## 注意事项

- 请确保你指定的字体文件路径（如 `simkai.ttf`）是正确的。Windows 下可以在目录`C:\Windows\Fonts`中找到系统自带的字体。
- 支持的图片格式包括 PNG、JPG 和 JPEG。

## TODO

- [x] 隐私水印全覆盖
- [x] 可调节倾斜角
- [x] 自定义水印文字
- [x] 可调节水印大小
- [x] 可调节水印间隔
- [x] 可调节水印颜色
- [x] 可调节水印透明度
- [x] 可调节水印字体
- [ ] 可添加图片水印

## 许可

该项目采用 MIT 许可证，详情请参阅 LICENSE 文件。
