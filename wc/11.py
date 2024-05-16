# 项目：hook_wc.py
# 时间：2024-05-16 13:20:47
# 运行环境：python3.9.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.9":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.9.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(gzip.decompress(b'\x1f\x8b\x08\x00\xaf\x97Ef\x02\xff\x01\x0e\x1c\xf1\xe3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00sH\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x00d\x01l\x05Z\x05e\x06e\x00\xa0\x07e\x02\xa0\x08d\x02\xa1\x01\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Ns+\x1b\x00\x00\x1f\x8b\x08\x00\xaf\x97Ef\x02\xff\xad[mp\x14\xc7\x99\xde\xf9\xd8\xd9\xdd\xd1J\x08!0`\x8c7\xb6\xb1-\xb0$0\x080\xd8N\x84\x10 0\xe2C``mg3\xda\x1eI+\xf6K\xbd\xb3\x12\xdaZ\x1c\x08`\x83\r\x01\x1c\x7f\x03F\xb2\r\xb1\x1d\xc7\x90\xc4wv\x0c\xb6\xaf\xae\xee\xc7\xfd\xba_wUWS\xf7\xe3*\xf1.\xa8\xea\xaa\x9c\xaa+\xff\xe1.\x97{\xdf\xb7gV\xbb+A9u\'\xa1\xee\x99\x9e\x9e\x9e\x99~\x9f~\xde\xe7\xedn\xa2\x9e\xaa\x1f\x1f\xfc\xfd\x08\xfe2u\x92\xc7\xc3<a\x0f\x93\x98\x1c\x97\xc2\x12\xe5rX\xa6\\\t+\x94\xaba\x95ro\xd8K\xb9\x16\xd6(\xf7\x85}\x94\xfb\xc3~\xc8\x95x \x11\x08\x07$lK\x8d\xeb\x89\x9ap\r\x1d{\xe3\xc1Dm\xb8V\x12\xcf\xa8\x0b\xd7A\xae\xc5g$\xea\xc3\xf5T\xe6\x8b\xcfL4\x84\x1b\xe0x\x01\x0b0\xfd\xa8\x14\x9e\xc5\xeea5,\x08G\x8dl!\xabeup4{\xa3\x87\xcd`\xf5G=\xac\xfe\x88\x1c\x9e\xc3f\xb2\x86\xa3\x9e\xf0]\xe6\\6k\xbf|F\xe2:k\x0c\xcf3g\xb3\xd9\xe6<\xe6?\xa2\x84\xe7\xb39cw\xb3\xbb\xd8\xdc\xa3\x1es\x819\x9f\xcdc\xf3O\xc9\xeb=G\xa4q)|\x8fy\x0f\xdea.dw\x9f\x83\x12\xc9c.4\xef\xc1\x9c\xc9=\x9e\xa6{\xb3c\xd03z\x94\xa7\x92kBKC\x8f\x85\x16\xe3\xaf\x9e4GB\x9d\xc9\xe1\x87\x1f2\xd2\xe9H\xf1\xfc\xb9\xe2\x97\x9f<\xd4\xb4V_\x1c*\x9c>5q\xf9\xf8\x8d\xaf\xde\xff\xf6\xfa\xdb\x03\x96\x95\xce\xacim\xb5Z\x12f\xeb\xf0@*\xb5?2\x92J\xc5\xf5\xc2\xe97\'^<\r\x15\n\xef\xbf\xfd\xcd\xe7\x1f\xdd\xfc\xf4r\xe1\xf4g7^\xfd\xa0x\xea\xdd\x9b\xe3\'u\xf3@:\xc5\xad\x90\xa8\x1f}\xe2\xbe\xe2\x89\x97\x8b\xe7\xbf\x80*\x0f\x16\xae\xbcpc\xec\xb0^*\xb8_\x14\xdc\xa7O\xa0\x19\xbb\x9b$\xdb\xcf\x0c\xcb\xb4b\t\x13\x8e\x03\x1d\xd0B\xcc\xdclp\xbc\x90\xe5\xf1\xb4\xc13xA\xdf\xbe\xa5\xa3gYdxY\xa4\r\xce\x94\x9d=\xed7\x04\x10\xfe\xf4\xc3\xa8\\\x86\x8b \xfc\xf9\xe1\xaf\x03\xb1\xf11`\xc3\xf2\x8c\x01&\xc6\xa5\x83r^\x1e\x94\x99L}\xfdA\xae\xdeR\xc6T(\xf1\x8eC\xaf\xed\xf1$\xe7\xa8\x1eK\x19\xd4F\x1f\x97<\xf8\xbb\x0f0\xd5\xe3Y\xea\xc9\xcbc\xca8\xb4\x90\xf7\xc4<\xe3\xf2A%\xaf\xe0\xdd\x96\x8f)\xe7<L\xc5\xf4\x82\x82\xfd\x9eW\x98w\x9e\xe7\xa0\n\xb9\x06\xb9\x17r\x1f\xe4\x1a\xe4~\xc8}\x90\x07 \xf7C\xaeC\x1e\x80\xbc\x06r=\xef\xcb\xfc\x1b\x0b\xe65hG>X\x93\xafa\xb5\xf9\x00\x1e\xaf\xf2\xd0Y]\xd9sT,\xb3|\xf9\x1a|\x9e\xe5?\x02o\x99\x97\xf2\xea~\x0f\xbc\xd1O\xd8\x0c\xaa_\x9f\x97\xa0\xfe\xcc\xbc\ni\xc3\x05\xaf\xd3\xca\xac\xbc\xbf\xac\xcd\xc6\xbc\xb7\xeclv\xd9\xf3th\xe9I(\x9b\x93\xd7\xbf\xff;\xb0\xbb\xf0\x99\xd3\xbc=\xb6v\x12\xca\xe6~\xbf\xd6\xb0\xbf\x9b\xe6u\xe7\x96\xbb\x08\xec\x8fYq\xa3\xb7%\x9aJ\xb4\xf6e\x93\xa3\x08\xad\xd6a\x93\xb76\xb7rc\xa45a\xc4\x92x\xda2\x98I%\'\xfe\x11\xac\x9dk\\<\xcdOV\x83K\x85c\x1f\x17\xce\xbed+P\xdfV\xe2\xa9\xfe\xb0b\xc5\xd2\xb6\x9aJ\x9bI[E\xf4\xd9\xb2\xd5\x1f\x0e\xc4\x92\xc31\xcb\xdc\xcd\xe3\xd9\x19p\xd3\x1f\x0f\x9d)\x9e>s\xe3\xfd/\xfex\xe8,\xe0>[\x8fc\n\n\xc5h\x11\x85\xb6\xa4g\x7f\x0c\xe5\x8b\xab*\xff\xe9\xe2\xab\xaf\xba\x7f\x85\xd3go\xfc\xfcj\xf1\xf5\xab7N\x1c/\x9e\xff\xf8\xdb\xeb\'\'\x0e\x7f]8v\xaap\xf50\x0c\x078\xbdy\xe5\xb3\xe2\xb9O\xa1\xc2\xcd\x17\x7fW<\x7f\xa8\xac\xe6a\xf1/{7>\x1a\x9f!.\x88g\xc0A\xe1\xfc\xd5o\xaf\x1f\x7f:[\x07\xd7\xbf\xbd~"\xf4\xcd\x17go\xfc\xea\n\x15)\xa2(;\xd3\xbd\xb5\xf8\xc6\xa5\xe2\xf9\x8b\xce\xb7\x94\x97\x16\xbe~\xa3\xba\xb4\xfc\x13\xcbJ\x8f]*\x9c~\xaf\xac7\xaa^\xe8\xe9\xc9.*\xab\xd9\x14\xb0\xfd\xdc\x1c\xca\x9a\x19+c+\xfd\xa6e\xd7d,\xc3\xcaf"\xd1\x143m\x15\xedg{\xe3)\x83el\xd52\x0fX\xf6\x8c\xcd=\xdb\xba\xd7\x9bx\xb9\x93\xf3\x14\xb7\xbdi\x1eKZ\xb6j\x1e\x88YMA[M\x1a\t3\x1c\x88\xa7\xa2F<B&\xe5f&\xac\xc1\xd1N\xc8\xbd\x1c\xcb0CCC\x06\xa6\x0ek<\x82\xc6\xc6\x1c\xcd\x1dV\xa1\xb8?\\\xc3#%\x93\xdb\xbeh*i\x99I\xebC\x0f\x9f\x0f\x9fqK\xdf>\xda\xbc!\x9b\x89":j\xa2\x03ft\x7f$\x1aOe\x19^\xcct#\xd5H\xba\x1c\x94d\xa9^\xaa\x93\xfc\x90jR\x03\xe4\xe5\xbf\xaa\xa4\xc3\xb5F8\xd2\xe0H\x95\xe6\xc0\x19\xfeje\xa5\xee\x19_\x00-F\x952&\xf3bg\xbaL\xf6\x0f\x1ed\xb2<\xf0\xd1\x11\x19F\x9e4&#\xa7\xc1\x11\xb2\x98\x07\xd8\r\x98\x89\xbf\x9b[oy\xc7\x80s\xc6|Lf\xca\xb8\x0c\xb9\xca\xbc\x94kN\xee\xc3\x1c\xeb[~\xe6\xb7\x80\x87\x8e c\x04\\\x16\xdb\x03\xa3\x10\x98P\x1f}G\x026\x93<\xb9\x10\xd4\xd3\xf3\x1e\xa8S\x83\xacrA=B|\x89\xfcxP}^\x1d\xfa;\x91/\x05\xaeL.\x84\xbaA\xaa[\x8b)\xf1\x82\x97\x98\xa2\x86\x98\x02Gx]\xf7\x84\x84\xdd+=tK\xba\x8f\xd7\xc2\xa1\xed\xb1\xa5\xd0-)\xf0\xdd]\xf8\xc1\xcd\xa5\x9f\xc2\xb1\xdf\xdc\xfc\xf9g\x85\xd3\xaf\x17\x8e_\xfd\xae\x11\xae\x95\xdc\xced\x1d\xfd;\x84\x1c\x0e\xa0\xf7\x0e\x15/^\x12N\xea\x99\xef\xe6A\xe1s\x85\xd3?+\xbev\xb5\xf8\xe6\x95\xc2\x99\xcb\x85\xf1_\x15^x\xab\xf8\xeb\xf7n\x8c\x7f\x92E\x0b\xde\x1f*\x9e\xff\xa8x\xe2+h{\xe2\xc2+\x13_\xbd%n\x05\xec~\xd7D\xc8>\xeb\x0c\xcc\x93\'n\x1c\xfb\xe57\x9f\xbf\\|\xfd\xf7\xc5\xb1\xeb\x85\xeb\xa7\'\x8e\x9d\xba\xf1\xe5\'\xae\xc3k\n\x92\xe1\x00\xb9\xe0\xbflo&n\x9ai[Nel\r\x90n&\x879\x8e\x1e\xde\x80U|\xdcL\xc7\x8d\xa8\xc9g\xe3\x99\x12\x07\xee\tt\x1e\x88\x9ai+\x96J\xf29P\xf8\xa1\xd7V\xf6\x9b\xa3\xd8X:\xc3\xd1\x8b\x85}\xd0F$cq[2\t\x96"A>\xa0\'\x80;\xefDx,\x10x\xa4_\x150\xa9J\xf7\xfdE\x95\x1b\t[\x8f\xc8s%\xbe\xfc\x8e\xe8z\xff\xfb\xa0\xebg\xb9\x07\x00Y^&\xd0\xa31\x05\x98[\xa0G\xadB\x8f\x7f\xf4\xf9\x12z\x00w\x84\x08mZ\xf4\x8cU\xa0Gc>\xaa\xeb\xafBO\xa0\x84\x9e@7\xbf\x07;\x00q\xc3\xef\xc7\xe4\x01L\x16a\xf2 $\xd9\xb9\x90\xdc\xce\xb2\xfc!\xb8\xd8\xa4\x93\xc1\xf8\xc3\x98\xa0\xa9\xf9bL\x96`\x8fz3\xe9x\xcc"\xfb\xf0fLZ0A\xcb\xf0\xd6R\xdfO\x1a\xa0V\x18`[_\'\x10\x07\x7f\x1a;rn\x95\x1dt\xa9\xcc\x06mh\x83j\x1d\xab\xb8:\xf62$\xa6\x07\xf4\xabGhW\xd0\x86\nS\x98\n9\x8ca\xa6A\xee\x85\xd1\xeb\x87\\#\x95\t\xe0 \x8d\xe9\x01\xed\x8a\n\xd3\x13\x0e\x08}\x19\xd6\x1dm\t\x9e\x9f5B\x1ed\xb3\xd9\x1c\xc8k\x85\x9a\x04\xfd\nZ\x12\xf2\x19\xecn\xb6\x00\xf2zP\xab\x0b!\x9f\xc9\xeee!\xc8\x1b\xd8\x0f\xd8}\x90\xcfbM\xec\x01\xb6\x88T\xec\x83\xec!(\x99\xcd\x1e\x06+,\xb6\xe5=\x1d\x15hR\x1cD\x11\x9a~Fh:\x02x\x8aH\xa0P<\x11\x19U\x14|\x13((8S\xe9Lv\xce\xbcL\x81T\xcb{\xc6|\xa0\xb3\xfc\xe3xW\xc0\xd2\xc7j\xe8\x08\xd8d08X;V\xc7\xa8\x0f\xce\xcb\x88J(\x93\xb0<2\x03\xf1\x12\xa9G\xbcDf\xb2\x00\xa4\r1\xbck\x16aE\xef\xe6w\xd1HK\x8f0{\xee\xca\x15\xacw\xb9\xc1\x96\xf7\xf6-k3V\xacxl\xe5\xb2\xb6e\x8f\xaeZ\xbd:wnk*\x17\x8b\xc7\x8d\xd6\xb6\x96\xa5\xa1\x87c\xdb\x07RIsm\xa8c\xfb\xee\x908\x0em\xeb\t-[\x19Y\x16y4\x14\x8f\xed7C[\x8d(\x16\xedm\n\xb5\xa7\xd3qs\x8f\xd9\xbb%f\xb5\xae\\\xda\xd6\xb2\xaceY[\xe8\xe1-\x9bvm}\xea\x11Qw#x\x8dTShk\xaa7\x167[\x97\xb5u.[\xb1z\xed\xda\x03\x99^\xfc\x8b\x8c\x18\xc9\xfe\xe8\x80\x91Z\xdb\xd6\xb2\xbce\xf9Zh.c\xa5\xb8\xb96iX\xb1a3\x02*=\xb7\xda\x15C\x07\x12V\x8be\xc4r\x03\xa9,*\xa2\x96h\xb2\x95\x9b\x06\x8b%\xfb\xdbG\x0c\xceZ\x7f\xd8o\xe4\xcc\x08\xba0\x9e\x8a?\xb1tY\x93\x9c\xd3wgL\xde\xdc\xde\x0f>-\xec\xdbi\xf6\x99\xdc\xe4\xc6\xfd@\xbe\xc4\x9c\xeb:7vu\x87\xb6\xef^\xf7TWGhK\xe7>A\xa7!\xf8\xd9\xda\xb5\xb1ok\xfb\xd2\x8d\x1d=C\x1b{\xbaz\x97\xaf\xdf\xd1\xb9\xae}\xc7\xee\xf6\xf6\x15\x1b\xbb\xdb\xd7w\xac\x8b\xed\xd8\xb2\xae\x7f\xc7\xfa\x95{\xb7\xad2\x1f\xdbg\xb6o\xcb,\x89n\x18\x1a1Vu\xee\xda\xbcd\xcf^j#\x96\xdb>\xb4\xc3\xdc;\xbcru\xacmxh\xe4\xb1\xf4\x86\x9d\x9d\x19>\x14[\xb7kg\xb4\x7f\xd5\xc8\xba\xa5;\xbb\xd2\xcb\xf9\xe6\xfd\xeb\xd3\x86\xf9\xf4\xe6\xa72\xe1\xa1}\x89\xb6]{Vm\xd8s\xa05\xb6-&\x1a\xd9\x10]\x92\xeb\xd8>ll\t\xf3X\xf4Q\xb6\xb7c\xe4\xd1U\x9d\xc3\xf1Mm|hIn\xa4k\xfb\xfa\xf6\xcd\x9b6\xb6\xf7%\x93\xcb\x92\x89\x1d\x9bV\x8d\xec\\\xbe\xbd\xc3\xb0:\xbbzW\xa7sm\x1b7\xc4\xa9\x91]\x9b\xb6\xc6\xe3\xd9\x91\x15\xe1}\x89\xe4\xb6\x91\xfe%\xd6\xc0H\xd7\xfa\xf6\x1d\xed\xeb\xe8*}ug\xf7\xfa\xea\x8e\x08\xcf\xda\x15\xdf\xb8aG\xfb\xb6xG\xd7\xd3\x07\x92[R\xe9\x1d\xc9=<\x84\xfc\xd1\xc81\xdc\x08\x07\xa2n\xa0b{cIf\x1e\xe0\xa8\x19\x05\xe2\xb4\xb4\x91\xc9\x00\xe8\x02\x193\x93\x01r\xefb\xb6\xce\x8d$K%vgc\xcc\xf6f\xd3iP-~f\x0e\xc7\xa2f\x17\xe3u\xe4\x1ezDe\xd0H)\xcb\xf6\r\x80uM\x0e~$\x9b&\x81\xea\x13\xcf\xcb\xd8u\xe9lo<\x16\x8d\x80\xa3 \xc7\xa0f\x8c\xb8e+\x89L\xbf\xed\x07\x9d\x943\xb7\x1a\xe9&\x05\x8a\xcdx\x1f\x7f\x8cZ6\xa2\xd1T\x16\x90Q\xc5_\xfe\x08\xc8\x9f\x98\x15\x89\xf4\xe3\xa8\r\x11u\xf9\x89\xae\x84(\xd1\xe1L\x96\xe4\xff\xf1\xab\xba\xa4i\x1a\x94\xe5j\xf6t\xb4\xb8wU\x84]\xb2\x13\x92\x13\x01\xdcG\x04\xc0p\x90\xa2{\x80a>(C\xae\x10\xa5k%\xb1\xafv\x938\xc7 \xf2\xf8g$X\x81\xa4\xa9\xc8Q\x8e\x8a\xa0\xe2\xc7\xdc\x8em\x92\xf9&<\xde0\x95\x8cy\x00\x92\xe7\xf1\xe1\xf4VRN\x837\x05\x01X\xf1\x92*\xfci\xeeK>\x05\t\xbc\x18\xf8\x19&=\x0e/\xd9\x0f\x11\xa2\x05|5&\x8fCD\xbd\xde\xf3\xdc\x1c\xf0z\xc0T\x96\n\x1c\xa6\xcc\xa3\xb8[\xf2\x0c-@\x85\xc5@a\xe5\x81\x8b\x90\xaf \r\x8c\x8b\xcf\xe1\xe8\x8b\t%\xb7\xe4\x07\x1f\x04O\xd3Ih\xc8\x80P0\x99\xad\x82\xc5\xc0\x9e0\xac\xcd$\xb3\x15\xb4\x9do\xc0\xc8\x0c\xc4c\xbd`>\xd6\x06R8\x15K\xda\x9a\x99$a\x1c\x180\x0f\xb0X?\xc8\xe6&\x95>\x9b"\x15#\\#\x9aC\x1dk\xd8\x12\x9bbTpJ\x91L\xac?y\x18?Rw\xfc\x91\x06\xfa\xb4Q\x98\xcf\xbd>%j\x0e\xb8=\xf3\x15$\x0cz\x83A\xbc\xcb\x94\x83\xaa\x85}\xa4b\x0f@\\\xeb\x1d\x94 \xaaE\x85\xe0\xa5\x88\xd8\x97\xf7\x01\x9bk\x96\x8a\xfd\x82=\x87<\x0e\xe5~*\xf7Y\xa01\xb1\x7f\x98\xbf\x11{P>\x18`\x811=\xaf\xe5\xe5\xbc\x1fz6p\x04"X\xc8A?\xf4k\xa0+t\xabf,\x98\xd7\xc7j\xa9_\xeb\xc61f\xf4\x8d\xcd\xc0\xda\x18Y\xe6!j\x84\x18R?OQ{\xde\x07\xef\xe5}\x1c\xadX?8\x13j\xf9\xc6]h\xd5t\xf3\xd5\xf0\x15\x13\xe8Ys\xfa\x86\x9d\x8b\xf9\x0fb\x99\xce\xb6=\xb6\x92\xe5q\xde\x8e\x16\n\xeem\xde\xd9\xb9cwg\xcf\xae\xe6\xae\xf5\xb7j\xf66\xef\xea\xda\n\'\xed[\xb7O\xdc\x04,\xf2-\x088o\x0e\xaa\xf5t\xf6\xf4tm\xeb\x86j<\x8c\xfd\xfc\x0c6\x8a7tv\xb7w\xe3\xddx\xd2\xd3\x05\xec\xb8k\xf7\xce\xce\xa6\x06\xae\x90\xb5\xd2\x865@\xa4\x00\x1e(\x95\xe6\xdb\xa80\x0b\x04\x10\xf6b\xba\x82?A\xd7 \xb2\x11bd\'&\xdb\x05b\x06\x8cG\xdbV\xf2\x1e,\xd9\x85\xc9:L\xf0c\xe8\xddAt" \xc2A\'\xae",\xf0\xb5DK :\x8d\xa4\x15\x81\xa7\xd4:\x87\x193\xcaM+\x1c\x80/\x8f\xa4\rne\xf8snCa\xddm\x01h)\x80\x12\x16B\xb3D\x1a\x04\x034\x18\xb1R\x11\xc4\'\xd0\x18\xc0\x05"6>E\x82\xea\x06c\x11\xc1T\xc7\x119\x0f\x12\xdcT\xfa\r\x02\xe8\x82\xd2\\\xf8]\x08\x81\x11\x8a!\x99\xca\xe5\xff\xf2\xfb\xfcR\xae\x16\xa08ywT*\x03\xa3V.M\xdf\xc6\xce\xeeC.\x19#\xc7?\x8e\xac\x02\xd0<\xaf\x1c\xc4#ePE^a\xea)\x19\'x\xc6\xbc\x00\x19\x10\xabc\x18\xeeH\x07\xd5\xbc\xca\xb4\xfd2\x0f\xa3\xbc\x10S28\x1d\x83S5\xe3\x12\x8aU(\xf7\xb3\x803\x05\xd4\x02\xd250\xfa*HW/H\xd79x-\xefL\x0f\x91`\xf5>\xefM\xea"G\xc1\xcat\x02Z\xec~\x90\x95M\n8\x84x\xcc\xa4\x9e\x07\x1eF\xfeOq\x16\x0e\xa6QBD\x92\xd9D\xaf\xc9sm\xae7\xc7\xeb\x18>\xb4X\x89\xech6Is\x1c#fok\xca\xc8Z\x03\xad`.\x06-\xc5 \xba\xc5\xf3\x0f%\xbe\x9b\xb0\x83\xb4\xc0\xb1\x83\xe8<\xdc\x80\x17S\xc0\xf8\x06\x06\x10\x14MgQ\xb0\xdex\xeb\xda\xc4[/\x14\xde\xff\xcd\xcdO/9A\xcc\x89\x97\x0b/}P\x1c\xfb\xbc\xf0\xc9;"\x82j\x15\x93p\xdf^?\xbc\xa1I\xb7!\xc8\x88\xf2\xd1\xb4\xc5\xd7\xb8LKX\x03\x08\xa7\x80\xa5(\x82!\x1c\xd7\xe4z\xad\x039\x8c\xabcI"\\\x12\xc8M\x9a\xa0\'_\xda\x18\xc50\x1e\xc3}\xf8\xbad\xc6\xb458\xca\xc6-\x8e\x0e\x86?:\x8d\x84\x9eQ\xf5\xad\x17&\x83\x19YF\xf9\xac\xfeY\xf3\xd6\x83\x1fB_4WF\xcf\x14\x92r\r\x80\x9d\xaa\x1b+\xd8\xcc_\x0e \x1b\x01t9O\xf3\xc28\xc7{^\x05f#5\x99\x97\x99\x0f\xce\x14\x82\x96\xe2*K\x00\x17^\xf1\x03\xa0\x00>8\xfb\x87\xac7\xa6"L\x00r\x12\xd3\x01P\xc7!\x1a\x06\xed\x9a\xf7\xb2 \xc0\xa9\x96f\xfa4V7\xcfCZVc3\xe8\xc8G\xf0\xaa\x17\x10b5\x0e\xdcf\xd2\x1c]\x03\xb59k\x1c]\xa2Z\x01\xc0\x7f\x06\x00\xfaJ\x00\xf4\x95\x01\xd0\xf7\xbc\x8f\x00\x089\x01\xb0\x11\x008\xbb\x9b\x1c\xce\xc4_\xe0\x07\x1cE?\xc51Vj?\xcelY\xa3i3\xec\xcf&\x11\x1e1\xc6\x07\xb1\xdbc\xd8\x1dK\\ \x0e\x837\xaa\xd6\x95F:\xd6J\x86n%C7\xa9\xb6\xdc\x07n)a\x02\xda\x18\xdf\x87\xd0S\xfbR<\xc1\xfb\xb0=2-v\xfa.\x81R\x9f\xa3yl\x19\x06\x82\xee(\x0fx:M\xa9\th\x16\x8f\x9f)\xbct\x11\xb0\x97k,\x03T\xa8\xcf\x00\x91\xccB\xcf\xdcR\x9e[\x13"\x1f\x0f\xd8\xe4\xac\xc4|\xf8\xe6\x93`\x0c{\x87\x8d8|\x14\xb2\x1e\x1fv\x15\x80\x00\xa4_\xc8\x04z\xb5\xfdD\xb2@s<\x8e\xa7\t\xe2M\xe7\x1d\x05oN\x83K\xea\xaa+\x88\x9e\x15%,\xd2\xef\x7fk\xbe\xd2\x91\xa6K.2\x91\xe9D\xd0\xa7\xc9!\x81\xd1:\xc0h\xd9\xd7U\xe0\xd3[\xaeC\x1e\xf5\x889j\xa45\x9c\xa5\x16\xf3\xd2\x14c;s9yGg\x08\xa5\x81\xa8\x04\xbbK\xdd\xd09^\xe2\xf0X\x02\xb9\x04\x05!_\x8f/\xaf\xd2\'\'\xcd\x11[\xeb52\xe6\xca\x15v\xa0w\xe5\n!+\xf8\x00\xd6\xe8!/\xc3h\x8a\xad\xc9+zk\x1eM7\xf0\x8c\x81\r\xd9Z4\x96\x1e0y\xb8\xc1\xa1\x06\x10\x1c.\xa9U\xf7\x15\xb6\xf8O\xf8%~\xea+\xe8\t\x08vs:|\xbfso\x05\xb9K\x8e\x0e\xebpG\xba\xe5\xb1$KF\xd5\xc5$\xd4\x08\xa0 \x141{E\x9a*\xae\x94\x14\xa6-/= 4\xb8j+\xa0\x8e\xf8O\xe83\x84\xb2\xe6\x8f\xe0\x04\x8a$\xbe\xa5\xea\r\x1f\x87\xe4_\xca\xb4!\xfa\x9eI=^\xf1z\x15\xa69\xe3JD\x11p\x02}\x94y\x1d\x19\xa8@\x11^g\xd0\xcbT \x85$\xf8\x1fM\xf8\x1f\xf40Tv\xd2Y\x10@O\x04\xde\x87\xff\x98<\x91\x8a^h\\*\xf7?\xe8M\x92\x0b\xe9\xbc\x06[\x04\x8a\x08B\x1ep\xe9\x81\xd5\xf6\xb8\x13h\xa0\x8b\xb3\xf8Y\x04\xfd\'q<\xaf\xbaC\x98\x98\xe6)\xd6\x8cc:\x8b\xe1 \x06\x8d0\xc2\xd3bl\x7f(a\xac\xc2\x8dD\x86\xfbJ#\x86\x9c\x8b\x964M\xb6/g+\xa3\xb9\x04M\xaa\xdc\xfc\xfa\\\xe1\xd8\xa5\xe2\xa7\xd7\xc0\x93|\xf3\xf9\xb5\x89\xf1\xbf\x11\xc3xW\xae\x01\x97\x93*\x870\x1fqF\xefp\xc5{\x8aqLqR\xbd;\x98m/<a4\'F\xef,\xd2\\\xc2\x86G0\xc11k\xcb|\x90^\xaa\xday\x04J\x0f\xfeW\xb4\xd6BB\t\x89\x0fr\x1a80\x834\x0f[\'\xe3\xc0\x9c/\xe5\x82(:\xdc\x9b*\x86\xa4Vn\xf7\x8f\xa6\x85%\xd8[>\x8f\xf6\xf6\x8c)b\x80\x82\xbdQ}(1\xc9q\x1e\xdeA\x8d\xc1\xe0e^\xe1<\x06}\xa4>\x8e\x83\x1b\xf1\x0b7B\nD#\xacx\xc6\x02\xccO\x96\r\x10\x0e\x02L\x87\xeb5\xf3<\xb8XB\xe5A\x07\x11\x01V\x8bm\x01"\xea \xd7K\x88\x08:\x88\x98\xd1\xcd\x9f\x15\xd1Q/\xf6\xcdQLp\x9eir)\xe5\xfb\xc1B\x18\x02go&\xd1\x90\xc5aU\xbcv\xb6p\xe1\x8d\x89\x8f@K\x1c\x9e8\xf4\xf6\xcd\xaf_|$t[<dgW\xdd\xe1*\x91\xb7\x05\xa7\xe7\xea\xe89\x95X\xf9\xb0\x86\xf41\x8dh\xa1\x86\xf7T\xca\xdeJ\xd0\x94\xa1E\x88\x0f\xf1\xd1GH\xb4\xa0Z\x15d\xff\xc24\\p\x0c\x92\xff\x98\x84K\x03\xc4\xb7\x9a\x8a\xd3\xf0.`@s\xe0\xc4)\xc2\xc5\x0fp\xa1\x97\x9dB\x11\xa5P\xf7$\xc5J\xc8\xdf\xe3\x1e\x88\x89\xe4q\xb1\x16F$\x01<\xee\xae;z\x99B@\x98$\x08\x88\xa7\x9c2 \x04\xe6\x154\x81\xf0\xa0\xf9Oq\x16 0\x90\xb1\x9d\x12}\x9e\x87"S\xa4\x13\x80J&M\x1a\x81j\x0c\xa5\t\x0c\xc1\xee\xbf\xd6\xec\xf1X\xc6j\xbd\xa5-\xda\xb7(\xb1\x88\x95Y\x1e\xbb\xfc\x9bk/\xe1\n\xd1g\xbf\xbdy\xe5\x1aZ\x90\xb8\xa1\x0e\xdaJ\xc7M\xf0\t\x1d\xe8\xdcoI\xad\x10\xcdf\x13\xe1\x99\x10\\\xc4\xa2q\xb3+\xb3\x13\xda}\n\x9a\rk1:n\npI8\xa5\xd4\x88\xed\x07M\xd9\x87\xb1\xc6m-k\xfbX*\x82\xef\xe6r\xc1>\x97\x0b\xc8\xa4\xb6\x1a\xb3\xcc\xc4\x146\xc0\x1b"\xf81\xe8c2\rD\xf5\x8ddP4\xeb\x83\xe4\xac\x89\x01J\x15\xa70@\xc9\xac\x7f\x8f\xcc\x0f\x92q^9\x0f\xc8\x82\x07@BNe\x01\xb5\x8a\x05\xbc\xc0\x02Z\x89\x05|`\xe8\xb12\x16\xc0\x18\x04\xcb\xf24\xba\x03(*\xc9\xf05\x17H\x86\x0e}UU\x1e\x84{@d\xa2\xc0t\x01\xe10\xc3\x0c\x87\x19\xea+\x98a\xa6\xc3\x0c\r\xdd\xc2S\x08z\x08\xfb\xc8@ \x9azK\x14\xb1\xfa\xfb`\xc5\x88c\x97\x8d:\xceC\x18\xb9\x9a\'\xd0\x8c\x13o\x1e\x03\x9c\x14_\x7f\xf1\xc6\xaf\xc6\xfex\xe8\x0c\xe8\xd0\x98\x157\x9d\xc5TZ\xb2$\x8a\xf8\xc3\xf9c\xd9\x86R\x99\xa0\x87?\\8\xe9\xe2\x8bh"W\xef@\xa0\xca\xa7P\x9c\xe9\x0e\xfa3%?q\xa2\x02 \xd5c\xfe4$5\x08\x8a\xf94\xe65\xa9\xa1j\xcc\xcf\x95\x1f\xc0\xf1\x8e\x9a\xc5yl\xc5\x88\xaf\x987\x1a\xfbkF\xfc\xf3\xa5\x11\x8f\xa3\\\x15\xc2\xc0%\xf8<4<\xe8g\x9a[\xca|\x17\x94U\xa0s"~\xb1k\x80Z8\xe0\x88\x89\xc0~P}%\x91\xe0\xbb\x8dH\xd0\x1d\xc3\xd7v\xe7\xd6\xfcU,\xd0L:\xbdU\xa4\xfc%\xd7\xb6d\xbb\xe2K_\x16.\xbd^\xfcx\xbc\xf8\xdaU\xd7Hd\xc0o\xbf<\xef\x10\xc4\xe9+\xa2\xd2w\xa8\xd6\xa0\xe6dX\xb0!7\x8b\xc6\x1b\xb5\\iL\xd0\x07\xd8\xcb\xfc\x14&?\xbf#\xd5o(\xf1\xbd:\x1d#L\x99\x97\x98|\xe4=h\xf79.\x19\xc8h\xefFi>\xd8<(\x13\xc7\xd7\xba\x84@\xb5oo\xf6\x17\xca\xb4 \xe8@apyP\xa9\xd0\x81*i>69\x0fQ\xd2\x81\x9b\xc1h\x1a\xd3\xc8H>\xf2\xf7\x1a\xd1|\xa0\xcc\xdf\xbb\xc6\xd5\xc8\xb8\xaac\\\xdf4\xc6\x85\xb1\x1cpB\xab.\x11\x02\xe5\x96\xba\xe6\xce\xf0\xe1\xe6i\xa2:+\xc7{\xc9\xdcB\xf9\xed\xe9\xa8\x1e\xc0w\x97,]8~\xa1\xf0\xcb\x97\x0b\'_/\x1f\xb1\xbb\xb2\x0b\xa7\xadP>|m_\x02\x02+\xa3\xdf\xdcpk&=%2\x12\xad2\xb9\xbfL\x12\xde\xd1\xb1\x7f\xa8V\xc9\xc0i\r\xedw\x1f\xd3<9\xbcA\xff\xc1\xf0\xae\x97\xa7\xb8\xf3\x1a1%L\xf5oo\xe8Wi|39&\x91\x89\xd1\xdce\x13L\x10\x04x\xc1\x9c\\\xec\x0b"\x13\xa3_\xc6\xb2\xbd`:\x10\xf9d*\x10\xf5G=b\xaf\x0f\xee\xd8\xa2u.\x11\xff\xab`T\x05\xc9\xbcd\xf6:\xc7\xec*\x90\xb9L\x13\xe5\xf5\x90k%\xb3\xd79f\x9f\xd9\x8d\xf1\xb4\x15\x1b\x8eY\xa3]l\x02_vrF\xe9NV7p\x85hw\xba\x9f\x1b\xcc$o_m\xfaI\xcb\n=W\xbcx\xe9\xe6\x95w\xcb\xad_\xd1]\xb2#\x820\x8a\xa4>\xc7E\xb7\xe7\x1ahr\xc43\xcf\xf1\x9b\xbf\x90\x870L\x95\x85\x03z\xc55[\x93l\xcb-Km%\xd5;8e\xd0>\xcebQ\x0b\xb5\xc5\x93]\xf0\xb8\xff\xc4G\xe5\x1eF\xc5^\xf6\xfe\xe4\xb7[\x1e\xa7\xbd\x1f\x99\'[&o!V\xda\x95\xfd\xc1\xed>\xa5\xc2\xcd\xbcF\xae\xe4u|4\xa1\xd2w{,nt\x01\xc9\xdf\x98\x06\x7f3\xa7\xbc\xdb\x8f\xca\x80\xf8\x17U\x99T\x95\x8d\x93@l\x9c\xee\xa3n\x8f\xc8O\xbe\x0f"ON\x83H.\x10\x89\x92Dx\x94*\xdf\xa3\xe1\x9ai\xe55\xf2?\x1aR\r\xdd[\x03\xd7\x82eX\xad-a\xb5\xce\xc1\xea\x8c\n\x8ar\x83\xd4\xfan\xfe\x16v\x12\xcd\xde\xfe\xf0\xfbR\x13-e\xee4\xa3\xa9I\xb8f\x8caSL4M\xc2\xb5\xa1d\xe3\x1b\xd7~Q|\xe7<X\x14 Z\xe1\x96\x1c\x088\x13Mo\xef*c\xb7\xd2=wD\x84\xbfl\xcei:Dl\xb8#,T\xc6\x8d\x91\x9dUHp\x08i\xbe\xb4p\x12\t>T\x1cPw\xca\xd6\x8c\xd2\x14\xc9\x8f\x1d\xbf\x83^\x07#\xd0S\xb4\t\x11\x8c\xae\xd0\xbc\xb6BF\xc7p\xc0\r(\x9e\xce\xcbp\x86~\x07`\xb0\xcas\xd0=\x83\xd0\xc29\x02c\xf7\xc9=\x14w:\x0b\xe5\xb9\x8e\xff\x83\x89\xd2@\xf8OMe\x15g:\x90S\xdd\x8c\xed\xc5j\x19\xdb\x17\xcdrn&- \x06\x8f+\x11\xc0\xa7O3\xfc*\xe6\x01\xc6\xef\xe8\x05j\xb0\x0b#\xe2I&\xf6z\x1d\xf9{w\xec\xd5\x83\xbe\xa3\xf9\xb8\xb2j\xb4\x8d\xa4B\xff\xeb\xe5C\xee\x1b\x1ar\xd8\xdf\xa0\xf6\x95\x83r\xbf\xc7\x99&\x96\xf3\xca\xb8\xfc,\xe8z\xd0\xf1j\xde\xbb_\xe5\xebq(B?K0\x00%\xd0\xfd\x92\x88\x03\x86\xea\x87\xd6\x0f\xd5[2.mA\xc4\xaf\xf2\x7fg\xdaAP\x00\xb8\x15\x14B\xb8\x15\x07\xfd8\xd1\x07\x83\xd3OsA\xf2\xc1@>\xc0<Y\x89?\x9b\xf7Q{\xbe\xbcfy\xa1L\xc3\x8578\xd7\x86\x9e%m\x10\xc8\xa3\xde\xd7/8\x13\xd6\xa8\x16,\x1f\xd4\xd4\xe09\xc1#8$k\xddk$/\xeb\xa6^\x15"\xd3\x99;\x98\xd0\xdd\x81\xda\xa4\x84\xfdh\xa5\x9eX\xce\xc4\xd9\xfc~\xb3;\x9b\x10\xe3\x986\xdd\\v\r\x96\xf3?\xcb\x96<\xdb\x02\t\xc8\x10\x04D\xb7\x910i\x9f\xe07\x9f\xff\xba$\x15\xfft\xf1\xcd\xa3k\xf8/pT\xa2=\x8a\x87\xae\x15_\xfd\xdb\xc2\xb1K\x7f\xba\xf8\xca\xd55\x13\xd8\xf5\xb4\xe6[8v\x84T&\x8eZ\xb7\nm\x1b\xe4\xef\x97\xa6\x00\x9a\xc54\x90ik\x19\xd3\xe0\xd1\x01\xdb\xdb\x17O\x19\x96\x08\x16\xbd\x1ct\x10\xa3\x11\t\x8arS\xe9M\'\x81\xf3.&\xef93\xe3\x96\x11\x0f\xebQ#3 \x14\x1f\xaeQ  lo\xc2\xb0\xa2\x03S\xa0%\xe6\xaf\xe9+S\x08\xad\xc54\xa0i\n\xf8\xcf\x9aW\x95\xebi\x86\xa9^\xc6\x05/\x9c{\xf2K\xa2\xa4\x01~\x17\x88i\xe0\xb2&\xa6L\x85\x96"\xce7i\x9c\x8f\x01\xea\xce\xd1\x06,\x08.\x14\x11\\0\x85\x95\x16\t\xc8\xa6\x18mzH\xfc{!\xd7ps\x15n\xf5\x95qk\rm\xa3\xe1G\xf3\xb4\x95\x86\xbf\x821\xe2\xb8\x87p\xa2;y\x8d\x93\x07\xe1z\x0e\xf2Z\xe7\xbc\x0e\xf3d\x9d\xf3\x04\x9f\xdb\xde zq\x7fw\xae\xf6\x89\xf2\x9f\xdc\xccE\xfb\x9a\x17%\x9a\x17\xb1\xd0\xa2Mk\x16m]\xb3\xa8\'\x8bk\xc8\x85\xeb\x87@\x19\xde\xfc\xfa\xcc\xcd\xf1\x93Y\xb4\x8eXn\xc2u}UD|\xcf\xdc\x92\x9e\xcb\xe2\x8a~\xe1\xc5/&^}\xab\xf0\xdaeb\xe0\xe9\x97\xa9\xc4*\x95\xd8\xc2\'6\xef}{\xfdp\xd3\x0c\xc1\xc3U\xb1\xc3\x86\x8a\xad\x02<\x89\xc9\x8b\x98\x9c\xc5\x04\xbb\x97_\xc4\x04\xf5\x1d\xc7 \x8e\xe3\x04??<\r\x9f(<\x9b|Y*m\xe7\xbaO\nUm\xec\xd4\xe5:\xb1\xc3\x00*v7I4<\x9a\xe6\xe0\x86\n\xdc\x9a\x1a\x89\xd8z$\x92H\xb1l\x1c\x8f\x83\x91\xc8P\xd6\x88\x8b+|s\xc9\x8f\xd0\x0c\x17+\xbd\xeb\xa0;\x97N\xd3\xd5\xe2\xd5\x8f\x95\xde\xfft\xe9\xd5\'\xbf\x84>\xe2\xfd\xd2\x97\xfc\xa6\xf2K&\xc3\xdf\x95\x90\xf4\xb9\xcb\xb3\xf0\xfaw\xf9\x15\xbf\xcf?\xdb\xdf\xe0\xbf\x17r\xc5\xdf\x08\xbf5pV\xef\x9f\x05\xe9,\xbf\xae/\xa0{\xa6\xec\x9d(9\xa5\xa54=\x82`\x1d\x07\x8a\x9c7y\xac`\xb8\x83\xd3#\x96$v\x13\xd2b\xacL\xfb#\xbc\xdd\xb7\xa4\xfb\x05\xeb\xdf#\xa6+\xc9P\xab\x88y\xf8\n\xf7M\xe9;p\xd1)\x99\n\xcb\xd1\xfd\xbc\x0b\xa7\x9c\xe4\x91h\xb5\x91\x82\xee\xda\x92ed\xf6\x9f\x93\xdc\xcd\x0e2Dv\x14\xdd\xf3\xcf\x9c=.\xb8S<\x12\xc9\x1e\x82\xd3\'\x1e\xaa\xfeo\x08\xfa\xffC\xc1C\xba^\xfc\xdd\x07\xc5\xa3\xb7\xfd\xdf\x117>\xbe\\8\xfeB\xe1\xc4o\xc3>\xe7?H\xd0\x06\xc6\n2\xa8\xd8A\x87_\xd9O\xa2\x1a\\\r\xae\t\xe1N\x7f\xe8\xcd\xb3$\xaa\x85\x90\x16\x1f\x08=w\xae\x04\xfc\xae\xe9B\xe1\xc7I\\\xa2D\xfe\x08\x9e\xc7\xdf\xc1+\xbf/\x19A\xb2\xbd\x19\xcb\xe0V\xae\xb1y\x9a\x1fx\x88&\x9eU\x9e\xddk\xfb"\x11\x96\x8a\x02\x9as\xee\x9e\x05\xa1\x8fh+%v4\xff\xa04\x91\x1bq\xc7\xaa]\x87"\xa3E\xecc\x1a48\xed\xa3\xb2\x83Y\x1e\x8f\xc7z[\xe8\xffy\xd0\xce\t\xda\x0e\x15\xae\xed\xc0\xa5\xa3TK\x07\xadC\xd1\x9aV\xb8\xde)\xdbN;\xa0\xb6\x98\xa3\xb4\x00&\xf6s\xe2\x06W\xdaa)@\x84}\xc3\x7f\x8b\xc92\xbc\xd3\xef\x80%C\xbb,\xec\x80\x99\xcc&L\x8e;\xc1\xfd\xe9,\xb8\x82D\xa6_\xec5\x9a?]\x90\xf9\xb8\x18\xcbO\xe2Wdp_\x89\x1a\xf0W1B\x90f\x14(\x97\xf5%\xfaL\xbd\xbe\xee\xa7\x9e\x9fzV\xf9\x03\xb8\x114\xa8.\xa0\xcd\xde\xff\x0b\x06\xc04\x84\xc64\x00\x00)\t\xda\x07marshal\xda\x04lzma\xda\x04gzip\xda\x03bz2\xda\x08binascii\xda\x04zlib\xda\x04exec\xda\x05loads\xda\ndecompress\xa9\x00r\n\x00\x00\x00r\n\x00\x00\x00\xfa\nPy-Fuscate\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xc47\x06\xeb\x0e\x1c\x00\x00')))
except KeyboardInterrupt:
	exit()