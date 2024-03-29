import sys
import importlib
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--NAME', required=True)

args = parser.parse_args()
subname = args.NAME


try:
    mymodule = importlib.import_module(subname)
    KMeansClustering = mymodule.KMeansClustering
except Exception as e:
    print(e)
    print("Run python SampleTest.py --NAME K_Means_Clustering ")
    sys.exit()


X1 = np.array([[8.34044009e+00, 1.44064899e+01, 2.28749635e-03, 6.04665145e+00,
        2.93511782e+00],
       [1.84677190e+00, 3.72520423e+00, 6.91121454e+00, 7.93534948e+00,
        1.07763347e+01],
       [8.38389029e+00, 1.37043900e+01, 4.08904499e+00, 1.75623487e+01,
        5.47751864e-01],
       [1.34093502e+01, 8.34609605e+00, 1.11737966e+01, 2.80773877e+00,
        3.96202978e+00],
       [1.60148914e+01, 1.93652315e+01, 6.26848356e+00, 1.38464523e+01,
        1.75277830e+01],
       [1.78921333e+01, 1.70088423e+00, 7.81095665e-01, 3.39660839e+00,
        1.75628501e+01],
       [1.96693668e+00, 8.42215250e+00, 1.91577906e+01, 1.06633057e+01,
        1.38375423e+01],
       [6.31031262e+00, 1.37300186e+01, 1.66925134e+01, 3.65765547e-01,
        1.50028863e+01],
       [1.97772218e+01, 1.49633131e+01, 5.60887984e+00, 1.57855866e+01,
        2.06452013e+00],
       [8.95787052e+00, 1.81719101e+01, 5.87228297e+00, 5.75550677e+00,
        2.60057144e+00],
       [3.87339157e-01, 1.35767107e+01, 4.23256232e+00, 5.31093319e+00,
        9.83146319e+00],
       [1.06725090e+00, 1.14823521e+01, 2.93457150e+00, 1.17861107e+01,
        1.39951672e+01],
       [2.04668858e+00, 8.28111976e+00, 1.38880032e+01, 8.28358539e+00,
        9.99069179e-01],
       [1.07179281e+01, 1.32758929e+01, 1.02977822e+01, 1.88918951e+01,
        1.17311008e+01],
       [1.80680383e+01, 2.74949408e+00, 2.78552695e+00, 1.61478258e+01,
        7.95353674e+00]])

X2 = np.array([[1.65354197, 9.2750858 , 3.4776586 , 7.50812103, 7.25997985,
        8.83306091],
       [6.23672207, 7.50942434, 3.48898342, 2.69927892, 8.95886218,
        4.2809119 ],
       [9.64840047, 6.63441498, 6.2169572 , 1.14745973, 9.49489259,
        4.49912133],
       [5.78389614, 4.08136803, 2.3702698 , 9.03379521, 5.73679487,
        0.02870327],
       [6.17144914, 3.26644902, 5.27058102, 8.85942099, 3.5726976 ,
        9.08535151],
       [6.23360116, 0.15821243, 9.29437234, 6.90896918, 9.9732285 ,
        1.72340508],
       [1.3713575 , 9.32595463, 6.96818161, 0.66000173, 7.55463053,
        7.53876188],
       [9.23024536, 7.11524759, 1.24270962, 0.19880134, 0.26210987,
        0.28306488],
       [2.46211068, 8.60027949, 5.38831064, 5.52821979, 8.42030892,
        1.24173315],
       [2.79183679, 5.85759271, 9.69595748, 5.61030219, 0.18647289,
        8.00632673],
       [2.32974274, 8.07105196, 3.87860644, 8.63541855, 7.47121643,
        5.56240234],
       [1.36455226, 0.5991769 , 1.21343456, 0.44551879, 1.07494129,
        2.25709339],
       [7.1298898 , 5.59716982, 0.1255598 , 0.7197428 , 9.6727633 ,
        5.68100462],
       [2.03293235, 2.52325745, 7.43825854, 1.95429481, 5.81358927,
        9.70019989],
       [8.46828801, 2.39847759, 4.93769714, 6.19955718, 8.289809  ,
        1.56791395],
       [0.18576202, 0.70022144, 4.86345111, 6.06329462, 5.68851437,
        3.17362409],
       [9.88616154, 5.79745219, 3.80141173, 5.50948219, 7.45334431,
        6.69232893],
       [2.64919558, 0.66334834, 3.70084198, 6.29717507, 2.1017401 ,
        7.52755554],
       [0.66536481, 2.60315099, 8.04754564, 1.93434283, 6.39460881,
        5.24670309],
       [9.2480797 , 2.6329677 , 0.65961091, 7.35065963, 7.7217803 ,
        9.07815853]])

