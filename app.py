import numpy as np
import pickle
import streamlit as st

##missed some modules
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier



# for model improvement
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import VotingClassifier

from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import joblib

##Okay clear

# loading the saved model 

# loaded_model
loaded_model = pickle.load(open('model/trained_model.pkl','rb'))

# Membuat fungsi

def Heart_disease_Prediction(input_data):
    
    
    # merubah data ke numpy array 
    input_data_array = np.asarray(input_data, dtype = np.float64)
    
    # reshape array
    input_data_reshaped =  input_data_array.reshape(1,-1)
    
    result = loaded_model.predict(input_data_reshaped)
    print("Prediksinya adalah : ",result)
    
    if (result[0] == 1):
      return "Orang tersebut memiliki penyakit jantung"        
    else:
      return "Orang tersebut memiliki tidak memiliki penyakit jantung"
  

def main():
    # judul
    st.markdown("<h1 style='text-align: center; color: red;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
    
    # Input Data
    
    age= st.text_input("Umur : ")
    sex= st.text_input("Kelamin : ")
    cp = st.text_input("Chest pain type : ")
    restbps = st.text_input("Tekanan darah (Dalam Numerik Angka) : ")
    chol = st.text_input("Kolestrol (Dalam Numerik Angka) (mg/dl) : ")
    fbs = st.text_input("Gula Darah Saat Puasa (0 = Salah Atau 1 = Benar) > 120 mg/dl : ")
    restecg = st.text_input("Resting electrocardiographic results (0-2) : ")
    thalach = st.text_input("Maximum heart rate achieved / Detak jantung maksimal yang dicapai : ")
    exang = st.text_input("Exercise induced angina : ")
    oldpeak = st.text_input("Oldpeak : ")
    slope = st.text_input("Slope of the peak exercise ST segment / Kemiringan puncak latihan segmen ST : ")
    ca = st.text_input("Number of major vessels (0-3) / Jumlah pembuluh darah besar (0-3) yang diwarnai dengan flourosopy : ")
    thal = st.text_input("chest pain type : ")
    
    
    # code-prediction 
    predict = '' # null string 
    
    # Button Prediction
    
    if st.button('Diagnosis Test Result'):
        predict = Heart_disease_Prediction([age, sex, cp, restbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ])
        
    st.success(predict)
    
    st.markdown("***")
    
    st.markdown("""
    
    Sample Untuk diisi: 
    
        29;1;1;130;204;0;0;202;0;0;2;0;2    => Sehat
    
        52;1;2;172;199;1;1;162;0;0.5;2;0;3	  => Dengan Penyakit Jantung """)
    
    st.markdown("""
    
    Informasi data yang harus diisi : 
        
        1. Usia: menampilkan usia individu.
        
        2. Jenis Kelamin: menampilkan jenis kelamin individu dengan format berikut :
            1 = laki-laki
            0 = perempuan
        
        3. Tipe nyeri dada: menampilkan jenis nyeri dada yang dialami seseorang dengan format sebagai berikut :
            1 = angina tipikal
            2 = angina atipikal
            3 = bukan - nyeri angina
            4 = tanpa gejala
        
        4. Tekanan Darah Istirahat: menampilkan nilai tekanan darah istirahat seseorang dalam mmHg (satuan)
        
        5. Kolestrol Serum: menampilkan kolesterol serum dalam mg/dl (unit)
        
        6. Gula Darah Puasa: membandingkan nilai gula darah puasa seseorang dengan 120mg/dl.
        Jika gula darah puasa > 120mg/dl maka : 
            1 (benar)
            lain : 0 (salah)
        
        7. EKG Istirahat : menampilkan hasil elektrokardiografi istirahat
            0 = biasa
            1 = mengalami kelainan gelombang ST-T
            2 = hipertrofi ventrikel kiri
        
        8. Detak jantung maksimal yang dicapai : menampilkan detak jantung maksimal yang dicapai oleh seorang individu.
        
        9.Angina akibat olahraga :
            1 = ya
            0 = tidak
        
        10. Oldpeak = Depresi ST yang disebabkan oleh olahraga dibandingkan istirahat
        
        11. Kemiringan puncak latihan segmen ST
        
        12. Jumlah pembuluh darah besar (0-3) yang diwarnai dengan flourosopy
        
        13. Thal : 0 = biasa; 1 = cacat tetap; 2 = cacat yang dapat dibalik""")
    
    st.text("\n\n")
    
    st.write(" \n\n\n\n")
    st.markdown("******")
    
    st.write("\n© 2024 Modifided")
if __name__ == '__main__':
    main()
    
    
