Rapidfresh is an advanced Linux system cleanup tool designed to perform various deep cleaning operations, secure file shredding, and network monitoring. It offers both a command-line interface (CLI) and a graphical user interface (GUI), enabling users to easily maintain and optimize their Linux systems for privacy and performance.
Features

    Clear Terminal History: Erase all traces of previous terminal commands.
    Clean Temporary Files: Remove unnecessary files from temporary directories.
    Clear Caches: Delete application cache files to reclaim disk space.
    Shred Sensitive Files: Securely delete sensitive files like SSH keys and system configurations.
    Clean Logs: Shred system log files to ensure privacy.
    Flush Network Settings: Reset network settings to enhance privacy and clear any unwanted configurations.
    Optimize TCP Protocols: Tweak and optimize TCP settings to improve network performance.
    Network Packet Visualizer: Real-time visualization of incoming and outgoing network packets using tcpdump.
    GUI Interface: An intuitive graphical interface for easy cleanup and monitoring.

Installation

    Clone the repository:

git clone https://github.com/yourusername/rapidfresh.git
cd rapidfresh

Install dependencies:

Make sure you have Python 3, Tkinter, and the Click library installed on your system. You can install required Python packages using:

pip install -r requirements.txt

You may need to install system dependencies like tcpdump and shred if they're not available on your system.

Run the tool:

    Command-line interface: Use the CLI to run specific cleaning functions.

python rapidfresh.py terminal  # To clear terminal history
python rapidfresh.py temp      # To clean temporary files
python rapidfresh.py cache     # To clear caches
python rapidfresh.py shred     # To shred sensitive files
python rapidfresh.py logs      # To clean logs
python rapidfresh.py network   # To flush network settings
python rapidfresh.py optimize_tcp  # To optimize TCP settings

Graphical user interface: Launch the GUI for easy cleanup with buttons and network monitoring.

        python rapidfresh.py gui

Usage
Command-Line Interface (CLI)

You can use the following commands to clean and optimize your system:

python rapidfresh.py terminal    # Clear terminal history
python rapidfresh.py temp        # Clean temporary files
python rapidfresh.py cache       # Clear caches
python rapidfresh.py shred       # Shred sensitive files
python rapidfresh.py logs        # Clean and shred logs
python rapidfresh.py network     # Flush network settings
python rapidfresh.py optimize_tcp  # Optimize TCP settings

Graphical User Interface (GUI)

To launch the GUI, use:

python rapidfresh.py gui

The GUI provides buttons to trigger each cleaning operation and displays real-time network packet information. You can monitor the network activity while performing clean-up tasks.
Requirements

    Python 3.x
    Tkinter for GUI support
    tcpdump for network monitoring
    shred for secure file deletion
    click for command-line interface

Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Make your changes.
    Commit your changes (`git commit -am 'Add

your feature'). 5. Push to the branch (git push origin feature/your-feature`). 6. Open a Pull Request.

Please ensure your code follows the PEP 8 style guidelines and is well-documented.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Click: A Python package for creating command-line interfaces.
    Tkinter: A standard Python library for building graphical user interfaces.
    Shred: A command-line tool for securely deleting files.
    Tcpdump: A command-line packet analyzer used for monitoring network traffic.
