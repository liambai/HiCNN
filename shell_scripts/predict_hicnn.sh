export PATH=/home/lbai5/anaconda3/bin:$PATH
cd singh_lab/HiCNN_software_package/
which python
python HiCNN_predict.py -f1 extracted_data/lowres_ch22.npy -f2 extracted_data/ch22_predict_out.txt -m trained_models/model_10 -r 16
