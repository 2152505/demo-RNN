import numpy as np

class SoftMax():

    # 函数原型：e^x/sum(e^x)
    def forward(self, input):
        '''
        正向计算求值
        :param input:
        :return:
        '''
        result = np.exp(input)
        return result / (np.sum(result) + 0.001)
        pass

    def backward(self, output):
        '''
        反向计算求梯度
        :param output: 是正向计算的结果，forward的计算结果
        :return:
        '''
        return output * (1 - output)
        pass
    pass

class Tanh():

    # 函数原型：e^x/sum(e^x)
    def forward(self, input):
        '''
        正向计算求值
        :param input:
        :return:
        '''
        result = np.exp(input)
        result2 = np.exp(-input)
        return (result - result2) / (result + result2)
        pass

    def backward(self, output):
        '''
        反向计算求梯度
        :param output: 是正向计算的结果，forward的计算结果
        :return:
        '''
        return 1 - output ** 2
        pass
    pass
