import warnings

warnings.simplefilter('ignore')

import torch
from utils import init_jit_model, read_batch, prepare_model_input


def run():
    device = torch.device('cpu')

    jit_model = './model/ua_v3_jit.model'
    model, decoder = init_jit_model(jit_model, device=device)

    test_files = [
        './recordings/ua_sample.wav',
        './recordings/audiobooks/arctic_65.wav',
        './recordings/audiobooks/arctic_1.wav',
        './recordings/audiobooks/arctic_43.wav',
    ]

    model_input = prepare_model_input(read_batch(test_files), device=device)
    output = model(model_input)
    for example in output:
        print(decoder(example.cpu()))


if __name__ == '__main__':
    run()
