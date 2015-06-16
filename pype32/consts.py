#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Copyright (c) 2013, Nahuel Riva 
# All rights reserved. 
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met: 
# 
#     * Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer. 
#     * Redistributions in binary form must reproduce the above copyright 
#       notice,this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution. 
#     * Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE. 

"""
Common definitions.
"""

__revision__ = "$Id$"

MZ_SIGNATURE = 0x5a4d
PE_SIGNATURE = 0x4550

SECTION_HEADER_LENGTH = 0x28

INTEL386 = 0x014c
COMMON_CHARACTERISTICS = 0x0102 # - file is executable
                                # - 32 bit word machine
PE32 = 0x010b
PE64 = 0x020b
WINDOWSGUI = 2
TERMINAL_SERVER_AWARE = 0x8000

IMAGE_NUMBEROF_DIRECTORY_ENTRIES = 16

EXPORT_DIRECTORY = 0
IMPORT_DIRECTORY = 1
RESOURCE_DIRECTORY = 2
EXCEPTION_DIRECTORY = 3
SECURITY_DIRECTORY = 4
RELOCATION_DIRECTORY = 5
DEBUG_DIRECTORY = 6
ARCHITECTURE_DIRECTORY = 7
RESERVED_DIRECTORY = 8
TLS_DIRECTORY = 9
CONFIGURATION_DIRECTORY = 10
BOUND_IMPORT_DIRECTORY = 11
IAT_DIRECTORY = 12
DELAY_IMPORT_DIRECTORY = 13
NET_METADATA_DIRECTORY = 14
RESERVED_DIRECTORY = 15

IMAGE_DOS_HEADER = 0
IMAGE_NT_HEADERS = 1
IMAGE_FILE_HEADER = 2
IMAGE_OPTIONAL_HEADER = 3
IMAGE_SECTION_HEADER = 4
IMAGE_DATA_DIRECTORY = 5
IMAGE_IMPORT_DESCRIPTOR = 6
NET_DIRECTORY = 7
NET_METADATA_HEADER = 8
IMAGE_COR20_HEADER = 9
NET_METADATA_STREAM_ENTRY = 10
NET_METADATA_STREAMS = 11
NET_METADATA_TABLE_HEADER = 12
NET_METADATA_TABLES = 13
IMAGE_DEBUG_DIRECTORY = 14
IMAGE_DEBUG_DIRECTORIES = 15
IMAGE_IMPORT_DESCRIPTOR_ENTRY = 16
IMPORT_ADDRESS_TABLE_ENTRY = 17
IMPORT_ADDRESS_TABLE = 18
IID_METADATA = 19
EXPORT_TABLE_ENTRY = 20
IMAGE_BASE_RELOCATION_ENTRY = 21
IMAGE_BOUND_IMPORT_DESCRIPTOR_ENTRY = 22
IMAGE_BOUND_FORWARDER_REF_ENTRY = 23
NET_TABLES = 24
IMAGE_OPTIONAL_HEADER64 = 25
TLS_DIRECTORY32 = 26
IMPORT_ADDRESS_TABLE_ENTRY64 = 27
TLS_DIRECTORY64 = 28
IMAGE_LOAD_CONFIG_DIRECTORY32 = 29
IMAGE_LOAD_CONFIG_DIRECTORY64 = 30
NET_RESOURCES = 31

SIZEOF_IMAGE_DEBUG_ENTRY32 = 28
SIZEOF_IMAGE_IMPORT_ENTRY32 = 20
SIZEOF_IMAGE_BOUND_IMPORT_ENTRY32 = 8
SIZEOF_IMAGE_BOUND_FORWARDER_REF_ENTRY32 = 8

DEFAULT_FILE_ALIGNMENT = 0x200
DEFAULT_PAGE_SIZE = 0x1000

IMAGE_ORDINAL_FLAG = 0x80000000L
IMAGE_ORDINAL_FLAG64 = 0x8000000000000000L
OPTIONAL_HEADER_MAGIC_PE = 0x10b
OPTIONAL_HEADER_MAGIC_PE_PLUS = 0x20b

