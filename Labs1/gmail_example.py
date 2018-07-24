from gmail import GMail, Message
from random import choice

gmail = GMail('Nhung nhúc <vequehomestay@gmail.com>','phong1910')

html_content = """
<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<h4 style="text-align: center;"><strong>Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></h4>
<h4 style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></h4>
<h1 style="color: #5e9ca0; text-align: center;">ĐƠN XIN PH&Eacute;P VỀ SỚM</h1>
<h1 style="color: #5e9ca0; text-align: center;">{{reason}}</h1>
<p>&nbsp;</p>
<p><em><strong>T&ecirc;n iem l&agrave;:</strong></em> Nhung nh&uacute;c</p>
<p><em><strong>Th&agrave;nh vi&ecirc;n lớp:</strong></em> C4E19</p>
<p>&nbsp;</p>
<p>Do h&ocirc;m nay l&agrave; thứ 6 ng&agrave;y 13, l&agrave; lịch quẩy thường ni&ecirc;n của em. Xin ph&eacute;p thầy cho nghỉ học về sớm để makeup.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">Xin tr&acirc;n trọng cảm ơn thầy!&nbsp;<img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
<p style="text-align: right;">&nbsp;</p>
<p style="text-align: right;">H&agrave; Nội một tối h&egrave;</p>
<p style="text-align: right;"><em><strong>Nhung nh&uacute;c</strong></em></p>
<p>&nbsp;</p>
"""

list_reason = ["ĐI CUA GIAI", "XEM CHUNG KẾT WORLDCUP", "ĐI HẸN HÒ TINDER", "ĐI QUẨY"]

pick_reason = choice(list_reason)

html_reason = html_content.replace("{{reason}}", pick_reason)

msg = Message('Nhung nhúc đang gửi thử email từ Python', to='ThayTuanAnh <20130075@student.hust.edu.vn>', html=html_reason)

gmail.send(msg)