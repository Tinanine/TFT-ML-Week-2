# Week 2 - Assignment 1

Coach: [Yiqi Yan](https://saoyan.github.io/)

## Goals  
* Implement Linear Regression from scratch. (The key is to understand gradient descend.)  
* Get familiar with Tensorflow.

## Implement Linear Regression from scratch  
* In *regression.py*, some key functions for Linear Regression are defined. **You task is to finished the computation of gradient in the function *gradientDescentOptimizer()*.**
* In *gradient_descent.py*, we build a linear regression model, invoking *gradientDescentOptimizer()* you've just finished. Just run the code, and if you finished your task correctly, you would see the following figures.  
![](https://github.com/TFTxiaozu/TFT-ML-Week-2/blob/master/assets/assign_1_1.png)  
![](https://github.com/TFTxiaozu/TFT-ML-Week-2/blob/master/assets/assign_1_2.png)  
![](https://github.com/TFTxiaozu/TFT-ML-Week-2/blob/master/assets/assign_1_3.png)  
![](https://github.com/TFTxiaozu/TFT-ML-Week-2/blob/master/assets/assign_1_4.png)

* In *gradient_descent_feature_scaling.py*, we build the same model, while the input values are normalized. Run this code and understand how normalization helps with optimization.  
**In any machine learning models, normalization is required as a default data-preprocessing method! Never forget to do this!**

## Get familiar with Tensorflow
* [Here some simple demos.](https://github.com/SaoYan/LearningTensorflow) Play with [*exp_1*](https://github.com/SaoYan/LearningTensorflow/blob/master/exp01_basic_usage.py) and [*exp_2*](https://github.com/SaoYan/LearningTensorflow/blob/master/exp02_simple_linear_model.py) and try to understand as much as you can.  
* There are some tutorials (in Chinese) to help you understand the code. For *exp_1*, refer to [section 2](https://mp.weixin.qq.com/s?__biz=MzIxOTQ3MTI5NQ==&mid=100000348&idx=1&sn=b71d4ce18a8fe6bb7962f161cb186107&scene=19#wechat_redirect). For *exp_2*, refer to [section 3](https://mp.weixin.qq.com/s?__biz=MzIxOTQ3MTI5NQ==&mid=100000351&idx=1&sn=20491f00e2bd5b49dfb7e9b03c99dcf0&scene=19#wechat_redirect).
