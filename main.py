import argparse, random
from PIL import Image
from get_image import get_image
from creat_photomosaic import creat_photomosaic

def main():
    parser = argparse.ArgumentParser(description='Creates a photomosaic from input image')

    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)

    args = parser.parse_args()

    ##### INPUT #####

    target_image = Image.open(args.target_image)

    # input image
    print('reading input folder...')
    input_images = get_image(args.input_folder)

    # 检查文件
    if input_images == []:
        print(f"No input image found in{args.input_folder}.Exiting")
        exit()

    random.shuffle(input_images)

    # 获取尺寸
    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))

    output_filename = 'mosaic.png'

    if args.outfile:
        output_filename = args.outfile

    reuse_images = True

    resize_intput = True

    ##### END INPUT ######

    print('starting photomoasic creation...')

    mosaic_image = creat_photomosaic(target_image, input_images, grid_size, reuse_images)

    # write out mosaic
    mosaic_image.save(output_filename, 'PNG')

    print(f"saved output to {output_filename}")

if __name__ == '__main__':
    main()