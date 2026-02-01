# awesome-osint-thai
A curated list of amazingly awesome OSINT for Thai 😋

## Government/Official Data

*Source of Information for government-classified data*

Most of the data could be bought e.g. [dbd](https://medium.com/incubate-co-th/%E0%B9%81%E0%B8%8A%E0%B8%A3%E0%B9%8C%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%AA%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2%E0%B8%98%E0%B8%B8%E0%B8%A3%E0%B8%81%E0%B8%B4%E0%B8%88%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B9%89%E0%B8%B2-56bdd0987000).

* **[Checkgon](https://checkgon.go.th/)**
  Validate if a bank-wallet-promptpay (financial address), a phone number, and a URL is a suspect of any frauds/suspect.
  You can report here as well.

* **[Department of Business Development](http://datawarehouse.dbd.go.th/)**
  All companies' financial stats include those not in the [SET](https://www.set.or.th/set/mainpage.do?language=en&country=US).

* **[Creden](https://creden.co/creditscore/business/main.html)**
  DBD (Department of Business Development) that could be queried using the person's name.

* **[opencorporates](https://opencorporates.com/)**
  API for DBD company data.

* **[RD Vat Check](https://vsreg.rd.go.th/VATINFOWSWeb/jsp/VATInfoWSServlet#)**
  Check if a VAT company is still operating by Thailand IRS.
  **Input:** Company ID

* **[e-Tax Invoice Search](https://etax.rd.go.th/ETAXSEARCH/normal-person)**
  Search for operators authorized to issue electronic tax invoices and receipts (e-Tax Invoice & e-Receipt system).

* **[Department of Lands](http://dolwms.dol.go.th/tvwebp/)**
  Identify all land properties to buy.

* **[Family Name Check](http://www.khonthai.com/online/WCHECKLNAME/)**
  Check if the family name is valid to create.

* **[Police Official Check](https://www.thaipolice.net/)**
  Verify if a given name/surname is a real police officer.
  **Returns:** Rank and department

* **[Revenue Department API](https://zenateconnect.github.io/RevenueDepartmentService/)**
  Obtain more info about a tax ID/national ID.
  **Input:** Tax ID or National ID

* **[konjingjing](https://github.com/ninyawee/konjingjing) (1mo)**
  Thai Citizen ID validation written in Rust, with Python and Node.js bindings.
  **Features:** `verify_id(id)` for validation, `get_id_meaning(id)` for extracting meaning (person type, province, amphoe, validity)

* **[national-id-meaning](https://github.com/heypoom/national-id-meaning) (⚠️ 3yr)** (⚠️ 2yr 9mo)
  Understand info behind national ID numbering.

* **[CheckMD](https://checkmd.tmc.or.th/)**
  Check if a name is a legal doctor.
  **Returns:** Doctor's specialties

* **[OIC Insurance License Verification](https://smart.oic.or.th/eservice/Menu1)**
  Verify if someone has a license to sell insurance from the Office of Insurance Commission (สำนักงานคณะกรรมการกำกับและส่งเสริมการประกอบธุรกิจประกันภัย).
  **Input:** Firstname, Surname, ID, or National ID

* **[NHSO Health Lookup](https://srmcitizen.nhso.go.th/)**
  Look up NHSO health information.
  **Input:** ID and date of birth

* **[Royal Thai Government Gazette](https://ratchakitcha.soc.go.th/)**
  Check if a person or company is in default/bankruptcy or has received royal decorations, ranks, or titles.
  Also includes government announcements, royal decrees, and official legal notices.

* **[TH Portal](https://thportal.bora.dopa.go.th/#/)**
  Centralize individual data including:
  - Living place
  - Driving license
  - Lands owned
  - Cars owned
  - Military notes

* **[ThaiD App](https://play.google.com/store/apps/details?id=th.go.dopa.bora.dims.ddopa&hl=en&pli=1)**
  Government Authentication (Sign in with ThaiD) for Thai citizens.
  Provides access to a lot of services by Ministry.

## OSINT Tools by Thais

* **[conan](https://github.com/tomhoma/conan) (2mo)** (28d)
  Blazingly fast username scanner written in Rust.

* **[Passkey-Raider](https://github.com/siamthanathack/Passkey-Raider) (10mo)** (7mo)
  Burp Suite extension for testing Passkey authentication implementations.

## Civic Tech

* **[act ai](https://actai.co/)**
  Check if a person is involved in any government projects.
  **Database:** 40 million projects
  **Input:** Name

## Gaming

*What do Thais play*

* **[Garena](https://www.garena.co.th/)**
  Thailand's 1st Gaming Distributor/Representative for online mobile gaming and PC.
  **Games:** LoL, RoV

* **[Steam](https://store.steampowered.com/)**
  The major PC gaming platform.

## Mobile Operator

*Mobile Operators in Thai*

* **[AIS](https://myais.ais.co.th/)**
  Thailand's 1st mobile operator.

* **[True](https://www.truecorp.co.th/)**

* **[DTAC](https://www.dtac.co.th/)**

## Banking

* **[SCB Easy](https://www.scbeasy.com/v1.4/site/presignon/index.asp)**
  The Siam Commercial Bank Personal Login Page.

## Population Data

*Related to the whole population instead of individuals - aggregate data*

* **[Thai Open Data](https://data.go.th)**
  The Demographics of Thailand.
  **Note:** Very bad in completeness and uniform format
  **APIs:** [Available](https://api.data.go.th)

* **[Bank Of Thailand](https://apiportal.bot.or.th/bot/public/)** __Recommended__
  The Economic Data from the Bank of Thailand.

* **[Official Statistics Registration Systems](http://stat.bora.dopa.go.th)**
  The Demographics of Thailand, separated by provinces.

## Others

* **[ศูนย์กลางข้อมูลให้ธุรกิจติดต่อราชการแบบเบ็ดเสร็จ](https://biz.govchannel.go.th/)**
  Central Government Business Data Platform.

* **[ศูนย์กลางแลกเปลี่ยนข้อมูลภาครัฐ](https://gdx.dga.or.th/Account/Login?ReturnUrl=%2f)**
  Data Channel for Government Officials.

## Metropolis

### Mueang, Udon Thani

* **[Live Stream](http://streaming.udoncity.go.th/index.php)**
  Live Stream for 20+ main street areas.

* **[BKK Traffic Cams](http://www.bmatraffic.com/index.aspx)**
  Very low FPS live stream of whole BKK traffic grid.

## Well-Maintained OSINT

* **[PhoneInfoga](https://github.com/sundowndev/PhoneInfoga) (25d)** (11d)
  International phone number OSINT.

* **[TorBot](https://github.com/DedSecInside/TorBot) (23d)** (2d)
  TOR Network spider bot.

* **[Photon](https://github.com/s0md3v/Photon) (1mo)** (7mo)
  Fast Domain OSINT scraper.

* **[Osintgram](https://github.com/Datalux/Osintgram) (5mo)** (2mo)
  Instagram OSINT.

* **[iKy](https://github.com/kennbroorg/iKy) (⚠️ 1yr 6mo)** (⚠️ 1yr 3mo)
  Email-based OSINT with futuristic interface.

* **[sn0int](https://github.com/kpcyrd/sn0int) (1yr)** (9mo)
  OSINT in RUST with complex domain exploration.

* **[spiderfoot](https://github.com/smicallef/spiderfoot) (⚠️ 1yr 1mo)** (10mo)
  Big OSINT.

* **[awesome-osint](https://github.com/jivoi/awesome-osint) (4d)** (3d)
  Gives an overview picture, many are not maintained.

# Contributing

Feel free to update this list by creating a pull request 🥰

