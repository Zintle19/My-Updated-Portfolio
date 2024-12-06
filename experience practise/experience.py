import tkinter as tk

def save_fitness_data(fitness_level):
    try:
        with open("FitnessData.txt", "a") as file:
            file.write(f"Fitness Level: {fitness_level}\n")
    except Exception as e:
        pass

def open_workout_schedule(fitness_level):
    root.destroy()
    
    workout_window = tk.Tk()
    workout_window.title("Workout Schedule")
    workout_window.geometry("1200x800")  # Enlarged size for desktop
    workout_window.configure(bg="#f0f8ff")

    schedule_label = tk.Label(workout_window, text=f"Workout Schedule for {fitness_level}", 
                              font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#4682b4")
    schedule_label.pack(pady=30)

    info_label = tk.Label(workout_window, text="This is where the workout schedule will be displayed.", 
                          font=("Helvetica", 24), bg="#f0f8ff", fg="#000000")
    info_label.pack(pady=20)

    back_button = tk.Button(workout_window, text="Back", font=("Helvetica", 18), bg="#4682b4", fg="white", command=workout_window.destroy)
    back_button.pack(pady=20)

    workout_window.mainloop()

def select_fitness_level(level):
    fitness_label.config(text=f"You selected: {level}")
    save_fitness_data(level)
    open_workout_schedule(level)

def go_back():
    root.destroy()

root = tk.Tk()
root.title("Fitness Tracker Experience")
root.geometry("1200x800")  # Enlarged size for desktop
root.configure(bg="#f0f8ff")

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=50)

heading_label = tk.Label(frame, text="Choose Your Exercise Level", font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#4682b4")
heading_label.pack(pady=10)

beginner_button = tk.Button(frame, text="Beginner", font=("Helvetica", 18), bg="#7fff00", width=15, command=lambda: select_fitness_level("Beginner"))
beginner_button.pack(pady=10)

intermediate_button = tk.Button(frame, text="Intermediate", font=("Helvetica", 18), bg="#ff8c00", width=15, command=lambda: select_fitness_level("Intermediate"))
intermediate_button.pack(pady=10)

advanced_button = tk.Button(frame, text="Advanced", font=("Helvetica", 18), bg="#ff6347", width=15, command=lambda: select_fitness_level("Advanced"))
advanced_button.pack(pady=10)

fitness_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#f0f8ff", fg="#000000")
fitness_label.pack(pady=30)

back_button = tk.Button(root, text="Back", font=("Helvetica", 18), bg="#4682b4", fg="white", command=go_back)
back_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", go_back)

root.mainloop()
