import re

from drone import Scout


def gen_scouts() -> dict:
    scout_dict = {}
    num_reg = re.compile(r"[1-5]{1}")  # Don't scrape more than 5 URLs at a go
    valid_input = False

    while not valid_input:
        num_scouts = input("How many scouts would you like to deploy? => ").strip()
        if re.fullmatch(num_reg, num_scouts):
            valid_input = True
        else:
            print("\nPlease enter a number between 1 and 5\n")

    for i in range(int(num_scouts)):
        # Dynamically create key names with vals of Scout objs
        scout_dict[f"s{[i + 1]}"] = Scout()

    return scout_dict


for s in gen_scouts().values():
    if s.page_data is not None:
        print("Captured page title!\n\n{0}".upper().format(s.page_data))
    else:
        print(f"\n\nNo HTML page content retrieved for {s.prefix + s.base_domain}")
