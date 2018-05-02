# Special value
DEFAULT = 0
INVALID_ID = 2 ** 32 - 1  # ulong maximum

# Return value
OK = 0
NOT_ONLINE = 1001
NOT_IDLE = 1002
NOT_AVAILABLE = 1003
NOT_READY = 1004
PARM_INVALID = 1005
ADDR_INVALID = 1006
MEMORY_FULL = 1007
SEQ_IN_USE = 1008
HALTED = 1009
ERROR_INIT = 1010
ERROR_COMM = 1011
DEVICE_REMOVED = 1012
NOT_CONFIGURED = 1013
LOADER_VERSION = 1014
ERROR_POWER_DOWN = 1018

# Device inquire and control types
DEVICE_NUMBER = 2000
VERSION = 2001
AVAIL_MEMORY = 2003
SYNCH_POLARITY = 2004
LEVEL_HIGH = 2006
LEVEL_LOW = 2007
TRIGGER_EDGE = 2005
EDGE_FALLING = 2008
EDGE_RISING = 2009
DEV_DMDTYPE = 2021
DMDTYPE_XGA = 1
DMDTYPE_1080P_095A = 3
DMDTYPE_XGA_07A = 4
DMDTYPE_XGA_055X = 6
DMDTYPE_WUXGA_096A = 7
DMDTYPE_DISCONNECT = 255
# TODO check is these constant values exist...
# DMDTYPE_XGA_055A =
# DMDTYPE_SXGA_PLUS =
# DMDTYPE_WQXGA_400MHZ_090A =
# DMDTYPE_WQXGA_480MHZ_090A =
USB_CONNECTION = 2016
DEV_DYN_SYNCH_OUT1_GATE = 2023
DEV_DYN_SYNCH_OUT2_GATE = 2024
DEV_DYN_SYNCH_OUT3_GATE = 2025
DDC_FPGA_TEMPERATURE = 2050
APPS_FPGA_TEMPERATURE = 2051
PCB_TEMPERATURE = 2052
DEV_DISPLAY_HEIGHT = 2057
DEV_DISPLAY_WIDTH = 2058
PWM_LEVEL = 2063
DEV_DMD_MODE = 2064
DMD_POWER_FLOAT = 1

# Sequence inquire and control types
BITPLANES = 2200
BITNUM = 2103
BIN_MODE = 2104
BIN_NORMAL = 2105
BIN_UNINTERRUPTED = 2106
PICNUM = 2201
FIRSTFRAME = 2101
LASTFRAME = 2102
FIRSTLINE = 2111
LASTLINE = 2112
LINE_INC = 2113
SCROLL_FROM_ROW = 2123
SCROLL_TO_ROW = 2124
SEQ_REPEAT = 2100
PICTURE_TIME = 2203
MIN_PICTURE_TIME = 2211
MAX_PICTURE_TIME = 2213
ILLUMINATE_TIME = 2204
MIN_ILLUMINATE_TIME = 2212
ON_TIME = 2214
OFF_TIME = 2215
SYNCH_DELAY = 2205
MAX_SYNCH_DELAY = 2209
SYNCH_PULSEWIDTH = 2206
TRIGGER_IN_DELAY = 2207
MAX_TRIGGER_IN_DELAY = 2210
DATA_FORMAT = 2110
DATA_MSB_ALIGN = 0
DATA_LSB_ALIGN = 1
DATA_BINARY_TOPDOWN = 2
DATA_BINARY_BOTTOMUP = 3
SEQ_PUT_LOCK = 2117
FLUT_MODE = 2118
FLUT_NONE = 0
FLUT_9BIT = 1
FLUT_18BIT = 2
FLUT_ENTRIES9 = 2120
FLUT_OFFSET9 = 2122
PWM_MODE = 2107
FLEX_PWM = 3

# Projection inquire and control types
PROJ_MODE = 2300
MASTER = 2301
SLAVE = 2302
PROJ_STEP = 2329
PROJ_STATE = 2400
PROJ_ACTIVE = 1200
PROJ_IDLE = 1201
PROJ_INVERSION = 2306
PROJ_UPSIDE_DOWN = 2307
PROJ_QUEUE_MODE = 2314
PROJ_LEGACY = 0
PROJ_SEQUENCE_QUEUE = 1
PROJ_QUEUE_ID = 2315
PROJ_QUEUE_MAX_AVAIL = 2316
PROJ_QUEUE_AVAIL = 2317
PROJ_PROGRESS = 2318
FLAG_QUEUE_IDLE = 1
FLAG_SEQUENCE_ABORTING = 2
FLAG_SEQUENCE_INDEFINITE = 4
FLAG_FRAME_FINISHED = 8
PROJ_RESET_QUEUE = 2319
PROJ_ABORT_SEQUENCE = 2320
PROJ_ABORT_FRAME = 2321
PROJ_WAIT_UNTIL = 2323
PROJ_WAIT_PIC_TIME = 0
PROJ_WAIT_ILLU_TIME = 1
FLUT_MAX_ENTRIES9 = 2324
FLUT_WRITE_9BIT = 2325
FLUT_WRITE_18BIT = 2326

# LED types
HLD_PT120_RED = 257
HLD_PT120_GREEN = 258
HLD_PT120_BLUE = 259
HLD_PT120_UV = 260
HLD_CBT90_WHITE = 262
HLD_PT120TE_BLUE = 263
HLD_CBT140_WHITE = 264

# LED inquire and control types
LED_SET_CURRENT = 1001
LED_BRIGHTNESS = 1002
LED_FORCE_OFF = 1003
LED_AUTO_OFF = 0
LED_OFF = 1
LED_ON = 2
LED_TYPE = 1101
LED_MEASURED_CURRENT = 1102
LED_TEMPERATURE_REF = 1103
LED_TEMPERATURE_JUNCTION = 1104

# Extended LED inquire and control types
LED_ALLOC_PARAMS = 2101
