# 回歸模型練習

## 介紹

回歸分析為監督式學習的一種，通常用於預測一種連續變量的值。回歸分析的目標是找到自變數和因變數之間的關係，便可以預測因變數的值。

- 回歸問題可以分為:

  - 線性回歸問題:
    - 在線性回歸問題中，自變數和因變數的關係為線性的。<br>
    - 線性回歸通常用於預測數值變量，例如房價、股票價個等等的。<br>
    - 線性回歸的目的是找到一條最佳的線性回歸線，找到最佳的擬合數據點。
  - 非線性回歸問題

- 回歸模型演算法介紹
  - 線性回歸(Linear Regression)
  - 多項式回歸(Polynomail Regression)
  - 決策樹回歸(DecisionTree Regressor)
  - 隨機森林回歸(Random Forest Regressor)
  - 支持項量回歸(Support Vectir Regression)

### 線性回歸(Linear Regression)

- 線性回歸是一種用於建立和分析數據之間關係的統計方法。
- 通常用於建立一個自變數(x)和一個因變數(y)之間的線性關係。
- 可以通過一條直線(稱為線性回歸線)來描述這種關係。

- 線性回歸的目標:

  - 找到一條最佳的線形回歸線，使其最佳地擬合數據點。

- 實際應用:
  - 當給定一個自變數時，現行回歸可以預測出相對應的因變數值。

![image](https://github.com/kaiser7410/ML-DL/blob/main/img/%E7%B7%9A%E6%80%A7.png)

### 多項式回歸(Polynomial Regression)

多項式回歸是一種在回歸分析中使用的線性回歸模型，其中自變數的冪被用作回歸線的項。<br>
他可以用於擬合非線性數據，通常用於預測數值型變量，例如房價、股票價格等等。

多項式回歸通過添加二次、三次或更高次方的向來擬合數據點，從而實現曲線擬合。

- 注意:
  - 使用多項式回歸模型十，需選擇適當的多項次次數(即最高多項是次數)。
  - 次數太低，模型可能無法捕捉到數據中的所有關係;次數太高，模型可能會出現過度擬合數據。

使用多項式回歸模型時，需要在多項式次數和模型性能之間進行權衡，已找到最佳的模型。

![image](https://github.com/kaiser7410/ML-DL/blob/main/img/%E5%A4%9A%E9%A0%85%E5%BC%8F.png)

### 決策樹回歸(Decision Tree Regressor)

決策樹回歸中，每一個內部節點都代表一個特徵，每一個葉節點都代表一個預測值。<br>
建立決策樹時，分裂節點時的目標是最小化平方誤差，即實際值和預測值之間的差異平方和。<br>
這使決策樹回歸非常適合處理非線性數據。

- 決策樹的優勢
  - 可以自然地處理這種數據類型，例如數值型、類別型和二進制型。
  - 可以捕捉不同特徵之間的交互作用，使它在複雜數據地建模非常有用。

![image](https://github.com/kaiser7410/ML-DL/blob/main/img/%E6%B1%BA%E7%AD%96%E6%A8%B9.png)

### 隨機森林回歸(Random Forest Regressor)

隨機森林回歸是一種集成式學習算法，結合了多個決策樹回歸模型，通過投票方式進行預測。<br>
與單獨的決策樹回歸模型相比，隨機森林回歸模型可以更好的避免過擬合的問題，提高模型泛化能力。

隨機森林的建模過程與決策樹類似，但是它使用了一個隨機的樣本和特徵子集來建構每個決策樹回歸模型。<br>
這種隨機性可以減少模型的方差，改善模型的泛化能力。

隨機森林還可以計算特徵的重要性，這對於特徵選擇和解釋能力非常有用。

![image](https://github.com/kaiser7410/ML-DL/blob/main/img/%E9%9A%A8%E6%A9%9F%E6%A3%AE%E6%9E%97.png)

### 支持向量回歸(Support Vector Regression)

支持向量是一種回歸分析法，使用支持向量機(Support Vector Machine)進行建模。<br>
在支持向量回歸模型中，模型的目標是找到一個最佳的超平面，使得這個超平面最大化在所有訓練樣本上的變季(margin)。<br>
通過引入核技巧(kernel trick)，支持向量回歸可以處理非線性數據，並解具有很強的泛化能力。

- 支持向量的優點
  - 可以處理高為數據，具有很好的魯棒性，並且在非線性數據建模中表現出色。
- 支持向量的缺點
  - 對參數的選擇非常敏感，需要進行複雜的參數調整過程。

![image](https://github.com/kaiser7410/ML-DL/blob/main/img/%E6%94%AF%E6%8C%81%E5%90%91%E9%87%8F.png)

## 練習

練習題目都是 Kaggle 上的 DataSet

- Insurance Claim Analysis: Demographic and Health<br>
  https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health?select=insurance_data.csv

- SECOND HAND CARS DATA SET | REGRESSION<br>
  https://www.kaggle.com/datasets/mayankpatel14/second-hand-used-cars-data-set-linear-regression
