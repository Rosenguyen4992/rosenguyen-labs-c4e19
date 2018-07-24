from urllib.request import urlopen

#1. Download webpage
url ="http://dantri.com.vn"
# 1.1. Open a connection
conn = urlopen(url)
# 1.2. Read data
data = conn.read()
# # 1.3. Decode
# html_content = data.decode('utf-8')
f = open('dantri.html', 'wb')
f.write(data)
f.close()

# save to file


#2. Extract ROI (Region of Interest)

#3. Extract info

#4. Save data to Excel file