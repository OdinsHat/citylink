CityLink Utilities
==================

The following package was developed to help process despatch requests with City Link couriers based in the UK.

It works by using the Mechanize library to navigate the commercial account holders admin area to carry out requests such as:

* Fetch pending collections
* Grab company reference numbers
* Grab CityLink reference numbers
* Get full HTML copy of collection manifest
* Email the manifest

Requirements
------------
The version below have been tested and working. Its possible other earlier and later versions may work.
* [https://pypi.python.org/pypi/mechanize/ Mechanize 0.2.5+]
* [https://pypi.python.org/pypi/lxml lxml 3.3.3+]
* [https://pypi.python.org/pypi/mailer Mailer 0.7+]



Examples
--------

### Email Manifest
```python
import citylink.CityLink

userid = "XXXXXX"
password = "XXXXXX"

cl = CityLink(userid, password)
cl.login()
cl.mail_manifest(emailfrom="from@test.com", emailto="to@test.com")
```

### Get list of CityLink reference codes
```python
import citylink.CityLink

userid = "XXXXXX"
password = "XXXXXX"

cl = CityLink(userid, password)
cl.login()
print(cl.fetch_citylink_refs())
```
