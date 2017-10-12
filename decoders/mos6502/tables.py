##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2017 David Banks <dave@hoglet.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

'''
  6502 Addressing Modes

  Map of Addressing Mode to Instruction Length

  Instruction tuple: (string, addressing mode)
'''

# Instructions without a prefix

class AddrMode:
    IMP, IMPA, BRA, IMM, ZP, ZPX, ZPY, INDX, INDY, IND, ABS, ABSX, ABSY, IND16, IND1X = range(15)

addr_mode_len_map = {
    AddrMode.IMP:   ( 1, '{0}'                     ),
    AddrMode.IMPA:  ( 1, '{0} A'                   ),
    AddrMode.BRA:   ( 2, '{0} PC+{1:02X}'          ), # TODO - improve this format
    AddrMode.IMM:   ( 2, '{0} #{1:02X}'            ),
    AddrMode.ZP:    ( 2, '{0} {1:02X}'             ),
    AddrMode.ZPX:   ( 2, '{0} {1:02X},X'           ),
    AddrMode.ZPY:   ( 2, '{0} {1:02X},Y'           ),
    AddrMode.INDX:  ( 2, '{0} ({1:02X}, X)'        ),
    AddrMode.INDY:  ( 2, '{0} ({1:02X}), Y'        ),
    AddrMode.IND:   ( 2, '{0} ({1:02X})'           ),
    AddrMode.ABS:   ( 3, '{0} {2:02X}{1:02X}'      ),
    AddrMode.ABSX:  ( 3, '{0} {2:02X}{1:02X}, X'   ),
    AddrMode.ABSY:  ( 3, '{0} {2:02X}{1:02X}, Y'   ),
    AddrMode.IND16: ( 3, '{0} ({2:02X}{1:02X})'    ),
    AddrMode.IND1X: ( 3, '{0} ({2:02X}{1:02X}, X)' ),
}

