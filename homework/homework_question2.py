import pandas as pd
import numpy as np
import scipy.stats as st


Data = pd.read_csv('D:\VSCODE_DATA\WEEK_7\homework_week_7_hypotesis\\titanic_2.csv')

'''
H0: Average age of passengers in Titanic is less than 28:μ0 <=28
HA : New research claims mean age is greater than 28: μ1 > 28
'''


#merkezi limit teoremi ile 100 kişi üzerinden bir örneklem ediniyoruz.

#Sample_1 28 yaşından küçük
Sample_1 = np.array([np.mean(Data[Data["age"] <=28].sample(20)["survived"].values) for i in range(100)])

#Sample_2 28 yaşından büyük
Sample_2 = np.array([np.mean(Data[Data["age"] >28].sample(20)["survived"].values) for i in range(100)])


#Bu sample lara ait mean'ler
mean_sample_1 = round(np.mean(Sample_1),4)
print("28 yaşından küçük için mean: ",mean_sample_1)

mean_sample_2 = round(np.mean(Sample_2),4)
print("28 yaşından büyük için mean: ",mean_sample_2)

#Class'ların etkisi
effect_of_age = round(mean_sample_1 - mean_sample_2,4)
print("Effect of Age: ",effect_of_age)


#Z-score hesaplama
'''
(Mean_1 - Mean_2) / iki popülasyon arasındaki farkların dağılımının standard sapması
'''
# iki popülasyon arasındaki farkların dağılımının standard sapmasını hesaplama
'''
sample_1 numune dağılımının standart sapmasının karesi/sample_1 numune dağılım'ın uzunluğu ile
sample_2 numune dağılımının standart sapmasının karesi/sample_2 numune dağılım'ın uzunluğu toplamının
karekökü
'''
# yani
sigma_sample_1 = np.std(Sample_1)
sigma_sample_2 = np.std(Sample_2)


sigma_difference = np.sqrt((sigma_sample_1**2)/len(Sample_1)  +  (sigma_sample_2**2)/len(Sample_2))
z_score = effect_of_age / sigma_difference
print("Z-score: ",round(z_score,2))

#P-value değerini bulma
'''
P-value değeri : scipy.stats.norm.sf(abs(z_score))
ile bulunur
'''
p_value = st.norm.sf(abs(z_score))*2
print("P_value :",p_value)

'''
p_value: 3.03e-190 çıkıyor.
significance level of 0.05 dan çok çok küçük bir değer olduğu için;
rejecting the Null hypothesis.
'''

