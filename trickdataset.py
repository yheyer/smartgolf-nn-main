import torch
import numpy as np
from os import walk

class TrickDataset:
    def __init__(self, rootfolder, label_list):
        self.rootfolder = rootfolder
        self.label_list = label_list
        self.data, self.labels = self.dataloader()
        print(self.rootfolder, self.label_list)


    def dataloader(self):

        # Iterates through directory including subfolders
        # Csv files are loaded into list (data) 
        data = []
        labels = []

        for root, dirs, files in walk(self.rootfolder):

            for file in files:
                # If file has a .csv extension, ent
                if file.endswith(".csv"):

                    # Only if the filename of the current csv contains a viable label, 
                    # the data and the label is added to the respective list 
                    for id, name in enumerate(self.label_list):
                        
                        if (file[0] == (name)):
                            path = (root+"/"+file)
                            sample = np.loadtxt(path, dtype=np.float32, delimiter=";")
                            sample = sample[199:300,3:6]
                            data.append(sample)
                            labels.append(id)
                        else: 
                            pass
                            
                        
        return data, labels
        
        
    def __len__(self):

        # Returns number of samples when accessed through len(<dataset_object>)
        return len(self.data)

    def __getitem__(self, idx):

        # Accessing an element of the Dataset through an index returns a dictionary containing two elements, the data and the corresponding label
        current_sample = self.data[idx]
        current_label = self.labels[idx]

        # When returning the sample tensor, its reshaped to "N Channels" and "N Timesteps" to fit imput format of Conv1d layer
        return [
            torch.tensor(current_sample, dtype=torch.float),#.view(9,120),
            torch.tensor(current_label, dtype=torch.long),
        ]

trick_list = ['0', '1', '2']
ds = TrickDataset(rootfolder="golfdata", label_list=trick_list)
