from numpy import asarray
from numpy import save
import straw
from scipy.sparse import csr_matrix
import utils

highres = utils.matrix_extract(18, 10000, "https://hicfiles.s3.amazonaws.com/hiseq/gm12878/in-situ/combined.hic")

print('dividing, filtering and downsampling files...')

highres_sub, index = utils.divide(highres)

print("highres shape: ", highres_sub.shape)

lowres = utils.genDownsample(highres,1/float(16))
lowres_sub,index = utils.divide(lowres)
print("lowres shape: ", lowres_sub.shape)

save('lowres_ch18.npy', lowres_sub)
save('highres_ch18.npy', highres_sub)
