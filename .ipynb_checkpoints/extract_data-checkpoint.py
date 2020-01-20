from numpy import asarray
from numpy import save
import straw

result=straw.straw("NONE", "https://hicfiles.s3.amazonaws.com/hiseq/gm12878/in-situ/combined.hic","1","21","BP", 100000)
save('data.npy', result)
