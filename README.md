### Flight Deals Notifier

#### Overview

Flight Deals Notifier is a Python program designed to help users find and track the lowest flight prices for their desired travel destinations. The program utilizes the Kiwi API for flight searches, the Sheety API for data storage in Google Sheets, and the Twilio API for sending SMS notifications. It aims to provide users with real-time updates on flight prices, allowing them to seize opportunities when prices drop.

#### Features

1. **Destination Data Management**: The program uses the Sheety API to fetch and update destination data, including IATA codes, from a Google Sheet.

2. **Flight Search**: It leverages the Kiwi API to perform flight searches from London to various destinations, considering factors such as date range and stopovers.

3. **Data Storage**: Flight information, including prices, IATA codes, and travel dates, is stored and managed using a `FlightData` class.

4. **Price Tracking and Notification**: The program compares the current lowest prices with historical prices and sends SMS notifications via Twilio when a lower price is found.

5. **Modular Structure**: The codebase is organized into modular components, such as `FlightSearch`, `DataManager`, `NotificationManager`, and `FlightData`, providing clarity and maintainability.

#### Usage

1. Set up API keys: Obtain and set up API keys for Kiwi, Sheety, and Twilio in the respective environment variables.

2. Install Dependencies: Install the required Python dependencies using `pip install -r requirements.txt`.

3. Run the Program: Execute `main.py` to initiate the flight search and notification process.

#### Dependencies

- `requests`: For making HTTP requests to APIs.
- `twilio`: Twilio API for sending SMS notifications.

#### Note

Ensure that appropriate API keys and environment variables are configured for seamless execution. The program aims to streamline the process of finding and booking affordable flights, keeping users informed about the latest deals.
