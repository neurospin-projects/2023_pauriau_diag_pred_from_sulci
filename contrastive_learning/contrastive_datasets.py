import numpy as np
from datasets.clinical_multisites import SCZDataset, ASDDataset, BipolarDataset
from datasets.open_bhb import OpenBHB, SubOpenBHB
from datasets.bhb_10k import HCPDataset


class ContrastiveOpenBHB(OpenBHB):
    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1


class ContrastiveSubOpenBHB(SubOpenBHB):
    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1


class ContrastiveSCZDataset(SCZDataset):

    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1


class ContrastiveASDDataset(ASDDataset):

    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1


class ContrastiveBipolarDataset(BipolarDataset):

    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1


class ContrastiveHCPDataset(HCPDataset):

    def __getitem__(self, idx: int):
        np.random.seed()
        x1, y1 = super().__getitem__(idx)
        x2, y1 = super().__getitem__(idx)
        return np.stack((x1, x2), axis=0), y1
