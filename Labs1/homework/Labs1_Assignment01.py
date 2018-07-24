from gmail import GMail, Message
from random import choice
import datetime
import threading


gmail = GMail('Nhung nhúc <vequehomestay@gmail.com>','phong1910')

html_content = """
<p style="text-align: center;"><strong>CỘNG H&Ograve;A X&Atilde; HỘI CHỦ NGHĨA VIỆT NAM</strong></p>
<p style="text-align: center;"><strong>Dộc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<h2 style="text-align: center;">&nbsp;</h2>
<h2 style="text-align: center;"><strong>ĐƠN XIN PH&Eacute;P ĐƯỢC ĐI HỌC TIẾP</strong></h2>
<p>&nbsp;</p>
<p><em><span style="text-decoration: underline;"><strong>K&iacute;nh gửi:</strong></span></em> Thầy Tuấn Anh</p>
<p><em><span style="text-decoration: underline;"><strong>T&ecirc;n t&ocirc;i l&agrave;:</strong></span></em> Nhung Nh&uacute;c</p>
<p>&nbsp;</p>
<p>Sau 2 buổi nghỉ học v&agrave; trốn l&agrave;m b&agrave;i tập về nh&agrave; v&igrave; c&ocirc;ng việc qu&aacute; bận rộn, t&ocirc;i viết đơn n&agrave;y để được đi học lại v&agrave; hứa sẽ nộp b&agrave;i tập về nh&agrave; đầy đủ.</p>
<p>L&aacute; thư n&agrave;y l&agrave; để l&agrave;m b&agrave;i tập gửi thư.</p>
<p>Cảm ơn thầy.</p>
<p>&nbsp;</p>
<table style="height: 6px;" width="591">
<tbody>
<tr>
<td style="width: 287px;">&nbsp;</td>
<td style="width: 288px; text-align: center;">
<p><strong>H&agrave; Nội, ng&agrave;y 23 th&aacute;ng 07 năm 2018</strong></p>
<p><strong>Người viết đơn</strong></p>
<p>Nhung nh&uacute;c</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
"""


def check():
    now_hour = (datetime.datetime.now()).hour
    if now_hour >= 12:
        msg = Message('Chị Nhung nộp bài tập gửi email', to='ThayTuanAnh <20130075@student.hust.edu.vn>', html=html_content)
        gmail.send(msg)
        print("Gửi thành công")
    else:
        print ("Chưa gửi")
        run_time()
        
def run_time():
    sec = 3
    t = threading.Timer(sec, check)
    t.start()

run_time()