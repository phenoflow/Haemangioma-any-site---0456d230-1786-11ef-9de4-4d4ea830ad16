# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"BBT8.14","system":"readv2"},{"code":"BBT3.00","system":"readv2"},{"code":"7A6G600","system":"readv2"},{"code":"B7J0111","system":"readv2"},{"code":"BBTC.00","system":"readv2"},{"code":"B7J0000","system":"readv2"},{"code":"BBT9.00","system":"readv2"},{"code":"G771200","system":"readv2"},{"code":"BBTH.00","system":"readv2"},{"code":"BBTG.00","system":"readv2"},{"code":"BBT8.12","system":"readv2"},{"code":"B7J0300","system":"readv2"},{"code":"PG42000","system":"readv2"},{"code":"BBT8.11","system":"readv2"},{"code":"B7J0z00","system":"readv2"},{"code":"BBT8.13","system":"readv2"},{"code":"BBT8.00","system":"readv2"},{"code":"BBT2.00","system":"readv2"},{"code":"BBT0.00","system":"readv2"},{"code":"BBGK.13","system":"readv2"},{"code":"BBT4.11","system":"readv2"},{"code":"2F25.00","system":"readv2"},{"code":"PH31200","system":"readv2"},{"code":"BBT4.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('haemangioma-any-site-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["haemangioma-any-site---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["haemangioma-any-site---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["haemangioma-any-site---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
