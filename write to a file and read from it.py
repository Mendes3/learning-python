from urllib import request
fw = open("sample.txt", 'w')   # creates a file in write mode
fw.write("hello,its bucky.\n")  # writing to a file
fw.write("bucky is crazy.\n")
fw.close()

# to read from the file
fr = open("sample.txt", 'r')  # opening file in read mode
text = fr.read()  # reads from the file and stores in text
print(text)
fr.close()

# reading any file from internet and saving data to our computer
# simple google

google_csv = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587807237&period2=1619343237&interval=1d&events=history&includeAdjustedClose=true"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)   # TO GET INTERNET ACCESS
    csv = response.read()                  # read from the file
    csv_str = str(csv)
    lines = csv_str.split("\\n")  # takes a string abd breaks it up
    dest_url = r"goog.csv"         # giving a destination address to save to our computer
    fr = open(dest_url,"w")       # opening a file to write to it
    for i in lines:
        fr.write(i + "\n")
    fr.close()


download_stock_data(google_csv)


