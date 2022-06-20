# Lazy Loader
 
from Tensorflow's lazy_loader

see
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py

install
```
!pip install git+https://github.com/joreeves/LazyLoader.git
```

usage
```
from lazyloader import LazyLoader

tf = LazyLoader('tf', globals(), 'tensorflow')
```
