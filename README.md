# MosaicImage 照片马赛克

> [!NOTE]
> 本项目为学习项目，参考了《Python极客项目编程》（Python Playground），仅供交流学习参考，请勿用于商业用途。

使用 Python 将一张目标图片拆分成网格，用图片库中最相近颜色的小图逐块替换，最终拼成一张"由无数小图组成"的马赛克照片（Photomosaic）。

## 效果原理

1. **切分**：把目标图片按 `m × n` 网格切成小方块
2. **取色**：计算每一块的 RGB 平均颜色
3. **匹配**：在图片库中找到平均颜色欧氏距离最小的小图
4. **拼接**：把匹配到的小图按原网格位置拼回一张完整大图

## 项目结构

```
MosaicImage/
├── main.py                 # 命令行入口，解析参数并生成马赛克
├── creat_photomosaic.py    # 核心流程：切分 → 匹配 → 拼接
├── split_image.py          # 把目标图片切分为 m×n 小块
├── average_RGB.py          # 用 numpy 计算图片平均 RGB 颜色
├── best_match_index.py     # 遍历图片库，找颜色距离最小的匹配图
├── create_image_grid.py    # 把匹配结果拼接回完整大图
├── get_image.py            # 读取文件夹内的图片（自动跳过损坏文件）
├── img_lib_noise/          # 示例图片库（200 张 jpg）
└── test_1.png              # 示例目标图片
```

## 环境要求

- Python ≥ 3.12
- 依赖：`pillow`、`numpy`

项目使用 [uv](https://docs.astral.sh/uv/) 管理依赖，安装方式：

```bash
uv sync
```

或手动安装依赖：

```bash
pip install pillow numpy
```

## 使用方法

```bash
uv run python main.py \
    --target-image test_1.png \
    --input-folder img_lib_noise \
    --grid-size 64 64 \
    --output-file mosaic.png
```

### 参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| `--target-image` | ✅ | 目标图片路径（将被马赛克化的图） |
| `--input-folder` | ✅ | 小图素材库所在文件夹 |
| `--grid-size` | ✅ | 网格尺寸，格式为 `行数 列数`，如 `64 64` |
| `--output-file` | ❌ | 输出文件名，默认 `mosaic.png` |

### 使用建议

- **`grid-size` 越大，马赛克越细腻**，但耗时和内存开销也随之增加
- 素材库越丰富（颜色覆盖越广），匹配效果越好
- 默认开启小图复用（`reuse_images = True`），素材较少时也能填满全图

## 示例

以仓库自带的 `test_1.png` 和 `img_lib_noise/`（200 张噪声图）为例：

```bash
uv run python main.py --target-image test_1.png --input-folder img_lib_noise --grid-size 32 32
```

运行结束后当前目录会生成 `mosaic.png`。

## 核心算法说明

- **颜色匹配**：对每块目标区域与素材图分别计算平均 RGB，以 RGB 三维空间中的平方欧氏距离为相似度，取距离最小者
- **素材预处理**：图片库的平均颜色只计算一次并缓存（`avgs` 列表），避免重复运算
- **进度反馈**：匹配过程按批次打印进度

## 已知限制 / TODO

- [ ] 匹配仅基于平均颜色，不感知纹理与结构，效果依赖素材库质量
- [ ] `main.py` 中 `reuse_images` / `resize_intput` 为硬编码，尚未暴露为命令行参数
- [ ] `main.py` 未开启 `reuse_images=False` 分支的测试路径
- [ ] `pyproject.toml` 中 `[project.scripts]` 入口指向尚未实现的 `mosaicimage:main`

## 声明

本项目为个人学习项目，实现思路参考了《Python极客项目编程》（*Python Playground*，Python Projects for the Curious Engineer），代码为学习过程中的实践与改写，仅供交流学习参考，请勿用于商业用途。

## License

MIT
