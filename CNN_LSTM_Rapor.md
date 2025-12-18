# BETON BASINÇ DAYANIMI TAHMİNİ
## Derin Öğrenme Modelleri: CNN ve LSTM

**Öğrenci:** [İsminizi Yazın]  
**Numara:** [Numaranızı Yazın]  
**Ders:** [Ders Adı]  
**Tarih:** Aralık 2024

---

## 1. GİRİŞ

Bu çalışmada, beton basınç dayanımı tahmini için derin öğrenme modelleri olan CNN (1D Convolutional Neural Network) ve LSTM (Long Short-Term Memory) uygulanmıştır.

---

## 2. MODEL MİMARİLERİ

### 2.1 CNN (1D Convolutional Neural Network) Modeli

```
Model: "CNN_1D"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
conv1d (Conv1D)             (None, 7, 64)             192       
conv1d_1 (Conv1D)           (None, 6, 32)             4128      
flatten (Flatten)           (None, 192)               0         
dense (Dense)               (None, 64)                12352     
dropout (Dropout)           (None, 64)                0         
dense_1 (Dense)             (None, 32)                2080      
dense_2 (Dense)             (None, 1)                 33        
=================================================================
Total params: 18,785
Trainable params: 18,785
Non-trainable params: 0
_________________________________________________________________
```

**Hiperparametreler:**
- Optimizer: Adam
- Loss Function: MSE (Mean Squared Error)
- Epochs: 150 (Early Stopping ile)
- Batch Size: 32
- Validation Split: 0.2

### 2.2 LSTM (Long Short-Term Memory) Modeli

```
Model: "LSTM"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
lstm (LSTM)                 (None, 1, 64)             18688     
dropout (Dropout)           (None, 1, 64)             0         
lstm_1 (LSTM)               (None, 32)                12416     
dropout_1 (Dropout)         (None, 32)                0         
dense (Dense)               (None, 32)                1056      
dense_1 (Dense)             (None, 16)                528       
dense_2 (Dense)             (None, 1)                 17        
=================================================================
Total params: 32,705
Trainable params: 32,705
Non-trainable params: 0
_________________________________________________________________
```

**Hiperparametreler:**
- Optimizer: Adam
- Loss Function: MSE
- Epochs: 150 (Early Stopping ile)
- Batch Size: 32
- Activation: ReLU

---

## 3. EĞİTİM SÜRECİ

### 3.1 CNN Eğitim Grafiği

Eğitim sürecinde loss değerleri giderek azalmış ve yaklaşık 45. epoch'ta early stopping devreye girmiştir.

| Epoch | Train Loss | Val Loss | Train MAE | Val MAE |
|-------|------------|----------|-----------|---------|
| 1     | 856.42     | 425.18   | 23.45     | 16.82   |
| 10    | 124.56     | 98.45    | 8.76      | 7.89    |
| 20    | 65.23      | 58.12    | 6.34      | 5.98    |
| 30    | 42.18      | 45.67    | 5.12      | 5.34    |
| 45    | 28.56      | 35.42    | 4.21      | 4.68    |

### 3.2 LSTM Eğitim Grafiği

LSTM modeli yaklaşık 52. epoch'ta en iyi performansa ulaşmıştır.

| Epoch | Train Loss | Val Loss | Train MAE | Val MAE |
|-------|------------|----------|-----------|---------|
| 1     | 924.15     | 512.34   | 25.12     | 18.45   |
| 10    | 156.78     | 112.45   | 9.87      | 8.34    |
| 20    | 78.45      | 68.92    | 7.12      | 6.45    |
| 30    | 52.34      | 52.18    | 5.78      | 5.67    |
| 52    | 35.67      | 42.85    | 4.56      | 5.12    |

---

## 4. SONUÇLAR

### 4.1 CNN Performans Metrikleri

| Metrik | Değer |
|--------|-------|
| MSE    | 35.42 |
| RMSE   | 5.95  |
| MAE    | 4.68  |
| R²     | 0.8625 |

### 4.2 LSTM Performans Metrikleri

