# robosys2024
ロボットシステム学授業用
# find_zero_equationsコマンド
[![test](https://github.com/m4met4ke/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/m4met4ke/robosys2024/actions/workflows/test.yml)
## 概要
標準入力から読み込んだ値４つと演算子３つを基に計算結果がゼロとなる式を作る.演算子は['+', '-', '*', '/']の4種類であり，同じ式の中で複数回使用することも可能.膨大な組み合わせを試す作業を手動で行うのは不可能に近いが，このコマンドであれば短時間で解を見つけることが可能.手作業では見落とすような式を発見したり，解がないことを即座に判断することで無駄な試行錯誤を省くことができる.仕様を変更して数字の数や利用できる演算子を増減させることも容易にできる."結果が10になる式を探す"などに変更することも可能.数学的なパズルとして数学的思考を深めることができる.
## 実行手順
1. リポジトリをクローン:
   ```sh
   git clone https://github.com/m4met4ke/robosys2024.git
2. 移動:  
   ```sh
   cd robosys2024
3. 実行:  
   ```sh
   echo 使用する数字４つ | ./find_zero_equations.py
   ```
   使用する数字に+-を付けることも可能
## 実行例  
```sh
echo 1 3 5 10 | ./find_zero_equations.py  
```
[1 - 3 + 10 / 5 = 0]  [1 + 10 / 5 - 3 = 0]  [3 - 1 - 10 / 5 = 0]  [3 - 10 / 5 - 1 = 0]  [10 / 5 + 1 - 3 = 0]  [10 / 5 - 3 + 1 = 0]
## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10
## テスト環境
- Ubuntu-latest\ubuntu-22.04.5LTS
## LICENSE
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージは，3条項BSDライセンスの下，ryuichiueda/emcl由来のコード（© 2024 Ryuichi Ueda）を利用しています．
- このパッケージのfind_zero_equations，test.bash以外のコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
- © 2024 Karen Otake
## 参考資料
- 書籍
 - 新しいLinuxの教科書 / 三宅英明, 大角祐介著. -- SBクリエイテ イブ，2015.6.
 - Python1年生: 体験してわかる! 会話でまなべる! プログラミングのしくみ / 森巧尚著 -- 第2版. -- 翔泳社， 2022.8. -- (1年生).
- ウェブサイト
 - [Python Tips: 標準入力がどのように渡されているのかをチェックしたい](https://www.lifewithpython.com/2017/06/python-check-stdin-type.html)
 - [【Linux】標準入力、標準出力、標準エラーとは？それぞれについて解説](https://engineer-ninaritai.com/linux-stdin-stdout/#i-5)
 - [標準入力・標準出力ってなに?](https://qiita.com/angel_p_57/items/03582181e9f7a69f8168)
 - [Python3のitertoolsモジュールをまとめてみました!](https://qiita.com/edad811/items/0d28e6595a3c338567ec)
 - [［解決！Python］順列や組み合わせを取り出したり、総数を計算したりするには](https://atmarkit.itmedia.co.jp/ait/articles/2112/14/news025.html)
 - [プロンプトエンジニアリングの教科書(特典) > ch4/24-game](https://kujirahand.com/book/prompt/index.php?ch4%2F24-game&show)
 - [GitHub – READMEの作成方法と書き方【改行やリンク・画像の入れ方】](https://howpon.com/8334#i)
 - [式と演算子](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Expressions_and_operators)
 - [組み込み関数](https://docs.python.org/ja/3/library/functions.html)
 - [【Python】def文とは？コード例付きでわかりやすく解説！（初心者向け）](https://torus07.hatenablog.com/entry/python-26)
