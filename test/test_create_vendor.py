__author__ = 'olga.ostapenko'

from model.vendor import Vendor

def test_create_vendor(app):
    app.session.login(username="admin@admin.com", password="12345678")
    app.vendor.create(
        Vendor(Company_Name="Test Company vv", Phone="12345678", Address="San Francisco", City="San Francisco",
               Zip_Code="12345", Web_Site="www.test.com", Description="test", VAD_First_Name="VAD First Name vv",
               VAD_Last_Name="VAD Last Name vv", Email="testvv@test.com", VAD_Phone="12345678"))
    app.session.logout()
