Carousell Product Tracker & Email Notifier
A Python script that scrapes product listings from Carousell.sg based on a search keyword and sends email alerts for new items matching specified price ranges and recency.

🔑 Keywords
Keyword	Description
requests	HTTP library used to fetch HTML content from Carousell
BeautifulSoup	Library used to parse and navigate HTML content
html5lib	Parser used with BeautifulSoup for reliable HTML interpretation
smtplib	Python module to send emails via SMTP
MIMEText	Formats email content for HTML/plain text emails
sys.argv	Command-line argument access to receive query and price range
query	The keyword to search for on Carousell
name[]	List storing scraped product names
price[]	List storing corresponding prices (e.g., "S$800")
day[]	List storing listing age (e.g., "2 hours ago")
Url[]	List storing complete product URLs
sc()	Function to scrape products based on query
crawl()	Function to filter products, compare prices, and trigger email if matched
eml()	Sends an email alert with product details
open(query, "a")	Keeps a log file to avoid repeat notifications for already sent products

🚀 Features
🔍 Scrapes product data (name, price, age, URL) from Carousell

📊 Filters listings by min/max price

⏱ Detects "fresh" listings (e.g., posted "minutes ago" or "1 hour ago")

📧 Sends alert emails using Gmail SMTP

💾 Prevents duplicate emails using local file logging

⚙️ Usage
bash
Copy code
python script.py <search_keyword> [min_price max_price]
Examples
bash
Copy code
python script.py iphone
python script.py "macbook pro" 800 2000
📬 Email Configuration
SMTP Server: smtp.gmail.com

Port: 587 (TLS)

Email: newproductremind@gmail.com

Password: Stored in plaintext in script (⚠️ not secure — use environment variables or .env)

💡 Tip: Enable App Passwords if using Gmail 2FA.

📁 Output
Log file saved as <query>.txt

Sent email contains:

makefile
Copy code
Name: iPhone 14 Pro
Url: https://carousell.sg/p/iphone-14-pro-123456
📄 How It Works
sc(query):

Constructs the search URL

Extracts product info from <a> and <p> tags

Collects names, prices, dates, and links

crawl(query, min_price, max_price):

Checks if each product's price is within range

Verifies if the product is recently posted

Skips if the product was already notified

Sends an email and logs the product

eml():

Formats the email content

Sends using SMTP
