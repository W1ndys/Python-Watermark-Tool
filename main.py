from PIL import Image, ImageDraw, ImageFont
import os
import math


# 将十六进制颜色代码转换为RGBA元组的函数
def hex_to_rgba(hex_color, alpha=255):
    hex_color = hex_color.strip("#")
    if len(hex_color) == 6:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    elif len(hex_color) == 3:
        r = int(hex_color[0] * 2, 16)
        g = int(hex_color[1] * 2, 16)
        b = int(hex_color[2] * 2, 16)
    else:
        raise ValueError("Invalid hex color code")
    return (r, g, b, alpha)


# 添加水印的函数
def add_watermark(
    input_image_path,
    output_image_path,
    watermark_text,
    font_size,
    angle,
    spacing,
    color,
):
    try:
        # 打开原始图片
        original = Image.open(input_image_path).convert("RGBA")
        txt_layer = Image.new("RGBA", original.size, (255, 255, 255, 0))

        # 设置字体及其大小
        font_path = "simkai.ttf"  # 替换为你系统中实际存在的字体路径
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(txt_layer)

        # 计算水印的尺寸
        text_bbox = draw.textbbox((0, 0), watermark_text, font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # 增加边界以避免文字被切割
        padding = 10
        padded_text_width = text_width + padding * 2
        padded_text_height = text_height + padding * 2

        # 计算旋转后图像的尺寸
        angle_rad = math.radians(angle)
        rotated_width = int(
            abs(padded_text_width * math.cos(angle_rad))
            + abs(padded_text_height * math.sin(angle_rad))
        )
        rotated_height = int(
            abs(padded_text_width * math.sin(angle_rad))
            + abs(padded_text_height * math.cos(angle_rad))
        )

        # 在图片上添加多个水印
        for x in range(0, original.width, rotated_width + spacing):
            for y in range(0, original.height, rotated_height + spacing):
                text_img = Image.new(
                    "RGBA", (padded_text_width, padded_text_height), (255, 255, 255, 0)
                )
                text_draw = ImageDraw.Draw(text_img)
                text_draw.text(
                    (padding, padding), watermark_text, fill=color, font=font
                )
                rotated_text_img = text_img.rotate(angle, expand=1)
                txt_layer.paste(rotated_text_img, (x, y), rotated_text_img)

        # 合并原始图片和水印图层
        watermarked = Image.alpha_composite(original, txt_layer)
        watermarked.save(output_image_path, "PNG")
    except Exception as e:
        print(f"Failed to process {input_image_path}: {e}")


# 批量处理图片的函数
def batch_add_watermark(
    input_dir, output_dir, watermark_text, font_size, angle, spacing, color_hex
):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    color_rgba = hex_to_rgba(color_hex)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            add_watermark(
                input_image_path,
                output_image_path,
                watermark_text,
                font_size,
                angle,
                spacing,
                color_rgba,
            )
            print(f"Processed: {filename}")

    # 打开输出目录
    if os.name == "nt":
        os.startfile(output_dir)
    elif os.name == "posix":
        os.system(f"xdg-open {output_dir}")


# 设置输入目录和输出目录
input_dir = "input"
output_dir = "output"
watermark_text = "https://github.com/W1ndys/Python-Watermark-Tool"

# 字体大小、角度、间隔和颜色（使用十六进制颜色代码）
font_size = 30
angle = 10
spacing = 5
color_hex = "#6e6e6e"

# 批量添加水印
batch_add_watermark(
    input_dir, output_dir, watermark_text, font_size, angle, spacing, color_hex
)