IMAGE_FILE_RELOCS_STRIPPED = 0x0001
IMAGE_FILE_EXECUTABLE_IMAGE = 0x0002
IMAGE_FILE_LINE_NUMS_STRIPPED = 0x0004
IMAGE_FILE_LOCAL_SYMS_STRIPPED = 0x0008
IMAGE_FILE_AGGRESIVE_WS_TRIM = 0x0010
IMAGE_FILE_LARGE_ADDRESS_AWARE = 0x0020
IMAGE_FILE_16BIT_MACHINE = 0x0040
IMAGE_FILE_BYTES_REVERSED_LO = 0x0080
IMAGE_FILE_32BIT_MACHINE = 0x0100
IMAGE_FILE_DEBUG_STRIPPED = 0x0200
IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP = 0x0400
IMAGE_FILE_NET_RUN_FROM_SWAP = 0x0800
IMAGE_FILE_SYSTEM = 0x1000
IMAGE_FILE_DLL = 0x2000
IMAGE_FILE_UP_SYSTEM_ONLY = 0x4000
IMAGE_FILE_BYTES_REVERSED_HI = 0x8000

IMAGE_SCN_CNT_CODE = 0x00000020
IMAGE_SCN_CNT_INITIALIZED_DATA = 0x00000040
IMAGE_SCN_CNT_UNINITIALIZED_DATA = 0x00000080
IMAGE_SCN_LNK_OTHER = 0x00000100
IMAGE_SCN_LNK_INFO = 0x00000200
IMAGE_SCN_LNK_REMOVE = 0x00000800
IMAGE_SCN_LNK_COMDAT = 0x00001000
IMAGE_SCN_MEM_FARDATA = 0x00008000
IMAGE_SCN_MEM_PURGEABLE = 0x00020000
IMAGE_SCN_MEM_16BIT = 0x00020000
IMAGE_SCN_MEM_LOCKED = 0x00040000
IMAGE_SCN_MEM_PRELOAD = 0x00080000
IMAGE_SCN_ALIGN_1BYTES = 0x00100000
IMAGE_SCN_ALIGN_2BYTES = 0x00200000
IMAGE_SCN_ALIGN_4BYTES = 0x00300000
IMAGE_SCN_ALIGN_8BYTES = 0x00400000
IMAGE_SCN_ALIGN_16BYTES = 0x00500000
IMAGE_SCN_ALIGN_32BYTES = 0x00600000
IMAGE_SCN_ALIGN_64BYTES = 0x00700000
IMAGE_SCN_ALIGN_128BYTES = 0x00800000
IMAGE_SCN_ALIGN_256BYTES = 0x00900000
IMAGE_SCN_ALIGN_512BYTES = 0x00A00000
IMAGE_SCN_ALIGN_1024BYTES = 0x00B00000
IMAGE_SCN_ALIGN_2048BYTES = 0x00C00000
IMAGE_SCN_ALIGN_4096BYTES = 0x00D00000
IMAGE_SCN_ALIGN_8192BYTES = 0x00E00000
IMAGE_SCN_ALIGN_MASK = 0x00F00000
IMAGE_SCN_LNK_NRELOC_OVFL = 0x01000000
IMAGE_SCN_MEM_DISCARDABLE = 0x02000000
IMAGE_SCN_MEM_NOT_CACHED = 0x04000000
IMAGE_SCN_MEM_NOT_PAGED = 0x08000000
IMAGE_SCN_MEM_SHARED = 0x10000000
IMAGE_SCN_MEM_EXECUTE = 0x20000000
IMAGE_SCN_MEM_READ = 0x40000000
IMAGE_SCN_MEM_WRITE = 0x80000000L

IMAGE_DEBUG_TYPE_UNKNOWN = 0
IMAGE_DEBUG_TYPE_COFF = 1
IMAGE_DEBUG_TYPE_CODEVIEW = 2
IMAGE_DEBUG_TYPE_FPO = 3
IMAGE_DEBUG_TYPE_MISC = 4
IMAGE_DEBUG_TYPE_EXCEPTION = 5
IMAGE_DEBUG_TYPE_FIXUP = 6
IMAGE_DEBUG_TYPE_OMAP_TO_SRC = 7
IMAGE_DEBUG_TYPE_OMAP_FROM_SRC = 8
IMAGE_DEBUG_TYPE_BORLAND = 9
IMAGE_DEBUG_TYPE_RESERVED10 = 10

