
#!/bin/bash

echo "-------------------------------------------"
echo "Vulnerability Scanner Setup"
echo "By: kader11000"
echo "-------------------------------------------"

read -p "Do you want to install required tools (nmap, nikto, sublist3r, dirb)? [y/n]: " install_tools

# Python requirements
echo "[*] Installing Python dependencies..."
pip install -r requirements.txt
echo "[+] Python packages installed."

if [[ "$install_tools" == "y" || "$install_tools" == "Y" ]]; then
    echo "[*] Installing system tools..."

    # Install Nmap
    if ! command -v nmap &> /dev/null; then
        echo "[*] Installing nmap..."
        sudo apt-get install -y nmap
    else
        echo "[=] nmap is already installed."
    fi

    # Install Nikto
    if [ ! -d "/opt/nikto" ]; then
        echo "[*] Installing Nikto..."
        sudo git clone https://github.com/sullo/nikto.git /opt/nikto
        sudo ln -s /opt/nikto/program/nikto.pl /usr/local/bin/nikto
    else
        echo "[=] Nikto is already installed."
    fi

    # Install Sublist3r
    if [ ! -d "/opt/Sublist3r" ]; then
        echo "[*] Installing Sublist3r..."
        sudo git clone https://github.com/aboul3la/Sublist3r.git /opt/Sublist3r
        pip install -r /opt/Sublist3r/requirements.txt
        sudo ln -s /opt/Sublist3r/sublist3r.py /usr/local/bin/sublist3r
    else
        echo "[=] Sublist3r is already installed."
    fi

    # Install Dirb
    if ! command -v dirb &> /dev/null; then
        echo "[*] Installing dirb..."
        sudo apt-get install -y dirb
    else
        echo "[=] dirb is already installed."
    fi

    echo "[+] All tools installed."
else
    echo "[=] Skipping system tools installation."
fi

echo "[✔] Setup complete. Run the app with: python app.py"
