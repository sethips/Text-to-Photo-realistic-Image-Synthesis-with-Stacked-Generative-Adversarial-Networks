# Dataset name: flowers, birds
DATASET_NAME = 'birds'
EMBEDDING_TYPE = 'cnn-rnn'
CONFIG_NAME = ''
GPU_ID = '0'
CUDA = True
WORKERS = 6

NET_G = '../data/models/netG_epoch_360.pth'
#NET_G = '/content/netG_epoch_360.pth'
NET_D = ''
STAGE1_G = '/content/netG_epoch_360.pth'
DATA_DIR = ''
VAL_DIR = '../data/models/netG_epoch_360'
VIS_COUNT = 64

Z_DIM = 100
IMSIZE = 64
STAGE = 1

#STAGE1_G = '/content/output/birds__2020_09_05_15_46_24/Model/netG_epoch_600.pth'



TRAIN_FLAG = False
TRAIN_BATCH_SIZE = 32
TRAIN_MAX_EPOCH = 100
TRAIN_SNAPSHOT_INTERVAL = 5
TRAIN_PRETRAINED_MODEL = ''
TRAIN_PRETRAINED_EPOCH = 600
TRAIN_LR_DECAY_EPOCH = 20
TRAIN_DISCRIMINATOR_LR = 0.0002
TRAIN_GENERATOR_LR = 0.0002


TRAIN_COEFF_KL = 2.0

# Modal options

GAN_CONDITION_DIM = 128
GAN_DF_DIM = 96
GAN_GF_DIM = 192
GAN_R_NUM = 2


TEXT_DIMENSION = 1024

EMBEDDING_FILENAME = "/char-CNN-RNN-embeddings.pickle"