import warnings

warnings.simplefilter('ignore')

import torch
from os.path import dirname
from utils import init_jit_model, read_batch, prepare_model_input


def run():
    device = torch.device('cpu')

    jit_model = dirname(__file__) + '/model/ua_v1_jit.model'
    model, decoder = init_jit_model(jit_model, device=device)

    test_files = [
        dirname(__file__) + '/recordings/my/1.wav',
        dirname(__file__) + '/recordings/my/2.wav',
        dirname(__file__) + '/recordings/my/3.wav',
    ]

    model_input = prepare_model_input(read_batch(test_files), device=device)
    output = model(model_input)
    for example in output:
        print(decoder(example.cpu()))


if __name__ == '__main__':
    run()