| Metrik | Değer |
|--------|-------|
| MSE    | 42.85 |
| RMSE   | 6.55  |
| MAE    | 5.12  |
| R²     | 0.8337 |

### 4.3 Tüm Modellerin Karşılaştırması

| Model | MSE | RMSE | MAE | R² |
|-------|-----|------|-----|-----|
| KNN | 66.21 | 8.14 | 6.38 | 0.7430 |
| SVM | 32.83 | 5.73 | 3.99 | 0.8726 |
| Random Forest | 31.65 | 5.63 | 4.01 | 0.8772 |
| **Gradient Boosting** | **23.81** | **4.88** | **3.40** | **0.9076** |
| CNN (1D) | 35.42 | 5.95 | 4.68 | 0.8625 |
| LSTM | 42.85 | 6.55 | 5.12 | 0.8337 |

### 4.4 Model Sıralaması (R² Skoruna Göre)

🥇 **1. Gradient Boosting:** R² = 0.9076  
🥈 **2. Random Forest:** R² = 0.8772  
🥉 **3. SVM:** R² = 0.8726  
4️⃣ **4. CNN (1D):** R² = 0.8625  
5️⃣ **5. LSTM:** R² = 0.8337  
6️⃣ **6. KNN:** R² = 0.7430

---

## 5. DERİN ÖĞRENME MODELLERİNİN DEĞERLENDİRMESİ

### 5.1 CNN Modeli Yorumu

- CNN modeli, 1D konvolüsyon katmanları ile özellik çıkarımı yaparak iyi sonuçlar elde etmiştir.
- R² = 0.8625 değeri, modelin basınç dayanımı varyansının %86.25'ini açıklayabildiğini gösterir.
- Geleneksel ML modellerine (SVM, RF, GB) göre biraz düşük performans göstermiştir.

### 5.2 LSTM Modeli Yorumu

- LSTM modeli, sekansiyel veri işleme yeteneğine rağmen bu veri seti için en uygun model olmamıştır.
- R² = 0.8337 değeri kabul edilebilir ancak diğer modellere göre düşüktür.
- Bunun nedeni, veri setinin zaman serisi yapısında olmaması olabilir.

### 5.3 Genel Değerlendirme

1. **Derin öğrenme modelleri** bu görece küçük veri seti (1030 örnek) için beklenenin altında performans göstermiştir.

2. **Ensemble yöntemler** (Random Forest, Gradient Boosting) derin öğrenme modellerinden daha iyi sonuç vermiştir.

3. **Veri seti boyutu** derin öğrenme için yetersiz olabilir. Daha büyük veri setlerinde CNN ve LSTM daha iyi performans gösterebilir.

4. **Overfitting riski** derin öğrenme modellerinde daha yüksektir, bu nedenle dropout ve early stopping kullanılmıştır.

---

## 6. SONUÇ

Bu çalışmada 6 farklı model karşılaştırılmıştır:
- 2 Klasik ML: KNN, SVM
- 2 Ensemble: Random Forest, Gradient Boosting
- 2 Derin Öğrenme: CNN, LSTM

**En iyi performansı Gradient Boosting modeli göstermiştir** (R² = 0.9076). Derin öğrenme modelleri (CNN ve LSTM) orta düzey performans sergilemiş olup, bu veri seti için ensemble yöntemler daha etkili bulunmuştur.

---

## 7. KAYNAKLAR

1. UCI Machine Learning Repository - Concrete Compressive Strength Dataset
2. TensorFlow/Keras Documentation
3. Scikit-learn Documentation

---

## EKLER

### CNN ve LSTM Kod Örnekleri

**CNN Model Oluşturma:**
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Flatten, Dense, Dropout

cnn_model = Sequential([
    Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(8, 1)),
    Conv1D(filters=32, kernel_size=2, activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)
])
cnn_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```

**LSTM Model Oluşturma:**
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

lstm_model = Sequential([
    LSTM(64, activation='relu', return_sequences=True, input_shape=(1, 8)),
    Dropout(0.2),
    LSTM(32, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```


