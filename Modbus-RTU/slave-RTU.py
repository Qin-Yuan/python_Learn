import sys
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial

PORT = "COM4"

def main():
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
    #Create the server
    server = modbus_rtu.RtuServer(serial.Serial(PORT))
    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")
        # 开始服务
        server.start()
        # 乘法寄存器
        #slave_1 = server.add_slave(1)
        #slave_1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)
        
        '''
        COILS = 1 线圈
        DISCRETE_INPUTS = 2 离散输入（数字量输入）
        HOLDING_REGISTERS = 3 乘法寄存器
        ANALOG_INPUTS = 4 模拟量输入
        '''
        while True:
            # 命令
            cmd = sys.stdin.readline()
            # 空格拆分成列表
            args = cmd.split(' ')
            # 退出
            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break
            # 创建从机：add_s 机号 
            elif args[0] ==  'add_s':
                slave_id = int(args[1])
                server.add_slave(slave_id)
                sys.stdout.write('成功添加从机： %d \r\n' % (slave_id))
            # 初始化从机：add_b 机号 hold 类型 初始地址 数据长度  
            # 只可操作一次
            elif args[0] == 'add_b':
                slave_id = int(args[1])
                name = args[2]
                block_type = int(args[3])
                starting_address = int(args[4])
                length = int(args[5])
                slave = server.get_slave(slave_id)
                slave.add_block(name, block_type, starting_address, length)
                sys.stdout.write('设置从机 %d 类型为 %d 起始地址为 %d 数据长度为 %d \r\n' % ((slave_id),block_type,starting_address,length))
            # 数据写入：add_v 机号 hold 地址 数据
            # 注意地址和数据大小不要超出初始化范围
            elif args[0] == 'set_v':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                values = []
                for val in args[4:]:
                    values.append(int(val))
                slave = server.get_slave(slave_id)
                slave.set_values(name, address, values)
                values = slave.get_values(name, address, len(values))
                sys.stdout.write('成功向从机 %d 在地址 %d 处写入数据： %s \r\n' % (slave_id,address,(str(values))))
            # 获得数据从机数据：get_v 机号 hold 地址 数据长度
            elif args[0] == 'get_v':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                length = int(args[4])
                slave = server.get_slave(slave_id)
                values = slave.get_values(name, address, length)
                sys.stdout.write('done: values read: %s\r\n' % (str(values)))
            else:
                sys.stdout.write("unknown command %s\r\n" % (args[0]))
    finally:
        server.stop()

if __name__ == "__main__":
    main()