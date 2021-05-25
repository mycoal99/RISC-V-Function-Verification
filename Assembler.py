
class Assembler():

    registers = ['$zero','$ra','$sp','$gp','$tp','$t0','$t1','$t2','$s0','$s1','$a0','$a1','$a2','$a3','$a4','$a5',
    '$a6','$a7','$s2','$s3','$s4','$s5','$s6','$s7','$s8','$s9','$s10','$s11','$t3','$t4','$t5','$t6']

    def __init__(self):
        self.current_commands = {}
        self.func_dict = {}
        self.machine_code = []
        self.function_calls = {
            'xor': self.xor_call,
            'div': self.div_call,
            'mul': self.mul_call,
            'sub': self.sub_call,
            'add': self.add_call,
            'addi': self.addi_call,
            'ori': self.ori_call,
            'slt': self.slt_call,
            'bne': self.bne_call,
            'blt': self.blt_call,
            'sw': self.sw_call,
            'lw': self.lw_call,
            'jal': self.jal_call,
            'jr': self.jr_call,
            'lui': self.lui_call,
        }

    def read_file(self, asm_filename):
        asm_file = open(asm_filename, "r")
        self.set_generator_values(asm_file)
        asm_file.close()


    def write_file(self, machine_filename):
        machine_file = open(machine_filename, "w")
        for line in self.machine_code:
            machine_file.write(line + '\n')
        machine_file.close()

    def _set_machine_code(self):
        self.machine_code = []
        for ind, command in enumerate(self.current_commands):
            if command[0][:2] == "0x":
                hex_str = command[0][2:]
                while(len(hex_str) < 8):
                    hex_str = '0' + hex_str
                self.machine_code.append(hex_str)
            else:
                call = self.function_calls[command[0]]
                call_code = call(command, ind)
                self.machine_code.append(call_code)


    def set_generator_values(self, asm_command_list):
        commands = [line.strip('\n:') for line in asm_command_list]
        commands = [line.replace('\t', ' ') for line in commands]
        commands = [line.replace(',', ' ') for line in commands]
        commands = [line.replace('(', ' ') for line in commands]
        commands = [line.replace(')', ' ') for line in commands]
        commands = list(filter(lambda a: a != '' and a != ' ', commands ))

        new_commands = []
        for line in commands:
            hash_position = line.find("#")
            if hash_position != -1:
                line = line[:hash_position]
            new_commands.append(line)

        new_commands = [line.split() for line in new_commands]

        self.func_dict = {}
        self.current_commands = new_commands
        for command in new_commands:
            if len(command) == 1 and command[0][:2] != "0x":
                func_ind = self.current_commands.index(command)
                self.current_commands.pop(func_ind)
                self.func_dict[command[0]] = func_ind
        self._set_machine_code()


    def twos_compliment(self, bin_str):
        #flip the bits
        bin_str = '0' + bin_str
        bin_str = bin_str.replace('1', '2')
        bin_str = bin_str.replace('0', '1')
        bin_str = bin_str.replace('2', '0')

        value = int(bin_str, 2)
        value += 1
        bin_str = bin(value)
        bin_str = bin_str[2:]

        return bin_str

    def conv_imm_2_str(self, imm_value):
        if imm_value[:2] == '0x':
            out = int(imm_value, 16)
        else:
            out = int(imm_value)
        return out

    def conv_2_bin(self, bin_len, value):
        bin_str = bin(value)
        sign = bin_str[0]
        if sign == '0':
            bin_str = bin_str[2:]
            appender = '0'
        if sign == '-':
            bin_str = bin_str[3:]
            bin_str = self.twos_compliment(bin_str)
            appender = '1'

        while(len(bin_str) < bin_len):
            bin_str = appender + bin_str
        
        if(len(bin_str) > bin_len):
            print("Warning: Binary length of value is longer than allowed. Hex might be wrong")

        return bin_str


    def conv_2_hex(self, bin_value):
        hex_str = hex(int(bin_value, 2))
        hex_str = hex_str[2:]
        while(len(hex_str) < 8):
            hex_str = '0' + hex_str

        return hex_str


    def get_immediate_for_jumps(self, function, line_index):
        function_line = self.func_dict[function]
        immediate = (function_line - line_index) * 4
        return immediate

    def xor_call(self,command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0000000' + rs2 + rs1 + '100' + rd + '0110011'    
        call_str = self.conv_2_hex(call_str)
        return call_str

    def sub_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0100000' + rs2 + rs1 + '000' + rd + '0110011'    
        call_str = self.conv_2_hex(call_str)
        return call_str

    def add_call(self, command, line_index):    
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0000000' + rs2 + rs1 + '000' + rd + '0110011'    
        call_str = self.conv_2_hex(call_str)
        return call_str

    def div_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0000001' + rs2 + rs1 + '100' + rd + '0110011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def mul_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0000001' + rs2 + rs1 + '000' + rd + '0110011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def addi_call(self, command, line_index):
        imm = self.conv_2_bin(12, self.conv_imm_2_str(command[3]))
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        
        call_str = imm + rs1 + '000' + rd + '0010011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def ori_call(self, command, line_index):
        imm = self.conv_2_bin(12, self.conv_imm_2_str(command[3]))
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        
        call_str = imm + rs1 + '110' + rd + '0010011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def slt_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[2]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = '0000000' + rs2 + rs1 + '010' + rd + '0110011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def bne_call(self, command, line_index):
        imm = self.get_immediate_for_jumps(command[3], line_index)
        imm = self.conv_2_bin(13, imm)
        rs1 = self.conv_2_bin(5, self.registers.index(command[1]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[2]))

        call_str = imm[0] + imm[2:8] + rs2 + rs1 + '001' + imm[8:12] + imm[1] + '1100011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def blt_call(self, command, line_index):
        imm = self.get_immediate_for_jumps(command[3], line_index)
        imm = self.conv_2_bin(13, imm)
        rs1 = self.conv_2_bin(5, self.registers.index(command[1]))
        rs2 = self.conv_2_bin(5, self.registers.index(command[2]))

        call_str = imm[0] + imm[2:8] + rs2 + rs1 + '100' + imm[8:12] + imm[1] + '1100011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def sw_call(self, command, line_index):
        rs2 = self.conv_2_bin(5, self.registers.index(command[1]))
        imm = self.conv_2_bin(12, self.conv_imm_2_str(command[2]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[3]))
        
        call_str = imm[0:7] + rs2 + rs1 + '010' + imm[7:12] + '0100011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def lw_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        imm = self.conv_2_bin(12, self.conv_imm_2_str(command[2]))
        rs1 = self.conv_2_bin(5, self.registers.index(command[3]))

        call_str = imm + rs1 + '010' + rd + '0000011'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def jal_call(self, command, line_index):
        imm = self.get_immediate_for_jumps(command[2], line_index)
        imm = self.conv_2_bin(21, imm)
        rd = self.conv_2_bin(5, self.registers.index(command[1]))

        call_str = imm[0] + imm[10:20] + imm[9] + imm[1:9] + rd + '1101111'
        call_str = self.conv_2_hex(call_str)

        return call_str

    def jr_call(self, command, line_index):
        rs1 = self.conv_2_bin(5, self.registers.index(command[1]))

        call_str = ('0' * 12) + rs1 + ('0' * 8) + '1100111'
        call_str = self.conv_2_hex(call_str)
        return call_str

    def lui_call(self, command, line_index):
        rd = self.conv_2_bin(5, self.registers.index(command[1]))
        imm = self.conv_2_bin(20, self.conv_imm_2_str(command[2]))
        
        call_str = imm + rd + '0110111'
        call_str = self.conv_2_hex(call_str)

        return call_str
