# sys_transformer

時系列データの変換と予測を行うためのTransformerモデルを実装したリポジトリです。本プロジェクトは、一つの株式の時系列データの予測に焦点を当てています。

## 特徴

- **柔軟なモデル設計**  
  自然言語処理（NLP）で一般的なTransformerアーキテクチャを時系列データ用あてはめました。非常に単純な実装がしてあります。
- **結果の可視化**
  Gradioを用いて様々なパラメータによる訓練後の予測結果を見ることができ、パラメータ調整がどのように推論に影響するかがわかります。
- **colab実装**
  ローカルにGPUがなくてもcolabで訓練しているためすぐに再学習ができます。
- **結果の比較**
  比較対象としてLSTMを実装してあります。こちらもTransformerと同様非常に単純な実装になっているため容易にカスタマイズが可能。
  


## 使用方法

以下の手順で `sys_transformer` を使用できます。

### 1. 環境のセットアップ

```bash
git clone https://github.com/2tsu/sys_transformer.git
cd sys_transformer
pip install -r requirements.txt