IMAGE_SUBSYSTEM_UNKNOWN = 0
IMAGE_SUBSYSTEM_NATIVE = 1
IMAGE_SUBSYSTEM_WINDOWS_GUI = 2
IMAGE_SUBSYSTEM_WINDOWS_CUI = 3
IMAGE_SUBSYSTEM_OS2_CUI = 5
IMAGE_SUBSYSTEM_POSIX_CUI = 7
IMAGE_SUBSYSTEM_WINDOWS_CE_GUI = 9
IMAGE_SUBSYSTEM_EFI_APPLICATION = 10
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 11
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER = 12
IMAGE_SUBSYSTEM_EFI_ROM = 13
IMAGE_SUBSYSTEM_XBOX = 14


IMAGE_FILE_MACHINE_UNKNOWN = 0
IMAGE_FILE_MACHINE_AM33 = 0x1d3
IMAGE_FILE_MACHINE_AMD64 = 0x8664
IMAGE_FILE_MACHINE_ARM = 0x1c0
IMAGE_FILE_MACHINE_EBC = 0xebc
IMAGE_FILE_MACHINE_I386 = 0x14c
IMAGE_FILE_MACHINE_IA64 = 0x200
IMAGE_FILE_MACHINE_MR32 = 0x9041
IMAGE_FILE_MACHINE_MIPS16 = 0x266
IMAGE_FILE_MACHINE_MIPSFPU = 0x366
IMAGE_FILE_MACHINE_MIPSFPU16 = 0x466
IMAGE_FILE_MACHINE_POWERPC = 0x1f0
IMAGE_FILE_MACHINE_POWERPCFP = 0x1f1
IMAGE_FILE_MACHINE_R4000 = 0x166
IMAGE_FILE_MACHINE_SH3 = 0x1a2
IMAGE_FILE_MACHINE_SH3DSP = 0x1a3
IMAGE_FILE_MACHINE_SH4 = 0x1a6
IMAGE_FILE_MACHINE_SH5 = 0x1a8
IMAGE_FILE_MACHINE_THUMB = 0x1c2
IMAGE_FILE_MACHINE_WCEMIPSV2 = 0x169

IMAGE_REL_BASED_ABSOLUTE = 0
IMAGE_REL_BASED_HIGH = 1
IMAGE_REL_BASED_LOW = 2
IMAGE_REL_BASED_HIGHLOW = 3
IMAGE_REL_BASED_HIGHADJ = 4
IMAGE_REL_BASED_MIPS_JMPADDR = 5
IMAGE_REL_BASED_SECTION = 6
IMAGE_REL_BASED_REL = 7
IMAGE_REL_BASED_MIPS_JMPADDR16 = 9
IMAGE_REL_BASED_IA64_IMM64 = 9
IMAGE_REL_BASED_DIR64 = 10
IMAGE_REL_BASED_HIGH3ADJ = 11

IMAGE_DLL_CHARACTERISTICS_RESERVED_0x0001 = 0x0001
IMAGE_DLL_CHARACTERISTICS_RESERVED_0x0002 = 0x0002
IMAGE_DLL_CHARACTERISTICS_RESERVED_0x0004 = 0x0004
IMAGE_DLL_CHARACTERISTICS_RESERVED_0x0008 = 0x0008
IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE = 0x0040
IMAGE_DLL_CHARACTERISTICS_FORCE_INTEGRITY = 0x0080
IMAGE_DLL_CHARACTERISTICS_NX_COMPAT = 0x0100
IMAGE_DLL_CHARACTERISTICS_NO_ISOLATION = 0x0200
IMAGE_DLL_CHARACTERISTICS_NO_SEH = 0x0400
IMAGE_DLL_CHARACTERISTICS_NO_BIND = 0x0800
IMAGE_DLL_CHARACTERISTICS_RESERVED_0x1000 = 0x1000
IMAGE_DLL_CHARACTERISTICS_WDM_DRIVER = 0x2000
IMAGE_DLL_CHARACTERISTICS_GUARD_CF = 0x4000 # http://www.virtualbox.org/svn/vbox/trunk/src/VBox/Runtime/include/internal/ldrPE.h
IMAGE_DLL_CHARACTERISTICS_TERMINAL_SERVER_AWARE = 0x8000

