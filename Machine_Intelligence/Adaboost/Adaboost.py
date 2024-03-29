import numpy as np
from sklearn.tree import DecisionTreeClassifier

from math import sqrt
import pandas as pd

"""
Use DecisionTreeClassifier to represent a stump.
------------------------------------------------
DecisionTreeClassifier Params:
    critereon -> entropy
    max_depth -> 1
    max_leaf_nodes -> 2
Use the same parameters
"""
# REFER THE INSTRUCTION PDF FOR THE FORMULA TO BE USED 

class AdaBoost:

    """
    AdaBoost Model Class
    Args:
        n_stumps: Number of stumps (int.)
    """

    def __init__(self, n_stumps=20):

        self.n_stumps = n_stumps
        self.stumps = []

    def fit(self, X, y):
        """
        Fitting the adaboost model
        Args:
            X: M x D Matrix(M data points with D attributes each)(numpy float)
            y: M Vector(Class target for all the data points as int.)
        Returns:
            the object itself
        """
        self.alphas = []

        sample_weights = np.ones_like(y) / len(y)
        for _ in range(self.n_stumps):

            st = DecisionTreeClassifier(
                criterion='entropy', max_depth=1, max_leaf_nodes=2)
            st.fit(X, y, sample_weights)
            y_pred = st.predict(X)

            self.stumps.append(st)

            error = self.stump_error(y, y_pred, sample_weights=sample_weights)
            alpha = self.compute_alpha(error)
            self.alphas.append(alpha)
            sample_weights = self.update_weights(
                y, y_pred, sample_weights, alpha)

        return self

    def stump_error(self, y, y_pred, sample_weights):
        """
        Calculating the stump error
        Args:
            y: M Vector(Class target for all the data points as int.)
            y_pred: M Vector(Class target predicted for all the data points as int.)
            sample_weights: M Vector(Weight of each sample float.)
        Returns:
            The error in the stump(float.)
        """

        # TODO
        error_expression=y_pred!=y
        error = np.where(error_expression,1,0)
        a1_e=np.sum(sample_weights*error)
        a2_w=np.sum(sample_weights)
        answer = a1_e/a2_w
        return answer
        pass

    def compute_alpha(self, error):
        """
        Computing alpha
        The weight the stump has in the final prediction
        Use eps = 1e-9 for numerical stabilty.
        Args:
            error:The stump error(float.)
        Returns:
            The alpha value(float.)
        """
        epsilon = 1e-9
        # TODO
        a=1-error
        b=error+epsilon
        value=np.log(a/b)
        alpha=0.5*value
        return alpha
        pass

    def update_weights(self, y, y_pred, sample_weights, alpha):
        """
        Updating Weights of the samples based on error of current stump
        The weight returned is normalized
        Args:
            y: M Vector(Class target for all the data points as int.)
            y_pred: M Vector(Class target predicted for all the data points as int.)
            sample_weights: M Vector(Weight of each sample float.)
            alpha: The stump weight(float.)
        Returns:
            new_sample_weights:  M Vector(new Weight of each sample float.)
        """

        # TODO
        error = self.stump_error(y, y_pred, sample_weights)
        if(error==0):
            mismatch=np.not_equal(y, y_pred)
            mismatch_type=mismatch.astype(int)
            mismatch_value=alpha *mismatch_type
            mismatch_exp=np.exp(mismatch_value)
            
            value=sample_weights * mismatch_exp
            return value
       
        for i in range(len(sample_weights)):
            sw1=sample_weights[i]
            
            if y[i] != y_pred[i]:
                sw2=(2*error)
            else:
                sw2=(2*(1-error))
            sample_weights[i] = sw1/sw2
        answer=sample_weights
        return answer
        pass

    def predict(self, X):
        """
        Predicting using AdaBoost model with all the decision stumps.
        Decison stump predictions are weighted.
        Args:
            X: N x D Matrix(N data points with D attributes each)(numpy float)
        Returns:
            pred: N Vector(Class target predicted for all the inputs as int.)
        """
        # TODO
        
        
        r=self.n_stumps
        value=[self.stumps[i].predict(X) for i in range(r)]
        
        predicted_value = np.array(value)
        answer=np.sign(predicted_value[0])
        return answer

        pass

    def evaluate(self, X, y):
        """
        Evaluate Model on test data using
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix
            y: True target of test data
        Returns:
            accuracy : (float.)
        """
        pred = self.predict(X)
        # find correct predictions
        correct = (pred == y)
        accuracy = np.mean(correct) * 100  # accuracy calculation
        return accuracy
