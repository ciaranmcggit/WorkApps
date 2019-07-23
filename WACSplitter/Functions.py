import csv
import os


def split_csv(csv_path, destination_folder, count, file_prefix):
    with open(csv_path, 'r') as source:
        reader = csv.reader(source)
        cleaned_file = clean_csv(reader, destination_folder)

    with open(cleaned_file, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)
        row_count = sum(1 for row in reader)-1

        file_idx = 0
        records_per_file = row_count/int(count)
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f"{file_prefix}_{file_idx}.csv"
            target_filepath = os.path.join(destination_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < records_per_file:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_idx += 1


def clean_csv(reader, folder):
    with open(folder + "tmp.csv", "w", newline='') as result:
        wtr = csv.writer(result)
        wtr.writerow(['SKUID', 'AWC'])
        for i, r in enumerate(reader):
            if i == 0:
                continue
            wtr.writerow((r[1], r[3]))
        return folder + "tmp.csv"