COMIMAGE_FLAGS_ILONLY = 0x00000001
COMIMAGE_FLAGS_32BITREQUIRED = 0x00000002
COMIMAGE_FLAGS_IL_LIBRARY = 0x00000004
COMIMAGE_FLAGS_STRONGNAMESIGNED = 0x00000008
COMIMAGE_FLAGS_NATIVE_ENTRYPOINT = 0x00000010
COMIMAGE_FLAGS_TRACKDEBUGDATA = 0x00010000
COMIMAGE_FLAGS_ISIBCOPTIMIZED = 0x00020000

CORILMETHOD_TINYFORMAT = 0x2
CORILMETHOD_FATFORMAT = 0x3
CORILMETHOD_MORESECTS = 0x8
CORILMETHOD_INITLOCALS = 0x10

ADDRESS_MASK32 = 0x7fffffff
ADDRESS_MASK64 = 0x7fffffffffffffff

RT_CURSOR = 1
RT_BITMAP = 2
RT_ICON = 3
RT_MENU = 4
RT_DIALOG = 5
RT_STRING = 6
RT_FONTDIR = 7
RT_FONT = 8
RT_ACCELERATOR = 9
RT_RCDATA = 10
RT_MESSAGETABLE = 11
RT_GROUP_CURSOR = 12
RT_GROUP_ICON = 14
RT_VERSION = 16
RT_DLGINCLUDE = 17
RT_PLUGPLAY = 19
RT_VXD = 20
RT_ANICURSOR = 21
RT_ANIICON = 22
RT_HTML = 23
RT_MANIFEST = 24

LANG_NEUTRAL = 0x00
LANG_INVARIANT = 0x7f
LANG_AFRIKAANS = 0x36
LANG_ALBANIAN = 0x1c
LANG_ARABIC = 0x01
LANG_ARMENIAN = 0x2b
LANG_ASSAMESE = 0x4d
LANG_AZERI = 0x2c
LANG_BASQUE = 0x2d
LANG_BELARUSIAN = 0x23
LANG_BENGALI = 0x45
LANG_BULGARIAN = 0x02
LANG_CATALAN = 0x03
LANG_CHINESE = 0x04
LANG_CROATIAN = 0x1a
LANG_CZECH = 0x05
LANG_DANISH = 0x06
LANG_DIVEHI = 0x65
LANG_DUTCH = 0x13
LANG_ENGLISH = 0x09
LANG_ESTONIAN = 0x25
LANG_FAEROESE = 0x38
LANG_FARSI = 0x29
LANG_FINNISH = 0x0b
LANG_FRENCH = 0x0c
LANG_GALICIAN = 0x56
LANG_GEORGIAN = 0x37
LANG_GERMAN = 0x07
LANG_GREEK = 0x08
LANG_GUJARATI = 0x47
LANG_HEBREW = 0x0d
LANG_HINDI = 0x39
LANG_HUNGARIAN = 0x0e
LANG_ICELANDIC = 0x0f
LANG_INDONESIAN = 0x21
LANG_ITALIAN = 0x10
LANG_JAPANESE = 0x11
LANG_KANNADA = 0x4b
LANG_KASHMIRI = 0x60
LANG_KAZAK = 0x3f
LANG_KONKANI = 0x57
LANG_KOREAN = 0x12
LANG_KYRGYZ = 0x40
LANG_LATVIAN = 0x26
LANG_LITHUANIAN = 0x27
LANG_MACEDONIAN = 0x2f
LANG_MALAY = 0x3e
LANG_MALAYALAM = 0x4c
LANG_MANIPURI = 0x58
LANG_MARATHI = 0x4e
LANG_MONGOLIAN = 0x50
LANG_NEPALI = 0x61
LANG_NORWEGIAN = 0x14
LANG_ORIYA = 0x48
LANG_POLISH = 0x15
LANG_PORTUGUESE = 0x16
LANG_PUNJABI = 0x46
LANG_ROMANIAN = 0x18
LANG_RUSSIAN = 0x19
LANG_SANSKRIT = 0x4f
LANG_SERBIAN = 0x1a
LANG_SINDHI = 0x59
LANG_SLOVAK = 0x1b
LANG_SLOVENIAN = 0x24
LANG_SPANISH = 0x0a
LANG_SWAHILI = 0x41
LANG_SWEDISH = 0x1d
LANG_SYRIAC = 0x5a
LANG_TAMIL = 0x49
LANG_TATAR = 0x44
LANG_TELUGU = 0x4a
LANG_THAI = 0x1e
LANG_TURKISH = 0x1f
LANG_UKRAINIAN = 0x22
LANG_URDU = 0x20
LANG_UZBEK = 0x43
LANG_VIETNAMESE = 0x2a
LANG_GAELIC = 0x3c
LANG_MALTESE = 0x3a
LANG_MAORI = 0x28
LANG_RHAETO_ROMANCE = 0x17
LANG_SAAMI = 0x3b
LANG_SORBIAN = 0x2e
LANG_SUTU = 0x30
LANG_TSONGA = 0x31
LANG_TSWANA = 0x32
LANG_VENDA = 0x33
LANG_XHOSA = 0x34
LANG_ZULU = 0x35
LANG_ESPERANTO = 0x8f
LANG_WALON = 0x90
LANG_CORNISH = 0x91
LANG_WELSH = 0x92
LANG_BRETON = 0x93

