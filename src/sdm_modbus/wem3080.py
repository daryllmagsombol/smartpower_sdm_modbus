from sdm_modbus import meter


class WEM3080T(meter.Meter):

    def __init__(self, *args, **kwargs):
        self.model = "WEM3080T"

        super().__init__(*args, **kwargs)

        self.registers = {
            "0x0001": (0x0001, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0002": (0x0002, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0003": (0x0003, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0004": (0x0004, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0005": (0x0005, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0006": (0x0006, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0007": (0x0007, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0008": (0x0008, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x0009": (0x0009, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000A": (0x000A, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000B": (0x000B, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000C": (0x000C, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000D": (0x000D, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000E": (0x000E, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),
            "0x000F": (0x000F, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 1, 1),

            "0x0010": (0x0010, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0011": (0x0011, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0012": (0x0012, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0013": (0x0013, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0014": (0x0014, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0015": (0x0015, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0016": (0x0016, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0017": (0x0017, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0018": (0x0018, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x0019": (0x0019, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001A": (0x001A, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001B": (0x001B, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001C": (0x001C, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001D": (0x001D, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001E": (0x001E, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),
            "0x001F": (0x001F, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 2, 1),

            "0x0020": (0x0020, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0021": (0x0021, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0022": (0x0022, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0023": (0x0023, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0024": (0x0024, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0025": (0x0025, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0026": (0x0026, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0027": (0x0027, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0028": (0x0028, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x0029": (0x0029, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002A": (0x002A, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002B": (0x002B, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002C": (0x002C, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002D": (0x002D, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002E": (0x002E, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),
            "0x002F": (0x002F, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 3, 1),

            "0x0030": (0x0030, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0031": (0x0031, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0032": (0x0032, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0033": (0x0033, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0034": (0x0034, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0035": (0x0035, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0036": (0x0036, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0037": (0x0037, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0038": (0x0038, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x0039": (0x0039, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003A": (0x003A, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003B": (0x003B, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003C": (0x003C, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003D": (0x003D, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003E": (0x003E, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),
            "0x003F": (0x003F, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 4, 1),

            "0x0040": (0x0040, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0041": (0x0041, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0042": (0x0042, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0043": (0x0043, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0044": (0x0044, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0045": (0x0045, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0046": (0x0046, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),
            "0x0047": (0x0047, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "", "", 5, 1),

            "l1_voltage": (0x0048, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L1 Voltage", "V", 6, 1),
            "l1_current": (0x0049, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L1 Current", "A", 6, 1),
            "l1_power_active": (0x004A, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L1 Power (Active)", "W", 6, 1),
            "l1_import_energy_active": (0x004B, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L1 Import Energy (Active)", "kWh", 6, 1),
            "l1_power_factor": (0x004D, 1, meter.registerType.INPUT, meter.registerDataType.UINT16, int, "L1 Power Factor", "", 6, 1),
            "l1_export_energy_active": (0x004E, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L1 Import Energy (Active)", "kWh", 6, 1),
            "l2_voltage": (0x0051, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L2 Voltage", "V", 6, 1),
            "l2_current": (0x0052, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L2 Current", "A", 6, 1),
            "l2_power_active": (0x0053, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L2 Power (Active)", "W", 6, 1),
            "l2_import_energy_active": (0x0054, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L2 Import Energy (Active)", "kWh", 6, 1),
            "l2_power_factor": (0x0056, 1, meter.registerType.INPUT, meter.registerDataType.UINT16, int, "L2 Power Factor", "", 6, 1),
            "l2_export_energy_active": (0x0057, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L2 Import Energy (Active)", "kWh", 6, 1),
            "l3_voltage": (0x005A, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L3 Voltage", "V", 6, 1),
            "l3_current": (0x005B, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L3 Current", "A", 6, 1),
            "l3_power_active": (0x005C, 1, meter.registerType.HOLDING, meter.registerDataType.UINT16, int, "L3 Power (Active)", "W", 6, 1),
            "l3_import_energy_active": (0x005D, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L3 Import Energy (Active)", "kWh", 6, 1),
            "l3_power_factor": (0x005F, 1, meter.registerType.INPUT, meter.registerDataType.UINT16, int, "L3 Power Factor", "", 6, 1),
            "l3_export_energy_active": (0x0060, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "L3 Import Energy (Active)", "kWh", 6, 1),
            "import_energy_active": (0x0063, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "Import Energy (Active)", "kWh", 6, 1),
            "frequency": (0x0065, 1, meter.registerType.INPUT, meter.registerDataType.UINT16, int, "Frequency", "Hz", 6, 1),
            "export_energy_active": (0x0066, 2, meter.registerType.INPUT, meter.registerDataType.UINT32, int, "Import Energy (Active)", "kWh", 6, 1)
        }