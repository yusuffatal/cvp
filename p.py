# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
from ffmpy import FFmpeg
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#client = LINE()
client = LINE("ECzdx4HCoDWt6yfCb4O5.IqtJipTzyCWvcrgownX/bq.zkcH9U4eSFSTH5GLVYOfJUT0tXp+Sk7FAMWeA0xvEWQ=")
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)

ki = LINE("ECkZIo6MDMeN0k1ljzS0.QWqSRx6fatWKqxNTrJpvua.iS+MI6cmGHnEnTA5qDWkVYLPygBjuwkQ4DjUrCuqZ9Y=")
#ki = LINE("EA9ws7qu8xUVtGL188j5.IqtJipTzyCWvcrgownX/bq.yQ/2KgspbDbXYrmE+DatSCSWkwk6kSQInqwG7AvFoEI=")
kiMid = ki.profile.mid
kiProfile = ki.getProfile()
kiSettings = ki.getSettings()
kiPoll = OEPoll(ki)
botStart = time.time()

clientMID = client.profile.mid
kiMID = ki.profile.mid

admin = ["u8904e320fb5961cc1509118e58dc7e05"]

msg_dict = {}

wordban = []
images = {}

settingss = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

settings = {
    "autoAdd": False,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "suf": True,
    "simsimi": False,
    "ya": True,
    "checkSticker": False,
    "changeVideoProfile": False,
    "changeVideoProfile2": False,
    "ChangeVideoProfilePicture": False,
   "ChangeVideoProfilePicture2": False,
    "changePictureProfile2": False,
    "ChangeVideoProfilevid": False,
    "ChangeVideoProfilevid2": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "changeGroupPicture2": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

Setmain = {
    "ayam": {},
}


list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        client.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
#Dont sell it fcking bitch *Akhirnya bisa bhs inggris
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def changeVideoAndPictureProfile2(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = ki.genOBSParams({'oid': kiMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = ki.server.postContent('{}/talk/vp/upload.nhn'.format(str(ki.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        ki.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def clientBot(op):
    try:
        if op.type == 0:
            return
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if clientMid in op.param3:
                if settings["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)


        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                client.leaveRoom(op.param1)

        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            for image in images:
                             if sender in admin:
                               if text.lower() == image:
                                  ki.sendImage(msg.to, images[image])
                            cmd = command(text)
                            if cmd == "983jwmslsuahoihelp":
                                helpMessage = helpmessage()
                                ki.sendMessage(to, str(helpMessage))
                            elif cmd.startswith("changetsg5443key:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    ki.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    ki.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "runtime":
                                if msg._from in admin:
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    ki.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd in ["kizuna gpicture","trapchan gpicture"]:
                                if msg._from in admin:
                                    group = ki.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    ki.sendImageWithURL(to, path)
                            elif cmd == "restart":
                                if msg._from in admin:
                                   ki.sendMessage(to, "Berhasil merestart Bot")
                                   restartBot()
                            elif cmd in ["about kizuna","about trapchan"]:
                                try:
                                    arr = []
                                    owner = "u8904e320fb5961cc1509118e58dc7e05"
                                    creator = ki.getContact(owner)
                                    contact = ki.getContact(kiMID)
                                    grouplist = ki.getGroupIdsJoined()
                                    contactlist = ki.getAllContactIds()
                                    blockedlist = ki.getBlockedContactIds()
                                    ret_ = "「 About @! 」"
                                    ret_ += "\n Name : {}".format(contact.displayName)
                                    ret_ += "\n Group : {}".format(str(len(grouplist)))
                                    ret_ += "\n Friend : {} ".format(str(len(contactlist)))
                                    ret_ += "\n Blocked : 736 "
                                    sendMention(to, str(ret_), [kiMID])
                                except Exception as e:
                                    ki.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "autoadd on":
                                if sender in admin: 
                                    settings["autoAdd"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                                if sender in admin: 
                                    settings["autoAdd"] = False
                                    ki.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autojoin on":
                                if sender in admin: 
                                    settings["autoJoin"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                                if sender in admin:
                                    settings["autoJoin"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "ya on":
                                if sender in admin: 
                                    settings["ya"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan sc")
                            elif cmd == "ya off":
                                if sender in admin:
                                    settings["ya"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan sc")
                            elif cmd == "autoleave on":
                                if sender in admin:
                                    settings["autoLeave"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                                if sender in admin:
                                    settings["autoLeave"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                                if sender in admin:
                                   settings["autoRespon"] = True
                                   ki.sendMessage(to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "autorespon off":
                                if sender in admin:
                                    settings["autoRespon"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                                if sender in admin:
                                    settings["autoRead"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                                if sender in admin:
                                    settings["autoRead"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                                if msg._from in admin:
                                   settings["autoJoinTicket"] = True
                                   ki.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autoJoinTicket off":
                                if msg._from in admin:
                                   settings["autoJoinTicket"] = False
                                   ki.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                                if sender in admin:
                                    settings["checkContact"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                                if sender in admin:
                                    settings["checkContact"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                                if sender in admin:
                                    settings["checkPost"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                                if sender in admin:
                                    settings["checkPost"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                                if sender in admin:
                                    settings["checkSticker"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                                if sender in admin:
                                    settings["checkSticker"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                                if sender in admin:
                                    settings["unsendMessage"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                                if sender in admin:
                                    settings["unsendMessage"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "suf on":
                                if sender in admin:
                                    settings["suf"] = True
                                    ki.sendMessage(to, "Berhasil mengaktifkan suf message")
                            elif cmd == "suf off":
                                if sender in admin:
                                    settings["suf"] = False
                                    ki.sendMessage(to, "Berhasil menonaktifkan suf message")
                            elif cmd == "status":
                                if sender in admin:
                                    try:
                                        ret_ = "âââ[ Status ]"
                                        if settings["autoAdd"] == True: ret_ += "\nâ ââ[ ON ] Auto Add"
                                        else: ret_ += "\nâ ââ[ OFF ] Auto Add"
                                        if settings["suf"] == True: ret_ += "\nâ ââ[ ON ] suf"
                                        else: ret_ += "\nâ ââ[ OFF ] suf"
                                        if settings["ya"] == True: ret_ += "\nâ ââ[ ON ] ya"
                                        else: ret_ += "\nâ ââ[ OFF ] ya"
                                        if settings["autoJoin"] == True: ret_ += "\nâ ââ[ ON ] Auto Join"
                                        else: ret_ += "\nâ ââ[ OFF ] Auto Join"
                                        if settings["autoLeave"] == True: ret_ += "\nâ ââ[ ON ] Auto Leave Room"
                                        else: ret_ += "\nâ ââ[ OFF ] Auto Leave Room"
                                        if settings["autoJoinTicket"] == True: ret_ += "\nâ ââ[ ON ] Auto Join Ticket"
                                        else: ret_ += "\nâ ââ[ OFF ] Auto Join Ticket"
                                        if settings["autoRead"] == True: ret_ += "\nâ ââ[ ON ] Auto Read"
                                        else: ret_ += "\nâ ââ[ OFF ] Auto Read"
                                        if settings["autoRespon"] == True: ret_ += "\nâ ââ[ ON ] Detect Mention"
                                        else: ret_ += "\nâ ââ[ OFF ] Detect Mention"
                                        if settings["checkContact"] == True: ret_ += "\nâ ââ[ ON ] Check Contact"
                                        else: ret_ += "\nâ ââ[ OFF ] Check Contact"
                                        if settings["checkPost"] == True: ret_ += "\nâ ââ[ ON ] Check Post"
                                        else: ret_ += "\nâ ââ[ OFF ] Check Post"
                                        if settings["checkSticker"] == True: ret_ += "\nâ ââ[ ON ] Check Sticker"
                                        else: ret_ += "\nâ ââ[ OFF ] Check Sticker"
                                        if settings["setKey"] == True: ret_ += "\nâ ââ[ ON ] Set Key"
                                        else: ret_ += "\nâ ââ[ OFF ] Set Key"
                                        if settings["unsendMessage"] == True: ret_ += "\nâ ââ[ ON ] Unsend Message"
                                        else: ret_ += "\nâ ââ[ OFF ] Unsend Message"
                                        ret_ += "\nâââ[ Status ]"
                                        ki.sendMessage(to, str(ret_))
                                    except Exception as e:
                                        ki.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "me":
                                if sender in admin:
                                   sendMention(to, "@!", [sender])
                                   ki.sendContact(to, sender)
                            elif cmd == "mymid":
                                if sender in admin:
                                   client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                if sender in admin:
                                   contact = client.getContact(sender)
                                   client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                if sender in admin:
                                   contact = client.getContact(sender)
                                   client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                if sender in admin:
                                   contact = client.getContact(sender)
                                   client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                if msg._from in admin:
                                   contact = client.getContact(sender)
                                   client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                if sender in admin:
                                   channel = client.getProfileCoverURL(sender)          
                                   path = str(channel)
                                   client.sendImageWithURL(to, path)
                            elif cmd == "my ticket":
                                if sender in admin:
                                    client.sendMessage(to, '? Your Ticket ?\nhttp://line.me/ti/p/{}'.format(client.getUserTicket().id))
                            elif cmd == "changedp":
                                if msg._from in admin:
                                   settings["changePictureProfile"] = True
                                   client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd in ["kizuna changedp","trapchan changedp"]:
                                if msg._from in admin:
                                   settings["changePictureProfile2"] = True
                                   ki.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == "kizuna cvp":
                                if msg._from in admin:
                                   settings["ChangeVideoProfilevid2"] = True
                                   client.sendMessage(to, "「Profile 」\nType : Change Profile Video Picture\nStatus : Send the video...")
                            elif cmd == "cvp":
                                if msg._from in admin:
                                   settings["ChangeVideoProfilevid"] = True
                                   client.sendMessage(to, "「Profile 」\nType : Change Profile Video Picture\nStatus : Send the video....")
                            elif cmd == 'gcreator':
                                if msg._from in admin:
                                   group = ki.getGroup(to)
                                   GS = group.creator.mid
                                   ki.sendContact(to, GS)
                            elif msg.text.lower().startswith("kizuna kick "):
                                if msg._from in admin:
                                   targets = []
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"][0]["M"]
                                   for x in key["MENTIONEES"]:
                                       targets.append(x["M"])
                                   for target in targets:
                                       try:
                                           ki.kickoutFromGroup(msg.to,[target])
                                       except:
                                           ki.sendMessage(msg.to,"Error")
                            elif cmd == 'inv:gcreator':
                                if msg.toType == 2:
                                   ginfo = ki.getGroup(msg.to)
                                   gCreator = ginfo.creator.mid
                                   try:
                                      ki.findAndAddContactsByMid(gCreator)
                                      ki.inviteIntoGroup(msg.to,[gCreator])
                                      print ("success inv gCreator")
                                   except:
                                      pass
                            elif cmd == 'lgid':
                                gid = ki.getGroupIdsJoined()
                                h = ""
                                for i in gid:
                                   h += "[%s]:%s\n" % (ki.getGroup(i).name,i)
                                ki.sendMessage(msg.to,h)
                            elif cmd in ["cgp"]:
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                            elif cmd in ["kizuna mention","trapchan mention"]:
                                if msg._from in admin:
                                    group = ki.getGroup(msg.to)
                                    nama = [contact.mid for contact in group.members]
                                    k = len(nama)//100
                                    for a in range(k+1):
                                        txt = u''
                                        s=0
                                        b=[]
                                        for i in group.members[a*100 : (a+1)*100]:
                                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                            s += 7
                                            txt += u'@Zero \n'
                                        ki.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                        ki.sendMessage(to, "Total {} Members".format(str(len(nama))))
                            elif cmd.startswith("accept"):
                                if msg._from in admin:
                                   gid = ki.getGroupIdsInvited()
                                   _list = ""
                                   for i in gid:
                                       if i is not None:
                                           gids = ki.getGroup(i)
                                           _list += gids.name
                                           ki.acceptGroupInvitation(i)
                                       else:
                                           break
                                   if gid is not None:
                                       ki.sendMessage(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                                   else:
                                       ki.sendMessage(msg.to,"Tidak ada grup yang tertunda saat ini")
                            elif cmd == 'listgroup':
                                    groups = ki.getGroupIdsJoined()
                                    ret_ = "「 Group List 」"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = ki.getGroup(gid)
                                        ret_ += "\nâ  {}. {} - {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n「 Total {} Groups 」".format(str(len(groups)))
                                    ki.sendMessage(to, str(ret_))
# Pembatas Script #   
                            elif cmd.startswith("kizuna getpp"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ki.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        ki.sendImageWithURL(to, str(path))
                            elif cmd.startswith("kizuna getvp "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ki.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        ki.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("tag: "):
                                if msg._from in admin:
                                   proses = text.split(":")
                                   strnum = text.replace(proses[0] + ":","")
                                   num =  int(strnum)
                                   Setmain["ayam"] = num
                                   ki.sendMessage(msg.to,"[ Status Spamtag ]\nBerhasil diubah jadi {} kali".format(str(strnum)))
                            elif "tag @" in msg.text:
                                if msg._from in admin:
                                   _name = msg.text.replace("tag @","")
                                   _nametarget = _name.rstrip(' ')
                                   gs = ki.getGroup(msg.to)
                                   for g in gs.members:
                                       if _nametarget == g.displayName:
                                           jmlh = int(Setmain["ayam"])
                                           if jmlh <= 1000:
                                               for x in range(jmlh):
                                                   try:
                                                       sendMention(to, "@!",[g.mid])
                                                   except Exception as e:
                                                       ki.sendMessage(msg.to,str(e))
                                       else:
                                          pass
                            elif "tag hai @" in msg.text:
                                if msg._from in admin:
                                   _name = msg.text.replace("tag hai @","")
                                   _nametarget = _name.rstrip(' ')
                                   gs = ki.getGroup(msg.to)
                                   for g in gs.members:
                                       if _nametarget == g.displayName:
                                           jmlh = int(Setmain["ayam"])
                                           if jmlh <= 1000:
                                               for x in range(jmlh):
                                                   try:
                                                       sendMention(to, "@! hai",[g.mid])
                                                   except Exception as e:
                                                       ki.sendMessage(msg.to,str(e))
                                       else:
                                          pass
                            elif cmd.startswith("kizuna getcover "):
                                if ki != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = ki.getProfileCoverURL(ls)
                                            path = str(channel)
                                            ki.sendImageWithURL(to, str(path))
                            elif msg.text.lower().startswith("gbc "):
                                if msg._from in admin:   
                                   sep = text.split(" ")
                                   txt = text.replace(sep[0] + " ","")
                                   groups = ki.getGroupIdsJoined()
                                   for group in groups:
                                       ki.sendMessage(group, "{}".format(str(txt)))
                                       ki.sendMessage(to, "Success broadcast to 198 group")
                            elif cmd.startswith("kizuna ssweb"):
                                if msg._from in admin:
                                   try:
                                       sep = text.split(" ")
                                       query = text.replace(sep[0] + " ","")
                                       r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                       data = r.text
                                       data = json.loads(data)
                                       ki.sendImageWithURL(to, data["result"])
                                   except Exception as error:
                                       logError(error)
                            elif cmd in ["kizuna invgcall","trapchan invgcall"]:
                                if msg._from in admin:
                                   if msg.toType == 2:
                                       sep = text.split(" ")
                                       strnum = text.replace(sep[0] + " ","")
                                       num = int(strnum)
                                       for var in range(0,num):
                                           group = ki.getGroup(to)
                                           members = [mem.mid for mem in group.members]
                                           ki.acquireGroupCallRoute(to)
                                           ki.inviteIntoGroupCall(to, contactIds=members)
                                        #ki.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                            elif text.lower() == 'rejectall':
                                ginvited = client.ginvited
                                if ginvited != [] and ginvited != None:
                                   for gid in ginvited:
                                       client.rejectGroupInvitation(gid)
                                       client.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                                else:
                                   client.sendMessage(to, "Tidak ada undangan yang tertunda")
                            elif text.startswith("imagetext"):
                                if msg._from in admin:
                                   sep = text.split(" ")
                                   textnya = text.replace(sep[0] + " ","")   
                                   url = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                                   ki.sendImageWithURL(msg.to, url)
                            elif cmd in ["kizuna invite","trapchan invite"]:
                                if msg._from in admin:
                                   key = msg.text[-33:]
                                   ki.findAndAddContactsByMid(key)
                                   ki.inviteIntoGroup(msg.to, [key])
                                   contact = ki.getContact(key)
                            elif cmd.startswith("searchvid "):
                                if msg._from in admin:
                                      sep = msg.text.split(" ")
                                      search = msg.text.replace(sep[0] + " ","")
                                      with requests.session() as web:
                                            web.headers["User-Agent"] = random.choice(settingss["userAgent"])
                                            url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                            data = url.text
                                            data = json.loads(data)
                                            if data["result"] != []:
                                                video = random.choice(data["result"]["videolist"])
                                                vid = video["url"]
                                                start = time.time()
                                                ki.sendVideoWithURL(msg.to, str(vid))
                            elif cmd.startswith("searchanime "):
                                if msg._from in admin:
                                      sep = msg.text.split(" ")
                                      anime = msg.text.replace(sep[0] + " ","%20")                
                                      with requests.session() as web:
                                            web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                      r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                                      data = r.text
                                      data = json.loads(data)
                                      ret_ = ''
                                      if data["data"] != []:
                                          for a in data["data"]:
                                              if a["attributes"]["subtype"] == "TV":
                                                  sin = a["attributes"]["synopsis"]
                                                  translator = Translator()
                                                  hasil = translator.translate(sin, dest='id')
                                                  sinop = hasil.text
                                                  ret_ += 'Anime : {} '.format(str(a["attributes"]["canonicalTitle"]))
                                                  ret_ += '\nRilis : '+str(a["attributes"]["startDate"])
                                                  ret_ += '\nRating : '+str(a["attributes"]["ratingRank"])
                                                  ret_ += '\nType : '+str(a["attributes"]["subtype"])
                                                  ret_ += '\nSinopsis :\n'+str(sinop)
                                                  ret_ += '\n\n'
                                                  ki.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                                                  ki.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("searchgif "):
                                if msg._from in admin:
                                  proses = text.split(" ")
                                  urutan = text.replace(proses[0] + " ","")
                                  count = urutan.split("|")
                                  search = str(count[0])
                                  r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                                  data = json.loads(r.text)
                                  if len(count) == 1:
                                      no = 0
                                      hasil = "「 Searching result 」\n"
                                      for aa in data["results"]:
                                          no += 1
                                          hasil += "\n" + str(no) + ". " + str(aa["title"])
                                          ret_ = "\nType: searchgif {} | number\ntoo see the gif".format(str(search))
                                      ki.sendMessage(msg.to,hasil+ret_)
                                  elif len(count) == 2:
                                      try:
                                          num = int(count[1])
                                          b = data["results"][num - 1]
                                          c = str(b["id"])
                                          dl = str(b["media"][0]["loopedmp4"]["url"])
                                          ki.sendVideoWithURL(msg.to,dl)
                                      except Exception as e:
                                          ki.sendMessage(msg.to," "+str(e))     
                            elif 'yutubmp4 ' in text.lower():
                                if msg._from in admin:
                                    textToSearch = (msg.text).replace('youtubemp4 ', "").strip()
                                    query = urllib.parse.quote(textToSearch)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    response = urllib.request.urlopen(url)
                                    html = response.read()
                                    soup = BeautifulSoup(html, "html.parser")
                                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                    dl = 'https://www.youtube.com' + results['href']
                                    vid = pafy.new(dl)
                                    stream = vid.streams
                                    for s in stream:
                                        vin = s.url
                                        hasil = ' Informasi \n\n'
                                        hasil += 'Judul video\n ' + vid.title
                                        hasil += '\n Tunggu loading selesai...'
                                    ki.sendMessage(msg.to,hasil)
                                    ki.sendVideoWithURL(msg.to,vin)
                                    print("[Notif] Search Youtube Success")     
                            elif cmd.startswith("get-video "):
                                if msg._from in admin:
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                          web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                          url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                          data = url.text
                                          data = json.loads(data)
                                          if data["result"] != []:
                                              video = random.choice(data["result"]["videolist"])
                                              vid = video["url"]
                                              start = timeit.timeit()
                                              ret = "? Informasi Video ?\n"
                                              ret += "? Judul : {}".format(str(data["result"]["title"]))
                                              ret += "\n? Author : {}".format(str(data["result"]["author"]))
                                              ret += "\n? Durasi : {}".format(str(data["result"]["duration"]))
                                              ret += "\n? Like nya : {}".format(str(data["result"]["likes"]))
                                              ret += "\n? Rating : {}".format(str(data["result"]["rating"]))
                                              ret += "\n? TimeTaken : {}".format(str(start))
                                              ret += "\n? Deskripsi : {}\n? Waiting Encoding ?".format(str(data["result"]["description"]))
                                              client.sendMessage(msg.to, str(ret))
                                              client.sendVideoWithURL(msg.to, str(vid))
                            elif cmd.startswith("kode wilayah"):
                                if msg._from in admin:
                                      ret_ = " Daftar Kode Wilayah \n\n"
                                      ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                                      ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                                      ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                                      ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                                      ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                                      ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                                      ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                                      ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                                      ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                                      ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                                      ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                                      ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                                      ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                                      ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                                      ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                                      ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                                      ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                                      ret_ += "\n\nUntuk melihat cctv,\nKetik cctv (kode wilayah)"                            
                                      ki.sendMessage(to, ret_)
                            elif cmd.startswith("cctv "):
                                if msg._from in admin:
                                      sep = msg.text.split(" ")
                                      cct = msg.text.replace(sep[0] + " ","")
                                      with requests.session() as s:
                                          s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                          r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                          soup = BeautifulSoup(r.content, 'html5lib')
                                          try:
                                              ret_ = " Informasi CCTV \nDaerah "
                                              ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                              ret_ += "\nCctv update per 5 menit"
                                              vid = soup.find('source')['src']
                                              ki.sendMessage(to, ret_)
                                              ki.sendVideoWithURL(to, vid)
                                          except:
                                              ki.sendMessage(to, "Data cctv tidak ditemukan!")
                            elif cmd.startswith("get-fs "):
                                if msg._from in admin:
                                      sep = msg.text.split(" ")
                                      anu = msg.text.replace(sep[0] + " "," ")                
                                      with requests.session() as web:
                                          web.headers["user-agent"] = random.choice(settingss["userAgent"])
                                          r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(urllib.parse.quote(anu)))
                                          data = r.text
                                          data = json.loads(data)
                                          if data["status"] == "success":
                                              ret_ = data["url"]
                                              ki.sendImageWithURL(msg.to,ret_)
                                          else:
                                              ki.sendMessage(msg.to, "Error")
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykizunakey":
                            ki.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        if text.lower() == "wordban list":
                                if wordban not in [[]]:
                                    no = 1
                                    wordbans = "[ Word ban ]\n"
                                    for word in wordban:
                                        wordbans+="\n{}. {}".format(str(no),str(word))
                                        no+=1
                                    wordbans+="\n\n[ Finish ]"
                                    ki.sendMessage(to, str(wordbans))
                                if wordban == []:
                                    ki.sendMessage(to, "No wordban saved.")
                
                        elif text.lower().startswith("addwordban: "):
                                word = text.replace("addwordban: ","")
                                if word not in wordban:
                                   wordban.append(word)
                                   ki.sendMessage(to, "Success add {} to wordban list.".format(str(word)))
                                else:
                                   ki.sendMessage(to, "{} already added on wordban list.".format(str(word)))
                		
                        elif text.lower().startswith("delwordban: "):
                                word = text.replace("delwordban: ","")
                                if word in wordban:
                                   wordban.remove(word)
                                   ki.sendMessage(to, "Success deleted {} from wordban list.".format(str(word)))
                                else:
                                   ki.sendMessage(to, "{} does not exist on wordban list.".format(str(word)))
                        elif text.lower() in wordban:
                           if msg._from not in admin:
                               ki.sendMessage(to, "Wordban detected")
                               ki.kickoutFromGroup(op.param1,[op.param2])
                        elif text.lower() == "mykizunakey on":
                            settings["setKey"] = True
                            ki.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "mykizunakey off":
                            settings["setKey"] = False
                            ki.sendMessage(to, "Berhasil menonaktifkan setkey")
                        elif text.lower() == "mykizunakey on":
                            settings["setKey"] = True
                            ki.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "mykizunakey off":
                            settings["setKey"] = False
                            ki.sendMessage(to, "Berhasil menonaktifkan setkey")
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                settings["Addimage"]["status"] = True
                                settings["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                client.sendMessage(msg.to, "Send picture") 
                            else:
                                ki.sendMessage(msg.to, "That photo is already in the list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                ki.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                client.sendMessage(msg.to, "Successfully deleted {}".format( str(name.lower())))
                            else:
                                client.sendMessage(msg.to, "The photo is not in the list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 List Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\n「 Total {} Images 」".format(str(len(images)))
                             client.sendMessage(to, ret_)
# Pembatas Script #
                    elif msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                        if msg.contentType == 1:
                           path = ki.downloadObjectMsg(msg_id)
                           msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                    elif msg.contentType == 1:
                        if msg._from in admin:
                            if settings["changePictureProfile"] == True:
                               path = client.downloadObjectMsg(msg_id)
                               settings["changePictureProfile"] = False
                               client.updateProfilePicture(path)
                               client.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg._from in admin:
                            if settings["changePictureProfile2"] == True:
                               path = ki.downloadObjectMsg(msg_id)
                               settings["changePictureProfile2"] = False
                               ki.updateProfilePicture(path)
                               ki.sendMessage(to, "Success")
                        if msg._from in admin:
                            if settings["Addimage"]["status"] == True:
                               path = ki.downloadObjectMsg(msg.id)
                               images[settings["Addimage"]["name"]] = str(path)
                               f = codecs.open("image.json","w","utf-8")
                               json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                               ki.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                               settings["Addimage"]["status"] = False                
                               settings["Addimage"]["name"] = ""
                    elif msg.contentType == 2:
                        if msg._from in admin:
                            if settings["ChangeVideoProfilevid"] == True:
                               videos = client.downloadObjectMsg(msg_id,saveAs="tmp/videos.mp4")
                               settings["ChangeVideoProfilevid"] = False
                               settings["ChangeVideoProfilePicture"] = True
                               pictures = "tmp/imag.jpg"
                               client.sendMessage(to, "[ Profile ] \nType: Change Profile Video Picture\nStatus: Waiting...")
                               settings["ChangeVideoProfilePicture"] = False
                               changeVideoAndPictureProfile(pictures, videos)
                               client.sendMessage(to, "[ Profile ]\nType: Change Profile Video Picture\nStatus: Profile Video Picture Hasbeen changed") 
                               client.deleteFile(videos)
                    elif msg.contentType == 2:
                        if msg._from in admin:
                            if settings["ChangeVideoProfilevid2"] == True:
                               videos = ki.downloadObjectMsg(msg_id,saveAs="tmp/videoss.mp4")
                               settings["ChangeVideoProfilevid2"] = False
                               settings["ChangeVideoProfilePicture2"] = True
                               pictures = "tmp/FB_IMG_15262308078397122.jpg"
                               ki.sendMessage(to, "「 Profile 」 \nType: Change Profile Video Picture\nStatus: Waiting...")
                               settings["ChangeVideoProfilePicture2"] = False
                               changeVideoAndPictureProfile2(pictures, videos)
                               ki.sendMessage(to, "「 Profile 」 \nType: Change Profile Video Picture\nStatus: Profile Video Picture Has been changed") 
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(msg.to,text)
                    if settings['simsimi'] == True:
                        try:
                            if sender in sender:
                                params = {'text': text}
                                r = requests.get('http://corrykalam.gq/simi.php?',params=params).json()
                                if text is not None:
                                   try:
                                       ki.sendMessage(receiver, r['answer'])
                                   except Exception as e:
                                       ki.sendMessage(receiver, str(e))
                                       logError(e)
                        except Exception as e:
                           ki.sendMessage(receiver, str(e))
                           logError(e)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["suf"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                        if "a " in msg.text.lower():
                            if settings["suf"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if msg.toType == 2:
                                        if to not in settings["changeGroupPicture"]:
                                            settings["changeGroupPicture"].append(to)
                                    #ki.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
#===============================================================================[clientMID - kiMID]
        if op.type == 19:
             if op.param3 in clientMID:
                   ki.inviteIntoGroup(op.param1,[op.param3])
                   client.acceptGroupInvitation(op.param1)
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   G = ki.getGroup(op.param1)
                   G.preventedJoinByTicket = False
                   ki.updateGroup(G)
        if op.type == 19:
          try:                      
            if op.param3 in kiMID:
              if op.param2 in clientMID:
                G = client.getGroup(op.param1)
                Ticket = client.reissueGroupTicket(op.param1)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
              else:
                G = client.getGroup(op.param1)
                Ticket = client.reissueGroupTicket(op.param1)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                wait["blacklist"][op.param2] = True
          except:
            pass
#==============================================================================#
        if op.type == 13 or op.type == 17:
                   G = client.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   invsend = 0
                   Ticket = client.reissueGroupTicket(op.param1)
                   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                   time.sleep(0.01)
        if op.type == 10 or op.type == 11:
          try:                      
            G = client.getGroup(op.param1)
            f = "tmp/img.jpg"
            ki.updateGroupPicture(op.param1, f)
          break
                   
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = ki.getGroup(at)
                                ryan = ki.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "?  Image Deleted ?\n? Sender : "
                                ret_ += "\n? Time Created : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                ki.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                ki.sendImage(at, msg_dict[msg_id]["data"])
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
