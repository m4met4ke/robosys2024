# robosys2024
ロボットシステム学授業用
# equalコマンド
[![test](https://github.com/m4met4ke/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/m4met4ke/robosys2024/actions/workflows/test.yml)
## 概要
標準入力から読み込んだ値４つと演算子３つを基に計算結果がゼロとなる式を作る.  
演算子は['+', '-', '*', '/']の4種類であり，同じ式の中で複数回使用することも可能.  
膨大な組み合わせを試す作業を手動で行うのは不可能に近いが，このコマンドであれば短時間で解を見つけることが可能.  
手作業では見落とすような式を発見したり，解がないことを即座に判断することで無駄な試行錯誤を省くことができる.  
仕様を変更して数字の数や利用できる演算子を増減させることも容易にできる.  
"結果が10になる式を探す"などに変更することも可能.  
数学的なパズルとして数学的思考を深めることができる.
## 実行手順
1. リポジトリをクローン:
   ```sh
   git clone https://github.com/m4met4ke/robosys2024.git
2. 移動:  
   ```sh
   cd robosys2024
3. 実行:  
   ```sh
   python3 equal.py <使用する数字４つ>
## 実行例
1. 通常:  
   ```sh
   python3 equal.py 1 3 5 10  
   [1 - 3 + 10 / 5 = 0]  [1 + 10 / 5 - 3 = 0]  [3 - 1 - 10 / 5 = 0]  [3 - 10 / 5 - 1 = 0]  [10 / 5 + 1 - 3 = 0]  [10 / 5 - 3 + 1 = 0]
2. 数字の過不足:  
   ```sh
   python3 equal.py 1 3 5  
   エラー: 四つの数字を入力してください  
   例: python3 equal.py 1 2 3 4  
3. 解なし:  
   ```sh
   python3 equal.py 8 3 3 6  
   等式は見つかりませんでした
## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10
## テスト環境
- Ubuntu 20.04 LTS
## LICENSE
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージは，3条項BSDライセンスの下，ryuichiueda/emcl由来のコード（© 2024 Ryuichi Ueda）を利用しています．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2024 Karen Otake
