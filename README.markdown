# 2つ目のキーボードを漢字直接入力専用にする

日本語入力のオン・オフのモード切り替えが面倒なので、
キーボードを2つ接続して、1つは日本語入力オフ時用、
もう1つは日本語入力オン時用として使う方法です。

キーボードを2つ接続して、1つは日本語入力(TUT-Code)用、
もう1つはそれ以外用として使う方法です。

[汎用キーバインディング変更ソフト「のどか」](http://www.appletkan.com/nodoka.htm)の
[複数キーボード対応](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_UnitID)
機能を使った試作です。(nodoka-4.28_sampleで試しました。)

日本語の送り付けは、[漢直Win](https://github.com/kanchoku/kw)同様に、PostMessage()でWM_CHARを送っています。
(IMEを使いたい場合は、SendInput()を使うと行けるかも?)

## 設定方法
TUT-Code用のtutcode.nodokaでは、キーボードK2を日本語入力用に使う形になっています。
K2の設定方法は
[のどかのドキュメント](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_UnitID)を参照してください。

[複数キーボード認識タイミングの変更設定](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_FakeUp)
をしないとK2モディファイヤが付かないようなので、~/dot.nodokaに以下を追加してください。

```
def option FakeUp = enable 20 84
```

(ただし、この設定をすると、Alt-Tabでウインドウ切り替えしようとしても、
すぐに表示が消えてしまって切り替えできなくなるようです。)

~/dot.nodokaに`include "tutcode.nodoka"`を追加。

```
include "tutcode.nodoka"
window MS-NotePad /:Notepad:Edit$/ : TUT-Code- # メモ帳で試す
```

## ファイルリスト
* tutcode.nodoka: dot.nodokaからのinclude用
* tut2.nodoka, tut3ty.nodoka, tut3gh.nodoka, tut3vm.nodoka, tut3bn.nodoka:
  tutcode.nodokaからincludeするファイル。
  (ファイルごとに別キーボードの追加がしやすいように別ファイル。)
* tool/: のどか用設定ファイル生成用スクリプト

## 課題
* キーボードを持ち替えるよりも、普通にモード切り替えの方が早い気もします。
* Alt-Tabでウインドウ切り替えしようとしても、
  すぐに表示が消えてしまって切り替えできない。

## 拡張案
* TUT-Codeの3打鍵のそれぞれのブロック用にキーボードを用意して、2打鍵化。
  ([ワイド版ストローク表の各ブロックに相当](http://www1.interq.or.jp/~deton/tutcode/#tuttable))
  ただし、そうすると、2打鍵用キーボード1個、3打鍵用キーボード4個、
  の5個の追加キーボードが必要。
* Try-Codeのような固定prefixキーによる3打鍵であれば、
  3打鍵用キーボードを1個追加すれば2打鍵化可能。

## 参考
* [複数キーボードを区別する方法 - applet@Hatena](http://d.hatena.ne.jp/applet_at_h/20100527/1274966606)。RawInput
* [「窓使いの憂鬱」を使って T-Code 入力してみる](http://homepage3.nifty.com/songs/tcode/mayu/)。クリップボード使用
* [Google 日本語入力キーボード ドラムセットバージョン](https://japan.googleblog.com/2010/04/google.html) (エイプリルフールネタですが)
