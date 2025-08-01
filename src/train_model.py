import numpy as np
import h5py
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
from absl import logging
from .utils import temporal_nms  # Ensure this utility function exists and works correctly
import torch
from .augmented_tsn import AugmentedTsn


#structure of h5 file:    process_recording(
                    #h5f,
                    #args.data_root,
                    #file_name,
                    #row["label"],
                   # row["split"]

def train_model(h5_file_path, epochs, ):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.CrossEntropyLoss()
    model = AugmentedTsn(num_classes=6,num_tsn_samples=5,sample_duration=1,decay=0.1)


    with h5py.File(h5_file_path, 'r') as f:
        histogram_data = f
        labels = f['label'][:]