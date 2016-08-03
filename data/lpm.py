def lpm_calculator(actual_head, ref_head, ref_head_lpm, pump_type,
        horse_power, power_dc, frequency):
    peak_lpm = 0.0
    lpm_factor = 0.0
    power_generation = 0.0
    lpm = 0.0

    # Frequency at which water starts
    fsw = 35 + ((actual_head - ref_head) * 0.25)

    if pump_type == 'SMB':
        if actual_head <= ref_head:
            peak_lpm = ref_head_lpm * (1 + ((ref_head - actual_head) * 0.025))
        else:
            peak_lpm = ref_head_lpm * (1 + ((ref_head - actual_head) * 0.0125))

        lpm_factor = peak_lpm / horse_power

        # Power generation(%) w.r.t input peak power
        power_generation = (power_dc / horse_power) * 100

        # LPM calculation
        if frequency < fsw:
            lpm = 1
        elif frequency > fsw and power_generation > 70:
            lpm = lpm_factor * power_dc
        else:
            lpm = lpm_factor * power_dc * 0.85

    return lpm
