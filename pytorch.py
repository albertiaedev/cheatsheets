#PYTORCH CHEATSHEET

#Imports
import torch
# Check the version of pytorch installed in your computer
print(f"PyTorch version: {torch.__version__}")
# Can also import the common abbreviation "nn" for "Neural Networks"
from torch import nn
# Almost everything in PyTorch is called a "Module" (you build neural networks by stacking together Modules)
module = nn.Linear(in_features=1,out_features=1)
print(type(module))


#Data imports
# Import PyTorch Dataset (you can store your data here) and DataLoader (you can load your data here)
from torch.utils.data import Dataset, DataLoader


#Creating tensors
# Create a single number tensor (scalar)
scalar = torch.tensor(7)
# Create a random tensor
random_tensor = torch.rand(size=(3, 4)) # this will create a tensor of size 3x4 but you can manipulate the shape how you want
# Multiply two random tensors
random_tensor_1 = torch.rand(size=(3, 4))
random_tensor_2 = torch.rand(size=(3, 4))
random_tensor_3 = random_tensor_1 * random_tensor_2 # PyTorch has support for most math operators in Python (+, *, -, /)


#Computer vision
# Base computer vision library
import torchvision
# Other components of TorchVision (premade datasets, pretrained models and image transforms)
from torchvision import datasets, models, transforms


#Text and natural language processing (NLP)
# Base text and natural language processing library
import torchtext
# Other components of TorchText (premade datasets, pretrained models and text transforms)
from torchtext import datasets, models, transforms


#Audio and speech
# Base audio and speech processing library
import torchaudio
# Other components of TorchAudio (premade datasets, pretrained models and text transforms)
from torchaudio import datasets, models, transforms


#Device-agnostic code (using PyTorch on CPU, GPU or MPS)
# Setup device-agnostic code 
if torch.cuda.is_available():
    device = "cuda" # NVIDIA GPU
elif torch.backends.mps.is_available():
    device = "mps" # Apple GPU
else:
    device = "cpu" # Defaults to CPU if NVIDIA GPU/Apple GPU aren't available

print(f"Using device: {device}")


#Sending a tensor to target device
# Create a tensor 
x = torch.tensor([1, 2, 3]) 
print(x.device) # defaults to CPU 
# Send tensor to target device
x = x.to(device)
print(x.device)

#Setting random seeds
import torch
# Set the random seed (you can set this to any number you like, it will "flavour"
# the randomness with that number.
torch.manual_seed(42)
# Create two random tensors
random_tensor_A = torch.rand(3, 4)
torch.manual_seed(42) # set the seed again (try commenting this out and see what happens)
random_tensor_B = torch.rand(3, 4)
print(f"Tensor A:\n{random_tensor_A}\n")
print(f"Tensor B:\n{random_tensor_B}\n")
print(f"Does Tensor A equal Tensor B? (anywhere)")
random_tensor_A == random_tensor_B
# Set random seed on GPU
torch.cuda.manual_seed(42)

# Neural Networks
from torch import nn
# Linear Layers
# Create a linear layer with 10 in features and out features
linear_layer = nn.Linear(in_features=10, out_features=10)
# Create an Identity layer
identity_layer = nn.Identity()
# Convolutional Layers
# Create a Conv1d layer (often used for text with a singular dimension)
conv1d = nn.Conv1d(in_channels=1, out_channels=10, kernel_size=3)
# Create a Conv2d layer (often used for images with Height x Width dimensions)
conv2d = nn.Conv2d(in_channels=3, # 3 channels for color images (red, green, blue)
                   out_channels=10, kernel_size=3)   
# Create a Conv3d layer (often used for video with Height x Width x Time dimensions)
conv3d = nn.Conv3d(in_channels=3, out_channels=10, kernel_size=3)
# Transformer Layers
# Create a Transformer model (model based on the paper "Attention Is All You Need" - https://arxiv.org/abs/1706.03762)
transformer_model = nn.Transformer()
# Create a single Transformer encoder cell
transformer_encoder = nn.TransformerEncoderLayer(d_model=768, # embedding dimension
                                                 nhead=12) # number of attention heads
# Stack together Transformer encoder cells
transformer_encoder_stack = nn.TransformerEncoder(encoder_layer=transformer_encoder, # from above
                                                  num_layers=6) # 6 Transformer encoders stacked on top of each other
# Create a single Transformer decoder cell
transformer_decoder = nn.TransformerDecoderLayer(d_model=768,
                                                 nhead=12)
# Stack together Transformer decoder cells
transformer_decoder_stack = nn.TransformerDecoder(decoder_layer=transformer_decoder, # from above
                                                  num_layers=6) # 6 Transformer decoders stacked on top of each other
# Recurrent Layers
# Create a single LSTM cell
lstm_cell = nn.LSTMCell(input_size=10, # can adjust as necessary
                        hidden_size=10) # can adjust as necessary
# Stack together LSTM cells
lstm_stack = nn.LSTM(input_size=10,
                     hidden_size=10,
                     num_layers=3) # 3 single LSTM cells stacked on top of each other
