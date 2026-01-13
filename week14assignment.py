def create_staff_dict(staff_list):
    return {staff['emp_id']: staff['department'] for staff in staff_list}

def audit_submissions(staff_dict, submitted_ids):
    s_ids = set(staff_dict.keys())
    sub_ids_set = set(submitted_ids)
    miss_time = s_ids - sub_ids_set
    invalid = sub_ids_set - s_ids
    return miss_time, invalid

def format_reminders(staff_dict, missing_set):
    return sorted(
        [f"REMINDER: Staff #{emp_id} ({staff_dict[emp_id]})"
         for emp_id in missing_set]
    )

staff = [
    {'emp_id': 101, 'department': "Sales"},
    {'emp_id': 102, 'department': "IT"},
    {'emp_id': 103, 'department': "HR"}
]

submitted = [101, 103, 500]
staff_dict = create_staff_dict(staff)
missing, invalid = audit_submissions(staff_dict, submitted)
report = format_reminders(staff_dict, missing)
print("Missing Timesheets:", missing)
print("Invalid IDs:", invalid)
print("Report:", report)
