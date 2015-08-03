# -*- coding: utf-8 -*-
from fuel.datasets.cifar100 import CIFAR100
from .data_utils import get_datasets, fuel_datasets_into_lists

fileinfo = [
    "cifar100.hdf5",
    "https://archive.org/download/kerosene_mnist/cifar100.hdf5"
]

def load_data(sets=['train', 'test'], sources=['features', 'coarse_labels']):
    def load_data_callback():
        return map(lambda s: CIFAR100(which_sets=[s], sources=sources), sets)

    fuel_datasets = get_datasets(load_data_callback, *fileinfo)
    return fuel_datasets_into_lists(fuel_datasets)
    