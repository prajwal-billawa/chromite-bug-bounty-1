from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_alu_logic(IPlugin):
    """
    This class contains methods to generate and validate the tests for bypass from
    ALU operation to ALU operation.
    """

    def __init__(self) -> None:
        super().__init__()
        self.isa = 'RV32I'
        self.isa_bit = 'rv32'
        self.offset_inc = 4
        self.xlen = 32
        self.num_rand_var = 100

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.isa = isa_yaml['hart0']['ISA']
        if 'RV32' in self.isa:
            self.isa_bit = 'rv32'
            self.xlen = 32
            self.offset_inc = 4
        else:
            self.isa_bit = 'rv64'
            self.xlen = 64
            self.offset_inc = 8
        return True

    def generate_asm(self) -> List[Dict[str,Union[Union[str, List[Any]], Any]]]:
        reg_file = base_reg_file.copy()
        test_dict = []
	""" The data dependent instruction are used to justify the bypass from the alu 
	operation to another alu operation.
	We are making use of 3 instruction add,sub and or which has x24 as the dependent 
	register.
	""" 
        
        asm = "\n\tadd x24,x20,x21 \n\tsub x18,x24,x19 \n\tor x25,x31,x24 \n\n"
        
        compile_macros = []

        test_dict.append({
            'asm_code': asm,
            'asm_sig' : '',
            'compile_macros': compile_macros,
            })


        return test_dict


    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv



