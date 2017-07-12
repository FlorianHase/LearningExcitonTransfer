
# Trained MLP models for exciton transfer property predictions

We provide parameters and hyperparameters of trained multi-layer perceptron (MLP) models. All parameters are uploaded for MLPs trained on PCA selected training sets due to the higher accuracy observed for out-of-sample predictions. 

We also provide a script `trainer.py` to illustrate how to employ the parameters and hyperparameters to construct a MLP model and use it for exciton transfer time and transfer efficiency predictions. Below is an example for how to use `trainer.py` for the prediction of a set of exciton Hamiltonians contained in `to_predict.hkl` with the MLP trained on the `CP43` dataset.

```python
from trainer import Predictor
        predictor = Predictor('CP43')
        predictor.create_session()
        predictor.predict('to_predict.hkl')
```

Note, that `trainer.py` expects the exciton Hamiltonians to be provided in units of [cm<sup>-1</sup>], to be reshaped into a vector and to be stored under the key `features`. A procedure for generating such a compressed file from a numpy array is illustrated in the script `generate_compressed_file.py`. 

