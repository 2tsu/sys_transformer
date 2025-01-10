# sys_transformer

時系列データの変換と予測を行うためのTransformerモデルを実装したリポジトリです。本プロジェクトは、特に金融データやIoTデータなど、複雑なパターンを持つ時系列データの予測に焦点を当てています。

## 特徴

- **柔軟なモデル設計**  
  自然言語処理（NLP）で一般的なTransformerアーキテクチャを時系列データ用に最適化。
- **高精度な予測**  
  過去のデータを学習し、未来の値を予測する能力を持つ。
- **モジュール構造**  
  カスタマイズ可能なコード設計により、さまざまなデータセットやユースケースに適応可能。
- **軽量で効率的**  
  PyTorchを使用し、GPU上での高速なトレーニングと推論をサポート。

## 使用方法

以下の手順で `sys_transformer` を使用できます。

### 1. 環境のセットアップ

```bash
git clone https://github.com/2tsu/sys_transformer.git
cd sys_transformer
pip install -r requirements.txt
