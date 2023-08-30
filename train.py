import os
import argparse
from sys import meta_path

import pandas as pd
import pickle


def train(args: argparse.Namespace):
    """ 학습을 위한 코드

    Args:
        args (argparse.ArgumentParser): 학습 시 필요한 변수들이 담긴 객체
    """

    m = model_cls(args)
    m.train()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_dir', type=str, default='', help='data directory')
    parser.add_argument('--filename', type=str, default='', help='output file name')    
    parser.add_argument('--iterations', type=int, default=1, help='default: 1')
    parser.add_argument('--batch_size', type=int, default=50, help='default: 50')
    parser.add_argument('--lr', type=float, default=0.025, help='default: 0.025)')
    
    args = parser.parse_args()
    print(args)
    
    train(args)