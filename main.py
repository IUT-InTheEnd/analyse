# Interface et deux boutons, un pour démarrer le clean up et l'autre pour lancer les analyses
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def install_dependencies():
    requirements_path = os.path.join(os.getcwd(), 'requirements.txt')
    subprocess.run(['pip3', 'install', '-r', requirements_path])

def start_cleanup():
    messagebox.showinfo("Clean Up", "Le processus de nettoyage a démarré.")
    script_dir = os.path.join(os.getcwd(), 'script', 'clean')
    processes = []
    for script in os.listdir(script_dir):
        if script.endswith('.py'):
            script_path = os.path.join(script_dir, script)
            process = subprocess.Popen(['python3', script_path])
            processes.append(process)
    for process in processes:
        process.wait()
    messagebox.showinfo("Clean Up", "Le processus de nettoyage est terminé.")

def start_analysis():
    messagebox.showinfo("Analysis", "Le processus d'analyse a démarré.")
    script_dir = os.path.join(os.getcwd(), 'script', 'analyse')
    for script in os.listdir(script_dir):
        if script.endswith('.py'):
            script_path = os.path.join(script_dir, script)
            subprocess.run(['python3', script_path])
    messagebox.showinfo("Analysis", "Le processus d'analyse est terminé.")


root = tk.Tk()
root.title("Interface de Nettoyage et d'Analyse")
root.geometry("300x150")
requirements_button = tk.Button(root, text="Installer les Dépendances", command=install_dependencies)
requirements_button.pack(pady=10)
cleanup_button = tk.Button(root, text="Démarrer le Clean Up", command=start_cleanup)
cleanup_button.pack(pady=10)
analysis_button = tk.Button(root, text="Lancer les Analyses", command=start_analysis)
analysis_button.pack(pady=10)
root.mainloop()