SUBLANG_NEUTRAL = 0x00
SUBLANG_DEFAULT = 0x01
SUBLANG_SYS_DEFAULT = 0x02
SUBLANG_ARABIC_SAUDI_ARABIA = 0x01
SUBLANG_ARABIC_IRAQ = 0x02
SUBLANG_ARABIC_EGYPT = 0x03
SUBLANG_ARABIC_LIBYA = 0x04
SUBLANG_ARABIC_ALGERIA = 0x05
SUBLANG_ARABIC_MOROCCO = 0x06
SUBLANG_ARABIC_TUNISIA = 0x07
SUBLANG_ARABIC_OMAN = 0x08
SUBLANG_ARABIC_YEMEN = 0x09
SUBLANG_ARABIC_SYRIA = 0x0a
SUBLANG_ARABIC_JORDAN = 0x0b
SUBLANG_ARABIC_LEBANON = 0x0c
SUBLANG_ARABIC_KUWAIT = 0x0d
SUBLANG_ARABIC_UAE = 0x0e
SUBLANG_ARABIC_BAHRAIN = 0x0f
SUBLANG_ARABIC_QATAR = 0x10
SUBLANG_AZERI_LATIN = 0x01
SUBLANG_AZERI_CYRILLIC = 0x02
SUBLANG_CHINESE_TRADITIONAL = 0x01
SUBLANG_CHINESE_SIMPLIFIED = 0x02
SUBLANG_CHINESE_HONGKONG = 0x03
SUBLANG_CHINESE_SINGAPORE = 0x04
SUBLANG_CHINESE_MACAU = 0x05
SUBLANG_DUTCH = 0x01
SUBLANG_DUTCH_BELGIAN = 0x02
SUBLANG_ENGLISH_US = 0x01
SUBLANG_ENGLISH_UK = 0x02
SUBLANG_ENGLISH_AUS = 0x03
SUBLANG_ENGLISH_CAN = 0x04
SUBLANG_ENGLISH_NZ = 0x05
SUBLANG_ENGLISH_EIRE = 0x06
SUBLANG_ENGLISH_SOUTH_AFRICA = 0x07
SUBLANG_ENGLISH_JAMAICA = 0x08
SUBLANG_ENGLISH_CARIBBEAN = 0x09
SUBLANG_ENGLISH_BELIZE = 0x0a
SUBLANG_ENGLISH_TRINIDAD = 0x0b
SUBLANG_ENGLISH_ZIMBABWE = 0x0c
SUBLANG_ENGLISH_PHILIPPINES = 0x0d
SUBLANG_FRENCH = 0x01
SUBLANG_FRENCH_BELGIAN = 0x02
SUBLANG_FRENCH_CANADIAN = 0x03
SUBLANG_FRENCH_SWISS = 0x04
SUBLANG_FRENCH_LUXEMBOURG = 0x05
SUBLANG_FRENCH_MONACO = 0x06
SUBLANG_GERMAN = 0x01
SUBLANG_GERMAN_SWISS = 0x02
SUBLANG_GERMAN_AUSTRIAN = 0x03
SUBLANG_GERMAN_LUXEMBOURG = 0x04
SUBLANG_GERMAN_LIECHTENSTEIN = 0x05
SUBLANG_ITALIAN = 0x01
SUBLANG_ITALIAN_SWISS = 0x02
SUBLANG_KASHMIRI_SASIA = 0x02
SUBLANG_KASHMIRI_INDIA = 0x02
SUBLANG_KOREAN = 0x01
SUBLANG_LITHUANIAN = 0x01
SUBLANG_MALAY_MALAYSIA = 0x01
SUBLANG_MALAY_BRUNEI_DARUSSALAM = 0x02
SUBLANG_NEPALI_INDIA = 0x02
SUBLANG_NORWEGIAN_BOKMAL = 0x01
SUBLANG_NORWEGIAN_NYNORSK = 0x02
SUBLANG_PORTUGUESE = 0x02
SUBLANG_PORTUGUESE_BRAZILIAN = 0x01
SUBLANG_SERBIAN_LATIN = 0x02
SUBLANG_SERBIAN_CYRILLIC = 0x03
SUBLANG_SPANISH = 0x01
SUBLANG_SPANISH_MEXICAN = 0x02
SUBLANG_SPANISH_MODERN = 0x03
SUBLANG_SPANISH_GUATEMALA = 0x04
SUBLANG_SPANISH_COSTA_RICA = 0x05
SUBLANG_SPANISH_PANAMA = 0x06
SUBLANG_SPANISH_DOMINICAN_REPUBLIC = 0x07
SUBLANG_SPANISH_VENEZUELA = 0x08
SUBLANG_SPANISH_COLOMBIA = 0x09
SUBLANG_SPANISH_PERU = 0x0a
SUBLANG_SPANISH_ARGENTINA = 0x0b
SUBLANG_SPANISH_ECUADOR = 0x0c
SUBLANG_SPANISH_CHILE = 0x0d
SUBLANG_SPANISH_URUGUAY = 0x0e
SUBLANG_SPANISH_PARAGUAY = 0x0f
SUBLANG_SPANISH_BOLIVIA = 0x10
SUBLANG_SPANISH_EL_SALVADOR = 0x11
SUBLANG_SPANISH_HONDURAS = 0x12
SUBLANG_SPANISH_NICARAGUA = 0x13
SUBLANG_SPANISH_PUERTO_RICO = 0x14
SUBLANG_SWEDISH = 0x01
SUBLANG_SWEDISH_FINLAND = 0x02
SUBLANG_URDU_PAKISTAN = 0x01
SUBLANG_URDU_INDIA = 0x02
SUBLANG_UZBEK_LATIN = 0x01
SUBLANG_UZBEK_CYRILLIC = 0x02
SUBLANG_DUTCH_SURINAM = 0x03
SUBLANG_ROMANIAN = 0x01
SUBLANG_ROMANIAN_MOLDAVIA = 0x02
SUBLANG_RUSSIAN = 0x01
SUBLANG_RUSSIAN_MOLDAVIA = 0x02
SUBLANG_CROATIAN = 0x01
SUBLANG_LITHUANIAN_CLASSIC = 0x02
SUBLANG_GAELIC = 0x01
SUBLANG_GAELIC_SCOTTISH = 0x02
SUBLANG_GAELIC_MANX = 0x03
