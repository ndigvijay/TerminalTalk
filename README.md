# TerminalTalk 🌐

Welcome to **TerminalTalk**, your go-to solution for easy and seamless texting over a WAN (Wide Area Network) and LAN (Local Area Network)! Whether you're chatting with friends across the room or across the globe, TerminalTalk makes it simple and enjoyable. 

## 🚀 Overview

**TerminalTalk** is a lightweight chat application that allows users to communicate in real-time using a simple terminal interface. Built using Python's socket programming, it leverages TCP connections for reliable messaging. This project is perfect for learning about networking concepts and building your own messaging system. 

### Key Features:
- 💬 Real-time messaging between users
- 🖥️ Connect over LAN or WAN
- 🛠️ Simple terminal-based user interface
- 🔒 Basic nickname handling for personalization

## 🖥️ Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Basic knowledge of using the terminal/command prompt

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saicharan1901/TerminalTalk.git
   cd TerminalTalk
   ```

## 📡 Running on LAN

To run TerminalTalk on a Local Area Network (LAN), follow these steps:

### Server Setup

1. **Open your terminal and navigate to the project directory:**
   ```bash
   cd TerminalTalk
   ```

2. **Run the server:**
   ```bash
   python server.py
   ```
   * The server will start listening for connections on your local IP address and the specified port (default: 7976).

### Client Setup

1. **On another device connected to the same network, open the terminal.**

2. **Connect to the server using the server's local IP address:**
   ```python
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect(('192.168.x.x', 7976)) # Replace with the server's local IP
   ```

3. **Run the client:**
   ```bash
   python client.py
   ```

### 🏠 Conclusion for LAN
You can now chat with users on the same network! 🎉

## 🌍 Running on WAN

To run TerminalTalk over a Wide Area Network (WAN), follow these steps:

### Step 1: Set Up ngrok

1. **If you haven't already, install `ngrok` using Homebrew:**
   ```bash
   brew install ngrok/ngrok/ngrok
   ```

2. **Authenticate ngrok with your account:**
   ```bash
   ngrok authtoken YOUR_AUTHTOKEN
   ```

### Step 2: Start Your Server

1. **In your terminal, navigate to the project directory:**
   ```bash
   cd TerminalTalk
   ```

2. **Run the server:**
   ```bash
   python server.py
   ```

### Step 3: Expose Your Server with ngrok

1. **Run ngrok to expose your server:**
   ```bash
   ngrok tcp 7976
   ```
   * Note the forwarding address given by ngrok (e.g., `tcp://0.tcp.in.ngrok.io:19049`).

### Step 4: Client Connection

1. **On any device, open the terminal and connect to ngrok's forwarding address:**
   ```python
   client.connect(('0.tcp.in.ngrok.io', 19049)) # Use the address from ngrok
   ```

2. **Run the client:**
   ```bash
   python client.py
   ```

### 🌟 Conclusion for WAN
You can now chat with friends no matter where they are! 🌍💬

## 🤝 Contribution

Feel free to fork the repository and submit pull requests! We welcome contributions to enhance **TerminalTalk**.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

For any questions or suggestions, please reach out at papinenisaicharan@gmail.com.
