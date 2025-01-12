from collections import OrderedDict

grammar = OrderedDict(
    {
        "Telheader_Quelle": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "Telheader_Ziel": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_destination",
        },
        "Telheader_TelSeq": {
            "type": "int",
            "length": 6,
            "dp": False,
            "df_val": False,
            "df_func": "get_sequence_number",
        },
        "Telheader_AnlZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "df_val": False,
            "df_func": "get_current_datetime",
        },
        "Satzart": {
            "type": "str",
            "length": 9,
            "dp": False,
            "df_val": "LBAMQ0051",
            "df_func": False,
        },
        "Lba_HOSTSTOCK_HostStockKz": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": "HOST",
            "df_func": False,
        },
        "Lba_LfdNummer": {
            "type": "int",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "TeId": {
            "type": "str",
            "length": 18,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_AId_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_AId_ArtNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_AId_Var": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "HMatQ": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Mngs_Mng": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "BestEinh": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Mngs_Gew": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "HostEinh": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_ResNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_SerienNrGrp": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_Charge": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_MHD": {
            "type": "date",
            "length": 8,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "MId_WeNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Seriennummer": {
            "type": "int",
            "length": 7,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
    }
)
