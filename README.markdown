# 2つ目のキーボードを日本語入力専用にする

日本語入力のオン・オフのモード切り替えが面倒なので、
物理的にキーボードを2つ接続して、1つを日本語入力用、
もう1つをそれ以外用として使う方法を試作しました。

つまり、日本語入力のオン・オフを切り替えるかわりに、
物理的にキーボードを持ち替えます:

* 日本語を入力したい時は、日本語入力専用キーボードで打つ
* 英字を入力したい時は、それ以外(英字)用キーボードで打つ

(なお、2つ目のキーボードでなく、[テンキーを日本語入力に使う方法](https://github.com/deton/nodoka-multikbd4ja/tree/master/tenkey4ja)の試作もあります)。

利点:

* モードを意識しないでよくなる
* 日本語を入力しようとしてキーを打ち始めた後で、日本語入力オフだったことに気付いて打ち直す等が発生しなくなる

[汎用キーバインディング変更ソフト「のどか」](http://www.appletkan.com/nodoka.htm)の
[複数キーボード対応](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_UnitID)
機能を使った試作です。
([nodoka-4.28_sample](https://osdn.jp/projects/nodoka4/releases/63839)で試しました。)

普通のIME用と漢字直接入力用(TUT-Code,T-Code)の2種類の設定ファイルを作りました。

## 普通のIME用
日本語入力用キーボードを打ち始めた時にIMEをオンにし、
英字用キーボードを打ち始めた時にIMEをオフにします。

## 漢字直接入力用
日本語の送り付けは、[漢直Win](https://github.com/kanchoku/kw)同様に、
[PostMessage()](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#function_PostMessage)により、UnicodeのWM_CHARを送っています。

(IMEを使って変換したい場合は、
[SendInput()](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#function_SendText)や
[&SetImeString()](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#function_SetImeString)を使うと行けるかも?)

## セットアップ
IMEonK2.nodokaやtutcode.nodokaでは、
キーボードK2を日本語入力用に、キーボードK1を英字用に使う形になっています。
K1,K2の設定方法は
[のどかのドキュメント](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_UnitID)を参照してください。

[複数キーボード認識タイミングの変更設定](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#def_option_FakeUp)
をしないとK1やK2モディファイヤが付かないようなので、
[自分用の設定ファイルdot.nodoka](http://www.appletkan.com/nodoka-doc/MANUAL-ja.html#dotnodoka)に以下を追加してください。

```
def option FakeUp = enable 20 84
```

(ただし、この設定をすると、Alt-Tabでウインドウ切り替えしようとしても、
すぐに表示が消えてしまって切り替えできなくなるようです。Windows7)

dot.nodokaに`include "IMEonK2.nodoka"`を追加。

または、tutcode.nodokaの場合は、以下を追加。

```
include "tutcode.nodoka"
window MS-NotePad /:Notepad:Edit$/ : tutcode # メモ帳で試す
```

## ファイルリスト
* IMEonK2.nodoka: 普通のIME用
* tutcode.nodoka: TUT-Code。dot.nodokaからのinclude用
* tut2.nodoka, tut3ty.nodoka, tut3gh.nodoka, tut3vm.nodoka, tut3bn.nodoka:
  tutcode.nodokaからincludeするファイル。
  (下記拡張案のブロックごとのキーボード追加をしやすいようにファイルを分割)
* tcode.nodoka: T-Code
* tool/
	* mk4nodoka.py: 漢字直接入力用設定ファイル生成用スクリプト(Python2用)
	* Makefile: TUT-Code用nodokaファイル生成用Makefile
	* split.awk: tut3??.nodokaファイル等に分割するためのスクリプト
	* tutcode.2, tutcode.3: TUT-Code表
	* tcode: T-Code表

## 課題、制限
* キーボードを持ち替えるよりも、普通にモード切り替えの方が早い気もします。
* Alt-Tabでウインドウ切り替えしようとしても、
  すぐに表示が消えてしまって切り替えできないようです。
* 漢字直接入力での部首合成変換、交ぜ書き変換未対応

## 拡張案
* 1打鍵かな用キーボード、1打鍵カタカナ用キーボード、2打鍵以上漢字直接入力用キーボード、1打鍵英字キーボードの、合計4個のキーボードを使う
* TUT-Codeの3打鍵のそれぞれのブロック用にキーボードを用意して、2打鍵化。
  ([ワイド版ストローク表の各ブロックに相当](http://www1.interq.or.jp/~deton/tutcode/#tuttable))
  ただし、そうすると、2打鍵用キーボード1個、3打鍵用キーボード4個、
  の5個の追加キーボードが必要。
* Try-Codeのような固定prefixキーによる3打鍵であれば、
  3打鍵用キーボードを1個追加すれば2打鍵化可能。

## 参考
* [テンキーを日本語入力専用にする](https://github.com/deton/nodoka-multikbd4ja/tree/master/tenkey4ja)。
  2つキーボードをつながないで、テンキーを日本語入力に使用
* [複数キーボードを区別する方法 - applet@Hatena](http://d.hatena.ne.jp/applet_at_h/20100527/1274966606)。RawInput
* [「窓使いの憂鬱」を使って T-Code 入力してみる](http://homepage3.nifty.com/songs/tcode/mayu/)。クリップボード使用
* [Google 日本語入力キーボード ドラムセットバージョン](https://japan.googleblog.com/2010/04/google.html) (エイプリルフールネタですが)
