class AccountTypes(object):
    ACCOUNT_TYPES = [
        (0, 'Supplier'),
        (1, 'Electricity Officer'),
        (2, 'Nodal Officer'),
        (3, 'Farmer'),
        (4, 'Manufacturer'),
        (5, 'Technician(cybermotion)'),
        (6, 'Technician(client)'),
        (7, 'Technician(location)'),
    ]

    @staticmethod
    def get_account_types():
        return AccountTypes.ACCOUNT_TYPES

    @staticmethod
    def to_dict():
        account_types = {}
        for account_type in AccountTypes.ACCOUNT_TYPES:
            acc_name = account_type[1].upper().replace(' ', '_')
            acc_code = account_type[0]
            account_types.update({acc_name: acc_code})

        return account_types


class StatesOfIndia(object):
    STATES = {
        "IN-AP": "Andhra Pradesh",
        "IN-AR": "Arunachal Pradesh",
        "IN-AS": "Assam",
        "IN-BR": "Bihar",
        "IN-CT": "Chhattisgarh",
        "IN-GA": "Goa",
        "IN-GJ": "Gujarat",
        "IN-HR": "Haryana",
        "IN-HP": "Himachal Pradesh",
        "IN-JK": "Jammu and Kashmir",
        "IN-JH": "Jharkhand",
        "IN-KA": "Karnataka",
        "IN-KL": "Kerala",
        "IN-MP": "Madhya Pradesh",
        "IN-MH": "Maharashtra",
        "IN-MN": "Manipur",
        "IN-ML": "Meghalaya",
        "IN-MZ": "Mizoram",
        "IN-NL": "Nagaland",
        "IN-OR": "Odisha",
        "IN-PB": "Punjab",
        "IN-RJ": "Rajasthan",
        "IN-SK": "Sikkim",
        "IN-TN": "Tamil Nadu",
        "IN-TG": "Telangana",
        "IN-TR": "Tripura",
        "IN-UT": "Uttarakhand",
        "IN-UP": "Uttar Pradesh",
        "IN-WB": "West Bengal",
        "IN-AN": "Andaman and Nicobar Island",
        "IN-CH": "Chandigarh",
        "IN-DN": "Dadra and Nagar Haveli",
        "IN-DD": "Daman and Diu",
        "IN-DL": "Delhi",
        "IN-LD": "Lakshadweep",
        "IN-PY": "Puducherry",
    }

    @staticmethod
    def get_state_names():
        return StatesOfIndia.STATES.items()
