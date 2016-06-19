# テンキーを日本語入力専用にする

日本語入力のオン・オフのモード切り替え不要にするため、
テンキーは日本語入力専用に使い、それ以外は英字用に使うための設定です。

* 日本語を入力したい時は、テンキーで打つ
* 英字を入力したい時は、テンキー以外で打つ


[汎用キーバインディング変更ソフト「のどか」](http://www.appletkan.com/nodoka.htm)
を使った試作です。
([nodoka-4.28_sample](https://osdn.jp/projects/nodoka4/releases/63839)で試しました。)

テンキーを打ち始めた時にIMEをオンにして、
ローマ字入力キーを送り付けたり、
かな文字列を
[&SendText()](http://www.appletkan.com/nodoka-doc/CUSTOMIZE-ja.html#function_SendText)
で送り付けたりしています。
(その他の方法として、IMEをオンにするだけにして、
後はIMEのローマ字テーブルをカスタマイズする方法もあると思います)

また、テンキー以外を打ち始めた時にIMEをオフにします。

## 片手入力方式4種類
* choi10key.nodoka: 片手チョイ入力
* twotouch.nodoka: [2タッチ入力、ポケベル打ち](https://ja.wikipedia.org/wiki/2%E3%82%BF%E3%83%83%E3%83%81%E5%85%A5%E5%8A%9B)
* cutkey.nodoka: [CUT Key](http://www.cutkey.jp)
* ksiki.nodoka: [K式入力](http://www.d-tech.jp)

## 参考
* [片手入力キーボード](http://www.jiten.com/dicmi/docs/k6/15094s.htm)
* [[PDF]CUT Key、小野式キー配列等](http://www.pitecan.com/UnixMagazine/PDF/if9902.pdf)
* [TouchMeKey等](http://www.pitecan.com/articles/HIS/InputSurvey/inputsurvey.html)
* [[PDF]片手かな文字入力方式Kie12](http://www.interaction-ipsj.org/archives/paper2005/pdf2005/interactive/B213.pdf)
* [2つ目のキーボードを日本語入力専用にする](https://github.com/deton/nodoka-multikbd4ja)
