#!/bin/python3
import subprocess
import os


def update_file(filename: str) -> None:
    # Grab the basename, toss the file extension ".mp4"
    basename, _ = os.path.splitext(filename)

    # Similarly, split the basename by "_" into a list, toss the timezone,
    # first names, and last initials
    year_month_date, hour_minute_sec, _, _, _ = str(basename).split("_")

    # Split the sets of time digits into their own lists by each "-"
    ymd_list = year_month_date.split("-")
    hms_list = hour_minute_sec.split("-")

    # Insert "." before the seconds digits
    hms_list.insert(2, ".")

    # Combine both lists and join each element into one string of text
    date_list = ymd_list + hms_list
    date_string = "".join(date_list)

    # Run touch on each file, using the date_string, print any output
    p = subprocess.Popen(["touch", "-mt", date_string, filename])
    if p.stdout:
        print(p.stdout)


def main():
    # Loop through each item in the current folder, run update_file() on each .mp4 found
    current_folder = os.getcwd()
    for item in os.listdir(current_folder):
        if os.path.isfile(item) and os.path.splitext(item)[1] == ".mp4":
            try:
                update_file(item)
            except RuntimeError:
                print("Couldn't update file: ", item)
        else:
            pass
    print("Finished :)")


if __name__ == "__main__":
    main()
