# Making Memberlist with images

画像つきの名簿を簡単に作るためのツール

## Requirement

-   Python3.x.x

## Usage

### 事前準備

-   Google Formなどを利用して，名簿化したい対象の情報を取得し，csvとして保存する．
    -   今回は，以下のフォーマットで保存するものとする

```csv
学籍番号,氏名,ふりがな,所属局
xx-xxxx,XXXXXX,XXXXXX,制作局
xx-xxxx,XXXXXX,XXXXXX,広報局
xx-xxxx,XXXXXX,XXXXXX,技術局
```

-   名簿化したい対象の画像を適切なサイズ（今回は2:3）にトリミングして，ファイル名を学籍番号(xx-xxxx)にする．
-   すべての画像を一つのディレクトリに保存する．

### 利用準備

-   メンバーリストをcsv形式で保存する

```bash
cp path/to/your/membe_list.csv data/csv/member_list.csv
```

-   名簿の画像ファイルを保存する

```bash
cp path/to/your/images/* data/images/
```

### 書き出し

```bash
python mklist.py
```

### 名簿の保存

-   ローカルhttpサーバを起動

```bash
python -m http.server
```

-   ページの表示
    -   google chrome で <http://0.0.0.0:8000> にアクセス
-   ページの印刷
    -   chromeの印刷機能でPDFに印刷
    -   詳細設定より，余白：なし にする
    -   画像が収まるサイズに倍率を変更する


## Install
```bash
git clone git@github.com:XapiMa/make-member-list.git
mkdir data/ data/csv/ data/images/
```

## Author

[XapiMa](https://github.com/XapiMa)
