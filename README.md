🌐 Internet Speed Twitter Bot
This Python project automates checking your internet speed and tweets your internet provider if your download/upload speeds fall below a promised threshold. It uses Selenium WebDriver to control a browser, scrape Speedtest results, and interact with Twitter (X.com).

🚀 Features
Automates internet speed tests via Speedtest.net

Compares the actual speed against promised download/upload speeds

Logs into Twitter/X and sends a complaint tweet automatically

Uses environment variables to keep sensitive info secure

🛠️ Technologies Used
Python 3.x

Selenium WebDriver

ChromeDriver

dotenv for managing secrets

📁 Project Structure

  📦 internet-speed-twitter-bot/
├── main.py                     # Main runner script
├── InternetSpeedTwitterBot.py  # Bot class and core logic
├── .env                        # Stores Twitter credentials (ignored by Git)

▶️ How to Use
  1. Clone the repository
     git clone https://github.com/yourusername/internet-speed-twitter-bot.git
     cd internet-speed-twitter-bot
  2. Install required packages
     pip install selenium python-dotenv

  3. Download ChromeDriver

     Download ChromeDriver matching your Chrome version.

     Add the path to ChromeDriver in your .env.
  4. Create a .env file
     TWITTER_EMAIL=your_twitter_email_or_username
     TWITTER_PASSWORD=your_twitter_password
     CHROME_DRIVER_PATH=/path/to/chromedriver
  5. Run the bot
     python main.py

⚠️ Warning
Twitter/X may detect and block automated logins. Use responsibly.

Selenium web scraping is fragile — if Twitter or Speedtest updates their UI, the bot may break.
