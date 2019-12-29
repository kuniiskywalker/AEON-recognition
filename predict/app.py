import numpy as np
from tensorflow.keras.models import Sequential, Model, load_model
from PIL import Image
import sys
import argparse

def main(args):
    parser = argparse.ArgumentParser(description='Options for predict image')
    parser.add_argument('-m', '--model_path', default='<DEFAULT_SAVE_DIRECTORY>', type=str, help='model save path')
    parser.add_argument('-s', '--size', default='<DEFAULT_SAVE_DIRECTORY>', type=int, help='input image size')
    parser.add_argument('-i', '--input_file', type=str, help='input image')
    args = parser.parse_args()

    classes = ["toda", "ushiku"]
    num_classes = len(classes)
    image_size = args.size

    image = Image.open(args.input_file)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image) * 255.0

    X = []
    X.append(data)
    X = np.array(X)

    model = load_model(args.model_path)

    result = model.predict([X])[0]
    predicted = result.argmax()

    percentage = int(result[predicted] * 100)

    print(result)
    print(classes[predicted], percentage)

if __name__ == '__main__':
    from sys import argv
    try:

        main(argv)

    except KeyboardInterrupt:
        pass
    sys.exit()
