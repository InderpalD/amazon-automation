import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


#credential obj
credential = ServiceAccountCredentials.from_json_keyfile_name('client_key.json', scope)

client = gspread.authorize(credential)

sheet = client.open('amazon').sheet1

records = sheet.get_all_records()
print(records)
