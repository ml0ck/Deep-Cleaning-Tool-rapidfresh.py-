import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
import click
import threading
import time

# --- Advanced Cleaning Functions ---
def clear_terminal_history():
    os.system('history -c')  # Clear Bash history
    os.system('cat /dev/null > ~/.bash_history')
    os.system('rm -f ~/.zsh_history')
    click.echo("Terminal history cleared!")

def clean_temp_files():
    temp_dirs = ['/tmp', '/var/tmp']
    for temp_dir in temp_dirs:
        subprocess.run(['rm', '-rf', f'{temp_dir}/*'], check=False)
    click.echo("Temporary files cleaned!")

def clean_cache():
    cache_dirs = ['~/.cache', '/var/cache']
    for cache_dir in cache_dirs:
        subprocess.run(['rm', '-rf', os.path.expanduser(cache_dir)], check=False)
    click.echo("Caches cleared!")

def shred_sensitive_files():
    sensitive_files = [
        '~/.ssh/known_hosts',
        '~/.ssh/id_rsa',
        '~/.ssh/id_rsa.pub',
        '/etc/hosts',
    ]
    for file in sensitive_files:
        expanded_file = os.path.expanduser(file)
        if os.path.exists(expanded_file):
            subprocess.run(['shred', '-u', expanded_file], check=False)
    click.echo("Sensitive files securely shredded!")

def clean_logs():
    log_dirs = ['/var/log']
    for log_dir in log_dirs:
        subprocess.run(['find', log_dir, '-type', 'f', '-exec', 'shred', '-u', '{}', ';'], check=False)
    click.echo("Logs cleaned and shredded!")

def network_flush():
    os.system('sudo iptables -F')
    os.system('sudo iptables -X')
    os.system('sudo iptables -t nat -F')
    os.system('sudo iptables -t nat -X')
    os.system('sudo iptables -t mangle -F')
    os.system('sudo iptables -t mangle -X')
    click.echo("Network settings flushed!")

def restart_and_optimize_tcp():
    # Restart TCP protocols
    os.system('sudo sysctl -w net.ipv4.tcp_syncookies=1')
    os.system('sudo sysctl -w net.ipv4.tcp_fin_timeout=15')
    os.system('sudo sysctl -w net.ipv4.tcp_keepalive_time=300')
    os.system('sudo sysctl -w net.core.rmem_max=16777216')
    os.system('sudo sysctl -w net.core.wmem_max=16777216')
    os.system('sudo sysctl -w net.ipv4.tcp_rmem="4096 87380 16777216"')
    os.system('sudo sysctl -w net.ipv4.tcp_wmem="4096 65536 16777216"')
    os.system('sudo sysctl -w net.core.netdev_max_backlog=5000')
    os.system('sudo sysctl -w net.core.somaxconn=1024')
    click.echo("TCP protocols restarted and optimized!")

def monitor_network_packets(callback):
    """Monitors incoming and outgoing packets using a command-line tool."""
    process = subprocess.Popen(
        ['sudo', 'tcpdump', '-l', '-n'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    try:
        for line in iter(process.stdout.readline, ''):
            callback(line.strip())
    finally:
        process.terminate()

# --- CLI Interface with Click ---
@click.group()
def cli():
    "Advanced cleaning tool for Linux."
    pass

@cli.command()
def terminal():
    "Clear terminal command traces."
    clear_terminal_history()

@cli.command()
def temp():
    "Clean temporary files."
    clean_temp_files()

@cli.command()
def cache():
    "Clear caches."
    clean_cache()

@cli.command()
def shred():
    "Shred sensitive files."
    shred_sensitive_files()

@cli.command()
def logs():
    "Clean and shred log files."
    clean_logs()

@cli.command()
def network():
    "Flush network settings."
    network_flush()

@cli.command()
def optimize_tcp():
    "Restart and optimize TCP protocols."
    restart_and_optimize_tcp()

@cli.command()
def gui():
    "Launch the graphical user interface."
    launch_gui()

# --- GUI Interface ---
def launch_gui():
    def run_cleanup(action):
        if action == 'terminal':
            clear_terminal_history()
        elif action == 'temp':
            clean_temp_files()
        elif action == 'cache':
            clean_cache()
        elif action == 'shred':
            shred_sensitive_files()
        elif action == 'logs':
            clean_logs()
        elif action == 'network':
            network_flush()
        elif action == 'tcp':
            restart_and_optimize_tcp()
        messagebox.showinfo("Success", f"{action.capitalize()} completed!")

    def update_packet_visualizer(line):
        # Simplify and format the packet information
        if "IP" in line:
            formatted_line = "\n".join(line.split())  # Simplify display for better readability
            visualizer_text.insert(tk.END, f"{formatted_line}\n\n")
            visualizer_text.see(tk.END)

    def start_packet_monitor():
        threading.Thread(target=monitor_network_packets, args=(update_packet_visualizer,), daemon=True).start()

    root = tk.Tk()
    root.title("Advanced Cleaning Tool")
    root.geometry("900x600")

    # Left Pane for Packet Visualizer
    left_frame = tk.Frame(root, width=450, height=600, bg="black")
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    tk.Label(left_frame, text="Network Packet Visualizer", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=5)

    visualizer_text = tk.Text(left_frame, bg="black", fg="lime", font=("Courier", 10), wrap=tk.WORD)
    visualizer_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    start_packet_monitor()

    # Right Pane for Actions
    right_frame = tk.Frame(root, width=450, height=600)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    tk.Label(right_frame, text="Deep Cleaning Tool", font=("Arial", 16, "bold"), fg="darkblue").pack(pady=10)

    tk.Button(right_frame, text="Clear Terminal History", command=lambda: run_cleanup('terminal'), bg="lightblue").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Clean Temporary Files", command=lambda: run_cleanup('temp'), bg="lightgreen").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Clear Caches", command=lambda: run_cleanup('cache'), bg="lightcoral").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Shred Sensitive Files", command=lambda: run_cleanup('shred'), bg="orange").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Clean and Shred Logs", command=lambda: run_cleanup('logs'), bg="yellow").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Flush Network Settings", command=lambda: run_cleanup('network'), bg="violet").pack(fill=tk.X, pady=5)
    tk.Button(right_frame, text="Restart and Optimize TCP", command=lambda: run_cleanup('tcp'), bg="cyan").pack(fill=tk.X, pady=5)

    tk.Button(right_frame, text="Exit", command=root.quit, bg="grey").pack(fill=tk.X, pady=10)

    tk.Label(right_frame, text="All rights reserved to @ml0ck", font=("Arial", 10), fg="gray").pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    cli()
