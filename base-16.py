# coding=UTF-8
# coded by Tegar Sabila
# 
import base64
# kode warna
m = "\033[31;1m"
k = "\033[32;1m"
h = "\033[36;1m"
b = "\033[34;1m"
p = "\033[37;1m"
n = "\033[00;1m"
logo = """{}
{} ╭━━╮            ╭╮╭━━━╮
 ┃╭╮┃           ╭╯┃┃╭━━╯
 ┃╰╯╰┳━━┳━━┳━━╮ ╰╮┃┃╰━━╮
{} ┃╭━╮┃╭╮┃━━┫┃━╋━━┫┃┃╭━╮┃
 ┃╰━╯┃╭╮┣━━┃┃━╋━┳╯╰┫╰━╯┃
 ╰━━━┻╯╰┻━━┻━━╯ ╰━━┻━━━╯
{}╭══════•›{}ꪶ ཻུ۪۪ꦽꦼ̷⸙ {}━  ━ {}ꪶ ཻུ۪۪ꦽꦼ̷⸙{}═══════╮
|                           |
|  {}Program Enkripsi Base16  {}|
|  {}Author {}: {}Tegar Sabila    {}|
|  {}Github {}: {}kelas-kode      {}|
|                           |
╰════════{}ꪶ ཻུ۪۪ꦽꦼ̷⸙ {}━  ━ {}ꪶ ཻུ۪۪ꦽꦼ̷⸙{}═══════╯{}
""".format(n, m, p, b, h, p, h, b, k, b, h, p, h, b , h, p, h, b, h, p, h, b, n)
class Enkrip:
    def __init__(self, file, output):
        self.file = file
        self.output = output
    def enkrip(self):
        try:
            file_ = file
            output_ = output
            bukaFile = open(file_).read()
            enk = base64.b16encode(bukaFile)
            wm = "#Encrypt by Tegar Sabila\n#Github : Https://github.com/kelas-kode\nimport base64\nexec(base64.b16decode('" + enk + "'))"
            ubah = file_.replace(file_, output_)
            simpan = open(ubah, 'w')
            simpan.write(wm)
            simpan.close()
            print "{}[{}✔{}]{} Hasil {}: {} {}".format(p, h, p, b, h, p, ubah)
        except:
            print "{}[{}!{}] {}File tidak ditemukan".format(p, m, p, m)

if __name__=="__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print logo
    file = raw_input("{}[{}*{}]{} File {}: {}".format(p, h, p, h, b, p))
    output = raw_input("{}[{}*{}]{} Output {}: {}".format(p, h, p, h, b, p))
    Enkrip(file, output).enkrip()