instr_table = {
    0x00: ( 'BRK', AddrMode.IMM  ),
    0x01: ( 'ORA', AddrMode.INDX ),
    0x02: ( '???', AddrMode.IMP  ),
    0x03: ( '???', AddrMode.IMP  ),
    0x04: ( 'TSB', AddrMode.ZP   ),
    0x05: ( 'ORA', AddrMode.ZP   ),
    0x06: ( 'ASL', AddrMode.ZP   ),
    0x07: ( '???', AddrMode.IMP  ),
    0x08: ( 'PHP', AddrMode.IMP  ),
    0x09: ( 'ORA', AddrMode.IMM  ),
    0x0A: ( 'ASL', AddrMode.IMPA ),
    0x0B: ( '???', AddrMode.IMP ),
    0x0C: ( 'TSB', AddrMode.ABS ),
    0x0D: ( 'ORA', AddrMode.ABS ),
    0x0E: ( 'ASL', AddrMode.ABS ),
    0x0F: ( '???', AddrMode.IMP ),
    0x10: ( 'BPL', AddrMode.BRA ),
    0x11: ( 'ORA', AddrMode.INDY ),
    0x12: ( 'ORA', AddrMode.IND ),
    0x13: ( '???', AddrMode.IMP ),
    0x14: ( 'TRB', AddrMode.ZP ),
    0x15: ( 'ORA', AddrMode.ZPX ),
    0x16: ( 'ASL', AddrMode.ZPX ),
    0x17: ( '???', AddrMode.IMP ),
    0x18: ( 'CLC', AddrMode.IMP ),
    0x19: ( 'ORA', AddrMode.ABSY ),
    0x1A: ( 'INC', AddrMode.IMPA ),
    0x1B: ( '???', AddrMode.IMP ),
    0x1C: ( 'TRB', AddrMode.ABS ),
    0x1D: ( 'ORA', AddrMode.ABSX ),
    0x1E: ( 'ASL', AddrMode.ABSX ),
    0x1F: ( '???', AddrMode.IMP ),
    0x20: ( 'JSR', AddrMode.ABS ),
    0x21: ( 'AND', AddrMode.INDX ),
    0x22: ( '???', AddrMode.IMP ),
    0x23: ( '???', AddrMode.IMP ),
    0x24: ( 'BIT', AddrMode.ZP ),
    0x25: ( 'AND', AddrMode.ZP ),
    0x26: ( 'ROL', AddrMode.ZP ),
    0x27: ( '???', AddrMode.IMP ),
    0x28: ( 'PLP', AddrMode.IMP ),
    0x29: ( 'AND', AddrMode.IMM ),
    0x2A: ( 'ROL', AddrMode.IMPA ),
    0x2B: ( '???', AddrMode.IMP ),
    0x2C: ( 'BIT', AddrMode.ABS ),
    0x2D: ( 'AND', AddrMode.ABS ),
    0x2E: ( 'ROL', AddrMode.ABS ),
    0x2F: ( '???', AddrMode.IMP ),
    0x30: ( 'BMI', AddrMode.BRA ),
    0x31: ( 'AND', AddrMode.INDY ),
    0x32: ( 'AND', AddrMode.IND ),
    0x33: ( '???', AddrMode.IMP ),
    0x34: ( 'BIT', AddrMode.ZPX ),
    0x35: ( 'AND', AddrMode.ZPX ),
    0x36: ( 'ROL', AddrMode.ZPX ),
    0x37: ( '???', AddrMode.IMP ),
    0x38: ( 'SEC', AddrMode.IMP ),
    0x39: ( 'AND', AddrMode.ABSY ),
    0x3A: ( 'DEC', AddrMode.IMPA ),
    0x3B: ( '???', AddrMode.IMP ),
    0x3C: ( 'BIT', AddrMode.ABSX ),
    0x3D: ( 'AND', AddrMode.ABSX ),
    0x3E: ( 'ROL', AddrMode.ABSX ),
    0x3F: ( '???', AddrMode.IMP ),
    0x40: ( 'RTI', AddrMode.IMP ),
    0x41: ( 'EOR', AddrMode.INDX ),
    0x42: ( '???', AddrMode.IMP ),
    0x43: ( '???', AddrMode.IMP ),
    0x44: ( '???', AddrMode.ZP ),
    0x45: ( 'EOR', AddrMode.ZP ),
    0x46: ( 'LSR', AddrMode.ZP ),
    0x47: ( '???', AddrMode.IMP ),
    0x48: ( 'PHA', AddrMode.IMP ),
    0x49: ( 'EOR', AddrMode.IMM ),
    0x4A: ( 'LSR', AddrMode.IMPA ),
    0x4B: ( '???', AddrMode.IMP ),
    0x4C: ( 'JMP', AddrMode.ABS ),
    0x4D: ( 'EOR', AddrMode.ABS ),
    0x4E: ( 'LSR', AddrMode.ABS ),
    0x4F: ( '???', AddrMode.IMP ),
    0x50: ( 'BVC', AddrMode.BRA ),
    0x51: ( 'EOR', AddrMode.INDY ),
    0x52: ( 'EOR', AddrMode.IND ),
    0x53: ( '???', AddrMode.IMP ),
    0x54: ( '???', AddrMode.ZP ),
    0x55: ( 'EOR', AddrMode.ZPX ),
    0x56: ( 'LSR', AddrMode.ZPX ),
    0x57: ( '???', AddrMode.IMP ),
    0x58: ( 'CLI', AddrMode.IMP ),
    0x59: ( 'EOR', AddrMode.ABSY ),
    0x5A: ( 'PHY', AddrMode.IMP ),
    0x5B: ( '???', AddrMode.IMP ),
    0x5C: ( '???', AddrMode.ABS ),
    0x5D: ( 'EOR', AddrMode.ABSX ),
    0x5E: ( 'LSR', AddrMode.ABSX ),
    0x5F: ( '???', AddrMode.IMP ),
    0x60: ( 'RTS', AddrMode.IMP ),
    0x61: ( 'ADC', AddrMode.INDX ),
    0x62: ( '???', AddrMode.IMP ),
    0x63: ( '???', AddrMode.IMP ),
    0x64: ( 'STZ', AddrMode.ZP ),
    0x65: ( 'ADC', AddrMode.ZP ),
    0x66: ( 'ROR', AddrMode.ZP ),
    0x67: ( '???', AddrMode.IMP ),
    0x68: ( 'PLA', AddrMode.IMP ),
    0x69: ( 'ADC', AddrMode.IMM ),
    0x6A: ( 'ROR', AddrMode.IMPA ),
    0x6B: ( '???', AddrMode.IMP ),
    0x6C: ( 'JMP', AddrMode.IND16 ),
    0x6D: ( 'ADC', AddrMode.ABS ),
    0x6E: ( 'ROR', AddrMode.ABS ),
    0x6F: ( '???', AddrMode.IMP ),
    0x70: ( 'BVS', AddrMode.BRA ),
    0x71: ( 'ADC', AddrMode.INDY ),
    0x72: ( 'ADC', AddrMode.IND ),
    0x73: ( '???', AddrMode.IMP ),
    0x74: ( 'STZ', AddrMode.ZPX ),
    0x75: ( 'ADC', AddrMode.ZPX ),
    0x76: ( 'ROR', AddrMode.ZPX ),
    0x77: ( '???', AddrMode.IMP ),
    0x78: ( 'SEI', AddrMode.IMP ),
    0x79: ( 'ADC', AddrMode.ABSY ),
    0x7A: ( 'PLY', AddrMode.IMP ),
    0x7B: ( '???', AddrMode.IMP ),
    0x7C: ( 'JMP', AddrMode.IND1X ),
    0x7D: ( 'ADC', AddrMode.ABSX ),
    0x7E: ( 'ROR', AddrMode.ABSX ),
    0x7F: ( '???', AddrMode.IMP ),
    0x80: ( 'BRA', AddrMode.BRA ),
    0x81: ( 'STA', AddrMode.INDX ),
    0x82: ( '???', AddrMode.IMP ),
    0x83: ( '???', AddrMode.IMP ),
    0x84: ( 'STY', AddrMode.ZP ),
    0x85: ( 'STA', AddrMode.ZP ),
    0x86: ( 'STX', AddrMode.ZP ),
    0x87: ( '???', AddrMode.IMP ),
    0x88: ( 'DEY', AddrMode.IMP ),
    0x89: ( 'BIT', AddrMode.IMM ),
    0x8A: ( 'TXA', AddrMode.IMP ),
    0x8B: ( '???', AddrMode.IMP ),
    0x8C: ( 'STY', AddrMode.ABS ),
    0x8D: ( 'STA', AddrMode.ABS ),
    0x8E: ( 'STX', AddrMode.ABS ),
    0x8F: ( '???', AddrMode.IMP ),
    0x90: ( 'BCC', AddrMode.BRA ),
    0x91: ( 'STA', AddrMode.INDY ),
    0x92: ( 'STA', AddrMode.IND ),
    0x93: ( '???', AddrMode.IMP ),
    0x94: ( 'STY', AddrMode.ZPX ),
    0x95: ( 'STA', AddrMode.ZPX ),
    0x96: ( 'STX', AddrMode.ZPY ),
    0x97: ( '???', AddrMode.IMP ),
    0x98: ( 'TYA', AddrMode.IMP ),
    0x99: ( 'STA', AddrMode.ABSY ),
    0x9A: ( 'TXS', AddrMode.IMP ),
    0x9B: ( '???', AddrMode.IMP ),
    0x9C: ( 'STZ', AddrMode.ABS ),
    0x9D: ( 'STA', AddrMode.ABSX ),
    0x9E: ( 'STZ', AddrMode.ABSX ),
    0x9F: ( '???', AddrMode.IMP ),
    0xA0: ( 'LDY', AddrMode.IMM ),
    0xA1: ( 'LDA', AddrMode.INDX ),
    0xA2: ( 'LDX', AddrMode.IMM ),
    0xA3: ( '???', AddrMode.IMP ),
    0xA4: ( 'LDY', AddrMode.ZP ),
    0xA5: ( 'LDA', AddrMode.ZP ),
    0xA6: ( 'LDX', AddrMode.ZP ),
    0xA7: ( '???', AddrMode.IMP ),
    0xA8: ( 'TAY', AddrMode.IMP ),
    0xA9: ( 'LDA', AddrMode.IMM ),
    0xAA: ( 'TAX', AddrMode.IMP ),
    0xAB: ( '???', AddrMode.IMP ),
    0xAC: ( 'LDY', AddrMode.ABS ),
    0xAD: ( 'LDA', AddrMode.ABS ),
    0xAE: ( 'LDX', AddrMode.ABS ),
    0xAF: ( '???', AddrMode.IMP ),
    0xB0: ( 'BCS', AddrMode.BRA ),
    0xB1: ( 'LDA', AddrMode.INDY ),
    0xB2: ( 'LDA', AddrMode.IND ),
    0xB3: ( '???', AddrMode.IMP ),
    0xB4: ( 'LDY', AddrMode.ZPX ),
    0xB5: ( 'LDA', AddrMode.ZPX ),
    0xB6: ( 'LDX', AddrMode.ZPY ),
    0xB7: ( '???', AddrMode.IMP ),
    0xB8: ( 'CLV', AddrMode.IMP ),
    0xB9: ( 'LDA', AddrMode.ABSY ),
    0xBA: ( 'TSX', AddrMode.IMP ),
    0xBB: ( '???', AddrMode.IMP ),
    0xBC: ( 'LDY', AddrMode.ABSX ),
    0xBD: ( 'LDA', AddrMode.ABSX ),
    0xBE: ( 'LDX', AddrMode.ABSY ),
    0xBF: ( '???', AddrMode.IMP ),
    0xC0: ( 'CPY', AddrMode.IMM ),
    0xC1: ( 'CMP', AddrMode.INDX ),
    0xC2: ( '???', AddrMode.IMP ),
    0xC3: ( '???', AddrMode.IMP ),
    0xC4: ( 'CPY', AddrMode.ZP ),
    0xC5: ( 'CMP', AddrMode.ZP ),
    0xC6: ( 'DEC', AddrMode.ZP ),
    0xC7: ( '???', AddrMode.IMP ),
    0xC8: ( 'INY', AddrMode.IMP ),
    0xC9: ( 'CMP', AddrMode.IMM ),
    0xCA: ( 'DEX', AddrMode.IMP ),
    0xCB: ( 'WAI', AddrMode.IMP ),
    0xCC: ( 'CPY', AddrMode.ABS ),
    0xCD: ( 'CMP', AddrMode.ABS ),
    0xCE: ( 'DEC', AddrMode.ABS ),
    0xCF: ( '???', AddrMode.IMP ),
    0xD0: ( 'BNE', AddrMode.BRA ),
    0xD1: ( 'CMP', AddrMode.INDY ),
    0xD2: ( 'CMP', AddrMode.IND ),
    0xD3: ( '???', AddrMode.IMP ),
    0xD4: ( '???', AddrMode.ZP ),
    0xD5: ( 'CMP', AddrMode.ZPX ),
    0xD6: ( 'DEC', AddrMode.ZPX ),
    0xD7: ( '???', AddrMode.IMP ),
    0xD8: ( 'CLD', AddrMode.IMP ),
    0xD9: ( 'CMP', AddrMode.ABSY ),
    0xDA: ( 'PHX', AddrMode.IMP ),
    0xDB: ( 'STP', AddrMode.IMP ),
    0xDC: ( '???', AddrMode.ABS ),
    0xDD: ( 'CMP', AddrMode.ABSX ),
    0xDE: ( 'DEC', AddrMode.ABSX ),
    0xDF: ( '???', AddrMode.IMP ),
    0xE0: ( 'CPX', AddrMode.IMM ),
    0xE1: ( 'SBC', AddrMode.INDX ),
    0xE2: ( '???', AddrMode.IMP ),
    0xE3: ( '???', AddrMode.IMP ),
    0xE4: ( 'CPX', AddrMode.ZP ),
    0xE5: ( 'SBC', AddrMode.ZP ),
    0xE6: ( 'INC', AddrMode.ZP ),
    0xE7: ( '???', AddrMode.IMP ),
    0xE8: ( 'INX', AddrMode.IMP ),
    0xE9: ( 'SBC', AddrMode.IMM ),
    0xEA: ( 'NOP', AddrMode.IMP ),
    0xEB: ( '???', AddrMode.IMP ),
    0xEC: ( 'CPX', AddrMode.ABS ),
    0xED: ( 'SBC', AddrMode.ABS ),
    0xEE: ( 'INC', AddrMode.ABS ),
    0xEF: ( '???', AddrMode.IMP ),
    0xF0: ( 'BEQ', AddrMode.BRA ),
    0xF1: ( 'SBC', AddrMode.INDY ),
    0xF2: ( 'SBC', AddrMode.IND ),
    0xF3: ( '???', AddrMode.IMP ),
    0xF4: ( '???', AddrMode.ZP ),
    0xF5: ( 'SBC', AddrMode.ZPX ),
    0xF6: ( 'INC', AddrMode.ZPX ),
    0xF7: ( '???', AddrMode.IMP ),
    0xF8: ( 'SED', AddrMode.IMP ),
    0xF9: ( 'SBC', AddrMode.ABSY ),
    0xFA: ( 'PLX', AddrMode.IMP ),
    0xFB: ( '???', AddrMode.IMP ),
    0xFC: ( '???', AddrMode.ABS ),
    0xFD: ( 'SBC', AddrMode.ABSX ),
    0xFE: ( 'INC', AddrMode.ABSX ),
    0xFF: ( '???', AddrMode.IMP ),
}
