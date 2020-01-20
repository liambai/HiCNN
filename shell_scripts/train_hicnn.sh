export PATH=/home/lbai5/anaconda3/bin:$PATH
cd singh_lab/HiCNN_software_package/
which python
python HiCNN_training.py -f1 extracted_data/lowres_ch21.npy -f2 extracted_data/highres_ch21.npy -f3 extracted_data/lowres_ch22.npy -f4 extracted_data/highres_ch22.npy -d . -r 16
