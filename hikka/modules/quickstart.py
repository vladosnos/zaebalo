# ÂŠī¸ Dan Gazizullin, 2021-2022
# This file is a part of Hikka Userbot
# đ https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# đ https://www.gnu.org/licenses/agpl-3.0.html

import logging
import os
from random import choice

from .. import loader, translations, utils
from ..inline.types import BotInlineCall

logger = logging.getLogger(__name__)

imgs = [
    "https://i.gifer.com/GmUB.gif",
    "https://i.gifer.com/Afdn.gif",
    "https://i.gifer.com/3uvT.gif",
    "https://i.gifer.com/2qQQ.gif",
    "https://i.gifer.com/Lym6.gif",
    "https://i.gifer.com/IjT4.gif",
    "https://i.gifer.com/A9H.gif",
]


@loader.tds
class QuickstartMod(loader.Module):
    """Notifies user about userbot installation"""

    strings = {
        "name": "Quickstart",
        "base": """đđŦđ§ <b>Hello.</b> You've just installed <b>Hikka</b> userbot.

â <b>Need help?</b> Feel free to join our support chat. We help <b>everyone</b>.

đŧ <b>You can find and install modules using @hikkamods_bot. Simply enter your search query and click âŠ Install on needed module</b>

đŖ <b>Check out community made channels with modules: <a href="https://t.me/hikka_ub/126">show</a></b>

đââī¸ <b>Quickstart:</b>

1ī¸âŖ <b>Type</b> <code>.help</code> <b>to see modules list</b>
2ī¸âŖ <b>Type</b> <code>.help &lt;ModuleName/command&gt;</code> <b>to see help of module ModuleName</b>
3ī¸âŖ <b>Type</b> <code>.dlmod &lt;link&gt;</code> <b>to load module from link</b>
4ī¸âŖ <b>Type</b> <code>.loadmod</code> <b>with reply to file to install module from it</b>
5ī¸âŖ <b>Type</b> <code>.unloadmod &lt;ModuleName&gt;</code> <b>to unload module ModuleName</b>

đĄ <b>Hikka supports modules from Friendly-Telegram, DragonUserbot and GeekTG, as well as its own ones.</b>""",
        "railway": (
            "đ <b>Your userbot is installed on Railway</b>. This platform has only"
            " <b>500 free hours per month</b>. Once this limit is reached, your"
            " <b>Hikka will be frozen</b>. Next month <b>you will need to go to"
            " https://railway.app and restart it</b>."
        ),
        "lavhost": (
            "âī¸ <b>Your userbot is installed on lavHost</b>. Make sure to join @lavhost"
            " for important notifications and updates. All questions regarding the"
            " platform should be asked in @lavhostchat."
        ),
        "miyahost": (
            "đ <b>Your userbot is installed on MiyaHost</b>. Make sure to join"
            " @miyahost for important notifications and updates. All questions"
            " regarding the platform should be asked in @miyahost_support."
        ),
        "language_saved": "đŦđ§ Language saved!",
        "language": "đŦđ§ English",
        "btn_support": "đĨˇ Support chat",
    }

    strings_ru = {
        "base": """đđˇđē <b>ĐŅĐ¸Đ˛ĐĩŅ.</b> ĐĸĐ˛ĐžĐš ŅĐˇĐĩŅĐąĐžŅ <b>Hikka</b> ŅŅŅĐ°ĐŊĐžĐ˛ĐģĐĩĐŊ.

â <b>ĐŅĐļĐŊĐ° ĐŋĐžĐŧĐžŅŅ?</b> ĐŅŅŅĐŋĐ°Đš Đ˛ ĐŊĐ°Ņ ŅĐ°Ņ ĐŋĐžĐ´Đ´ĐĩŅĐļĐēĐ¸. ĐŅ ĐŋĐžĐŧĐžĐŗĐ°ĐĩĐŧ <b>Đ˛ŅĐĩĐŧ</b>.

đŧ <b>ĐĸŅ ĐŧĐžĐļĐĩŅŅ Đ¸ŅĐēĐ°ŅŅ Đ¸ ŅŅŅĐ°ĐŊĐ°Đ˛ĐģĐ¸Đ˛Đ°ŅŅ ĐŧĐžĐ´ŅĐģĐ¸ ŅĐĩŅĐĩĐˇ @hikkamods_bot. ĐŅĐžŅŅĐž Đ˛Đ˛ĐĩĐ´Đ¸ ĐŋĐžĐ¸ŅĐēĐžĐ˛ŅĐš ĐˇĐ°ĐŋŅĐžŅ Đ¸ ĐŊĐ°ĐļĐŧĐ¸ âŠ Install ĐŊĐ° ĐŊŅĐļĐŊĐžĐŧ ĐŧĐžĐ´ŅĐģĐĩ</b>

đŖ <b>ĐĐ°ĐŗĐģŅĐŊĐ¸ Đ˛ ĐēĐ°ĐŊĐ°ĐģŅ Ņ ĐŧĐžĐ´ŅĐģŅĐŧĐ¸, ŅĐžĐˇĐ´Đ°ĐŊĐŊŅĐŧĐ¸ ĐēĐžĐŧŅŅĐŊĐ¸ŅĐ¸: <a href="https://t.me/hikka_ub/126">ĐŋĐžĐēĐ°ĐˇĐ°ŅŅ</a></b>

đââī¸ <b>ĐŅŅŅŅŅĐš ĐŗĐ°ĐšĐ´:</b>

1ī¸âŖ <b>ĐĐ°ĐŋĐ¸ŅĐ¸</b> <code>.help</code> <b>ŅŅĐžĐąŅ ŅĐ˛Đ¸Đ´ĐĩŅŅ ŅĐŋĐ¸ŅĐžĐē ĐŧĐžĐ´ŅĐģĐĩĐš</b>
2ī¸âŖ <b>ĐĐ°ĐŋĐ¸ŅĐ¸</b> <code>.help &lt;ĐĐ°ĐˇĐ˛Đ°ĐŊĐ¸Đĩ ĐŧĐžĐ´ŅĐģŅ/ĐēĐžĐŧĐ°ĐŊĐ´Đ°&gt;</code> <b>ŅŅĐžĐąŅ ŅĐ˛Đ¸Đ´ĐĩŅŅ ĐžĐŋĐ¸ŅĐ°ĐŊĐ¸Đĩ ĐŧĐžĐ´ŅĐģŅ</b>
3ī¸âŖ <b>ĐĐ°ĐŋĐ¸ŅĐ¸</b> <code>.dlmod &lt;ŅŅŅĐģĐēĐ°&gt;</code> <b>ŅŅĐžĐąŅ ĐˇĐ°ĐŗŅŅĐˇĐ¸ŅŅ ĐŧĐžĐ´ŅĐģŅ Đ¸Đˇ ŅŅŅĐģĐēĐ°</b>
4ī¸âŖ <b>ĐĐ°ĐŋĐ¸ŅĐ¸</b> <code>.loadmod</code> <b>ĐžŅĐ˛ĐĩŅĐžĐŧ ĐŊĐ° ŅĐ°ĐšĐģ, ŅŅĐžĐąŅ ĐˇĐ°ĐŗŅŅĐˇĐ¸ŅŅ ĐŧĐžĐ´ŅĐģŅ Đ¸Đˇ ĐŊĐĩĐŗĐž</b>
5ī¸âŖ <b>ĐĐ°ĐŋĐ¸ŅĐ¸</b> <code>.unloadmod &lt;ĐĐ°ĐˇĐ˛Đ°ĐŊĐ¸Đĩ ĐŧĐžĐ´ŅĐģŅ&gt;</code> <b>ŅŅĐžĐąŅ Đ˛ŅĐŗŅŅĐˇĐ¸ŅŅ ĐŧĐžĐ´ŅĐģŅ</b>

đĄ <b>Hikka ĐŋĐžĐ´Đ´ĐĩŅĐļĐ¸Đ˛Đ°ĐĩŅ ĐŧĐžĐ´ŅĐģĐ¸ Đ¸Đˇ Friendly-Telegram, DragonUserbot Đ¸ GeekTG, Đ° ŅĐ°ĐēĐļĐĩ ŅĐ˛ĐžĐ¸ ŅĐžĐąŅŅĐ˛ĐĩĐŊĐŊŅĐĩ.</b>
""",
        "railway": (
            "đ <b>ĐĸĐ˛ĐžĐš ŅĐˇĐĩŅĐąĐžŅ ŅŅŅĐ°ĐŊĐžĐ˛ĐģĐĩĐŊ ĐŊĐ° Railway</b>. ĐĐ° ŅŅĐžĐš ĐŋĐģĐ°ŅŅĐžŅĐŧĐĩ ŅŅ"
            " ĐŋĐžĐģŅŅĐ°ĐĩŅŅ ŅĐžĐģŅĐēĐž <b>500 ĐąĐĩŅĐŋĐģĐ°ŅĐŊŅŅ ŅĐ°ŅĐžĐ˛ Đ˛ ĐŧĐĩŅŅŅ</b>. ĐĐžĐŗĐ´Đ° ĐģĐ¸ĐŧĐ¸Ņ ĐąŅĐ´ĐĩŅ"
            " Đ´ĐžŅŅĐ¸ĐŗĐŊĐĩŅ, ŅĐ˛ĐžĐš <b>ŅĐˇĐĩŅĐąĐžŅ ĐąŅĐ´ĐĩŅ ĐˇĐ°ĐŧĐžŅĐžĐļĐĩĐŊ</b>. Đ ŅĐģĐĩĐ´ŅŅŅĐĩĐŧ ĐŧĐĩŅŅŅĐĩ <b>ŅŅ"
            " Đ´ĐžĐģĐļĐĩĐŊ ĐąŅĐ´ĐĩŅŅ ĐŋĐĩŅĐĩĐšŅĐ¸ ĐŊĐ° https://railway.app Đ¸ ĐŋĐĩŅĐĩĐˇĐ°ĐŋŅŅŅĐ¸ŅŅ ĐĩĐŗĐž</b>."
        ),
        "lavhost": (
            "âī¸ <b>ĐĸĐ˛ĐžĐš ŅĐˇĐĩŅĐąĐžŅ ŅŅŅĐ°ĐŊĐžĐ˛ĐģĐĩĐŊ ĐŊĐ° lavHost</b>. ĐŅŅŅĐŋĐ¸ Đ˛ @lavhost, ŅŅĐžĐąŅ"
            " ĐŋĐžĐģŅŅĐ°ŅŅ Đ˛Đ°ĐļĐŊŅĐĩ ŅĐ˛ĐĩĐ´ĐžĐŧĐģĐĩĐŊĐ¸Ņ Đ¸ ĐžĐąĐŊĐžĐ˛ĐģĐĩĐŊĐ¸Ņ. ĐŅĐĩ Đ˛ĐžĐŋŅĐžŅŅ, ŅĐ˛ŅĐˇĐ°ĐŊĐŊŅĐĩ Ņ"
            " ĐŋĐģĐ°ŅŅĐžŅĐŧĐžĐš, ŅĐģĐĩĐ´ŅĐĩŅ ĐˇĐ°Đ´Đ°Đ˛Đ°ŅŅ Đ˛ @lavhostchat."
        ),
        "miyahost": (
            "đ <b>ĐĸĐ˛ĐžĐš ŅĐˇĐĩŅĐąĐžŅ ŅŅŅĐ°ĐŊĐžĐ˛ĐģĐĩĐŊ ĐŊĐ° MiyaHost</b>. ĐŅŅŅĐŋĐ¸ Đ˛ @miyahost, ŅŅĐžĐąŅ"
            " ĐŋĐžĐģŅŅĐ°ŅŅ Đ˛Đ°ĐļĐŊŅĐĩ ŅĐ˛ĐĩĐ´ĐžĐŧĐģĐĩĐŊĐ¸Ņ Đ¸ ĐžĐąĐŊĐžĐ˛ĐģĐĩĐŊĐ¸Ņ. ĐŅĐĩ Đ˛ĐžĐŋŅĐžŅŅ, ŅĐ˛ŅĐˇĐ°ĐŊĐŊŅĐĩ Ņ"
            " ĐŋĐģĐ°ŅŅĐžŅĐŧĐžĐš, ŅĐģĐĩĐ´ŅĐĩŅ ĐˇĐ°Đ´Đ°Đ˛Đ°ŅŅ Đ˛ @miyahost_support."
        ),
        "language_saved": "đˇđē Đ¯ĐˇŅĐē ŅĐžŅŅĐ°ĐŊĐĩĐŊ!",
        "language": "đˇđē Đ ŅŅŅĐēĐ¸Đš",
        "btn_support": "đĨˇ Đ§Đ°Ņ ĐŋĐžĐ´Đ´ĐĩŅĐļĐēĐ¸",
    }

    strings_it = {
        "base": """đđŽđš <b>Ciao.</b> Il tuo userbot <b>Hikka</b> Ã¨ stato installato.

â <b>Hai bisogno di aiuto?</b> Entra nel nostro gruppo di supporto. Aiutiamo <b>tutti</b>.

đŧ <b>Puoi cercare e installare moduli tramite @hikkamods_bot. Basta inserire una richiesta di ricerca e premere âŠ Installa sul modulo desiderato</b>

đŖ <b>Guarda i canali dei moduli creati dalla community: <a href="https://t.me/hikka_ub/126">mostra</a></b>

đââī¸ <b>Guida rapida:</b>

1ī¸âŖ <b>Scrivi</b> <code>.help</code> <b>per vedere l'elenco dei moduli</b>
2ī¸âŖ <b>Scrivi</b> <code>.help &lt;Nome del modulo/comando&gt;</code> <b>per vedere la descrizione del modulo</b>
3ī¸âŖ <b>Scrivi</b> <code>.dlmod &lt;link&gt;</code> <b>per caricare il modulo dal link</b>
4ī¸âŖ <b>Scrivi</b> <code>.loadmod</code> <b>come risposta al file per caricare il modulo da esso</b>
5ī¸âŖ <b>Scrivi</b> <code>.unloadmod &lt;Nome del modulo&gt;</code> <b>per scaricare il modulo</b>

đĄ <b>Hikka supporta i moduli di Friendly-Telegram, DragonUserbot e GeekTG, oltre ai suoi moduli personali.</b>
""",
        "railway": (
            "đ <b>Il tuo userbot Ã¨ stato installato su Railway.</b> Su questa"
            " piattaforma ricevi solo <b>500 ore gratuite al mese</b>. Quando il limite"
            " verrÃ  raggiunto, <b>il tuo userbot verrÃ  congelato</b>. Nel mese"
            " successivo <b>devi andare su https://railway.app e riavviarlo</b>."
        ),
        "lavhost": (
            "âī¸ <b>Il tuo userbot Ã¨ installato su lavHost</b>. Unisciti a @lavhost, per"
            " ricevere importanti notifiche e aggiornamenti. Tutte le domande relative"
            " alla piattaforma devono essere poste in @lavhostchat."
        ),
        "miyahost": (
            "đ <b>Il tuo userbot Ã¨ installato su MiyaHost</b>. Unisciti a @miyahost,"
            " per ricevere importanti notifiche e aggiornamenti. Tutte le domande"
            " relative alla piattaforma devono essere poste in @miyahost_support."
        ),
        "language_saved": "đŽđš Lingua salvata!",
        "language": "đŽđš Italiano",
        "btn_support": "đĨˇ Gruppo di supporto",
    }

    strings_de = {
        "base": """đđŠđĒ <b>Hallo.</b> Dein Userbot <b>Hikka</b> ist installiert.

â <b>Brauchst du Hilfe?</b> Trete unserem Support-Chat bei. Wir helfen <b>allen</b>.

đŧ <b>Du kannst Module Ãŧber @hikkamods_bot suchen und installieren. Gib einfach einen Suchbegriff ein und drÃŧcke auf âŠ Install auf dem gewÃŧnschten Modul</b>

đŖ <b>Schaue dir die Module-KanÃ¤le an, die von der Community erstellt wurden: <a href="https://t.me/hikka_ub/126">anzeigen</a></b>

đââī¸ <b>Schnellstart:</b>

1ī¸âŖ <b>Schreibe</b> <code>.help</code> <b>um eine Liste der Module zu sehen</b>
2ī¸âŖ <b>Schreibe</b> <code>.help &lt;Modulname/Befehl&gt;</code> <b>um die Beschreibung des Moduls zu sehen</b>
3ī¸âŖ <b>Schreibe</b> <code>.dlmod &lt;Link&gt;</code> <b>um ein Modul aus dem Link zu laden</b>
4ī¸âŖ <b>Schreibe</b> <code>.loadmod</code> <b>als Antwort auf eine Datei, um ein Modul aus der Datei zu laden</b>
5ī¸âŖ <b>Schreibe</b> <code>.unloadmod &lt;Modulname&gt;</code> <b>um ein Modul zu entladen</b>

đĄ <b>Hikka unterstÃŧtzt Module von Friendly-Telegram, DragonUserbot und GeekTG sowie eigene Module.</b>
""",
        "railway": (
            "đ <b>Dein Userbot ist auf Railway installiert</b>. Du erhÃ¤ltst nur <b>500"
            " kostenlose Stunden pro Monat</b> auf dieser Plattform. Wenn das Limit"
            " erreicht ist, wird dein <b>Userbot eingefroren</b>. Im nÃ¤chsten Monat"
            " musst du zu https://railway.app gehen und ihn neu starten.</b>"
        ),
        "lavhost": (
            "âī¸ <b>Dein Userbot ist auf lavHost installiert</b>. Trete @lavhost bei, um"
            " wichtige Benachrichtigungen und Updates zu erhalten. Alle Fragen, die"
            " sich auf die Plattform beziehen, sollten im @lavhostchat gestellt werden."
        ),
        "miyahost": (
            "đ <b>Dein Userbot ist auf MiyaHost installiert</b>. Trete @miyahost bei,"
            " um wichtige Benachrichtigungen und Updates zu erhalten. Alle Fragen, die"
            " sich auf die Plattform beziehen, sollten im @miyahost_support gestellt"
            " werden."
        ),
        "language_saved": "đŠđĒ Sprache gespeichert!",
        "language": "đŠđĒ Deutsch",
        "btn_support": "đĨˇ Support-Chat",
    }

    strings_uz = {
        "base": """đđēđŋ <b>Salom.</b> <b>Hikka</b> Sizning yuzer botingiz sozlandi.

â <b>Yordam kerakmi?</b> Siz bizning qollab quvvatlash guruhimizga qo'shilishingiz mumkin. guruhimzda  <b>barcha savollaringizga javob olasiz</b>.

đŧ <b>Modullar @hikkamods_bot ushbu botimiz orqali siz har qanday yuzerbotga tegishli bo'lgan modullarni o'rnatishingiz mumkun botga kalit so'zni yuboring va  âŠ O'rnatish tugmasini bosing</b>

đŖ <b>Homiylar tomonidan yaratilgan modullar kanalini ko'rish: <a href="https://t.me/hikka_ub/126">kanalni ko'rish</a></b>

đââī¸ <b>Tez ishga tushurish:</b>

1ī¸âŖ <b>Modullar royhatini ko'rish uchun</b> <code>.help buyrug'ini</code> <b>yozing</b>
2ī¸âŖ <b>Modul haqida ma'lumot olish uchun</b> <code>.help &lt;Modul nomi/buyruq&gt;</code> <b>yozing</b>
3ī¸âŖ <b>Modulni havola orqali o'rnatish uchun</b> <code>.dlmod &lt;Link&gt;</code> <b>yozing</b>
4ī¸âŖ <b>Modulni fayl orqali yuklash uchun</b> <code>.loadmod</code> <b>faylga javoban yozing</b>
5ī¸âŖ <b>Modulni olib tashlash uchun</b> <code>.unloadmod &lt;Modul nomi&gt;</code> <b>yozing</b>

đĄ <b>Hikka, Friendly-Telegram, DragonUserbot ve GeekTG O'z Modullarini qollab quvvatlaydi.</b>
""",
        "railway": (
            "đ <b>Sizning yuzerbotingiz Railwayda o'rnatilgan</b>. Bu platforma,"
            " <b>oyiga atigi 500 soat bepul jihati</b> Railway bergan muddat tugagandan"
            " so'ng sizning bo'tingiz  <b>to'xtatiladi</b>. Keyingi oy,"
            " https://railway.app havolasi orqali yuzerbotingizni qayta ishga tushira"
            " olasiz.</b>"
        ),
        "lavhost": (
            "âī¸ <b>Sizning foydalanuvchi botingiz lavHost-da o'rnatildi</b>. Kiritish"
            " uchun @lavhost ga a'zo bo'ling, shuningdek muhim xabarlar va"
            " yangilanishlar olishingiz mumkin. Platforma haqida savollaringizni"
            " @lavhostchat ga yozing."
        ),
        "miyahost": (
            "đ <b>Sizning foydalanuvchi botingiz MiyaHost-da o'rnatildi</b>. Kiritish"
            " uchun @miyahost ga a'zo bo'ling, shuningdek muhim xabarlar va"
            " yangilanishlar olishingiz mumkin. Platforma haqida savollaringizni"
            " @miyahost_support ga yozing."
        ),
        "language_saved": "đēđŋ Til saqlandi!",
        "language": "đēđŋ O'zbekcha",
        "btn_support": "đĨˇ Qo'llab-quvvatlash guruhi",
    }

    strings_tr = {
        "base": """đđšđˇ <b>Merhaba.</b> <b>Hikka</b> kullanÄącÄą botunuz kuruldu.

â <b>YardÄąma mÄą ihtiyacÄąnÄąz var?</b> YardÄąm grubumuza katÄąlabilirsin. Herkese <b>yardÄąm ediyoruz</b>.

đŧ <b>ModÃŧlleri @hikkamods_bot ile arayabilir ve kurabilirsiniz. Sadece anahtar kelimeleri girin ve istediÄiniz modÃŧlÃŧn âŠ Kur butonuna basÄąn</b>

đŖ <b>Topluluk tarafÄąndan oluÅturulan modÃŧl kanallarÄą gÃļrÃŧntÃŧleyin: <a href="https://t.me/hikka_ub/126">gÃļster</a></b>

đââī¸ <b>HÄązlÄą baÅlangÄąÃ§:</b>

1ī¸âŖ <b>ModÃŧller listesini gÃļrmek iÃ§in</b> <code>.help</code> <b>yazÄąn</b>
2ī¸âŖ <b>ModÃŧl hakkÄąnda bilgi almak iÃ§in</b> <code>.help &lt;Modul adÄą/Komut&gt;</code> <b>yazÄąn</b>
3ī¸âŖ <b>Bir baÄlantÄądan modÃŧl yÃŧklemek iÃ§in</b> <code>.dlmod &lt;Link&gt;</code> <b>yazÄąn</b>
4ī¸âŖ <b>Bir modÃŧlÃŧ bir dosyadan yÃŧklemek iÃ§in</b> <code>.loadmod</code> <b>bir dosyanÄąn yanÄątÄąnÄą yazÄąn</b>
5ī¸âŖ <b>Bir modÃŧlÃŧ kaldÄąrmak iÃ§in</b> <code>.unloadmod &lt;Modul adÄą&gt;</code> <b>yazÄąn</b>

đĄ <b>Hikka, Friendly-Telegram, DragonUserbot ve GeekTG modÃŧllerini de dahil olmak Ãŧzere kendi modÃŧllerini destekler.</b>
""",
        "railway": (
            "đ <b>KullanÄącÄą botunuz Railway'de kuruldu</b>. Bu platform, <b>aylÄąk"
            " sadece 500 saati Ãŧcretsiz olarak</b> saÄlamaktadÄąr. SÄąnÄąrÄą aÅtÄąÄÄąnÄązda,"
            " kullanÄącÄą botunuz <b>durdurulur</b>. Gelecek ay, https://railway.app"
            " adresinden botunuzu yeniden baÅlatmanÄąz gerekmektedir.</b>"
        ),
        "lavhost": (
            "âī¸ <b>lavHost'a kurulumunuz tamamlandÄą.</b> Ãnemli duyurular ve"
            " gÃŧncellemeleri almak iÃ§in @lavhost'a katÄąlÄąn. Platformla ilgili"
            " sorularÄąnÄązÄą @lavhostchat'da sorabilirsiniz."
        ),
        "miyahost": (
            "đ <b>MiyaHost'a kurulumunuz tamamlandÄą.</b> Ãnemli duyurular ve"
            " gÃŧncellemeleri almak iÃ§in @miyahost'a katÄąlÄąn. Platformla ilgili"
            " sorularÄąnÄązÄą @miyahost_support'da sorabilirsiniz."
        ),
        "language_saved": "đšđˇ Dil kaydedildi!",
        "language": "đšđˇ TÃŧrkÃ§e",
        "btn_support": "đĨˇ Destek grubu",
    }

    strings_es = {
        "base": """
đŧ <b>Para buscar e instalar mÃŗdulos, vaya a @hikkamods_bot y escriba las palabras clave.</b>

đŖ <b>Para ver los canales de la comunidad creados, haga clic aquÃ­: <a href="https://t.me/hikka_ub/126">Ver</a></b>

đââī¸ <b>Para comenzar de inmediato:</b>

1ī¸âŖ <b>Para ver la lista de mÃŗdulos, escriba</b> <code>.help</code> <b>y presione</b>
2ī¸âŖ <b>Para obtener informaciÃŗn sobre el mÃŗdulo, escriba</b> <code>.help &lt;nombre del mÃŗdulo/comando&gt;</code> <b>y presione</b>
3ī¸âŖ <b>Para instalar el mÃŗdulo desde el enlace, escriba</b> <code>.dlmod &lt;enlace&gt;</code> <b>y presione</b>
4ī¸âŖ <b>Para cargar el mÃŗdulo desde el archivo, escriba</b> <code>.loadmod</code> <b>y responda al archivo que desea cargar</b>
5ī¸âŖ <b>Para eliminar el mÃŗdulo, escriba</b> <code>.unloadmod &lt;nombre del mÃŗdulo&gt;</code> <b>y presione</b>

đĄ <b>Para admitir mÃŗdulos, tambiÃŠn incluye Hikka, Friendly-Telegram, DragonUserbot y GeekTG.</b>
""",
        "railway": (
            "đ <b>Se ha creado el bot de usuario en Railway</b> esta plataforma ofrece"
            " <b>500 horas gratis al mes</b> una vez que llegue al lÃ­mite, el <b>bot de"
            " usuario serÃĄ bloqueado hasta el prÃŗximo mes</b> por favor, reinicie <b>el"
            " bot de usuario en https://railway.app</b>"
        ),
        "lavhost": (
            "âī¸ <b>Tu bot de usuario estÃĄ instalado en lavHost</b>. Ãnete a @lavhost"
            " para recibir notificaciones y actualizaciones importantes. Todas las"
            " preguntas relacionadas con la plataforma deben hacerse en @lavhostchat."
        ),
        "miyahost": (
            "đ <b>Tu bot de usuario estÃĄ instalado en MiyaHost</b>. Ãnete a @miyahost"
            " para recibir notificaciones y actualizaciones importantes. Todas las"
            " preguntas relacionadas con la plataforma deben hacerse en"
            " @miyahost_support."
        ),
        "language_saved": "đĒđ¸ ÂĄEl idioma se ha guardado!",
        "language": "đĒđ¸ EspaÃąol",
        "btn_support": "đĨˇ Grupo de soporte",
    }

    strings_kk = {
        "base": """đđ°đŋ <b>ĐĄĶĐģĐĩĐŧĐĩŅŅŅĐˇ ĐąĐĩ.</b> ĐĄŅĐˇĐ´ŅŌŖ <b>Hikka</b> ĐąĐžŅŅŌŖŅĐˇ ĐžŅĐŊĐ°ŅŅĐģĐ´Ņ.

â <b>ĐĶŠĐŧĐĩĐē ĐēĐĩŅĐĩĐē ĐŋĐĩ?</b> ĐŅĐˇĐ´ŅŌŖ ĐēĶŠĐŧĐĩĐē ŅĶŠĐšĐģĐĩŅŅ ĐēŅŅĐ°ĐąŅĐŊĐ° ĐēŅŅŅŌŖŅĐˇ. ĐŅĐˇ <b>ĐąĐ°ŅĐģŅŌ</b>ŌĐ° ĐēĶŠĐŧĐĩĐēŅĐĩŅĐĩĐŧŅĐˇ.

đŧ <b>ĐĄŅĐˇ @hikkamods_bot Đ°ŅŌŅĐģŅ ĐŧĐžĐ´ŅĐģŅĐ´Ņ ŅĐˇĐ´ĐĩŅ ĐļĶĐŊĐĩ ĐžŅĐŊĐ°ŅŅŌĐ° ĐąĐžĐģĐ°Đ´Ņ. ĐĸĐ°ĐŋŅŅŅŅŅ ŅĐˇĐ´ĐĩŅ ŌŌąŅĐ°ĐģŅĐŊ ĐĩĐŊĐŗŅĐˇŅŌŖŅĐˇ ĐļĶĐŊĐĩ ĐēĐĩŅĐĩĐē ĐŧĐžĐ´ŅĐģŅĐ´ŅŌŖ Ō¯ŅŅŅĐŊĐ´ĐĩĐŗŅ âŠ Install ŅŌ¯ĐšĐŧĐĩŅŅĐŊ ĐąĐ°ŅŅŌŖŅĐˇ</b>

đŖ <b>ĐĐžĐŧŅŅĐŊĐ¸ŅĐ¸ ĐļĐ°ŅĐ°ŌĐ°ĐŊ ĐŧĐžĐ´ŅĐģŅĐ´ĐĩŅĐ´ŅŌŖ ĐēĐ°ĐŊĐ°ĐģŅĐŊĐ° ĐēŅŅŅŌŖŅĐˇ: <a href="https://t.me/hikka_ub/126">ĐēĶŠŅŅĐĩŅŅ</a></b>

đââī¸ <b>ĐŅĐģĐ´Đ°Đŧ ŌŌąŅĐ°Đģ:</b>

1ī¸âŖ <b>ĐĐžĐ´ŅĐģŅĐ´ĐĩŅ ŅŅĐˇŅĐŧŅĐŊ ĐēĶŠŅŅ Ō¯ŅŅĐŊ</b> <code>.help</code> <b>ĐļĐ°ĐˇŅŌŖŅĐˇ</b>
2ī¸âŖ <b>ĐĐžĐ´ŅĐģŅĐ´ŅŌŖ ŅĐ¸ĐŋĐ°ŅŅĐ°ĐŧĐ°ŅŅĐŊ ĐēĶŠŅŅ Ō¯ŅŅĐŊ</b> <code>.help &lt;ĐĐžĐ´ŅĐģŅ/ĐēĐžĐŧĐ°ĐŊĐ´Đ° Đ°ŅĐ°ŅŅ&gt;</code> <b>ĐļĐ°ĐˇŅŌŖŅĐˇ</b>
3ī¸âŖ <b>ĐĄŅĐģŅĐĩĐŧĐĩĐ´ĐĩĐŊ ĐŧĐžĐ´ŅĐģŅĐ´Ņ ĐžŅĐŊĐ°ŅŅ Ō¯ŅŅĐŊ</b> <code>.dlmod &lt;ŅŅĐģŅĐĩĐŧĐĩ&gt;</code> <b>ĐļĐ°ĐˇŅŌŖŅĐˇ</b>
4ī¸âŖ <b>Đ¤Đ°ĐšĐģĐ´Đ°ĐŊ ĐŧĐžĐ´ŅĐģŅĐ´Ņ ĐžŅĐŊĐ°ŅŅ Ō¯ŅŅĐŊ</b> <code>.loadmod</code> <b>ĐļĐ°ĐˇŅŌŖŅĐˇ</b>
5ī¸âŖ <b>ĐĐžĐ´ŅĐģŅĐ´Ņ ĐļĐžŅ Ō¯ŅŅĐŊ</b> <code>.unloadmod &lt;ĐĐžĐ´ŅĐģŅ Đ°ŅĐ°ŅŅ&gt;</code> <b>ĐļĐ°ĐˇŅŌŖŅĐˇ</b>

đĄ <b>Hikka Friendly-Telegram, DragonUserbot ĐļĶĐŊĐĩ GeekTG ĐŧĐžĐ´ŅĐģĐ´ĐĩŅŅĐŊĐĩĐŊ, ĶĐšŅĐŋĐĩŅĐĩ ĐļĐĩŌŖŅĐģ ĐŧĐžĐ´ŅĐģĐ´ĐĩŅĐ´ĐĩĐŊ ŌĐ°ĐŧŅĐ°ĐŧĐ°ŅŅĐˇ ĐĩŅĐĩĐ´Ņ.</b>
""",
        "railway": (
            "đ <b>ĐĄŅĐˇĐ´ŅŌŖ ĐąĐžŅŅŌŖŅĐˇ Railway ĐŋĐģĐ°ŅŅĐžŅĐŧĐ°ŅŅĐŊĐ´Đ° ĐžŅĐŊĐ°ŅŅĐģĐ´Ņ.</b> ĐŌąĐģ ĐŋĐģĐ°ŅŅĐžŅĐŧĐ°"
            " <b>Đ°ĐšĐ´Đ°ŌŅ 500 ŅĐ°ŌĐ°ŅŅŅŌŖ ĐąĐĩŅĐŋĐģĐ°ŅŅŅŌŅĐŊ</b> ĐąĐĩŅĐĩĐ´Ņ. ĐĐ¸ĐŧĐ¸Ņ Đ°ŅŌŅĐ°ĐģŌĐ°ĐŊĐ´Đ°,"
            " <b>ĐąĐžŅŅŌŖŅĐˇ ŌŌąĐģŅĐŋŅĐ°ĐģĐ°Đ´Ņ</b>. ĐĐĩĐģĐĩŅŅ Đ°ĐšĐ´Đ° <b>https://railway.app ĐļĶĐŊĐĩ ĐžĐŊŅ"
            " ŌĐ°ĐšŅĐ° ĐļŌ¯ĐēŅĐĩŅ ŌĐ°ĐļĐĩŅ</b>."
        ),
        "lavhost": (
            "âī¸ <b>ĐĄŅĐˇĐ´ŅŌŖ ĐĐĩĐēĐĩ ĐąĐžŅŅŌŖŅĐˇ lavHost-ŅĐ° ĐžŅĐŊĐ°ŅŅĐģŌĐ°ĐŊ</b>. ĐĐ°ŌŖŅĐˇĐ´Ņ"
            " ŅĐ°ĐąĐ°ŅĐģĐ°ĐŊĐ´ŅŅŅĐģĐ°Ņ ĐŧĐĩĐŊ ĐļĐ°ŌŖĐ°ŅŅŅĐģĐ°Ņ Đ°ĐģŅ Ō¯ŅŅĐŊ @lavhost-ŌĐ° ĐēŅŅŅŌŖŅĐˇ. ĐĐģĐ°ŅŅĐžŅĐŧĐ°"
            " ĐļĶĐŊĐĩ ŌĐ°ŅĐĩĐģĐĩŅ ŅŅŅĐ°ĐģŅ ĐąĐ°ŅĐģŅŌ ŅŌąŅĐ°ŌŅĐ°ŅĐ´Ņ @lavhostchat-ŌĐ° ĐļŅĐąĐĩŅŅŌŖŅĐˇ."
        ),
        "miyahost": (
            "đ <b>ĐĄŅĐˇĐ´ŅŌŖ ĐĐĩĐēĐĩ ĐąĐžŅŅŌŖŅĐˇ MiyaHost-ŅĐ° ĐžŅĐŊĐ°ŅŅĐģŌĐ°ĐŊ</b>. ĐĐ°ŌŖŅĐˇĐ´Ņ"
            " ŅĐ°ĐąĐ°ŅĐģĐ°ĐŊĐ´ŅŅŅĐģĐ°Ņ ĐŧĐĩĐŊ ĐļĐ°ŌŖĐ°ŅŅŅĐģĐ°Ņ Đ°ĐģŅ Ō¯ŅŅĐŊ @miyahost-ŌĐ° ĐēŅŅŅŌŖŅĐˇ. ĐĐģĐ°ŅŅĐžŅĐŧĐ°"
            " ĐļĶĐŊĐĩ ŌĐ°ŅĐĩĐģĐĩŅ ŅŅŅĐ°ĐģŅ ĐąĐ°ŅĐģŅŌ ŅŌąŅĐ°ŌŅĐ°ŅĐ´Ņ @miyahost_support-ŌĐ° ĐļŅĐąĐĩŅŅŌŖŅĐˇ."
        ),
        "language_saved": "đ°đŋ ĐĸŅĐģ ŅĐ°ŌŅĐ°ĐģĐ´Ņ!",
        "language": "đ°đŋ ŌĐ°ĐˇĐ°ŌŅĐ°",
        "btn_support": "đĨˇ ŌĐžĐģĐ´Đ°Ņ ŅĶŠĐšĐģĐĩŅŅ ĐēŅŅĐ°ĐąŅ",
    }

    strings_tt = {
        "base": """đđĨ <b>ĐĄĶĐģĐ°Đŧ.</b> ĐĄĐĩĐˇĐŊĐĩŌŖ ŅĐˇĐĩŅĐąĐžŅ <b>Hikka</b> ŅŅĐŊĐ°ŅŅŅŅŅĐģĐŗĐ°ĐŊ.
â <b>Đ¯ŅĐ´ĶĐŧ ĐēĐ¸ŅĶĐēĐŧĐĩ?</b> ĐĐĩĐˇĐŊĐĩŌŖ ŅŅĐ´ĶĐŧ ŅĐ°ŅŅĐŊĐ° ĐēĐĩŅĐĩĐŗĐĩĐˇ. ĐĐĩĐˇ <b>ŌģĶŅĐēĐĩĐŧĐŗĶ</b> ĐąŅĐģŅŅĐ°ĐąŅĐˇ.
đŧ <b>ĐĄĐĩĐˇ ĐŧĐžĐ´ŅĐģŅĐģĶŅĐŊĐĩ @hikkamods_bot Đ°ŅĐ° ŅĐˇĐģĐ¸ ŌģĶĐŧ ŅŅĐŊĐ°ŅŅŅŅĐ° Đ°ĐģĐ°ŅŅĐˇ. ĐĐ°Đ´Đ¸ ŅĐˇŅĐŗŅĐˇ ŅĐˇĐģĶŌ¯ ĐˇĐ°ĐŋŅĐžŅ ŌģĶĐŧ ĐąĐ°ŅŅĐŗŅĐˇ âŠ install ĐąŅ ĐēĐ¸ŅĶĐēĐģĐĩ ĐŧĐžĐ´ŅĐģĐĩ</b>
đŖ <b>ĐĐžĐŧŅŅĐŊĐ¸ŅĐ¸ ŅŅĐ°ĐŗĐ°ĐŊ ĐŧĐžĐ´ŅĐģŅĐģĶŅ ĐąĐĩĐģĶĐŊ ĐēĐ°ĐŊĐ°ĐģĐģĐ°ŅĐŊŅ ĐēĐ°ŅĐ°ĐŗŅĐˇ: <a href="https://t.me/hikka_ub/126">ĐēŌ¯ŅŅĶŅĐĩŅĐŗĶ</a></b>
đââī¸ <b>ĐĸĐ¸Đˇ ĐąĐĩĐģĐĩŅĐŧĶĐģĐĩĐē:</b>
1ī¸âŖ <b>Đ¯ĐˇŅĐŗŅĐˇ <b><code>.help</code></b> ĐŧĐžĐ´ŅĐģŅĐģĶŅ Đ¸ŅĐĩĐŧĐģĐĩĐŗĐĩĐŊ ĐēŌ¯ŅŌ¯ ĶŠŅĐĩĐŊ</b>
2ī¸âŖ <b>Đ¯ĐˇŅĐŗŅĐˇ</b> <code>.help &lt;ĐĐžĐ´ŅĐģŅ Đ¸ŅĐĩĐŧĐĩ/ĐēĐžĐŧĐ°ĐŊĐ´Đ°ŅŅ&gt;</code> <b>ĐŧĐžĐ´ŅĐģŅ ŅĐ°ŅĐ˛Đ¸ŅĐģĐ°ĐŧĐ°ŅŅĐŊ ĐēŌ¯ŅŌ¯ ĶŠŅĐĩĐŊ</b>
3ī¸âŖ <b>Đ¯ĐˇŅĐŗŅĐˇ</b> <code>.dlmod &lt;ŅŅĐģŅĐ°ĐŧĐ°&gt;</code> <b>ŅŅĐģŅĐ°ĐŧĐ°Đ´Đ°ĐŊ ĐŧĐžĐ´ŅĐģŅĐŊĐĩ ĐšĶŠĐēĐģĶŌ¯ ĶŠŅĐĩĐŊ</b>
4ī¸âŖ <b>Đ¯ĐˇŅĐŗŅĐˇ</b> <code>.loadmod</code> <b>ŅĐ°ĐšĐģĐŗĐ° ŌĐ°Đ˛Đ°Đŋ, Đ°ĐŊĐŊĐ°ĐŊ ĐŧĐžĐ´ŅĐģŅĐŊĐĩ ĐšĶŠĐēĐģĶŌ¯ ĶŠŅĐĩĐŊ</b>
5ī¸âŖ <b>Đ¯ĐˇŅĐŗŅĐˇ</b> <code>.unloadmod &lt;ĐŧĐžĐ´ŅĐģŅ Đ¸ŅĐĩĐŧĐĩ&gt;</code> <b>ĐŧĐžĐ´ŅĐģŅĐŊĐĩ ĐąŅŅĐ°ŅŅ ĶŠŅĐĩĐŊ</b>
đĄ <b>Hikka Friendly-Telegram ŌģĶĐŧ GeekTG ĐŧĐžĐ´ŅĐģŅĐģĶŅĐĩĐŊ, ŅŅĐģĐ°Đš ŅĐē Ō¯ĐˇĐĩĐŊĐĩĐēĐĩĐŊ ŅŅĐŋĐģŅĐš.</b>
""",
        "railway": (
            "đ <b>ĐĄĐ¸ĐŊĐĩŌŖ ŅĐˇĐĩŅĐąĐžŅ Railway ŅĐ°ĐšŅŅĐŊĐ´Đ° ŅŅĐŊĐ°ŅŅŅŅŅĐģĐŗĐ°ĐŊ</b>. ĐŅ ĐŋĐģĐ°ŅŅĐžŅĐŧĐ°Đ´Đ° ŅĐĩĐˇ"
            " Đ°ĐšĐŗĐ° <b>500 ĐąŅŅĐģĐ°Đš ŅĶĐŗĐ°ŅŅ Đ°ĐģĐ°ŅŅĐˇ</b>. ĐĐ¸ĐŧĐ¸Ņ ŌĐ¸ŅĐēĶŅ, ŅĐĩĐˇĐŊĐĩŌŖ <b>ŅĐˇĐĩŅĐąĐžŅ"
            " ŅŅŌŖĐ´ŅŅŅĐģĐ°ŅĐ°Đē</b>. ĐĐ¸ĐģĶŅĐĩ Đ°ĐšĐ´Đ° <b>ŅĐĩĐˇ ĐēŌ¯ŅĶŅĐŗĶ ŅĐ¸ĐĩŅ https://railway.app ŌģĶĐŧ"
            " Đ°ĐŊŅ ŅŌŖĐ°Đ´Đ°ĐŊ ŅŅĐģĶŅĐĩĐŋ ŌĐ¸ĐąĶŅŌ¯</b>."
        ),
        "lavhost": (
            "âī¸ <b>ĐĄĐĩĐˇĐĩŅĐąĐžŅŅŌŖ ŅĐĩĐˇ lavHost ŌĐ¸ĐąĶŅĐĩĐģĐ´Đĩ</b>. ĐĶĐēĐ¸ĐŊ @lavhost ŌĐ¸ĐąĶŅĐĩĐģĐŗĶĐŊ"
            " ŅĶĐąĶŅĐģĶŅ ŌģĶĐŧ ŅŌŖĐ° ŅŌŖĐ°ĐģŅĐēĐģĐ°Ņ Ō¯ĐˇĐĩĐŊĶ Đ°ĐģŅ ĶŠŅĐĩĐŊ ĐēĐĩŅĐĩĐŗĐĩĐˇ. ĐĄĐĩĐˇĐĩŅĐąĐžŅ ŌĐ¸ĐąĶŅĐĩĐģĐŗĶĐŊ"
            " ŅĶĐąĶŅĐģĶŅ ŌģĶĐŧ ŅŌŖĐ° ŅŌŖĐ°ĐģŅĐēĐģĐ°Ņ ŅŅŅŅĐŊĐ´Đ° ŅĐžŅĐ°ŅĐģĐ°ŅĐŊŅ @lavhostchat ŌĐ¸ĐąĶŅĐĩĐŗĐĩĐˇ."
        ),
        "miyahost": (
            "đ <b>ĐĄĐĩĐˇĐĩŅĐąĐžŅŅŌŖ ŅĐĩĐˇ MiyaHost ŌĐ¸ĐąĶŅĐĩĐģĐ´Đĩ</b>. ĐĶĐēĐ¸ĐŊ @miyahost ŌĐ¸ĐąĶŅĐĩĐģĐŗĶĐŊ"
            " ŅĶĐąĶŅĐģĶŅ ŌģĶĐŧ ŅŌŖĐ° ŅŌŖĐ°ĐģŅĐēĐģĐ°Ņ Ō¯ĐˇĐĩĐŊĶ Đ°ĐģŅ ĶŠŅĐĩĐŊ ĐēĐĩŅĐĩĐŗĐĩĐˇ. ĐĄĐĩĐˇĐĩŅĐąĐžŅ ŌĐ¸ĐąĶŅĐĩĐģĐŗĶĐŊ"
            " ŅĶĐąĶŅĐģĶŅ ŌģĶĐŧ ŅŌŖĐ° ŅŌŖĐ°ĐģŅĐēĐģĐ°Ņ ŅŅŅŅĐŊĐ´Đ° ŅĐžŅĐ°ŅĐģĐ°ŅĐŊŅ @miyahost_support"
            " ŌĐ¸ĐąĶŅĐĩĐŗĐĩĐˇ."
        ),
        "language_saved": "đĨ ĐĸĐĩĐģ ŅĐ°ĐēĐģĐ°ĐŊĐŗĐ°ĐŊ!",
        "language": "đĨ ĐĸĐ°ŅĐ°Ņ ŅĐĩĐģĐĩ",
        "btn_support": "đĨˇ Đ¯ŅĐ´ĶĐŧ ŅĐ°ŅŅ",
    }

    async def client_ready(self):
        if self.get("disable_quickstart"):
            raise loader.SelfUnload

        self.mark = (
            lambda: [
                [
                    {
                        "text": self.strings("btn_support"),
                        "url": "https://t.me/hikka_talks",
                    }
                ],
            ]
            + [
                [
                    {
                        "text": "đŠââī¸ Privacy Policy",
                        "url": "https://docs.google.com/document/d/15m6-pb1Eya8Zn4y0_7JEdvMLAo_v050rFMaWrjDjvMs/edit?usp=sharing",
                    },
                    {
                        "text": "đ EULA",
                        "url": "https://docs.google.com/document/d/1sZBk24SWLBLoGxcsZHW8yP7yLncToPGUP1FJ4dS6z5I/edit?usp=sharing",
                    },
                ]
            ]
            + utils.chunks(
                [
                    {
                        "text": (
                            getattr(self, f"strings_{lang}")
                            if lang != "en"
                            else self.strings._base_strings
                        )["language"],
                        "callback": self._change_lang,
                        "args": (lang,),
                    }
                    for lang in [
                        "en",
                        "ru",
                        "it",
                        "de",
                        "uz",
                        "tr",
                        "es",
                        "kk",
                        "tt",
                    ]
                ],
                3,
            )
        )

        self.text = (
            lambda: self.strings("base")
            + (
                "\n"
                + (
                    self.strings("railway")
                    if "RAILWAY" in os.environ
                    else (
                        self.strings("lavhost")
                        if "LAVHOST" in os.environ
                        else (
                            self.strings("miyahost") if "MIYAHOST" in os.environ else ""
                        )
                    )
                )
            ).rstrip()
        )

        await self.inline.bot.send_animation(self._client.tg_id, animation=choice(imgs))
        await self.inline.bot.send_message(
            self._client.tg_id,
            self.text(),
            reply_markup=self.inline.generate_markup(self.mark()),
            disable_web_page_preview=True,
        )

        self.set("disable_quickstart", True)

    async def _change_lang(self, call: BotInlineCall, lang: str):
        self._db.set(translations.__name__, "lang", lang)
        await self.allmodules.reload_translations()

        await call.answer(self.strings("language_saved"))
        await call.edit(text=self.text(), reply_markup=self.mark())
