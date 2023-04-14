import tkinter as tk
from database import Database
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def clear_charts():
    global canvas

    if canvas is not None:
        canvas.get_tk_widget().pack_forget()
        canvas = None


def plot_charts():
    global canvas

    clear_charts()

    data = conn.getArray(
        f"SELECT time, temperature, humidity, voltage FROM data WHERE device_id = {ID}")

    if len(data) > 0:
        fig, axs = plt.subplots(3, sharex=True, figsize=(10, 8))
        fig.suptitle(f'Device {ID} Data')

        time, temperature, humidity, voltage = list(map(list, zip(*data)))

        if temp_var.get():
            axs[0].plot(time, temperature, 'r')
            axs[0].set_ylabel('Temperature')

        if humidity_var.get():
            axs[1].plot(time, humidity, 'g')
            axs[1].set_ylabel('Humidity')

        if voltage_var.get():
            axs[2].plot(time, voltage, 'b')
            axs[2].set_ylabel('Voltage')
            axs[2].set_xlabel('Time')

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()


def main():
    global temp_var, humidity_var, voltage_var, root, conn, ID, canvas

    ID = 1
    conn = Database("iot", "localhost", "root", "1234")
    canvas = None

    root = tk.Tk()
    root.title("Wykresy IoT")

    temp_var = tk.BooleanVar()
    humidity_var = tk.BooleanVar()
    voltage_var = tk.BooleanVar()

    temp_check = tk.Checkbutton(root, text="Temperatura", variable=temp_var)
    temp_check.pack()

    humidity_check = tk.Checkbutton(
        root, text="Wilgotność", variable=humidity_var)
    humidity_check.pack()

    voltage_check = tk.Checkbutton(root, text="Napięcie", variable=voltage_var)
    voltage_check.pack()

    show_charts_button = tk.Button(
        root, text="Pokaż wykresy", command=plot_charts)
    show_charts_button.pack()

    clear_charts_button = tk.Button(root, text="Anuluj", command=clear_charts)
    clear_charts_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
