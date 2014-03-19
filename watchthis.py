#!/usr/bin/env python

'''
Path Watcher
Verri Andriawan, tiduronline.com
< verri@tiduronline.com, cloud.and.ri@gmail.com >

http://tiduronline.com/
'''


from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import getcwd
import smtplib
from time import ctime


EFrom   = 'source_email',
ETo     = 'destination_email'
EUser   = 'useremail'
EPass   = 'password Email'


def sendMail(msg):
    """
    Sending Mail function
    """


    message = "\r\n".join([
        "Subject: Symlink hilang bro",
        "From: system@monitor",
        "To: emaillu@taruhsini",
        "",
        msg
    ])

    sm = smtplib.SMTP_SSL('smtp.server.disini', 'port_disini')
    sm.login(EUser,EPass)
    sm.sendmail(EFrom, ETo, message )
    sm.quit()



class tellMeError( FileSystemEventHandler ):
    def on_deleted(self, event):
        if event.src_path == getcwd()+'/symlink':

            msg = "Bro tulung bro symlinknya ilang bro\nServer Time : " + ctime()
            sendMail(msg)


                

if __name__ == '__main__':
    watchit = tellMeError()

    handle = Observer()
    handle.schedule(watchit, path='./', recursive=False)
    handle.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        handle.stop()

    handle.join()
        