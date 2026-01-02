import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AutoGitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Only track Python files
        if event.src_path.endswith(".py"):
            print(f"Detected change in {event.src_path}, pushing to GitHub...")
            os.system("git add .")
            os.system('git commit -m "Auto-update via script"')
            os.system("git push")

if __name__ == "__main__":
    path = "."  # Current folder
    event_handler = AutoGitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Watching for changes in project folder...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
