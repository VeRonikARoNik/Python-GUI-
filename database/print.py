from database import Database
import matplotlib.pyplot as plt

conn = Database("iot", "localhost", "root", "1234")

# Device {id} from argument
ID = 1

array = conn.getArray(f"SELECT time, temperature, humidity, voltage FROM data WHERE device_id = {ID}")

if len(array) > 0:
    # Transpose the array
    transposed_array = list(map(list, zip(*array)))

    # Assign variables to each column of the transposed array
    time, temperature, humidity, voltage = transposed_array

    # Create subplots
    fig, axs = plt.subplots(3, sharex=True, figsize=(10, 8))
    fig.suptitle(f'Device {ID} Data')

    # Plot temperature
    axs[0].plot(time, temperature, 'r')
    axs[0].set_ylabel('Temperature')

    # Plot humidity
    axs[1].plot(time, humidity, 'g')
    axs[1].set_ylabel('Humidity')

    # Plot voltage
    axs[2].plot(time, voltage, 'b')
    axs[2].set_ylabel('Voltage')
    axs[2].set_xlabel('Time')

    # Display the plots
    plt.show()

else:
    print(f"No data found for device ID {ID}")
