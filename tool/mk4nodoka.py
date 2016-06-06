#!/usr/bin/python
# coding: utf8
import sys

if len(sys.argv) > 1:
    keymapname = sys.argv[1]
else:
    keymapname = 'tutcode'

NODOKAKEY = {
    ';': 'Semicolon', ',': 'Comma', '.': 'Period', '/': 'Slash', ' ': 'Space',
    '1': '_1', '2': '_2', '3': '_3', '4': '_4', '5': '_5',
    '6': '_6', '7': '_7', '8': '_8', '9': '_9', '0': '_0',
}

def main():
    keymaps = {}
    for line in sys.stdin:
        parseline(keymaps, line.rstrip("\n"))
    output(keymaps)

def parseline(keymaps, line):
    """'キーシーケンス\t漢字'形式の行を解析してkeymaps辞書に登録
    
    例: 'rlk\tぁ'
    入力ファイルはUTF-8
    """
    f = line.split('\t')
    seq = f[0]
    kanji = f[1]
    seqlen = len(seq)
    seqhead = seq[:-1]
    seqlast = seq[-1]
    addseq(keymaps, seqlen, seqhead, seqlast, kanji)
    # 1つ短いシーケンスも追加
    if seqlen > 1:
        addseq(keymaps, seqlen - 1, seqhead[:-1], seqhead[-1], '\t' + seqhead)

def addseq(keymaps, seqlen, seqhead, seqlast, kanji):
    if seqlen in keymaps:
        if seqhead in keymaps[seqlen]:
            keymaps[seqlen][seqhead][seqlast] = kanji
        else:
            keymaps[seqlen][seqhead] = {seqlast: kanji}
    else:
        keymaps[seqlen] = {seqhead: {seqlast: kanji}}

def output(keymaps):
    for seqlen in sorted(keymaps, reverse=True):
        for seqhead in sorted(keymaps[seqlen]):
            printkeymap(seqhead)
            for seqlast in sorted(keymaps[seqlen][seqhead]):
                nodokakey = mkkeyname(seqlast)
                kanji = keymaps[seqlen][seqhead][seqlast]
                if kanji[0] == '\t': # 他のkeymapへ
                    print "key {} = &Prefix({})".format(nodokakey, mkmapname(kanji[1:]))
                else:
                    print "key {} = &PostMessage(ToItself, 0x0102, {:#x}, 1) # {}".format(nodokakey, ord(kanji.decode('utf-8')), kanji)

def printkeymap(seq):
    if len(seq) == 0:
        print "\nkeymap {} : Global".format(keymapname)
    else:
        print "\nkeymap {}".format(mkmapname(seq))

def mkmapname(seq):
    return "{}-{}".format(keymapname, conv2nodokakey("-".join(seq)))

def mkkeyname(ch):
    key = conv2nodokakey(ch)
    if key.isupper():
        return 'S-K2-' + key
    else:
        return 'K2-' + key

def conv2nodokakey(str):
    for k, v in NODOKAKEY.iteritems():
        str = str.replace(k, v)
    return str

if __name__ == "__main__":
    main()
