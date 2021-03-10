# @Author : 游永全
# @Date : 2021/3/10
# @Edition : Python3
# @System : Raspberry_Pi
import smbus
import time
import csv


def sensor():
    # Get I2C bus
    bus = smbus.SMBus(1)
    # SHT31 address, 0x44(68)
    bus.write_i2c_block_data(0x44, 0x2C, [0x06])
    time.sleep(5)
    # SHT31 address, 0x44(68)
    # Read data back from 0x00(00), 6 bytes
    # Temp MSB, Temp LSB, Temp CRC, Humidity MSB, Humidity LSB, Humidity CRC
    data = bus.read_i2c_block_data(0x44, 0x00, 6)
    # Convert the data
    temp = data[0] * 256 + data[1]
    c_temp = -45 + (175 * temp / 65535.0)
    # f_temp = -49 + (315 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    t = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime(time.time()))
    h = '%.2f' % humidity
    c = '%.2f' % c_temp
    with open('SHT31.csv', 'a', encoding='utf-8', newline='')as _f:
        _row = [t, h, c]
        _write = csv.writer(_f)
        _write.writerow(_row)
    print('时间：', t, end='，')
    print("湿度：", h, "%", end='，')
    print("温度：", c, "℃")


def main():
    with open('SHT31.csv', 'w', encoding='utf-8', newline='') as f:
        row = ['Time', 'Humidity(%)', 'Temperature(℃)']
        write = csv.writer(f)
        write.writerow(row)
    while True:
        try:
            sensor()
            time.sleep(5)
        except KeyboardInterrupt:
            break
    print('程序已关闭')


if __name__ == '__main__':
    main()
