CityLink Utilities
==================

The following package was developed to help process despatch requests with 
[City Link](https://www.city-link.co.uk/) couriers based in the UK.

They lacked an API for easy management of various functions such as retrieving 
manifests, reference codes, etc.

This package works by using the Mechanize library to navigate your commercial account 
admin area to carry out requests such as:

* Fetch pending collections
* Grab company reference numbers
* Grab CityLink reference numbers
* Get full HTML copy of collection manifest
* Email the manifest

Requirements
------------
The version below have been tested and working. Its possible other earlier and later versions may work.
* [Mechanize 0.2.5+](https://pypi.python.org/pypi/mechanize/) 
* [lxml 3.3.3+](https://pypi.python.org/pypi/lxml) 
* [Mailer 0.7+](https://pypi.python.org/pypi/mailer)



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
