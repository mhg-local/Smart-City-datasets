import sqlite3
import urllib.request, urllib.parse, urllib.error
import json
import ssl

conn = sqlite3.connect('Addresses.sqlite')
cur = conn.cursor()


class RetrieveAddress:
    def __init__(self):
        cur.executescript('''
           create table if not exists Addresses (
                id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT unique,
                Address     TEXT,
                FormattedAddress   TEXT
            );
            ''')
        conn.commit()

    def getFormattedAddress(self, address, *addresses):

        for item in addresses:
            address += " "
            address += item

        api_key = False

        if self.addressExists(address):
            return self.getFormattedAddressFromSQL(address)

        else:
            if api_key is False:
                api_key = 42
                serviceurl = 'http://py4e-data.dr-chuck.net/json?'
            else:
                serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            if len(address) < 1: return
            parms = dict()
            parms['address'] = address
            if api_key is not False: parms['key'] = api_key
            url = serviceurl + urllib.parse.urlencode(parms)

            # print('Retrieving', url)
            uh = urllib.request.urlopen(url, context=ctx)
            data = uh.read().decode()
            # print('Retrieved', len(data), 'characters')

            try:
                js = json.loads(data)
            except:
                js = None

            if not js or 'status' not in js or js['status'] != 'OK':
                print('==== Failure To Retrieve ====')
                print(data)
                return
            formattedAddress = js["results"][0]["formatted_address"]
            self.addAddressToSQL(address, formattedAddress)
            return formattedAddress

    def addAddressToSQL(self, address, formattedAddress):
        cur.execute('''INSERT OR IGNORE INTO Addresses (Address, FormattedAddress)
                            VALUES ( ?, ?)''', (address, formattedAddress))

        conn.commit()

    @staticmethod
    def addressExists(address):
        sqlstr = 'SELECT Address FROM Addresses'
        for row in cur.execute(sqlstr):
            if address == row[0]:
                return True
        return False

    @staticmethod
    def getFormattedAddressFromSQL(address):
        sqlstr = 'SELECT Address, FormattedAddress FROM Addresses'
        for row in cur.execute(sqlstr):
            if address == row[0]:
                return row[1]
