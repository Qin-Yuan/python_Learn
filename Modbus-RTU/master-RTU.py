import serial
import sys
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "COM3"
#PORT = '/dev/ttyp5'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")
        '''
            1、READ_COILS H01 读线圈
            2、READ_DISCRETE_INPUTS H02 读离散输入
            3、READ_HOLDING_REGISTERS H03 读寄存器
            4、READ_INPUT_REGISTERS H04 读输入寄存器
            5、WRITE_SINGLE_COIL H05 写单一线圈
            6、WRITE_SINGLE_REGISTER H06 写单一寄存器
            7、WRITE_MULTIPLE_COILS H15 写多个线圈
            8、WRITE_MULTIPLE_REGISTERS H16 写多寄存器
        '''
        while True:
            logger.info("\n请输入正确的指令")
            # 指令格式：机号 功能代码 起始地址 结束地址
            cmd = sys.stdin.readline()
            # 空格拆分成列表
            args = cmd.split(' ')
            # 读线圈
            if args[1]=='1':
                logger.info(master.execute(int(args[0]), cst.READ_COILS, int(args[2]), int(args[3])))
            # 读离散输入
            elif args[1]=='2': 
                logger.info(master.execute(int(args[0]), cst.DISCRETE_INPUTS, int(args[2]), int(args[3])))  
            # 读寄存器
            elif args[1]=='3':  
                logger.info(master.execute(int(args[0]), cst.HOLDING_REGISTERS, int(args[2]), int(args[3])))
            # 读输入寄存器
            elif args[1]=='4':  
                logger.info(master.execute(int(args[0]), cst.READ_INPUT_REGISTERS, int(args[2]), int(args[3])))
            else :
                print("功能代码错误")
                
    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()