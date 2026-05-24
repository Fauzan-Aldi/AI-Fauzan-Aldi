"""
System tools — time, environment info, shell commands, etc.
"""

import datetime
import platform


def register(mcp):

    @mcp.tool()
    def get_current_time() -> str:
        """Return the current date and time in ISO 8601 format."""
        return datetime.datetime.now().isoformat()

    @mcp.tool()
    def get_system_info() -> dict:
        """Return basic information about the host system."""
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "python_version": platform.python_version(),
        }

    @mcp.tool()
    def cari_uang_mode() -> str:
        """
        Activates 'Cari Uang' (Hustle) mode. Opens Spotify, GitHub, Burp Suite, and Antigravity IDE.
        Use this when the user says 'saya mau cari uang'.
        """
        import webbrowser
        import os
        import subprocess

        try:
            # Open Spotify
            os.system("start spotify:")
            
            # Open GitHub
            webbrowser.open("https://github.com/Fauzan-Aldi")
            
            # Open BurpSuite
            burp_path = r"C:\Program Files\BurpSuiteCommunity\BurpSuiteCommunity.exe"
            if os.path.exists(burp_path):
                subprocess.Popen([burp_path])
            else:
                os.system("start burpsuite")
                
            # Open Antigravity IDE
            antigravity_path = r"C:\Users\Asus\AppData\Local\Programs\Antigravity IDE\Antigravity IDE.exe"
            if os.path.exists(antigravity_path):
                subprocess.Popen([antigravity_path])
                
            return "Workspace is ready, Fauzan. Let's make some money."
        except Exception as e:
            return f"Error activating cari uang mode: {str(e)}"
