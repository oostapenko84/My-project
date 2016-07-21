__author__ = 'olga.ostapenko'

from model.company import Company


def test_create_company(app):
    app.session.login(username="admin@admin.com", password="12345678")
    app.company.create(
        Company(Company_Name="Test Company vv", CAD_First_Name="FN vv", CAD_Last_Name="LN vv", Email="testvv@test.com",
                Phone="12345678", Fax="12345678", Address="San Francisco", City="San Francisco",
                Zip_Code="12345", Web_Site="www.test.com", Description="test", Points="1000"))
    app.session.logout()
