
# Vulnerability Scanner Project

This project is a Flask-based web application designed to scan websites for vulnerabilities using various tools such as:

- Nikto
- Nmap
- Sublist3r
- Dirb

## Requirements

1. Python 3.x
2. Flask
3. Nikto
4. Nmap
5. Sublist3r
6. Dirb

You can install the necessary dependencies using pip:

```
pip install Flask
```

Additionally, you need to install the tools:

- Nikto: https://cirt.net/Nikto2
- Nmap: https://nmap.org/
- Sublist3r: https://github.com/aboul3la/Sublist3r
- Dirb: https://github.com/v0re/dirb

## How to Run the Application

1. Clone this repository or download the ZIP file.
2. Navigate to the project directory.
3. Install the dependencies as mentioned above.
4. Run the Flask application:
   
   ```
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000`.

## Authentication

To access the web interface, you will need to enter the following password:

```
kader11000
```

## Scanning Websites

1. Enter the target website URL.
2. Select the scanning tool you want to use (Nikto, Nmap, Sublist3r, or Dirb).
3. Press "Start Scan" to initiate the scan.
4. View the results in the terminal-like interface.
5. Optionally, you can download the scan results as a text file.

## Notes

- This application is intended for educational purposes and responsible security testing only.
- Make sure you have permission to scan the websites you target.

