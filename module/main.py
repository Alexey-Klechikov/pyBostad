import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta
from .log import Log
from typing import List


@dataclass
class Account:
    login: str
    password: str
    username: str


def ping_generic_schema(
    message: str,
    url: str,
    base: str,
    accounts: List[Account],
    static_fields: dict = {},
    dynamic_fields: List[str] = [],
) -> str:
    try:
        for account in accounts:
            with requests.session() as s:
                headers = {
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                }

                info = {}
                for k, v in static_fields.items():
                    info[k.format(base=base)] = v.format(
                        login=account.login, password=account.password
                    )

                r_get = s.get(url)
                soup = BeautifulSoup(r_get.text, "html.parser")

                for field in dynamic_fields:
                    info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                response_post = s.post(url, data=info, headers=headers)
                soup = BeautifulSoup(response_post.text, "html.parser")

                success = True if str(soup).find(account.username) > 0 else False
                message += (
                    ("(OK - " if success else "(Error - ") + account.username + ") "
                )
                message = ("" if success else "---") + message

    except:
        message = "---" + message

    return message


class Walk_Bostad:
    def __init__(self):
        self.log = []

        # Generic schema
        self._heimstaden()
        self._rikshem()
        self._bostaden_umea()
        self._aranas()
        self._lkf()
        self._einar_mattsson()
        self._forvaltaren()
        self._derome_fastighet()
        self._sollentuna_hem()
        self._hasselby_hem()
        self._haninge_bostader()
        self._vasby_hem()
        self._heba_fast()
        self._ekero_bostader()

        # Custom schema
        self._wallenstram()
        self._tyreso_bostader()
        self._upplands_brohus()


    def _heimstaden(self):
        url = "https://mitt.heimstaden.com/mina-sidor/logga-in"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ]

        message = ping_generic_schema(
            "Global, HeimStaden: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _rikshem(self):
        url = "https://minasidor.rikshem.se/mina-sidor/logga-in/Default.aspx"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$"
        accounts = [
            Account("198904041236", "C804BBa0", "Alexey Klechikov"),
            Account("198903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ]

        message = ping_generic_schema(
            "Global, RiksHem: ", url, base, accounts, static_fields, dynamic_fields
        )
        self.log.append(message)

    def _bostaden_umea(self):
        url = "https://www.bostaden.umea.se/mina-sidor/logga-in"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("Alexey", "C804BBa0", "Alexey Klechikov"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
            "{base}hdnSelectedTab": "p",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
        ]

        message = ping_generic_schema(
            "Umea, Bostaden: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _aranas(self):
        url = "https://marknad.aranas.se/User/MyPagesLogin.aspx"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ]

        message = ping_generic_schema(
            "Goteborg, Aranas: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _lkf(self):
        url = "https://minasidor.lkf.se/User/MyPagesLogin.aspx"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ]

        message = ping_generic_schema(
            "Lund, lkf: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _einar_mattsson(self):
        url = "https://minasidor.einarmattsson.se/User/MyPagesLogin.aspx"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ]

        message = ping_generic_schema(
            "Stockholm, EinarMattsson: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _forvaltaren(self):
        url = "https://www.forvaltaren.se/mina-sidor/logga-in"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]

        message = ping_generic_schema(
            "Stockholm, Forvaltaren: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _wallenstram(self):
        message, ACCOUNTS = "Global, Wallenstam: ", [
            ["alexey.klechikov@gmail.com", "=Munk6V7", "Alexey Klechikov"],
            ["elena.belan@hotmail.com", "GForward!5", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.wallenstam.se/sv/mina-sidor/logga-in/Login/"

                with requests.session() as s:
                    # 1 - Login
                    info = {"Username": account[0], "Password": account[1]}
                    s.post(URL, data=info)  # Login

                    # 2 - Kö
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, "html.parser")

                    # 3 - Update kö
                    info = {
                        "ViewModel.FormView.UserId": soup.find(
                            "input", attrs={"id": "ViewModel_FormView_UserId"}
                        )[
                            "value"
                        ],  # type: ignore
                        "renewButton": "Förnya köplats",
                    }
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/UpdateQueue/"
                    s.post(URL, data=info)  # Update queue

                    # 4 - Check
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _derome_fastighet(self):
        url = "https://minasidor.deromefastighet.se/Account/Login?returnUrl="
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        }
        dynamic_fields = ["__RequestVerificationToken"]

        message = ping_generic_schema(
            "Global, DeromeFastighet: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _vasby_hem(self):
        url = "https://www.vasbyhem.se/Account/Login"
        base = ""
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "UserID": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        }
        dynamic_fields = ["__RequestVerificationToken"]

        message = ping_generic_schema(
            "Stockholm, HaningeBostader: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _upplands_brohus(self):
        message, ACCOUNTS = "Stockholm, Upplands-Brohus: ", [
            ["198904041236", "C804BBa0", "Alexey Klechikov"],
            ["elbl0001", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://marknad.upplands-brohus.se/pgLogin.aspx"

                with requests.session() as s:
                    info = {
                        "__EVENTTARGET": "DoLogin",
                        "__EVENTARGUMENT": "{"
                        + f'"method":"LOGIN","username":"{account[0]}","password":"{account[1]}"'
                        + "}",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")
                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _heba_fast(self):
        url = "https://www.hebafast.se/mina-sidor/logga-in"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ]

        message = ping_generic_schema(
            "Stockholm, HebaFast: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _hasselby_hem(self):
        url = "https://bostad.hasselbyhem.se/User/MyPagesLogin.aspx"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ]

        message = ping_generic_schema(
            "Stockholm, HasselbyHem: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _ekero_bostader(self):
        url = "https://minasidor.ekerobostader.se/mina-sidor/logga-in"
        base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        ]
        static_fields = {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        }
        dynamic_fields = [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ]

        message = ping_generic_schema(
            "Stockholm, EkeroBostader: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _haninge_bostader(self):
        url = "https://minasidor.haningebostader.se/"
        base = ""
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        }
        dynamic_fields = ["__RequestVerificationToken"]

        message = ping_generic_schema(
            "Stockholm, HaningeBostader: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _sollentuna_hem(self):
        url = "https://minasidor.sollentunahem.se/mina-sidor/logga-in"
        base = ""
        accounts = [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ]
        static_fields = {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        }
        dynamic_fields = ["__RequestVerificationToken"]

        message = ping_generic_schema(
            "Stockholm, SollentunaHem: ",
            url,
            base,
            accounts,
            static_fields,
            dynamic_fields,
        )
        self.log.append(message)

    def _tyreso_bostader(self):
        message, ACCOUNTS = "Stockholm, TyresoBostader: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.tyresobostader.se/mina-sidor/logga-in"
                with requests.session() as s:
                    # Login
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)

                    # Update
                    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$"

                    info = {
                        f"{base}txtNoOfAdults": "2",
                        f"{base}txtNoOfChildren": "1",
                        f"{base}chkAreas$0": "AREA_213",
                        f"{base}chkAreas$8": "AREA_212",
                        f"{base}chkAreas$16": "AREA_229",
                        f"{base}chkAreas$1": "AREA_211",
                        f"{base}chkAreas$9": "AREA_194",
                        f"{base}chkAreas$17": "AREA_208",
                        f"{base}chkAreas$2": "AREA_198",
                        f"{base}chkAreas$10": "AREA_533",
                        f"{base}chkAreas$18": "AREA_195",
                        f"{base}chkAreas$3": "AREA_207",
                        f"{base}chkAreas$11": "AREA_205",
                        f"{base}chkAreas$19": "AREA_209",
                        f"{base}chkAreas$4": "AREA_227",
                        f"{base}chkAreas$12": "AREA_222",
                        f"{base}chkAreas$20": "AREA_496",
                        f"{base}chkAreas$5": "AREA_223",
                        f"{base}chkAreas$13": "AREA_210",
                        f"{base}chkAreas$21": "AREA_206",
                        f"{base}chkAreas$6": "AREA_203",
                        f"{base}chkAreas$14": "AREA_199",
                        f"{base}chkAreas$22": "AREA_202",
                        f"{base}chkAreas$7": "AREA_196",
                        f"{base}chkAreas$15": "AREA_197",
                        f"{base}chkAreas$23": "AREA_201",
                        f"{base}txtMaxCost": "10000",
                        f"{base}drpMinRooms": "2",
                        f"{base}drpMaxRooms": "3",
                        f"{base}rblConsent": "1",
                        f"{base}rblSubscribe": "0",
                        f"{base}btnSave": "Spara",
                    }
                    URL = "https://www.tyresobostader.se/mina-sidor/intresseanmalan/lagenhet"

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)


def run():
    walk_obj = Walk_Bostad()
    Log(walk_obj.log)