c1 = np.array([[8.34044009e+00, 1.44064899e+01, 2.28749635e-03, 6.04665145e+00,
        2.93511782e+00],
       [1.84677190e+00, 3.72520423e+00, 6.91121454e+00, 7.93534948e+00,
        1.07763347e+01],
       [8.38389029e+00, 1.37043900e+01, 4.08904499e+00, 1.75623487e+01,
        5.47751864e-01],
       [1.34093502e+01, 8.34609605e+00, 1.11737966e+01, 2.80773877e+00,
        3.96202978e+00],
       [1.60148914e+01, 1.93652315e+01, 6.26848356e+00, 1.38464523e+01,
        1.75277830e+01]])

c2 = np.array([[1.65354197, 9.2750858 , 3.4776586 , 7.50812103, 7.25997985,
        8.83306091],
       [6.23672207, 7.50942434, 3.48898342, 2.69927892, 8.95886218,
        4.2809119 ],
       [9.64840047, 6.63441498, 6.2169572 , 1.14745973, 9.49489259,
        4.49912133],
       [5.78389614, 4.08136803, 2.3702698 , 9.03379521, 5.73679487,
        0.02870327]])

ca1 = np.array([0, 1, 2, 3, 4, 3, 1, 3, 2, 0, 1, 1, 1, 4, 2])

ca2 = np.array([0, 1, 2, 3, 0, 3, 1, 1, 1, 0, 0, 3, 1, 0, 3, 3, 1, 3, 1, 1])

mstep_c1 = np.array([[ 8.64915531, 16.28919997,  2.93728523,  5.90107911,  2.76784463],
       [ 1.46299744,  9.09750785,  9.42482842,  8.7958569 ,  9.8879153 ],
       [15.40971679, 10.47239906,  4.16115059, 16.49858702,  3.52193625],
       [12.53726536,  7.92566628,  9.54913522,  2.19003757, 12.17592205],
       [13.36640975, 16.32056221,  8.2831329 , 16.36917372, 14.62944193]])
mstep_c2 = np.array([[2.9959006 , 5.79868739, 5.95221242, 6.51351151, 4.86079121,
        8.23746828],
       [5.77874143, 6.14770584, 3.71528917, 3.07506615, 7.05480103,
        5.00533337],
       [9.64840047, 6.63441498, 6.2169572 , 1.14745973, 9.49489259,
        4.49912133],
       [4.11421586, 1.43346745, 4.39667782, 5.82471834, 5.47750469,
        2.71304922]])

eval1 = 23012.931596198356
eval2 = 8085.5338382680275


def assert_close(x, y):

    assert abs(x-y) < 1.5 * 1e-2

def test1():

    try:
        model = KMeansClustering(5)
        model.centroids = np.copy(c1)
        oca1 = model.e_step(X1)
        np.testing.assert_array_equal(oca1, ca1)
        print('Passed E Step Test Case 1')
    except Exception as e:
        print(f'Failed E Step Test Case 1 {e}')

    try:
        model = KMeansClustering(5)
        model.centroids = np.copy(c1)
        model.m_step(X1, ca1)
        np.testing.assert_almost_equal(model.centroids, mstep_c1, decimal = 2)
        print('Passed M Step Test Case 1')
    except Exception as e:
        print(f'Failed M Step Test Case 1 {e}')

    try:
        model = KMeansClustering(5)
        model.centroids = np.copy(c1)
        oeval1 = model.evaluate(X1)
        assert_close(oeval1, eval1)
        print('Passed Eval Test Case 1')
    except Exception as e:
        print(f'Failed Eval Test Case 1 {e}')

def test2():

    try:
        model = KMeansClustering(4)
        model.centroids = np.copy(c2)
        oca2 = model.e_step(X2)
        np.testing.assert_array_equal(oca2, ca2)
        print('Passed E Step Test Case 2')
    except Exception as e:
        print(f'Failed E Step Test Case 2 {e}')

    try:
        model = KMeansClustering(4)
        model.centroids = np.copy(c2)
        model.m_step(X2, ca2)
        np.testing.assert_almost_equal(model.centroids, mstep_c2, decimal = 2)
        print('Passed M Step Test Case 2')
    except Exception as e:
        print(f'Failed M Step Test Case 2 {e}')

    try:
        model = KMeansClustering(4)
        model.centroids = np.copy(c2)
        oeval2 = model.evaluate(X2)
        assert_close(oeval2, eval2)
        print('Passed Eval Test Case 2')
    except Exception as e:
        print(f'Failed Eval Test Case 2 {e}')

if __name__ == '__main__':

    test1()
    test2()
