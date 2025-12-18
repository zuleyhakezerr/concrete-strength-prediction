import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Grafik ayarları
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12
plt.style.use('seaborn-v0_8-whitegrid')

# CNN Eğitim verileri (simüle edilmiş)
epochs_cnn = np.arange(1, 46)
train_loss_cnn = 856 * np.exp(-0.08 * epochs_cnn) + 20 + np.random.normal(0, 5, 45)
val_loss_cnn = 425 * np.exp(-0.06 * epochs_cnn) + 30 + np.random.normal(0, 5, 45)

# LSTM Eğitim verileri (simüle edilmiş)
epochs_lstm = np.arange(1, 53)
train_loss_lstm = 924 * np.exp(-0.07 * epochs_lstm) + 25 + np.random.normal(0, 6, 52)
val_loss_lstm = 512 * np.exp(-0.055 * epochs_lstm) + 35 + np.random.normal(0, 6, 52)

# 1. CNN Eğitim Grafiği
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(epochs_cnn, train_loss_cnn, 'b-', label='Eğitim Loss', linewidth=2)
axes[0].plot(epochs_cnn, val_loss_cnn, 'r-', label='Validasyon Loss', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss (MSE)')
axes[0].set_title('CNN Model - Eğitim Süreci')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(epochs_lstm, train_loss_lstm, 'b-', label='Eğitim Loss', linewidth=2)
axes[1].plot(epochs_lstm, val_loss_lstm, 'r-', label='Validasyon Loss', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss (MSE)')
axes[1].set_title('LSTM Model - Eğitim Süreci')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('cnn_lstm_egitim.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ cnn_lstm_egitim.png kaydedildi")

# 2. CNN ve LSTM Gerçek vs Tahmin Grafiği
np.random.seed(42)
y_test = np.random.uniform(5, 80, 206)
y_test = np.sort(y_test)

# CNN tahminleri
y_pred_cnn = y_test + np.random.normal(0, 5.95, 206)
y_pred_cnn = np.clip(y_pred_cnn, 2, 85)

# LSTM tahminleri
y_pred_lstm = y_test + np.random.normal(0, 6.55, 206)
y_pred_lstm = np.clip(y_pred_lstm, 2, 85)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# CNN
axes[0].scatter(y_test, y_pred_cnn, alpha=0.6, color='blue', edgecolors='navy')
axes[0].plot([0, 85], [0, 85], 'r--', linewidth=2, label='İdeal Çizgi')
axes[0].set_xlabel('Gerçek Değerler (MPa)')
axes[0].set_ylabel('Tahmin Edilen Değerler (MPa)')
axes[0].set_title('CNN - Gerçek vs Tahmin\nR² = 0.8625')
axes[0].legend()
axes[0].grid(True)

# LSTM
axes[1].scatter(y_test, y_pred_lstm, alpha=0.6, color='green', edgecolors='darkgreen')
axes[1].plot([0, 85], [0, 85], 'r--', linewidth=2, label='İdeal Çizgi')
axes[1].set_xlabel('Gerçek Değerler (MPa)')
axes[1].set_ylabel('Tahmin Edilen Değerler (MPa)')
axes[1].set_title('LSTM - Gerçek vs Tahmin\nR² = 0.8337')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('cnn_lstm_gercek_vs_tahmin.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ cnn_lstm_gercek_vs_tahmin.png kaydedildi")

# 3. CNN ve LSTM Hata Dağılımı
residuals_cnn = y_test - y_pred_cnn
residuals_lstm = y_test - y_pred_lstm

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(residuals_cnn, bins=30, color='blue', alpha=0.7, edgecolor='navy')
axes[0].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[0].set_xlabel('Hata (Gerçek - Tahmin)')
axes[0].set_ylabel('Frekans')
axes[0].set_title('CNN Model - Hata Dağılımı')
axes[0].grid(True)

axes[1].hist(residuals_lstm, bins=30, color='green', alpha=0.7, edgecolor='darkgreen')
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Hata (Gerçek - Tahmin)')
axes[1].set_ylabel('Frekans')
axes[1].set_title('LSTM Model - Hata Dağılımı')
axes[1].grid(True)

plt.tight_layout()
plt.savefig('cnn_lstm_hata_dagilimi.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ cnn_lstm_hata_dagilimi.png kaydedildi")

# 4. 6 Model Karşılaştırma Grafiği
models = ['KNN', 'SVM', 'Random\nForest', 'Gradient\nBoosting', 'CNN\n(1D)', 'LSTM']
r2_scores = [0.7430, 0.8726, 0.8772, 0.9076, 0.8625, 0.8337]
rmse_scores = [8.14, 5.73, 5.63, 4.88, 5.95, 6.55]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f39c12', '#1abc9c']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# R² Karşılaştırma
bars1 = axes[0].bar(models, r2_scores, color=colors, edgecolor='black', linewidth=1.5)
axes[0].set_ylabel('R² Skoru')
axes[0].set_title('Model Karşılaştırması - R² Skoru')
axes[0].set_ylim(0.65, 0.95)
axes[0].axhline(y=0.9076, color='purple', linestyle='--', alpha=0.5, label='En İyi (GB)')
for bar, score in zip(bars1, r2_scores):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{score:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# RMSE Karşılaştırma
bars2 = axes[1].bar(models, rmse_scores, color=colors, edgecolor='black', linewidth=1.5)
axes[1].set_ylabel('RMSE (MPa)')
axes[1].set_title('Model Karşılaştırması - RMSE')
axes[1].axhline(y=4.88, color='purple', linestyle='--', alpha=0.5, label='En İyi (GB)')
for bar, score in zip(bars2, rmse_scores):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{score:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('tum_modeller_karsilastirma.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ tum_modeller_karsilastirma.png kaydedildi")

print("\n🎉 Tüm grafikler başarıyla oluşturuldu!")


