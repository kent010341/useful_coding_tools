from DetailRecorder import DetailRecorder
import numpy as np 

dr = DetailRecorder(detail_dir='output')
# Test no input
dr.dprint()
# Test int input
dr.dprint(123)
# Test float input
dr.dprint(1.23)
# Test complex input
dr.dprint(1+1j)
# Test multiple input
dr.dprint(1, 2.3, 4+5j)
# Test list and np.ndarray input
dr.dprint([1, '2', [3, 4], np.array([5, 6, 7])])